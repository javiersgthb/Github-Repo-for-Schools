// This program calculates an employee's take home pay. 
#include <iostream>
using namespace std;
int main()
{
   double salary = 1250.00;
   double stateTax;
   double federalTax;
   double numDependents = 2;
   double dependentDeduction;
   double totalWithholding;
   double takeHomePay;

   // Calculate state tax here

   cout << "State Tax: $" << stateTax << endl;
   // Calculate federal tax here

   cout << "Federal Tax: $" << federalTax << endl;
   // Calculate dependent deduction here

   cout << "Dependents: $" << dependentDeduction << endl;
   // Calculate total withholding here

   // Calculate take-home pay here

   cout << "Salary: $" << salary << endl;
   cout << "Take-Home Pay: $" << takeHomePay << endl;
   return 0;
}
