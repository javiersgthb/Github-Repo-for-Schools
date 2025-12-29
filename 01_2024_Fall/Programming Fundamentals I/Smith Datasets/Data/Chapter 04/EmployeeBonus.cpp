// EmployeeBonus.cpp - This program calculates an employee's yearly bonus. 

#include <iostream>
#include <string>
using namespace std;
int main()
{
   // Declare and initialize variables here
   string employeeFirstName; 
   string employeeLastName;
   double numTransactions;
   double numShifts;
   double dollarValue;
   double score;
   double bonus;
   const double BONUS_1 = 50.00;
   const double BONUS_2 = 75.00;
   const double BONUS_3 = 100.00; 
   const double BONUS_4 = 200.00;
   
   // This is the work done in the housekeeping() function			
   cout << "Enter employee's first name: ";
   cin >> employeeFirstName;
   cout << "Enter employee's last name: ";
   cin >> employeeLastName;
   cout << "Enter number of shifts: ";
   cin >> numShifts;
   cout << "Enter number of transactions: ";
   cin >> numTransactions; 
   cout << "Enter dollar value of transactions: ";
   cin >> dollarValue; 

   // This is the work done in the detailLoop()function
   // Write your code here
	
   // This is the work done in the endOfJob() function
   // Output.  
   cout << "Employee Name: " << employeeFirstName << " " << employeeLastName << endl;
   cout << "Employee Bonus: $" << bonus << endl;
   return 0;
} 	
