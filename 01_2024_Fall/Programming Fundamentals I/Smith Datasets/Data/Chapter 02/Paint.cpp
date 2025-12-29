// This calculates the number of gallons of paint needed. 
#include <iostream>
using namespace std;
int main()
{
   double height1 = 9;
   double height2 = 9;
   int width1 = 19.5;
   double width2 = 20.0;
   double squareFeet;
   int numGallons;
   numGallons = squareFeet / 150;
   squareFeet = (width1 * height1 + width2 * height2) * 2;
   cout << "Number of Gallons: " << numGallons << endl;
   return 0;
}
