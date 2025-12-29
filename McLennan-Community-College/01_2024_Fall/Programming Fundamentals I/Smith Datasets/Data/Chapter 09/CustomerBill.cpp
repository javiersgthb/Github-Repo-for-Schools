/* Program Name: CustomerBill.cpp 
   Function: This program uses a function to print a company name and address     and then prints a customer name and    balance.
   Input:  Interactive
   Output: Company name and address, customer name and balance
*/  
#include <iostream>
#include <string>
void nameAndAddress(); // function declaration
using namespace std;
int main()
{ 
   // Declare variables local to main()
   string firstName;
   string lastName;
   double balance;
     
   // Get interactive input
   cout << "Enter customer's first name: ";
   cin >> firstName;
   cout << "Enter customer's last name: ";
   cin >> lastName;
   cout << "Enter customer's balance: ";
   cin >> balance;
     
   // Call nameAndAddress() function
   nameAndAddress();
   // Output customer name and address
   cout << "Customer Name:  " << firstName << " " << lastName << endl;
   cout << "Customer Balance:  " << balance << endl;   
 
   return 0;
} // End of main() function
   
void nameAndAddress()
{
   // Declare and initialize local, constant Strings
   const string ADDRESS_LINE1 = "ABC Manufacturing";
   const string ADDRESS_LINE2 = "47 Industrial Lane";
   const string ADDRESS_LINE3 = "Wild Rose, WI 54984";

   // Output	
   cout << ADDRESS_LINE1 << endl;
   cout << ADDRESS_LINE2 << endl;
   cout << ADDRESS_LINE3 << endl;
}  // End of nameAndAddress() function
     
