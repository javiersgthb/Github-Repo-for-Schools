// Overloaded.cpp - This program illustrates overloaded functions. 
// Input:  None
// Output:  Bill printed in various ways  

#include <iostream>
#include <string>
using namespace std;

void printBill(double);
void printBill(double, double);
void printBill(double, string);
void printBill(double, double, string);

int main() 
{
   double bal = 250.00, discountRate = .05; 
   string msg = "Due in 10 days.";  

   printBill(bal);  			// Call version #1
   printBill(bal, discountRate);  	// Call version #2
   printBill(bal, msg);  		// Call version #3
   printBill(bal, discountRate, msg); 	// Call version #4
			     	
   return 0;
} // End of main() function
	
// printBill() function #1
void printBill(double balance)	
{
   cout << "Thank you for your order." << endl;
   cout << "Please remit " << balance << endl;		
} // End of printBill #1 function

// printBill() function #2
void printBill(double balance, double discount)	
{
   double newBal;
   newBal = balance - (balance * discount);
   cout << "Thank you for your order." << endl;
   cout << "Please remit " << newBal << endl;		
} // End of printBill #2 function

// printBill() function #3
void printBill(double balance, string message)	
{
   cout << "Thank you for your order." << endl;
   cout << message << endl;
   cout << "Please remit " << balance << endl;		
} // End of printBill #3 function

// printBill() function #4
void printBill(double balance, double discount, string message)		
{
   double  newBal;
   newBal = balance - (balance * discount);
   cout << "Thank you for your order." << endl;
   cout << message << endl;
   cout << "Please remit " << newBal << endl;		
} // End of printBill #4 function
