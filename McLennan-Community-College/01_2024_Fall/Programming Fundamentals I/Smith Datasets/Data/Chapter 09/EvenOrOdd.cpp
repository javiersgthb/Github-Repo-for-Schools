// EvenOrOdd.cpp - This program determines if a number input by the user is an 
// even number or an odd number.  
// Input:  Interactive
// Output:  The number entered and whether it is even or odd

#include <iostream>
#include <string>
void evenOrOdd(int);
using namespace std;

int main() 
{
   int number;              	
   cout << "Enter a number or 999 to quit: ";
   cin >> number; 
	
   while(number != 999)
   {
      evenOrOdd(number);
      cout << "Enter a number or 999 to quit: ";
      cin >> number; 
   }
   return 0;
} // End of main function
	
void evenOrOdd(int number)
{
   if((number % 2) == 0)
      cout << "Number: " << number << " is even." << endl;
   else
      cout << "Number: " << number << " is odd." << endl;
} // End of evenOrOdd function



