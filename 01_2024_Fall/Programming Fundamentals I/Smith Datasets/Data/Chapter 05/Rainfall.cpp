// Rainfall.cpp - This program finds the average rainfall for a week.  
// Input:  Rainfall, in inches, for each day of one week
// Output: Prints the seven rainfall amounts and their average 

#include <iostream>
#include <string>
using namespace std;
int main()
{
   double rainfall;	// Daily rainfall amount 
   double sum = 0; 	// Accumulates sum of seven rainfall amounts
   double average; 	// Average of seven rainfall amounts
   int counter; 		// Loop control variable
   const int DAYS_IN_WEEK = 7; // Constant number of days in a week
		
   // This is the work done in the detailLoop() function
   // Loop for seven days
   for(counter = 1; counter <= DAYS_IN_WEEK; counter++)
   {
      cout << "Enter rainfall amount for Day " << counter << ": ";
      cin >> rainfall;
      cout << "Day " << counter << " rainfall amount is " << 
              rainfall << " inches" << endl;
      sum += rainfall;
   }	
		
   // Calculate average
   average = sum / DAYS_IN_WEEK;
   
   // This is the work done in the endOfJob() function
   // Output average	
   cout << "Average Rainfall amount is " << average << endl;
   return 0; 
} // End of main()


