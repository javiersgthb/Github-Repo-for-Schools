#include <iostream>
#include <string>
using namespace std;

int main()
{
   double target[3];
   double source[] = {1.0, 5.5, 7.9};
   int loopIndex; 
   // Copy values from source to target
   for(loopIndex = 0; loopIndex < 3; loopIndex++)
      target[loopIndex] = source[loopIndex];
   // Assign values to two elements of target
   target[0] = 2.0;
   target[1] = 4.5;
   // Print values stored in source and target 
   for(loopIndex = 0; loopIndex < 3; loopIndex++)
   {
      cout << "Source " << source[loopIndex] << endl;
      cout << "Target " << target[loopIndex] << endl;
   }
}

