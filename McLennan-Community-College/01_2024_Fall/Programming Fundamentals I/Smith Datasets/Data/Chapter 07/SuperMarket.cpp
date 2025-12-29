// SuperMarket.cpp - This program creates a report that lists weekly hours worked 
// by employees of a supermarket. The report lists total hours for 
// each day of one week. 
// Input:  Interactive
// Output: Report. 

#include <iostream>
#include <string>
using namespace std;
int main() 
{
   // Declare variables.
   const string HEAD1 = "WEEKLY HOURS WORKED";
   const string DAY_FOOTER = "                                Day Total ";
   // Leading spaces in DAY_FOOTER are intentional.
   const string SENTINEL = "done";		        // Named constant for sentinel value. 
   double hoursWorked = 0;       		        // Current record hours.
   string dayOfWeek;			                // Current record day of week.
   double hoursTotal = 0;      		                // Hours total for a day.
   string prevDay = ""; 		   		// Previous day of week.
   bool notDone = true;				        // loop control
  
   // Print two blank lines.
   cout << endl << endl; 
   // Print heading.
   cout << "\t\t\t\t\t" << HEAD1 << endl;
   // Print two blank lines.
   cout << endl << endl;  

   // Read first record 
   cout << "Enter day of week or done to quit: ";
   cin >> dayOfWeek;
   if(dayOfWeek  == SENTINEL)
      notDone = false;
   else
   {
      cout << "Enter hours worked: ";
      cin >> hoursWorked;
      prevDay = dayOfWeek;
   }	   
		
   while(notDone == true)
   {	
      // Implement control break logic here
      // Include work done in the dayChange() function
   }
   cout << "\t\t" << DAY_FOOTER << hoursTotal << endl;
					
   return 0;

} // End of main() 
	


