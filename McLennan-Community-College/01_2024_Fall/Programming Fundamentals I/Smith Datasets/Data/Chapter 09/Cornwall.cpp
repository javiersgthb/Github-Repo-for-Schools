// Cornwall.cpp - This program computes hotel guest rates.
// Input:  None
// Output:  Hotel guest rate

#include <iostream>
#include <string>
using namespace std;

double computeRate(int);
double computeRate(int, string);

int main() 
{
   int days;
   string mealPlan; 
   string question;
   double rate = 0.0;   
               	
   cout << "How many days do you plan to stay? " << endl;
   cin >> days;
   cout << "Do you want a meal plan? Y or N: " << endl;
   cin >> question;	
  
   // Figure out which arguments to pass to the computeRate() function and
   // then call the computeRate() function							
   
   cout << "The rate for your stay is $" << rate << endl;

   return 0;
} // End of main() function
	
	
// Write computeRate functions here.

