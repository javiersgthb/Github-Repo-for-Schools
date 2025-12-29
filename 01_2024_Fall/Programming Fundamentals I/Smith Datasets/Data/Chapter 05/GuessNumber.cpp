// GuessNumber.cpp - This program allows a user to guess a number between 1 and 10. 
// Input:  User guesses numbers until they get it right 
// Output: Tells users if they are right or wrong 

#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
using namespace std;

int main()
{
		
   int number; 	// Number to be guessed
   int userNumber;	// User's guess
   string keepGoing;  // Contains a "Y" or "N" determining if the user wants to continue

   // This is the work done in the detailLoop() function
   srand((unsigned)time(NULL)); 
   number = (rand() % 10) + 1; // Generate random number
   	
   // Prime the loop
   cout << "Do you want to guess a number? Enter Y or N: ";
   cin >> keepGoing;

   // Validate input
   


		
   // Enter loop if they want to play
   while(keepGoing == "Y")
   {
      // Get user's guess
      cout << "I'm thinking of a number. .\n Try to guess by entering a number between 1 and 10: ";
      cin >> userNumber; 
      // Validate input
      


      // Test to see if the user guessed correctly
      if(userNumber == number)
      {
         keepGoing = "N"; 
         cout << "You are a genius. That's correct!";
      }
      else
      {
         cout << "That's not correct. Do you want to guess again? Enter Y or N: ";
         cin >> keepGoing;
         // Validate input
           


      }
   } // End of while loop
   return 0;
} // End of main()
	

