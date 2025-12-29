// PointerPractice.cpp - This program demonstrates pointers.
// Input:  None
// Output:  Values of variables
#include <iostream>
using namespace std;

int main() 
{
   int num = 777;
   int* ptr_num; 

   ptr_num = &num;  // Assigns address of num to ptr_num

   cout << "Value of num is: " << num << endl;

   cout << "Value of num is: " << *ptr_num << endl;

   cout << "Address of num is: " << &num << endl;

   cout << "Address of num is: " << ptr_num << endl;

   cout << "Address of ptr_num is: " << &ptr_num << endl;

   return 0;
} // End of main() function

