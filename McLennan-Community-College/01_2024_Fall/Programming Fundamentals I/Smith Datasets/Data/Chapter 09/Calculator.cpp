// Calculator.cpp - This program performs arithmetic, ( +. -, *. / ) on two numbers.
// Input:  Interactive
// Output:  Result of arithmetic operation

#include <iostream>
#include <string>
using namespace std;

// Write performOperation() function declaration here

int main() 
{
   double numberOne, numberTwo;              	
   string operation;
   double result; 	
						
   cout << "Enter the first number: ";
   cin >> numberOne; 
   cout << "Enter the second number: ";
   cin >> numberTwo; 
   cout << "Enter an operator (+.-.*,/): ";
   cin >> operation;
		
   // Call performOperation method here		
   

   cout << numberOne;
   cout << " " << operation << " ";
   cout << numberTwo;
   cout << " = ";
   cout << result << endl;
	
   return 0;

} // End of main() function
	
	
// Write performOperation function here
