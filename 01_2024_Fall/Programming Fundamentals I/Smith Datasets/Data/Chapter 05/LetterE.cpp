// LetterE.cpp - This program prints the letter E with 3 asterisks
// across and 5 asterisks down. 
// Input:  None
// Output: Prints the outline of the letter E. 

#include <iostream>
#include <string>
using namespace std;
int main()
{								
   const int NUM_ACROSS = 3; 	// Number of asterisks to print across
   const int NUM_DOWN = 5;	// Number of asterisks to print down
   int row;	// Loop control for row number
   int column;	// Loop control for column number

   // This is the work done in the detailLoop() function
   // Write a loop to control the number of rows.
   // Write a loop to control the number of columns
      // Decide when to print an asterisk in every column.
            cout << "*";
      // Decide when to print asterisk in column 1.   
            cout << "*";
      // Decide when to print a space instead of an asterisk.   
            cout << " "; 
      // Figure out where to place this statement that prints a newline.
      cout << endl;
   }
   
   // This is the work done in the endOfJob() function
   return 0; 
} // End of main()

