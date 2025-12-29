// ChangeCase.cpp - This program converts characters to lowercase and uppercase.
// Input:  Interactive
// Output:  Uppercase and lowercase versions of the user-entered string
#include <iostream>
#include <string>
using namespace std;

int main() 
{
   const int LEN = 9;
   char sample1[LEN];
   char sample2[LEN];
   char result1;
   char result2;
   int i; 

   cout << "Enter 9 lowercase characters: ";
   for(i = 0; i < LEN; i++)		 
   {
      cin >> sample1[i];

      // Convert sample1[i] to uppercase and assign it to result1

      cout << result1 << endl;
   }
   cin.ignore(256,'\n');
   cout << "Enter 9 uppercase characters: ";
   for(i = 0; i < LEN; i++)		 
   {
      cin >> sample2[i];

      // Convert sample2[i] to lowercase and assign it to result2

      cout << result2 << endl;
   }
   cin.ignore(256,'\n');
   return 0;

} // End of main() function

