#include <iostream>
#include <string>
using namespace std;

int main()
{
   // Declare variables 
   int item, badItemCount = 0;
   const int SIZE = 6;
   int VALID_ITEMS[] = {106, 108, 307, 405, 457, 688};
   int sub;
   bool foundIt = false;
   const string MSG_YES = "Item Available";
   const string MSG_NO = "Item not found";
   const int FINISH = 999;
	
   // This is the work done in the getReady() function	
   // Get user input 
   cout << "Enter item number or " << FINISH << " to quit ";
   cin >> item;
   
   // Loop through array 
   while(item != FINISH)
   {
      // This is the work done in the findItem() function
      foundIt = false;
      sub = 0; 
      while(sub < SIZE)
      {
         // Test to see if this item is a valid item
         if(item == VALID_ITEMS[sub])
            foundIt = true; 	// Set flag to true
         sub += 1; 		// Increment loop index 
      }      
      // Test value of foundIt
      if(foundIt == true)
         cout << MSG_YES << endl;
      else
      {
         cout << MSG_NO << endl;
	 badItemCount++;
      }
      cout << "Enter item number or " << FINISH << " to quit ";
      cin >> item;
   }
   // This is the work done in the finishUp() function
   cout << badItemCount << " items had invalid numbers." << endl;
   return 0;
}


