import json
import importlib
import os
import re
from datetime import datetime, timedelta

try:
    from pypdf import PdfReader
except ImportError:
    PdfReader = None

class BudgetManager:
    def __init__(self, filename="budget_data.json"):
        self.filename = filename
        self.data = self.load_data()
    
    def load_data(self):
        default_data = {
            "income_sources": {},
            "overtime_reimbursements": {},
            "expenses": {
                "housing": {
                    "rent": 0,
                    "utilities": 0,
                    "internet": 0
                },
                "transportation": {
                    "car_payment": 0,
                    "gas": 0,
                    "insurance": 0,
                    "maintenance": 0
                },
                "food": {
                    "groceries": 0,
                    "dining_out": 0
                },
                "entertainment": {
                    "subscriptions": 0,
                    "activities": 0
                },
                "other": {
                    "miscellaneous": 0
                }
            },
            "debts": {},
            "savings_goal": 0,
            "savings_timeframe_months": 0,
            "deduction_percentages": {
                "federal_withholding": 0.12,
                "state_withholding": 0.05,
                "social_security": 0.062,
                "medicare": 0.0145,
            },
            "retirement_percentages": {
                "traditional_401k": 0.03,
                "roth_401k": 0.03,
            },
            "retirement_start_after_paychecks": 2,
            "fixed_deductions": {
                "health_insurance": 0
            },
            "savings_accounts": {},
            "tracking": {
                "biweekly_entries": [],
                "monthly_totals": {},
                "yearly_totals": {}
            }
        }
        
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r') as f:
                    loaded_data = json.load(f)
                    # Merge loaded data with defaults to ensure all keys exist
                    for key in default_data:
                        if key not in loaded_data:
                            loaded_data[key] = default_data[key]
                        elif key == "deduction_percentages" and isinstance(loaded_data[key], dict):
                            for deduction_key in default_data["deduction_percentages"]:
                                if deduction_key not in loaded_data[key]:
                                    loaded_data[key][deduction_key] = default_data["deduction_percentages"][deduction_key]
                        elif key == "fixed_deductions" and isinstance(loaded_data[key], dict):
                            for deduction_key in default_data["fixed_deductions"]:
                                if deduction_key not in loaded_data[key]:
                                    loaded_data[key][deduction_key] = default_data["fixed_deductions"][deduction_key]
                        elif key == "retirement_percentages" and isinstance(loaded_data[key], dict):
                            for deduction_key in default_data["retirement_percentages"]:
                                if deduction_key not in loaded_data[key]:
                                    loaded_data[key][deduction_key] = default_data["retirement_percentages"][deduction_key]
                        elif key == "expenses" and isinstance(loaded_data[key], dict):
                            for category in default_data["expenses"]:
                                if category not in loaded_data[key]:
                                    loaded_data[key][category] = default_data["expenses"][category]
                        elif key == "tracking" and isinstance(loaded_data[key], dict):
                            for tracking_key in default_data["tracking"]:
                                if tracking_key not in loaded_data[key]:
                                    loaded_data[key][tracking_key] = default_data["tracking"][tracking_key]

                    # Backward compatibility: migrate old 401(k) keys out of tax withholding settings.
                    loaded_data.setdefault("retirement_percentages", default_data["retirement_percentages"].copy())
                    old_traditional = loaded_data["deduction_percentages"].pop("traditional_401k", None)
                    old_roth = loaded_data["deduction_percentages"].pop("roth_401k", None)
                    if old_traditional is not None and "traditional_401k" not in loaded_data["retirement_percentages"]:
                        loaded_data["retirement_percentages"]["traditional_401k"] = old_traditional
                    if old_roth is not None and "roth_401k" not in loaded_data["retirement_percentages"]:
                        loaded_data["retirement_percentages"]["roth_401k"] = old_roth

                    # Enforce VA compensation exclusion from withholding/retirement deduction math.
                    for source_data in loaded_data.get("income_sources", {}).values():
                        if not isinstance(source_data, dict):
                            continue
                        if source_data.get("source_type") == "va_compensation":
                            source_data["exclude_from_deductions"] = True
                            source_data["tax_free"] = True

                    return loaded_data
            except json.JSONDecodeError:
                print("Warning: Budget file is corrupted. Creating new budget.")
        return default_data
    
    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=2)
        print("Budget saved successfully!")

    def _is_yes(self, value):
        """Treat yes/y in any case as True."""
        return str(value).strip().lower() in ("yes", "y")
    
    def add_income_source(self):
        """Add a new income source with pay frequency"""
        print("\n--- ADD/UPDATE INCOME SOURCE ---")
        source_name = input("Enter income source name (e.g., Primary Job, Side Gig): ")
        name_lower = source_name.strip().lower()
        is_va_comp_source = "va" in name_lower and "comp" in name_lower
        if source_name in self.data["income_sources"]:
            update = input(f"'{source_name}' already exists. Update it? (yes/no): ").lower()
            if not self._is_yes(update):
                return
        
        try:
            print("\nPay Frequency Options:")
            print("1. Biweekly (every 2 weeks - 26 periods/year)")
            print("2. Monthly")
            
            frequency_choice = input("Select frequency (1-2): ")
            frequency_map = {"1": "biweekly", "2": "monthly"}
            frequency = frequency_map.get(frequency_choice, "monthly")
            
            if frequency == "biweekly":
                next_pay_date = input("Enter first pay date (YYYY-MM-DD): ")
                # Validate date
                datetime.strptime(next_pay_date, "%Y-%m-%d")
                
                is_prorated = self._is_yes(input("Was this pay period prorated (mid-period hire)? (yes/no): "))
                
                if is_prorated:
                    hourly_rate = float(input("Enter hourly rate: $"))
                    hours_paid = float(input("Enter number of hours paid for this period: "))
                    base_amount = hourly_rate * hours_paid

                    has_extra_deductions = self._is_yes(
                        input("Any additional deductions beyond standard withholdings? (yes/no): ")
                    )
                    extra_deductions = 0.0
                    if has_extra_deductions:
                        extra_deductions = float(input("Enter total additional deduction amount for this period: $"))
                        if extra_deductions < 0:
                            print("Deduction amount cannot be negative.")
                            return

                    amount_per_period = base_amount - extra_deductions
                    if amount_per_period < 0:
                        print("Deductions exceed calculated pay. Please review entries.")
                        return

                    print(f"Calculated pay: ${hourly_rate:.2f}/hr × {hours_paid} hrs = ${base_amount:.2f}")
                    if has_extra_deductions:
                        print(f"Adjusted for additional deductions: -${extra_deductions:.2f}")
                        print(f"Amount used for this pay period: ${amount_per_period:.2f}")
                else:
                    amount_per_period = float(input("Enter amount per biweekly paycheck: $"))
                
                if is_va_comp_source:
                    is_tax_free = True
                    print("VA compensation is set as tax-free and excluded from withholding/401(k) calculations.")
                else:
                    is_tax_free = self._is_yes(input("Is this income tax-free? (yes/no): "))
                
                self.data["income_sources"][source_name] = {
                    "amount_per_period": amount_per_period,
                    "frequency": frequency,
                    "next_pay_date": next_pay_date,
                    "tax_free": is_tax_free,
                    "exclude_from_deductions": bool(is_va_comp_source),
                    "source_type": "va_compensation" if is_va_comp_source else "employment",
                }
                print(f"Added '{source_name}': ${amount_per_period:.2f} biweekly (starting {next_pay_date})")
                
            else:  # monthly
                amount = float(input(f"Enter monthly amount for {source_name}: $"))
                if is_va_comp_source:
                    is_tax_free = True
                    print("VA compensation is set as tax-free and excluded from withholding/401(k) calculations.")
                else:
                    is_tax_free = self._is_yes(input("Is this income tax-free? (yes/no): "))
                
                self.data["income_sources"][source_name] = {
                    "amount": amount,
                    "frequency": frequency,
                    "tax_free": is_tax_free,
                    "exclude_from_deductions": bool(is_va_comp_source),
                    "source_type": "va_compensation" if is_va_comp_source else "employment",
                }
                print(f"Added '{source_name}': ${amount:.2f} monthly")
                
        except ValueError as e:
            print(f"Invalid input: {e}")

    def add_income_source_with_method(self):
        """Choose how to add/update income source: manual entry or payslip upload."""
        print("\n--- ADD/UPDATE INCOME SOURCE ---")
        print("1. Manual entry")
        print("2. Upload payslip")

        method_choice = input("Choose method (1-2): ").strip()
        if method_choice == "1":
            self.add_income_source()
        elif method_choice == "2":
            self.add_income_from_payslip()
        else:
            print("Invalid choice. Returning to menu.")

    def _parse_date_string(self, value):
        """Convert common date formats to YYYY-MM-DD."""
        if not value:
            return None

        cleaned = value.strip()
        date_formats = [
            "%Y-%m-%d",
            "%m/%d/%Y",
            "%m/%d/%y",
            "%m-%d-%Y",
            "%m-%d-%y",
            "%d/%m/%Y",
            "%d/%m/%y",
            "%d-%m-%Y",
            "%d-%m-%y",
        ]

        for date_format in date_formats:
            try:
                return datetime.strptime(cleaned, date_format).strftime("%Y-%m-%d")
            except ValueError:
                continue
        return None

    def _extract_first_amount(self, pattern, text):
        """Return first currency/number match as float for a regex pattern."""
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if not match:
            return None

        raw_value = match.group(1).replace(",", "").strip()
        try:
            return float(raw_value)
        except ValueError:
            return None

    def _read_payslip_text(self, file_path):
        """Extract text from TXT, PDF, or image payslips."""
        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".txt":
            with open(file_path, "r", encoding="utf-8", errors="ignore") as text_file:
                return text_file.read()

        if extension == ".pdf":
            if PdfReader is None:
                raise RuntimeError("Missing dependency: install 'pypdf' to read PDF payslips.")
            reader = PdfReader(file_path)
            return "\n".join((page.extract_text() or "") for page in reader.pages)

        image_extensions = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"}
        if extension in image_extensions:
            try:
                image_module = importlib.import_module("PIL.Image")
                pytesseract_module = importlib.import_module("pytesseract")
            except ImportError as import_error:
                raise RuntimeError(
                    "Missing dependencies: install 'pillow' and 'pytesseract' for image OCR."
                ) from import_error
            with image_module.open(file_path) as image:
                return pytesseract_module.image_to_string(image)

        raise ValueError("Unsupported file type. Use .txt, .pdf, or an image file.")

    def _extract_payslip_fields(self, text):
        """Try to pull common payslip fields from text."""
        date_pattern = (
            r"(?:pay\s*date|date\s*paid|payment\s*date)\s*[:\-]?\s*"
            r"(\d{1,4}[/-]\d{1,2}[/-]\d{1,4})"
        )
        date_match = re.search(date_pattern, text, flags=re.IGNORECASE)
        pay_date = self._parse_date_string(date_match.group(1)) if date_match else None

        # Fallback for table-style slips that label this as Check Date.
        if pay_date is None:
            check_date_match = re.search(
                r"check\s*date\D+(\d{1,2}[/-]\d{1,2}[/-]\d{4})",
                text,
                flags=re.IGNORECASE,
            )
            if check_date_match:
                pay_date = self._parse_date_string(check_date_match.group(1))

        # Additional fallback for lines that contain pay period begin/end/check date values.
        if pay_date is None:
            period_line_match = re.search(
                r"(\d{1,2}[/-]\d{1,2}[/-]\d{4})\s+"
                r"(\d{1,2}[/-]\d{1,2}[/-]\d{4})\s+"
                r"(\d{1,2}[/-]\d{1,2}[/-]\d{4})",
                text,
            )
            if period_line_match:
                pay_date = self._parse_date_string(period_line_match.group(3))

        # VA letters often include an Effective Date instead of a check date.
        if pay_date is None:
            effective_date_match = re.search(
                r"effective\s*date\s*[:\-]?\s*([A-Za-z]+\s+\d{1,2},\s+\d{4})",
                text,
                flags=re.IGNORECASE,
            )
            if effective_date_match:
                try:
                    pay_date = datetime.strptime(
                        effective_date_match.group(1), "%B %d, %Y"
                    ).strftime("%Y-%m-%d")
                except ValueError:
                    pay_date = None

        gross_pay = self._extract_first_amount(
            r"(?:gross\s*pay|gross\s*wages?|total\s*gross)\s*[:\-]?\s*\$?\s*([0-9,]+(?:\.[0-9]{1,2})?)",
            text,
        )

        # VA benefit verification letter: Gross Benefit Amount <newline> $X,XXX.XX
        if gross_pay is None:
            va_gross_match = re.search(
                r"gross\s*benefit\s*amount\s*\$?\s*([0-9,]+(?:\.[0-9]{2})?)",
                text,
                flags=re.IGNORECASE,
            )
            if va_gross_match:
                try:
                    gross_pay = float(va_gross_match.group(1).replace(",", ""))
                except ValueError:
                    gross_pay = None

        # VA summary letter: Your current monthly award amount is: <newline> $X,XXX.XX
        if gross_pay is None:
            va_award_match = re.search(
                r"current\s*monthly\s*award\s*amount\s*is\s*:?\s*\$?\s*([0-9,]+(?:\.[0-9]{2})?)",
                text,
                flags=re.IGNORECASE,
            )
            if va_award_match:
                try:
                    gross_pay = float(va_award_match.group(1).replace(",", ""))
                except ValueError:
                    gross_pay = None

        # Fallback for table-style slips: Current <gross> <pre-tax> <taxes> <post-tax> <net>
        if gross_pay is None:
            current_row_match = re.search(
                r"current\s+([0-9,]+\.[0-9]{2})\s+[0-9,]+\.[0-9]{2}\s+[0-9,]+\.[0-9]{2}\s+[0-9,]+\.[0-9]{2}\s+[0-9,]+\.[0-9]{2}",
                text,
                flags=re.IGNORECASE,
            )
            if current_row_match:
                try:
                    gross_pay = float(current_row_match.group(1).replace(",", ""))
                except ValueError:
                    gross_pay = None

        # Extra fallback for earnings summary line: Earnings <amount> <ytd>
        if gross_pay is None:
            earnings_row_match = re.search(
                r"earnings\s+([0-9,]+\.[0-9]{2})\s+[0-9,]+\.[0-9]{2}",
                text,
                flags=re.IGNORECASE,
            )
            if earnings_row_match:
                try:
                    gross_pay = float(earnings_row_match.group(1).replace(",", ""))
                except ValueError:
                    gross_pay = None
        hourly_rate = self._extract_first_amount(
            r"(?:hourly\s*rate|rate\s*per\s*hour|pay\s*rate)\s*[:\-]?\s*\$?\s*([0-9,]+(?:\.[0-9]{1,4})?)",
            text,
        )
        hours_paid = self._extract_first_amount(
            r"(?:hours?\s*(?:worked|paid)?|regular\s*hours?)\s*[:\-]?\s*([0-9,]+(?:\.[0-9]{1,2})?)",
            text,
        )

        # Fallback for table-style row: Regular Hourly <dates> <hours> <rate> <amount> <ytd>
        regular_hourly_row = re.search(
            r"regular\s+hourly\s+\S+\s+([0-9]+(?:\.[0-9]+)?)\s+([0-9]+(?:\.[0-9]+)?)\s+[0-9,]+\.[0-9]{2}",
            text,
            flags=re.IGNORECASE,
        )
        if regular_hourly_row:
            try:
                if hours_paid is None:
                    hours_paid = float(regular_hourly_row.group(1))
                if hourly_rate is None:
                    hourly_rate = float(regular_hourly_row.group(2))
            except ValueError:
                pass

        return {
            "pay_date": pay_date,
            "gross_pay": gross_pay,
            "hourly_rate": hourly_rate,
            "hours_paid": hours_paid,
        }

    def add_income_from_payslip(self):
        """Add/update income source by extracting values from a payslip file."""
        print("\n--- ADD INCOME FROM PAYSLIP ---")
        print("Supported files: .txt, .pdf, .png, .jpg, .jpeg, .tif, .tiff, .bmp, .webp")
        file_path = input("Enter payslip file path: ").strip().strip('"')

        if not file_path:
            print("No file provided.")
            return
        if not os.path.exists(file_path):
            print("File not found.")
            return

        try:
            payslip_text = self._read_payslip_text(file_path)
            extracted = self._extract_payslip_fields(payslip_text)
        except Exception as error:
            print(f"Could not parse payslip: {error}")
            return

        text_lower = payslip_text.lower()
        is_va_comp_letter = (
            "department of veterans affairs" in text_lower
            or "gross benefit amount" in text_lower
            or "current monthly award amount" in text_lower
        )

        print("\nExtracted values (review before saving):")
        if is_va_comp_letter:
            print(f"  Effective date (reference): {extracted['pay_date'] or 'Not found'}")
        else:
            print(f"  Pay date: {extracted['pay_date'] or 'Not found'}")
        print(f"  Gross pay: ${extracted['gross_pay']:.2f}" if extracted["gross_pay"] is not None else "  Gross pay: Not found")
        print(f"  Hourly rate: ${extracted['hourly_rate']:.2f}" if extracted["hourly_rate"] is not None else "  Hourly rate: Not found")
        print(f"  Hours paid: {extracted['hours_paid']}" if extracted["hours_paid"] is not None else "  Hours paid: Not found")

        if is_va_comp_letter:
            print("  Detected VA compensation letter: defaulting to monthly income.")

        source_name = input("\nEnter income source name (e.g., Primary Job, Side Gig): ").strip()
        if not source_name:
            print("Income source name is required.")
            return

        if source_name in self.data["income_sources"]:
            update = input(f"'{source_name}' already exists. Update it? (yes/no): ").lower()
            if not self._is_yes(update):
                return

        existing_source = self.data["income_sources"].get(source_name, {})
        existing_paychecks_recorded = existing_source.get("paychecks_recorded")

        if is_va_comp_letter:
            use_monthly = self._is_yes(
                input("Use monthly frequency for VA compensation? (yes/no): ")
            )
            frequency = "monthly" if use_monthly else "biweekly"
            if frequency == "biweekly":
                print("Note: VA compensation is typically monthly. Biweekly selected by user.")
        else:
            print("\nPay Frequency Options:")
            print("1. Biweekly (every 2 weeks - 26 periods/year)")
            print("2. Monthly")

            frequency_choice = input("Select frequency (1-2): ")
            frequency = "biweekly" if frequency_choice == "1" else "monthly"

        try:
            if frequency == "biweekly":
                pay_date = extracted["pay_date"]
                if pay_date:
                    use_extracted = input(f"Use extracted pay date {pay_date}? (yes/no): ").lower()
                    if not self._is_yes(use_extracted):
                        pay_date = None

                if not pay_date:
                    pay_date_input = input("Enter first pay date (YYYY-MM-DD): ")
                    pay_date = self._parse_date_string(pay_date_input)
                    if not pay_date:
                        print("Invalid date format.")
                        return

                is_prorated = self._is_yes(input("Was this pay period prorated (mid-period hire)? (yes/no): "))

                if is_prorated:
                    hourly_rate = extracted["hourly_rate"]
                    hours_paid = extracted["hours_paid"]

                    if hourly_rate is not None:
                        use_rate = self._is_yes(input(f"Use extracted hourly rate ${hourly_rate:.2f}? (yes/no): "))
                        if not use_rate:
                            hourly_rate = None
                    if hourly_rate is None:
                        hourly_rate = float(input("Enter hourly rate: $"))

                    if hours_paid is not None:
                        use_hours = self._is_yes(input(f"Use extracted hours paid {hours_paid}? (yes/no): "))
                        if not use_hours:
                            hours_paid = None
                    if hours_paid is None:
                        hours_paid = float(input("Enter number of hours paid for this period: "))

                    base_amount = hourly_rate * hours_paid

                    has_extra_deductions = self._is_yes(
                        input("Any additional deductions beyond standard withholdings? (yes/no): ")
                    )
                    extra_deductions = 0.0
                    if has_extra_deductions:
                        extra_deductions = float(input("Enter total additional deduction amount for this period: $"))
                        if extra_deductions < 0:
                            print("Deduction amount cannot be negative.")
                            return

                    amount_per_period = base_amount - extra_deductions
                    if amount_per_period < 0:
                        print("Deductions exceed calculated pay. Please review entries.")
                        return

                    print(f"Calculated pay: ${hourly_rate:.2f}/hr x {hours_paid} hrs = ${base_amount:.2f}")
                    if has_extra_deductions:
                        print(f"Adjusted for additional deductions: -${extra_deductions:.2f}")
                        print(f"Amount used for this pay period: ${amount_per_period:.2f}")
                else:
                    amount_per_period = extracted["gross_pay"]
                    if amount_per_period is not None:
                        use_gross = self._is_yes(input(f"Use extracted gross pay ${amount_per_period:.2f}? (yes/no): "))
                        if not use_gross:
                            amount_per_period = None
                    if amount_per_period is None:
                        amount_per_period = float(input("Enter amount per biweekly paycheck: $"))

                if is_va_comp_letter:
                    is_tax_free = True
                    print("VA compensation is set as tax-free and excluded from withholding/401(k) calculations.")
                else:
                    is_tax_free = self._is_yes(input("Is this income tax-free? (yes/no): "))

                self.data["income_sources"][source_name] = {
                    "amount_per_period": amount_per_period,
                    "frequency": "biweekly",
                    "next_pay_date": pay_date,
                    "tax_free": is_tax_free,
                    "exclude_from_deductions": bool(is_va_comp_letter),
                    "source_type": "va_compensation" if is_va_comp_letter else "employment",
                    "paychecks_recorded": (
                        existing_paychecks_recorded + 1
                        if isinstance(existing_paychecks_recorded, int) and existing_paychecks_recorded >= 1
                        else 1
                    ),
                }
                print(f"Added '{source_name}': ${amount_per_period:.2f} biweekly (starting {pay_date})")
            else:
                amount = extracted["gross_pay"]
                if amount is not None:
                    use_gross = self._is_yes(input(f"Use extracted monthly amount ${amount:.2f}? (yes/no): "))
                    if not use_gross:
                        amount = None
                if amount is None:
                    amount = float(input(f"Enter monthly amount for {source_name}: $"))

                if is_va_comp_letter:
                    is_tax_free = True
                    print("VA compensation is set as tax-free and excluded from withholding/401(k) calculations.")
                else:
                    is_tax_free = self._is_yes(input("Is this income tax-free? (yes/no): "))

                self.data["income_sources"][source_name] = {
                    "amount": amount,
                    "frequency": "monthly",
                    "tax_free": is_tax_free,
                    "exclude_from_deductions": bool(is_va_comp_letter),
                    "source_type": "va_compensation" if is_va_comp_letter else "employment",
                    "paychecks_recorded": (
                        existing_paychecks_recorded + 1
                        if isinstance(existing_paychecks_recorded, int) and existing_paychecks_recorded >= 1
                        else 1
                    ),
                }
                print(f"Added '{source_name}': ${amount:.2f} monthly")
        except ValueError as error:
            print(f"Invalid input: {error}")
    
    def remove_income_source(self):
        """Remove an income source"""
        if not self.data["income_sources"]:
            print("No income sources found.")
            return
        
        print("\nCurrent income sources:")
        for i, (source, data) in enumerate(self.data["income_sources"].items(), 1):
            if data.get("frequency") == "monthly":
                amount = data["amount"]
                print(f"{i}. {source}: ${amount:.2f}/month")
            else:
                amount = data["amount_per_period"]
                freq = data["frequency"]
                print(f"{i}. {source}: ${amount:.2f}/{freq}")
        
        try:
            choice = int(input("Enter the number of the source to remove (0 to cancel): "))
            if choice == 0:
                return
            source_to_remove = list(self.data["income_sources"].keys())[choice - 1]
            del self.data["income_sources"][source_to_remove]
            print(f"Removed '{source_to_remove}'")
        except (ValueError, IndexError):
            print("Invalid choice.")
    
    def add_overtime_reimbursement(self):
        """Add overtime pay or company reimbursement"""
        print("\n--- ADD OVERTIME/REIMBURSEMENT ---")
        item_name = input("Enter item name (e.g., Overtime, Mileage Reimbursement): ")
        if item_name in self.data["overtime_reimbursements"]:
            update = input(f"'{item_name}' already exists. Update it? (yes/no): ").lower()
            if not self._is_yes(update):
                return
        try:
            amount = float(input(f"Enter monthly amount for {item_name}: $"))
            is_tax_free = self._is_yes(input("Is this tax-free? (yes/no): "))
            self.data["overtime_reimbursements"][item_name] = {
                "amount": amount,
                "tax_free": is_tax_free
            }
            tax_status = " (tax-free)" if is_tax_free else ""
            print(f"Added/updated '{item_name}': ${amount:.2f}{tax_status}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    def remove_overtime_reimbursement(self):
        """Remove overtime/reimbursement"""
        if not self.data["overtime_reimbursements"]:
            print("No overtime/reimbursements found.")
            return
        
        print("\nCurrent overtime/reimbursements:")
        for i, (item, data) in enumerate(self.data["overtime_reimbursements"].items(), 1):
            amount = data["amount"] if isinstance(data, dict) else data
            tax_free = data.get("tax_free", False) if isinstance(data, dict) else False
            tax_status = " (tax-free)" if tax_free else ""
            print(f"{i}. {item}: ${amount:.2f}{tax_status}")
        
        try:
            choice = int(input("Enter the number to remove (0 to cancel): "))
            if choice == 0:
                return
            item_to_remove = list(self.data["overtime_reimbursements"].keys())[choice - 1]
            del self.data["overtime_reimbursements"][item_to_remove]
            print(f"Removed '{item_to_remove}'")
        except (ValueError, IndexError):
            print("Invalid choice.")
    
    def count_pay_periods_in_month(self, year, month, start_date_str, frequency):
        """Count how many pay periods occur in a given month"""
        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        
        # Get first and last day of the month
        month_start = datetime(year, month, 1)
        if month == 12:
            month_end = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            month_end = datetime(year, month + 1, 1) - timedelta(days=1)
        
        count = 0
        current_pay_date = start_date
        
        # Move forward if start date is before month
        if current_pay_date < month_start:
            days_diff = (month_start - current_pay_date).days
            if frequency == "biweekly":
                periods_to_add = (days_diff // 14) + 1
                current_pay_date += timedelta(days=14 * periods_to_add)
            elif frequency == "weekly":
                periods_to_add = (days_diff // 7) + 1
                current_pay_date += timedelta(days=7 * periods_to_add)
        
        # Count pay periods in this month
        period_days = 14 if frequency == "biweekly" else 7
        while current_pay_date <= month_end:
            if current_pay_date >= month_start:
                count += 1
            current_pay_date += timedelta(days=period_days)
        
        return count

    def _get_pay_period_indices_in_month(self, year, month, start_date_str, frequency):
        """Return pay dates in month with their global paycheck index from the start date."""
        if not start_date_str or frequency not in ["biweekly", "weekly"]:
            return []

        start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        month_start = datetime(year, month, 1)
        if month == 12:
            month_end = datetime(year + 1, 1, 1) - timedelta(days=1)
        else:
            month_end = datetime(year, month + 1, 1) - timedelta(days=1)

        period_days = 14 if frequency == "biweekly" else 7
        paycheck_index = 1
        current_pay_date = start_date

        if current_pay_date < month_start:
            days_diff = (month_start - current_pay_date).days
            periods_to_add = days_diff // period_days
            current_pay_date += timedelta(days=period_days * periods_to_add)
            paycheck_index += periods_to_add
            while current_pay_date < month_start:
                current_pay_date += timedelta(days=period_days)
                paycheck_index += 1

        paychecks = []
        while current_pay_date <= month_end:
            if current_pay_date >= month_start:
                paychecks.append((current_pay_date, paycheck_index))
            current_pay_date += timedelta(days=period_days)
            paycheck_index += 1

        return paychecks

    def get_retirement_eligible_income_for_month(self, year, month):
        """Income base used for retirement contributions for a given month."""
        start_after = int(self.data.get("retirement_start_after_paychecks", 2))
        eligible_income = 0.0

        for source_data in self.data["income_sources"].values():
            if not isinstance(source_data, dict):
                continue
            if source_data.get("exclude_from_deductions", False):
                continue
            if source_data.get("tax_free", False):
                continue

            frequency = source_data.get("frequency")
            if frequency in ["biweekly", "weekly"]:
                amount_per_period = source_data.get("amount_per_period", 0)
                paychecks = self._get_pay_period_indices_in_month(
                    year,
                    month,
                    source_data.get("next_pay_date"),
                    frequency,
                )
                recorded_paychecks = source_data.get("paychecks_recorded")
                if isinstance(recorded_paychecks, int) and recorded_paychecks >= 0:
                    eligible_count = sum(
                        1 for _, pay_idx in paychecks
                        if start_after <= pay_idx <= recorded_paychecks
                    )
                else:
                    eligible_count = sum(1 for _, pay_idx in paychecks if pay_idx >= start_after)
                eligible_income += amount_per_period * eligible_count
            elif frequency == "monthly":
                # For monthly sources, apply contribution percentage to monthly amount.
                eligible_income += source_data.get("amount", 0)

        return eligible_income
    
    def get_gross_income(self):
        """Calculate total monthly gross income accounting for pay frequency"""
        now = datetime.now()
        year = now.year
        month = now.month
        
        total = 0
        # Regular income sources
        for source_data in self.data["income_sources"].values():
            if isinstance(source_data, dict):
                if source_data.get("frequency") == "monthly":
                    total += source_data.get("amount", 0)
                elif source_data.get("frequency") in ["biweekly", "weekly"]:
                    pay_periods = self.count_pay_periods_in_month(
                        year, month, 
                        source_data.get("next_pay_date"),
                        source_data.get("frequency")
                    )
                    total += source_data.get("amount_per_period", 0) * pay_periods
        
        # Overtime and reimbursements (monthly)
        for item_data in self.data["overtime_reimbursements"].values():
            if isinstance(item_data, dict):
                total += item_data.get("amount", 0)
            else:
                total += item_data
        
        return total
    
    def get_taxable_income(self):
        """Calculate only taxable income (excluding tax-free sources)"""
        now = datetime.now()
        year = now.year
        month = now.month
        
        taxable = 0
        # Regular income sources
        for source_data in self.data["income_sources"].values():
            if isinstance(source_data, dict):
                if source_data.get("exclude_from_deductions", False):
                    continue
                if not source_data.get("tax_free", False):
                    if source_data.get("frequency") == "monthly":
                        taxable += source_data.get("amount", 0)
                    elif source_data.get("frequency") in ["biweekly", "weekly"]:
                        pay_periods = self.count_pay_periods_in_month(
                            year, month,
                            source_data.get("next_pay_date"),
                            source_data.get("frequency")
                        )
                        taxable += source_data.get("amount_per_period", 0) * pay_periods
        
        # Overtime and reimbursements
        for item_data in self.data["overtime_reimbursements"].values():
            if isinstance(item_data, dict):
                if not item_data.get("tax_free", False):
                    taxable += item_data.get("amount", 0)
            else:
                taxable += item_data
        
        return taxable
    
    def calculate_deductions(self):
        """Calculate total deductions from taxable income"""
        now = datetime.now()
        taxable_income = self.get_taxable_income()
        retirement_income = self.get_retirement_eligible_income_for_month(now.year, now.month)
        
        # Calculate tax withholding deductions.
        deductions = {}
        for deduction_type, percentage in self.data["deduction_percentages"].items():
            deductions[deduction_type] = taxable_income * percentage

        # Calculate retirement contributions separately from tax withholdings.
        for deduction_type, percentage in self.data.get("retirement_percentages", {}).items():
            deductions[deduction_type] = retirement_income * percentage
        
        # Add fixed deductions
        for deduction_type, amount in self.data["fixed_deductions"].items():
            if deduction_type in deductions:
                deductions[deduction_type] += amount
            else:
                deductions[deduction_type] = amount
        
        return deductions, sum(deductions.values())
    
    def calculate_net_income(self):
        """Calculate net income after deductions"""
        gross_income = self.get_gross_income()
        deductions, total_deductions = self.calculate_deductions()
        net_income = gross_income - total_deductions
        return gross_income, total_deductions, net_income, deductions
    
    def get_gross_income_for_month(self, year, month):
        """Calculate gross income for a specific month accounting for pay frequency"""
        total = 0
        # Regular income sources
        for source_data in self.data["income_sources"].values():
            if isinstance(source_data, dict):
                if source_data.get("frequency") == "monthly":
                    total += source_data.get("amount", 0)
                elif source_data.get("frequency") in ["biweekly", "weekly"]:
                    pay_periods = self.count_pay_periods_in_month(
                        year, month,
                        source_data.get("next_pay_date"),
                        source_data.get("frequency")
                    )
                    total += source_data.get("amount_per_period", 0) * pay_periods
        
        # Overtime and reimbursements
        for item_data in self.data["overtime_reimbursements"].values():
            if isinstance(item_data, dict):
                total += item_data.get("amount", 0)
            else:
                total += item_data
        
        return total
    
    def get_taxable_income_for_month(self, year, month):
        """Calculate taxable income for a specific month"""
        taxable = 0
        # Regular income sources
        for source_data in self.data["income_sources"].values():
            if isinstance(source_data, dict):
                if source_data.get("exclude_from_deductions", False):
                    continue
                if not source_data.get("tax_free", False):
                    if source_data.get("frequency") == "monthly":
                        taxable += source_data.get("amount", 0)
                    elif source_data.get("frequency") in ["biweekly", "weekly"]:
                        pay_periods = self.count_pay_periods_in_month(
                            year, month,
                            source_data.get("next_pay_date"),
                            source_data.get("frequency")
                        )
                        taxable += source_data.get("amount_per_period", 0) * pay_periods
        
        # Overtime and reimbursements
        for item_data in self.data["overtime_reimbursements"].values():
            if isinstance(item_data, dict):
                if not item_data.get("tax_free", False):
                    taxable += item_data.get("amount", 0)
            else:
                taxable += item_data
        
        return taxable
    
    def set_deduction_percentages(self):
        """Set tax withholding percentages."""
        print("\n--- SET TAX WITHHOLDING PERCENTAGES ---")
        print("WARNING: Tax withholding percentages are typically updated only when tax laws change.")
        print("These are applied to your taxable income for the entire year.\n")
        
        confirm = input("Continue with updating deduction percentages? (yes/no): ").lower()
        if not self._is_yes(confirm):
            return
        
        print("(Enter as decimals, e.g., 0.12 for 12%. Press Enter to keep current value)\n")
        
        deduction_labels = {
            "federal_withholding": "Federal Income Tax Withholding",
            "state_withholding": "State Income Tax Withholding",
            "social_security": "Social Security (FICA)",
            "medicare": "Medicare (FICA)",
        }
        
        changes_made = False
        for key, label in deduction_labels.items():
            try:
                current = self.data["deduction_percentages"].get(key, 0)
                new_value = input(f"{label} (current: {current*100:.2f}%): ")
                if new_value.strip():
                    percentage = float(new_value)
                    if percentage < 0 or percentage > 1:
                        print("Percentage must be between 0 and 1.")
                        continue
                    self.data["deduction_percentages"][key] = percentage
                    changes_made = True
            except ValueError:
                print("Invalid input. Keeping previous value.")
        
        if changes_made:
            print("\nTax withholding percentages updated!")
        else:
            print("\nNo changes made.")

    def set_retirement_contributions(self):
        """Set 401(k) contribution rates and paycheck start rule."""
        print("\n--- SET RETIREMENT CONTRIBUTIONS ---")
        print("These are separate from tax withholding and typically begin after enrollment.")
        print("(Enter as decimals, e.g., 0.03 for 3%. Press Enter to keep current value)\n")

        self.data.setdefault("retirement_percentages", {
            "traditional_401k": 0.03,
            "roth_401k": 0.03,
        })

        try:
            current_start = int(self.data.get("retirement_start_after_paychecks", 2))
            start_value = input(
                f"Start applying 401(k) after paycheck number (current: {current_start}): "
            ).strip()
            if start_value:
                parsed_start = int(start_value)
                if parsed_start < 1:
                    print("Paycheck number must be at least 1.")
                    return
                self.data["retirement_start_after_paychecks"] = parsed_start
        except ValueError:
            print("Invalid paycheck number. Keeping previous value.")

        retirement_labels = {
            "traditional_401k": "Traditional 401(k) Contribution",
            "roth_401k": "Roth 401(k) Contribution",
        }

        changes_made = False
        for key, label in retirement_labels.items():
            try:
                current = self.data["retirement_percentages"].get(key, 0)
                new_value = input(f"{label} (current: {current*100:.2f}%): ").strip()
                if new_value:
                    percentage = float(new_value)
                    if percentage < 0 or percentage > 1:
                        print("Percentage must be between 0 and 1.")
                        continue
                    self.data["retirement_percentages"][key] = percentage
                    changes_made = True
            except ValueError:
                print("Invalid input. Keeping previous value.")

        if changes_made:
            print("\nRetirement contribution settings updated!")
        else:
            print("\nNo contribution percentage changes made.")
    
    def set_fixed_deductions(self):
        """Set fixed dollar amount deductions"""
        print("\n--- SET FIXED DEDUCTIONS ---")
        print("These are fixed monthly amounts.\n")
        
        try:
            current = self.data["fixed_deductions"].get("health_insurance", 0)
            new_value = input(f"Health Insurance Premium (current: ${current:.2f}/month): $")
            if new_value.strip():
                amount = float(new_value)
                if amount >= 0:
                    self.data["fixed_deductions"]["health_insurance"] = amount
                    print("Fixed deductions updated!")
                else:
                    print("Amount cannot be negative.")
            else:
                print("No changes made.")
        except ValueError:
            print("Invalid input.")
    
    def view_deduction_percentages(self):
        """View current deduction percentages"""
        print("\n--- DEDUCTION SETTINGS ---")
        deduction_labels = {
            "federal_withholding": "Federal Income Tax Withholding",
            "state_withholding": "State Income Tax Withholding",
            "social_security": "Social Security (FICA)",
            "medicare": "Medicare (FICA)",
        }

        retirement_labels = {
            "traditional_401k": "Traditional 401(k) Contribution",
            "roth_401k": "Roth 401(k) Contribution",
        }

        print("\nTax Withholding Percentages:")
        for key, label in deduction_labels.items():
            percentage = self.data["deduction_percentages"].get(key, 0)
            print(f"  {label}: {percentage*100:.2f}%")

        print("\nRetirement Contributions:")
        start_after = int(self.data.get("retirement_start_after_paychecks", 2))
        print(f"  Start after paycheck number: {start_after}")
        for key, label in retirement_labels.items():
            percentage = self.data.get("retirement_percentages", {}).get(key, 0)
            print(f"  {label}: {percentage*100:.2f}%")
        
        health_insurance = self.data["fixed_deductions"].get("health_insurance", 0)
        print(f"\n  Health Insurance (fixed): ${health_insurance:.2f}/month")
    
    def view_expense_categories(self):
        """View all expense categories and subcategories"""
        print("\n--- EXPENSE CATEGORIES ---")
        for category, subcategories in self.data["expenses"].items():
            print(f"\n{category.upper()}:")
            if isinstance(subcategories, dict):
                for subcategory, amount in subcategories.items():
                    print(f"  {subcategory}: ${amount:.2f}")
            else:
                print(f"  Amount: ${subcategories:.2f}")
    
    def add_expense(self):
        """Add or update an expense"""
        print("\n--- ADD/UPDATE EXPENSE ---")
        self.view_expense_categories()
        
        category = input("\nEnter category (or create new one): ").lower().strip()
        if not category:
            print("Invalid category name.")
            return
        
        if category not in self.data["expenses"]:
            # New category - ask if they want to create it
            confirm = input(f"Category '{category}' doesn't exist. Create it? (yes/no): ").lower()
            if not self._is_yes(confirm):
                return
            self.data["expenses"][category] = {}
        
        # Now add subcategory
        if isinstance(self.data["expenses"][category], dict):
            subcategory = input(f"Enter subcategory for '{category}' (or press Enter for default): ").lower().strip()
            if not subcategory:
                subcategory = "default"
            
            try:
                amount = float(input(f"Enter monthly amount for {category}/{subcategory}: $"))
                if amount < 0:
                    print("Amount cannot be negative.")
                    return
                
                # If subcategory exists, add to it; otherwise create it
                if subcategory in self.data["expenses"][category]:
                    self.data["expenses"][category][subcategory] += amount
                    print(f"Added ${amount:.2f} to {category}/{subcategory}")
                else:
                    self.data["expenses"][category][subcategory] = amount
                    print(f"Created {category}/{subcategory}: ${amount:.2f}")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            # Legacy format - convert to new format
            try:
                amount = float(input(f"Enter amount for {category}: $"))
                if amount < 0:
                    print("Amount cannot be negative.")
                    return
                self.data["expenses"][category] = {
                    "default": self.data["expenses"][category] + amount
                }
                print(f"Added ${amount:.2f} to {category}")
            except ValueError:
                print("Invalid input. Please enter a number.")
    
    def remove_expense(self):
        """Remove an expense subcategory"""
        print("\n--- REMOVE EXPENSE ---")
        self.view_expense_categories()
        
        category = input("\nEnter category to remove from: ").lower().strip()
        if category not in self.data["expenses"]:
            print("Category not found.")
            return
        
        if isinstance(self.data["expenses"][category], dict):
            if not self.data["expenses"][category]:
                print(f"No expenses in '{category}'.")
                return
            
            subcategories = list(self.data["expenses"][category].keys())
            for i, subcategory in enumerate(subcategories, 1):
                print(f"{i}. {subcategory}: ${self.data['expenses'][category][subcategory]:.2f}")
            
            try:
                choice = int(input("Enter number to remove (0 to cancel): "))
                if choice == 0:
                    return
                subcategory_to_remove = subcategories[choice - 1]
                del self.data["expenses"][category][subcategory_to_remove]
                print(f"Removed {category}/{subcategory_to_remove}")
            except (ValueError, IndexError):
                print("Invalid choice.")
    
    def add_debt(self):
        name = input("Enter debt name (e.g., Credit Card, Student Loan): ")
        try:
            monthly_payment = float(input(f"Enter monthly payment for {name}: $"))
            self.data["debts"][name] = monthly_payment
            print(f"Added debt '{name}' with monthly payment of ${monthly_payment:.2f}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    def set_savings_goal(self):
        try:
            goal = float(input("Enter your savings goal amount: $"))
            months = int(input("Enter timeframe in months: "))
            self.data["savings_goal"] = goal
            self.data["savings_timeframe_months"] = months
            monthly_savings = goal / months
            print(f"To save ${goal:.2f} in {months} months, save ${monthly_savings:.2f}/month")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
    
    def allocate_savings(self):
        print("\n--- SAVINGS ALLOCATION ---")
        print("Set up to 4 savings accounts with percentage allocations:")
        print("(Percentages must total 100% or less)\n")
        
        self.data.setdefault("savings_accounts", {})
        allocate = input("Would you like to set up savings allocations? (yes/no): ").lower()
        
        if not self._is_yes(allocate):
            return
        
        accounts = {
            "emergency_fund": "Emergency Fund",
            "sinking_fund_1": "Sinking Fund 1",
            "sinking_fund_2": "Sinking Fund 2",
            "sinking_fund_3": "Sinking Fund 3"
        }
        
        total_percentage = 0
        temp_allocations = {}
        
        for key, label in accounts.items():
            try:
                percentage = float(input(f"Enter percentage for {label} (0 to skip): "))
                if percentage < 0:
                    print("Percentage cannot be negative.")
                    continue
                if percentage > 0:
                    temp_allocations[key] = percentage
                    total_percentage += percentage
            except ValueError:
                print("Invalid input. Skipping this account.")
        
        if total_percentage > 100:
            print(f"Error: Total percentage ({total_percentage}%) exceeds 100%")
            return
        
        self.data["savings_accounts"] = temp_allocations
        print(f"\nSavings allocation set! Total: {total_percentage}%")

    def update_savings_accounts(self):
        if not self.data.get("savings_accounts"):
            print("No savings accounts configured. Please set them up first.")
            return
        
        print("\n--- CURRENT SAVINGS ALLOCATIONS ---")
        for key, percentage in self.data["savings_accounts"].items():
            label = key.replace("_", " ").title()
            print(f"{label}: {percentage}%")
    
    def add_biweekly_entry(self):
        """Add actual biweekly paycheck entry"""
        print("\n--- ADD BI-WEEKLY PAYCHECK ENTRY ---")
        try:
            entry_date = input("Enter date (YYYY-MM-DD) or press Enter for today: ")
            if not entry_date:
                entry_date = datetime.now().strftime("%Y-%m-%d")
            
            # Validate date format
            datetime.strptime(entry_date, "%Y-%m-%d")
            
            biweekly_gross = float(input("Enter bi-weekly gross income (prorated amount if mid-period hire): $"))
            biweekly_deductions = float(input("Enter bi-weekly deductions (for this pay period): $"))
            biweekly_expenses = float(input("Enter bi-weekly actual expenses: $"))
            biweekly_debt_payment = float(input("Enter bi-weekly debt payments (snowball): $"))
            
            entry = {
                "date": entry_date,
                "gross": biweekly_gross,
                "deductions": biweekly_deductions,
                "net": biweekly_gross - biweekly_deductions,
                "expenses": biweekly_expenses,
                "debt_payment": biweekly_debt_payment,
                "remaining": (biweekly_gross - biweekly_deductions) - biweekly_expenses - biweekly_debt_payment
            }
            
            self.data["tracking"]["biweekly_entries"].append(entry)
            print(f"\nBi-weekly entry added for {entry_date}")
            print(f"  Net Income: ${entry['net']:.2f}")
            print(f"  Expenses: ${entry['expenses']:.2f}")
            print(f"  Debt Payment (Snowball): ${entry['debt_payment']:.2f}")
            print(f"  Remaining: ${entry['remaining']:.2f}")
            
        except ValueError as e:
            print(f"Invalid input: {e}")
    
    def view_biweekly_entries(self):
        """View all bi-weekly entries"""
        if not self.data["tracking"]["biweekly_entries"]:
            print("No bi-weekly entries recorded yet.")
            return
        
        print("\n--- BI-WEEKLY ENTRIES ---")
        for i, entry in enumerate(self.data["tracking"]["biweekly_entries"], 1):
            print(f"\n{i}. {entry['date']}")
            print(f"   Gross Income: ${entry['gross']:.2f}")
            print(f"   Deductions: -${entry['deductions']:.2f}")
            print(f"   Net Income: ${entry['net']:.2f}")
            print(f"   Expenses: -${entry['expenses']:.2f}")
            print(f"   Debt Payment (Snowball): -${entry['debt_payment']:.2f}")
            print(f"   Remaining: ${entry['remaining']:.2f}")
    
    def calculate_monthly_from_biweekly(self):
        """Calculate monthly totals from bi-weekly entries"""
        if not self.data["tracking"]["biweekly_entries"]:
            print("No bi-weekly entries to calculate from.")
            return
        
        # Group by month
        monthly_data = {}
        for entry in self.data["tracking"]["biweekly_entries"]:
            month_key = entry["date"][:7]  # YYYY-MM format
            
            if month_key not in monthly_data:
                monthly_data[month_key] = {
                    "gross": 0,
                    "deductions": 0,
                    "net": 0,
                    "expenses": 0,
                    "debt_payment": 0,
                    "remaining": 0,
                    "entries_count": 0
                }
            
            monthly_data[month_key]["gross"] += entry["gross"]
            monthly_data[month_key]["deductions"] += entry["deductions"]
            monthly_data[month_key]["net"] += entry["net"]
            monthly_data[month_key]["expenses"] += entry["expenses"]
            monthly_data[month_key]["debt_payment"] += entry["debt_payment"]
            monthly_data[month_key]["remaining"] += entry["remaining"]
            monthly_data[month_key]["entries_count"] += 1
        
        self.data["tracking"]["monthly_totals"] = monthly_data
        print("Monthly totals calculated from bi-weekly entries!")
    
    def view_monthly_totals(self):
        """View monthly totals"""
        if not self.data["tracking"]["monthly_totals"]:
            print("No monthly totals calculated yet.")
            print("Run 'Calculate Monthly from Bi-weekly' first.")
            return
        
        print("\n--- MONTHLY TOTALS (from actual biweekly entries) ---")
        yearly_gross = 0
        yearly_deductions = 0
        yearly_net = 0
        yearly_expenses = 0
        yearly_debt = 0
        yearly_remaining = 0
        
        for month, data in sorted(self.data["tracking"]["monthly_totals"].items()):
            print(f"\n{month} ({data['entries_count']} pay periods):")
            print(f"  Gross Income: ${data['gross']:.2f}")
            print(f"  Deductions: -${data['deductions']:.2f}")
            print(f"  Net Income: ${data['net']:.2f}")
            print(f"  Expenses: -${data['expenses']:.2f}")
            print(f"  Debt Payment (Snowball): -${data['debt_payment']:.2f}")
            print(f"  Remaining: ${data['remaining']:.2f}")
            
            yearly_gross += data["gross"]
            yearly_deductions += data["deductions"]
            yearly_net += data["net"]
            yearly_expenses += data["expenses"]
            yearly_debt += data["debt_payment"]
            yearly_remaining += data["remaining"]
        
        # Store yearly totals
        self.data["tracking"]["yearly_totals"] = {
            "gross": yearly_gross,
            "deductions": yearly_deductions,
            "net": yearly_net,
            "expenses": yearly_expenses,
            "debt_payment": yearly_debt,
            "remaining": yearly_remaining
        }
        
        print(f"\n{'='*40}")
        print("YEARLY TOTALS:")
        print(f"  Gross Income: ${yearly_gross:.2f}")
        print(f"  Deductions: -${yearly_deductions:.2f}")
        print(f"  Net Income: ${yearly_net:.2f}")
        print(f"  Expenses: -${yearly_expenses:.2f}")
        print(f"  Debt Payment (Snowball): -${yearly_debt:.2f}")
        print(f"  Remaining: ${yearly_remaining:.2f}")
    
    def show_summary(self):
        """Show budget summary for current month"""
        print("\n" + "="*60)
        print("BUDGET SUMMARY (CURRENT MONTH)")
        print("="*60)
        
        now = datetime.now()
        current_month_str = f"Based on {now.strftime('%B %Y')}"
        print(f"\n{current_month_str}")
        
        # Get current month's expected income accounting for pay frequency.
        gross_income, total_deductions, net_income, deductions = self.calculate_net_income()
        
        print(f"\nINCOME SOURCES:")
        if self.data["income_sources"]:
            for source, data in self.data["income_sources"].items():
                if data.get("frequency") == "monthly":
                    amount = data.get("amount", 0)
                    tax_free = data.get("tax_free", False)
                    tax_status = " (tax-free)" if tax_free else ""
                    print(f"  {source}: ${amount:.2f}{tax_status}")
                else:
                    pay_periods = self.count_pay_periods_in_month(
                        now.year, now.month,
                        data.get("next_pay_date"),
                        data.get("frequency")
                    )
                    amount = data.get("amount_per_period", 0) * pay_periods
                    tax_free = data.get("tax_free", False)
                    tax_status = " (tax-free)" if tax_free else ""
                    frequency = data.get("frequency")
                    print(f"  {source}: ${amount:.2f} ({pay_periods}x {frequency}){tax_status}")
        
        if self.data["overtime_reimbursements"]:
            print(f"\nOVERTIME / REIMBURSEMENTS:")
            for item, data in self.data["overtime_reimbursements"].items():
                if isinstance(data, dict):
                    amount = data.get("amount", 0)
                    tax_free = data.get("tax_free", False)
                    tax_status = " (tax-free)" if tax_free else ""
                else:
                    amount = data
                    tax_status = ""
                print(f"  {item}: ${amount:.2f}{tax_status}")
        
        if not self.data["income_sources"] and not self.data["overtime_reimbursements"]:
            print("  No income sources added yet.")
            return
        
        print(f"\nGross Income: ${gross_income:.2f}")
        
        # Deductions breakdown
        print(f"\nDEDUCTIONS:")
        deduction_labels = {
            "federal_withholding": "Federal Income Tax",
            "state_withholding": "State Income Tax",
            "social_security": "Social Security (FICA)",
            "medicare": "Medicare (FICA)",
            "traditional_401k": "Traditional 401(k) Contribution",
            "roth_401k": "Roth 401(k) Contribution",
            "health_insurance": "Health Insurance"
        }
        
        for key, label in deduction_labels.items():
            if key in deductions:
                amount = deductions[key]
                if amount > 0:
                    print(f"  {label}: -${amount:.2f}")
        
        print(f"\nTotal Deductions: -${total_deductions:.2f}")
        print(f"Net Income (after deductions): ${net_income:.2f}")
        
        # Savings allocation
        savings_allocation = sum(self.data.get("savings_accounts", {}).values())
        total_allocated_to_savings = (net_income * savings_allocation) / 100
        
        if self.data.get("savings_accounts"):
            print(f"\nSAVINGS ALLOCATION ({savings_allocation}%):")
            for key, percentage in self.data["savings_accounts"].items():
                label = key.replace("_", " ").title()
                allocated = (net_income * percentage) / 100
                print(f"  {label}: {percentage}% (${allocated:.2f})")
            print(f"Total allocated to savings: ${total_allocated_to_savings:.2f}")
        
        # Expenses
        total_expenses = 0
        print(f"\nEXPENSES:")
        for category, subcategories in self.data["expenses"].items():
            category_total = 0
            if isinstance(subcategories, dict):
                for subcategory, amount in subcategories.items():
                    if amount > 0:
                        print(f"  {category}/{subcategory}: ${amount:.2f}")
                        category_total += amount
                        total_expenses += amount
            else:
                if subcategories > 0:
                    print(f"  {category}: ${subcategories:.2f}")
                    total_expenses += subcategories
            
            if category_total > 0:
                print(f"  --> {category} subtotal: ${category_total:.2f}")
        
        print(f"Total Expenses: ${total_expenses:.2f}")
        
        # Debts
        total_debts = sum(self.data["debts"].values())
        if self.data["debts"]:
            print(f"\nDEBTS AND LOANS (SNOWBALL):")
            for debt, payment in self.data["debts"].items():
                print(f"  {debt}: ${payment:.2f}/month")
            print(f"Total Debt Payments: ${total_debts:.2f}")
        
        available_after_savings = net_income - total_allocated_to_savings
        remaining = available_after_savings - total_expenses - total_debts
        print(f"\nAvailable after savings allocation: ${available_after_savings:.2f}")
        print(f"Remaining after expenses and debts: ${remaining:.2f}")
        
        if self.data["savings_goal"] > 0 and self.data["savings_timeframe_months"] > 0:
            monthly_needed = self.data["savings_goal"] / self.data["savings_timeframe_months"]
            print(f"\nSAVINGS GOAL: ${self.data['savings_goal']:.2f} in {self.data['savings_timeframe_months']} months")
            print(f"Monthly savings needed: ${monthly_needed:.2f}")
        print("="*60 + "\n")
    
    def income_menu(self):
        while True:
            print("\n--- INCOME MANAGEMENT ---")
            print("1. Add/Update income source")
            print("2. Remove income source")
            print("3. Add/Update overtime or reimbursement")
            print("4. Remove overtime or reimbursement")
            print("5. Back")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_income_source_with_method()
            elif choice == "2":
                self.remove_income_source()
            elif choice == "3":
                self.add_overtime_reimbursement()
            elif choice == "4":
                self.remove_overtime_reimbursement()
            elif choice == "5":
                return
            else:
                print("Invalid choice. Please try again.")

    def deductions_menu(self):
        while True:
            print("\n--- DEDUCTIONS ---")
            print("1. Set tax withholding percentages")
            print("2. Set retirement contributions (401k)")
            print("3. Set fixed deductions")
            print("4. View deduction settings")
            print("5. Back")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.set_deduction_percentages()
            elif choice == "2":
                self.set_retirement_contributions()
            elif choice == "3":
                self.set_fixed_deductions()
            elif choice == "4":
                self.view_deduction_percentages()
            elif choice == "5":
                return
            else:
                print("Invalid choice. Please try again.")

    def expenses_menu(self):
        while True:
            print("\n--- EXPENSES ---")
            print("1. View expense categories")
            print("2. Add/Update expense")
            print("3. Remove expense")
            print("4. Back")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.view_expense_categories()
            elif choice == "2":
                self.add_expense()
            elif choice == "3":
                self.remove_expense()
            elif choice == "4":
                return
            else:
                print("Invalid choice. Please try again.")

    def savings_menu(self):
        while True:
            print("\n--- SAVINGS ---")
            print("1. Set savings goal")
            print("2. Allocate savings accounts")
            print("3. View savings allocations")
            print("4. Back")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.set_savings_goal()
            elif choice == "2":
                self.allocate_savings()
            elif choice == "3":
                self.update_savings_accounts()
            elif choice == "4":
                return
            else:
                print("Invalid choice. Please try again.")

    def tracking_menu(self):
        while True:
            print("\n--- PAYCHECK TRACKING ---")
            print("1. Add bi-weekly paycheck entry")
            print("2. View bi-weekly entries")
            print("3. Calculate monthly from bi-weekly")
            print("4. View monthly & yearly totals")
            print("5. Back")

            choice = input("Enter your choice (1-5): ")

            if choice == "1":
                self.add_biweekly_entry()
            elif choice == "2":
                self.view_biweekly_entries()
            elif choice == "3":
                self.calculate_monthly_from_biweekly()
            elif choice == "4":
                self.view_monthly_totals()
            elif choice == "5":
                return
            else:
                print("Invalid choice. Please try again.")

    def main_menu(self):
        while True:
            print("\n--- BUDGET MANAGER ---")
            print("1. Manage income")
            print("2. Manage deductions")
            print("3. Manage expenses")
            print("4. Manage savings")
            print("5. Add debt or loan")
            print("6. Paycheck tracking")
            print("7. View budget summary (current month)")
            print("8. Exit")

            choice = input("Enter your choice (1-8): ")

            if choice == "1":
                self.income_menu()
            elif choice == "2":
                self.deductions_menu()
            elif choice == "3":
                self.expenses_menu()
            elif choice == "4":
                self.savings_menu()
            elif choice == "5":
                self.add_debt()
            elif choice == "6":
                self.tracking_menu()
            elif choice == "7":
                self.show_summary()
            elif choice == "8":
                save_choice = input("Save changes before exit? (yes/no): ").strip().lower()
                if self._is_yes(save_choice):
                    self.save_data()
                elif save_choice.strip().lower() not in ["no", "n"]:
                    print("Invalid choice. Returning to menu.")
                    continue
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manager = BudgetManager()
    manager.main_menu()