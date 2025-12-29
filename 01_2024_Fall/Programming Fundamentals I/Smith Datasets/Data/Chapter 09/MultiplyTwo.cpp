// MultiplyTwo.cpp - This program calculates the prodcut of two numbers. 
// It demonstrates pass by reference. 
// Input:  None
// Output:  The product of two numbers

#include <iostream>
using namespace std;
// Write function declaration here


int main() 
{
   int num1 = 10; 
   int num2 = 20;
   int product = 0;              			

   // Print value of product before function call
   cout << "Value of product is: " << product << endl;

   // Call multiplyNumbers using pass by reference for product
   

   // Print value of calculated product
   cout << num1 << " * " << num2 << " is " << product << endl; 						
   return 0;
} // End of main function
	
// Write multiplyNumbers function here; use pass by reference for result of multiplication



