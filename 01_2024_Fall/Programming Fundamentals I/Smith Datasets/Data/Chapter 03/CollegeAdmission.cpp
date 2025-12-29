/* Program Name: CollegeAdmission.cpp 
   Function: This program determines if a student will be admitted or rejected. 
   Input:  Interactive
   Output: Accept or Reject
*/  

#include <iostream>
using namespace std;
int main()
{ 
   // Declare variables
   
     
   // Prompt for and get user input 
   
   
   // Test using admission requirements and print Accept or Reject 
   if(testScore >= 90)
   {
      if(classRank >= 25)
      {
         cout << "Accept" << endl;
      }
      else
	 cout << "Reject" << endl; 
   }
   else 
   {
      if(testScore >= 80)
      {
         if(classRank >= 50)
	    cout << "Accept" << endl;
	 else
	    cout << "Reject" << endl;
      }
      else
      {
         if(testScore >= 70)
	 {
            if(classRank >=75) 
               cout << "Accept" << endl;
            else
               cout << "Reject" << endl;
	 }
	 else
            cout << "Reject" << endl;
      }
   }

}  //End of main() function
    

