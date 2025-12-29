// fileIOTest.cpp 
// Input:  inputFile.dat
// Output: outputFile.dat

#include <fstream>
#include <iostream>
#include <string>
using namespace std;
int main()
 {
   string firstName; 
   string lastName;
   double salary;
   double new_salary;
   const double INCREASE = 1.15; 
   ifstream data_in;
   ofstream data_out;

   // Open input and output file
   data_in.open("inputFile.dat");
   data_out.open("outputFile.dat");

   // Read record from input file
   data_in >> firstName; 
   data_in >> lastName;
   data_in >> salary;
   // Calculate new salary
   new_salary = salary * INCREASE;
   // Write record to output file
   data_out << firstName << endl;
   data_out << lastName << endl;
   data_out << new_salary << endl;
   // Close files
   data_in.close();
   data_out.close();
   return 0;
} // End of main function
