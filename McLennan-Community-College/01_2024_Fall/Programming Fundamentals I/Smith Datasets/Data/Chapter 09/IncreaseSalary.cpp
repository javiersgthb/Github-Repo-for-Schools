// IncreaseSalary.cpp - This program demonstrates pass by reference.
// Input:  None
// Output:  Beginning salary along with new salary 
#include <iostream>
using namespace std;

void increase(double, double, double&); 
int main() 
{
   double salary = 50000.00;
   double raise = .15;
   double new_salary;
   
   cout << "Salary is: " << salary << endl;

   // Call the increase function; the variables salary and raise
   // are passed by value, the variable new_salary is passed by    
   // reference. 	 
   increase(salary, raise, new_salary);

   cout << "New salary is: " << new_salary << endl;
   return 0;
} // End of main() function

void increase(double amt, double pcnt, double& new_sal)
{
   // Changes the value of new_salary in the main function
   new_sal = amt * (1 + pcnt);
   return;
}