// GrossPay.cpp - This program computes an employee's gross pay. 
// Input:  Interactive
// Output:  The employee's hours worked and their gross pay 

#include <iostream>
#include <string>
using namespace std;
double getHoursWorked();

int main() 
{
   double hours;	
   const double PAY_RATE = 12.00;	
   double gross;
		     	
   hours = getHoursWorked();
   gross = hours * PAY_RATE;
		
   cout << "Hours worked: " << hours << endl;
   cout << "Gross pay is: " << gross << endl;
	
   return 0;
} // End of main() function
	
double getHoursWorked()
{
   double workHours;

   cout << "Please enter hours worked: ";
   cin >> workHours; 
		
   return workHours;
} // End of getHoursWorked function

