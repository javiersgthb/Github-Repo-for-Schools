// Employee.cpp
#include <string>
using namespace std;
class Employee
{
   public: 
      void setLastName(string);
      void setHourlyWage(double);
      double getHourlyWage();
      double getWeeklyPay();
      string getLastName();
   private:	
      string lastName;
      double hourlyWage;
      double weeklyPay;
      void calculateWeeklyPay();
}; // You end a class definition with a semicolon

void Employee::setLastName(string name)
{
   lastName = name;
   return;
}
void Employee::setHourlyWage(double wage)
{
   hourlyWage = wage;
   calculateWeeklyPay();
   return;
}
string Employee::getLastName()
{
   return lastName;
}
double Employee::getHourlyWage()
{
   return hourlyWage;
}
double Employee::getWeeklyPay()
{
   return weeklyPay;
}
void Employee::calculateWeeklyPay()
{
   const int WORK_WEEK_HOURS = 40;
   weeklyPay = hourlyWage * WORK_WEEK_HOURS;
   return;
}
