#include <iostream>
#include <string>
using namespace std;
int main()
{
      int item, badItemCount = 0;
      double price; 
      const int SIZE = 6;
      int VALID_ITEMS[] = {106, 108, 307, 405, 457, 688};
      double VALID_PRICES[] = {0.59, 0.99, 4.50, 15.99, 17.50, 39.00};
      int sub;
      bool foundIt = false;
      const string MSG_YES = "Item Available";
      const string MSG_NO = "Item not found";
      const int FINISH = 999;
		
      // This is the work done in the getReady() function
      cout << "Enter next item number or " << FINISH << " to quit ";
      cin >> item;
		
      while(item != FINISH)
      {
         // This is the work done in the findItem() function
         foundIt = false;
         sub = 0;
         while(sub < SIZE)
         {
            if(item == VALID_ITEMS[sub])
            {
               foundIt = true;
               price = VALID_PRICES[sub];
            }
            sub++;
         }
         if(foundIt == true)
         {
            cout << MSG_YES << endl;
            cout << "The price of " << item << 
                               " is " << price << endl;
         }
         else
         {
            cout << MSG_NO << endl;
            badItemCount++;
         }
         cout << "Enter next item number or " << FINISH << " to quit ";
         cin >> item;
      }
      // This is the work done in the finishUp() function
      cout << badItemCount << " items had invalid numbers" << endl;
      return 0;
   
}
