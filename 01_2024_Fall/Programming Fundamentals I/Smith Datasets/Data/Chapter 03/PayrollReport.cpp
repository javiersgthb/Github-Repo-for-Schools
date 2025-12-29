#include <iostream>
#include <string>
using namespace std;
int main()
{
   // Declare variables and constants local to main
   string name;
   double gross, deduct, net;
   const double RATE = 0.25;
   const string QUIT = "XXX";
   const string REPORT_HEADING = "Payroll Report";
   const string END_LINE = "**End of report";
   // Work done in the housekeeping() function
   cout << REPORT_HEADING << endl; 
   cout << "Enter employee's name: ";
   cin >> name;
   while(name != QUIT)
   {
         // work done in the detailLoop() function
         cout << "Enter employee's gross pay: ";
         cin >> gross;
         deduct = gross * RATE; 
         net = gross - deduct;
         cout << "Name: " << name  << endl;
         cout << "Gross Pay: " << gross << endl;
         cout << "Deductions: " << deduct <<endl;
         cout << "Net Pay: " << net << endl;
         cout << "Enter employee's name: ";
         cin >> name;
   }
      // work done in the endOfJob() function
    cout << END_LINE;
    return 0;
} // End of main function
