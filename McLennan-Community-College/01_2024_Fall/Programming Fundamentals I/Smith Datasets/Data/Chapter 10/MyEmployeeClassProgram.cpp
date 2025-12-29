// This program uses the programmer-defined Employee class. 
#include "Employee.cpp"
#include <iostream>
using namespace std;

int main()
{
      const double LOW = 9.00;
      const double HIGH = 14.65;
      Employee myGardener;

      myGardener.setLastName("Greene");
      myGardener.setHourlyWage(LOW);
      cout << "My gardener makes " << myGardener.getWeeklyPay() << " per week." << endl;

      myGardener.setHourlyWage(HIGH);
      cout << "My gardener makes " << myGardener.getWeeklyPay() << " per week." << endl;
      return 0;
}
