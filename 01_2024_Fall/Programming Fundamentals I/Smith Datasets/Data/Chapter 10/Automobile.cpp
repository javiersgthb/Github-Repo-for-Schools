// Automobile.cpp
#include "Vehicle.cpp"
#include <iostream>
using namespace std; 
class Automobile : public Vehicle
{
   public: 
      void accelerate(double); 
      void setConvertibleStatus(bool);
      bool getConvertibleStatus();
   private:	
      bool convertibleStatus; 
}; 

void Automobile::accelerate(double mph)
{
   if(getSpeed() + mph > getMaxSpeed())
      cout << "This automobile cannot go that fast" << endl; 
   else
      setSpeed(getSpeed() + mph);
}

void Automobile::setConvertibleStatus(bool status)
{
   convertibleStatus = status;
   return;
}

bool Automobile::getConvertibleStatus()
{
   return convertibleStatus;
}

