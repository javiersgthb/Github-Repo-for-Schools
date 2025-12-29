// HouseholdSize.cpp - This program uses a bubble sort to arrange up to 300 household sizes in
// descending order and then prints the mean and median household size. 
// Input:  Interactive.
// Output:  Mean and median household size. 

#include <iostream>
#include <string>
using namespace std;

int main() 
{
   // Declare variables.
		
   const int SIZE = 300;	// Number of household sizes
   int householdSizes[SIZE];   	// Array used to store 300 household sizes
   int x; 
   int limit = SIZE;
   int householdSize = 0;
   int pairsToCompare;
   bool switchOccurred; 
   int temp;
   double sum = 0;
   double mean = 0;
   int median = 0;

   // Input household size		
   cout << "Enter household size or 999 to quit: ";
   cin >> householdSize;
   
   // This is the work done in the fillArray() function
   x = 0;
   while(x < limit && householdSize != 999)   
   {
      // Place value in array.
      householdSizes[x] = householdSize;
      // Calculate total of household sizes
      
      x++;    // Get ready for next input item.
      cout << "Enter household size or 999 to quit: ";
      cin >> householdSize;
   }  // End of input loop.
		
   
   // Find the mean
   
   // This is the work done in the sortArray() function

   // This is the work done in the displayArray() function

   // Print the mean

   // Find the median
   
   // Print the median
    		
   return 0;
} // End of main function






