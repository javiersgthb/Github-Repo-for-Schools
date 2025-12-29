// PassEntireArray.cpp - This program quadruples the values stored in an array. 
// Input:  None
// Output:  The original values and the quadrupled values 

#include <iostream>
#include <string>
using namespace std;

void quadrupleTheValues(int[]);
int main() 
{
   const int LENGTH = 4; 	
   int someNums[] = {10, 12, 22, 35};
   int x; 

   cout << "At beginning of main function. . . " << endl;
   x = 0;
   while (x < LENGTH)
   {
      cout << someNums[x] << endl;
      x++;
   }
   quadrupleTheValues(someNums);
   cout << "At the end of main function. . . " << endl;
   x = 0;
   while (x < LENGTH)
   {
      cout << someNums[x] << endl;
      x++;
   }
   return 0;
} // End of main() function
	
void quadrupleTheValues(int vals[])
{
   const int LENGTH = 4;
   int x;

   x = 0;
   while(x < LENGTH)
   {
      cout << " In quadrupleTheValues() function, value is " << vals[x] << endl;
      x++;
   }
   x = 0;
   while(x < LENGTH)
   {
      vals[x] = vals[x] * 4;
      x++;
   }
   x = 0;
   while(x < LENGTH)
   {
      cout << "  After change, value is " << vals[x] << endl;
      x++;
   }
   return;
} // End of quadrupleTheValues function
