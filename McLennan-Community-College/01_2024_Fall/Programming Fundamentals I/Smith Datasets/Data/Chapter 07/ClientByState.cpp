// ClientByState.cpp - This program creates a report that lists
// clients with a count of the number of clients for each state. 
// Input:  client.dat
// Output:  Report

#include <fstream>
#include <iostream>
#include <string>
using namespace std;

int main() 
{
   // Declarations
   ifstream fin;
   const string TITLE = "\n\nCompany Clients by State of Residence\n\n";    	
   string name = "", city = "", state = "";
   int count = 0; 
   string oldState = "";
   bool done; 

   fin.open("client.dat"); 								
   // This is the work done in the getReady() function		
   cout << TITLE << endl;
   fin >> name;
   if(!(fin.eof()))
   {
      fin >> city;
      fin >> state;
      done = false;
      oldState = state;
   }
   else
      done = true; 
   while(done == false)
   {
      // This is the work done in the produceReport() function
      if(state != oldState)
      {
         // This is the work done in the controlBreak() function
	 cout << "\t\t\tCount for " << oldState << " " << count << endl;
	 count = 0;
	 oldState = state;
      }
      cout << name << " " << city << " " << state << endl;
      count++;
      fin >> name;
      if(!(fin.eof()))
      {
         fin>> city;
         fin >> state;
	 done = false;
      }
      else
	 done = true; 
   }
   // This is the work done in the finishUp() function		
   cout << "\t\t\tCount for " << oldState << " " << count << endl;
   fin.close();
			
   return 0;
} // End of main() 

