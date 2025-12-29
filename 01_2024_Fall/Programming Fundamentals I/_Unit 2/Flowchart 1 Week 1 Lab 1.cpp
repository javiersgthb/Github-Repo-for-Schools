int main()
{
    double balance;
    double rate;
    double annualInterestEarned;
    double biAnnualInterestEarned;
	double quarterlyInterestEarned;

    cout << "Enter Balance: $";
    cin >> balance;
	cout << "Enter Rate (decimal): ";
    cin >> rate;

    annualInterestEarned = (balance*rate)/100;
    biAnnualInterestEarned = (balance*rate)/2/100;
	quarterlyInterestEarned = (balance*rate)/3/100;

	cout << "Annual Interest: $" << annualInterestEarned << endl;
    cout << "Bi-Annual Interest: $"  << biAnnualInterestEarned << endl;
    cout << "Quarterly Interest: $" << quarterlyInterestEarned << endl;
    cout << "Code by Javier Silva" << endl;

    return 0;
}
