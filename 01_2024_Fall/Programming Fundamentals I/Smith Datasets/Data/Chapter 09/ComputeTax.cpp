// ComputeTax.cpp - This program computes tax given a balance 
// and a rate 
// Input:  Interactive
// Output:  The balance, tax rate, and computed tax 

#include <iostream>
#include <string>
void computeTax(double, double);
using namespace std;

int main() 
{
   double balance;              	
   double rate;
				
   cout << "Enter balance: ";
   cin >> balance; 
   cout << "Enter rate: ";
   cin >> rate; 
	
   computeTax(balance, rate);
					
   return 0;
} // End of main() function
	
void computeTax(double amount, double rate)
{
   double tax;

   tax = amount * rate;
   cout << "Amount: " << amount << " Rate: " << rate << " Tax: " 
        << tax << endl;
} // End of computeTax function


