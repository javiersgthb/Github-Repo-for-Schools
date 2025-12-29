#include <iostream>
using namespace std;
int main()
{
       int originalNumber;
       int calculatedAnswer;
       cout << "Enter a number to double or 0 to end: " << endl; 
       cin >> originalNumber;
       while(originalNumber != 0)
       {
         calculatedAnswer = originalNumber * 2;
         cout << originalNumber << " doubled is " 
	      << calculatedAnswer << endl;
         cout << "Enter a number to double or 0 to end: " << endl; 
         cin >> originalNumber;

       }
       return 0; 
}
