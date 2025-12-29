/* Temperature.cpp - This C++ program converts a Fahrenheit 
   temperature to Celsius.
   Input:  Interactive
   Output: Fahrenheit temperature followed by Celsius 
   temperature
*/
#include <iostream>
using namespace std;

int main()
{
   double fahrenheit;
   double celsius;

   // Prompt user
   cout << "Enter Fahrenheit temperature: ";
   // Get interactive user input
   cin >> fahrenheit;
   // Calculate celsius
   celsius = (fahrenheit - 32.0) * (5.0/9.0);
   // Output
   cout << "Fahrenheit temperature:" << fahrenheit << endl;
   cout << "Celsius temperature:" << celsius << endl;
	     
   return 0;
}
	     
