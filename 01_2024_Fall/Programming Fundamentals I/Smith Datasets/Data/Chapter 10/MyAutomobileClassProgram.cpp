// This program uses the programmer-defined Automobile class. 
#include "Automobile.cpp"
#include <iostream>
using namespace std; 
int main()
{
   Automobile automobileOne;
   bool convertible; 
   
   automobileOne.setMaxSpeed(100.0);
   automobileOne.setSpeed(35.0);
   automobileOne.accelerate(10.0);
   cout << "The current speed is " << automobileOne.getSpeed() << endl;

   automobileOne.accelerate(60.0);
   cout << "The current speed is " << automobileOne.getSpeed() << endl;

   automobileOne.setConvertibleStatus(true);
   convertible = automobileOne.getConvertibleStatus(); 

   if(convertible == true)
      cout << "This automobile is a convertible" << endl; 
   else
      cout << "This automobile is not a convertible" << endl; 
   
   return 0;
}
