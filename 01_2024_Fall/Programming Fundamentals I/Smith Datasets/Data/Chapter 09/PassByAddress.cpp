// PassByAddress.cpp - This program demonstrates pass by address.
// Input:  None
// Output:  Values of variables
#include <iostream>
using namespace std;

void swap(int*, int*);

int main() 
{
   int num1 = 5;
   int num2 = 10;
   
   cout << "Value of num1 is: " << num1 << endl;

   cout << "Value of num2 is: " << num2 << endl;

   swap(&num1, &num2);

   cout << "Value of num1 is: " << num1 << endl;

   cout << "Value of num2 is: " << num2 << endl;

   return 0;
} // End of main() function

void swap(int* val1, int* val2)
{
   int temp;
   temp = *val1;
   *val1 = *val2;
   *val2 = temp; 
} 