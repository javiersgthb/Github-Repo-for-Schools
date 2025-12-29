// This program uses the programmer-defined Vehicle class. 
#include "Vehicle.cpp"
#include <iostream>
using namespace std; 
int main()
{
   Vehicle vehicleOne;
   
   vehicleOne.setMaxSpeed(100.0);
   vehicleOne.setSpeed(35.0);
   vehicleOne.accelerate(10.0);
   cout << "The current speed is " << vehicleOne.getSpeed() << endl;

   vehicleOne.accelerate(60.0);
   cout << "The current speed is " << vehicleOne.getSpeed() << endl;
   
   return 0;
}
