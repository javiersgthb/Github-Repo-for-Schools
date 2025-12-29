// MovieGuide.cpp - This program allows each theater patron to enter a value from 0 to 4 
// indicating the number of stars that the patron awards to the Guide's featured movie of the 
// week. The program executes continuously until the theater manager enters a negative number to 
// quit. At the end of the program, the average star rating for the movie is displayed.  

#include <iostream>
#include <string>
using namespace std;

int main()
{
		
   // Declare and initialize variables.
   double numStars;         	 // star rating.
   double averageStars;  	 // average star rating.
   double totalStars = 0; 	 // total of star ratings.
   int numPatrons = 0;           // keep track of number of patrons
			
	
   // This is the work done in the housekeeping() function
   // Get input.
   cout << "Enter rating for featured movie: ";
   cin >> numStars; 
				
   // This is the work done in the detailLoop() function
   // Write while loop here    

   // This is the work done in the endOfJob() function
   cout << "Average Star Value: " << averageStars << endl; 
   return 0;
} // End of main() 


