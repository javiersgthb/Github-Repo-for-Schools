#include <iostream>
#include <iomanip>
using namespace std;
int main()
{
   double value = 3.14159;
   cout << value << endl;
   cout << setprecision(1) << value << endl; 
   cout << setprecision(2) << value << endl; 
   cout << setprecision(3) << value << endl; 
   cout << setprecision(4) << value << endl; 
   cout << setprecision(5) << value << endl; 
   cout << setprecision(6) << value << endl; 
   return 0;
}