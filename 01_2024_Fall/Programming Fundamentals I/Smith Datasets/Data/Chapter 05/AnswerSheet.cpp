// AnswerSheet.cpp - This program prints a quiz answer sheet.
// Input:  None.
// Output: Answer Sheet.


#include <iostream>
#include <string>
using namespace std;

int main()
{
   string quizName; 		
   int partCounter;
   int questionCounter;
   const int PARTS = 5;
   const int QUESTIONS = 3;
   const string QUIT = "ZZZ";
   const string PART_LABEL = "Part ";
   const string LINE = ". _____";
   
   // This is the work done in the housekeeping() function
   cout << "Enter quiz name or " << QUIT << " to quit: ";
   cin >> quizName;
  
   // This is the work done in the detailLoop() function 
   while(quizName!= QUIT)
   {
      cout << quizName << endl;
      partCounter = 1;
      while(partCounter <= PARTS)
      {
         cout << PART_LABEL << partCounter << endl;
         questionCounter = 1;
         while(questionCounter <= QUESTIONS)
         {
            cout << questionCounter << LINE << endl;
            questionCounter++;
         }
         partCounter++;
      }
      cout << "Enter quiz name or " << QUIT << " to quit: ";
      cin >> quizName;	
   }
   // This is the work done in the endOfJob() function
   return 0;
} // End of main() 


