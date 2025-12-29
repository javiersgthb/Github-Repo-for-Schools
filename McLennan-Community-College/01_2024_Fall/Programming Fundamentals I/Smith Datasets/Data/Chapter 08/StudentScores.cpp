// StudentScores.cpp - This program interactively reads a 
// variable number of student test scores, stores the 
// scores in an array, and then sorts the scores in
// ascending order. 
// Input:  Interactive
// Output:  Sorted list of student scores 

#include <iostream>
using namespace std;

int main()
{
   // Declare variables
   // Maximum size of array
   const int SIZE = 100;		
   // Array of student scores
   int scores[SIZE];   
   int x;
   int temp;
   // Actual number of elements in array
   int numberOfEls = 0; 	      
   int comparisons;
   const int QUIT = 999;
   bool didSwap;
		
   // Work done in the fillArray function
   x = 0;
   cout << "Enter a score or " << QUIT << " to quit ";
   cin >> scores[x]; 
   x++;	
   while(x < SIZE && scores[x-1] != QUIT)   
   {
      cout << "Enter a score or " << QUIT << " to quit ";
      cin >> scores[x]; 
      x++;
   }  // End of input loop
   numberOfEls = x-1;
   comparisons = numberOfEls -1;

   // Work done in the sortArray() function
   didSwap = true;	// Set flag to true
   // Outer loop controls number of passes over data
   while(didSwap == true) // Test flag
   {
      x = 0;
      didSwap = false;
      // Inner loop controls number of items to compare
      while(x < comparisons)
      {
         if(scores[x] > scores[x+1]) // Swap?
         {
            // Work done in the swap() function
            temp = scores[x + 1];
            scores[x+1] = scores[x];
            scores[x] = temp;
            didSwap = true;
         }
         x++;   // Get ready for next pair
      }
      comparisons--;
   } 

		
   // Work done in the displayArray() function
   x = 0;
   while(x < numberOfEls)
   {
      cout << scores[x] << endl;
      x++;
   }
   return 0;
} // End of main() function 


