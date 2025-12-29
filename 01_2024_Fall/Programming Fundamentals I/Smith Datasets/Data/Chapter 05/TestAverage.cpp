// This program calculates an average test score given individual test scores. 
// Input:  Interactive - Student Test Scores
// Output: Number of Students taking the test and the test score average 

#include <iostream>
#include <string>
using namespace std; 
int main()
{
   // Declare variables
   int testScore;
   int numStudents; 
   int stuCount;
   double testTotal;
   double average;
				
   // This is the work done in the housekeeping() function
   // Get user input to control loop
   cout << "Enter number of students: ";
   cin >> numStudents;		
		
   // Initialize accumulator variable to 0
   testTotal = 0; 

   // This is the work done in the detailLoop() function
   // Loop for each student
   for(stuCount = 0; stuCount < numStudents; stuCount++)
   {
      // Input student test score
      cout << "Enter student's score: ";
      cin >> testScore;
      // Accumulate total of test scores
      testTotal += testScore;
   }
   // Calculate average test score
   average = testTotal / stuCount;
   // Output number of students and average test score
   cout << "Number of Students: " << stuCount << endl;
   cout << "Average Test Score: " << average << endl;
		
   return 0;
}



