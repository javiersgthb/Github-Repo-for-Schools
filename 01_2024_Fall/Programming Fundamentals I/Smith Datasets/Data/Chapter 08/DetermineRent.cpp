#include <iostream>
using namespace std;

int main() 
{
   // Declare variables.
   const int FLOORS = 5;
   const int BEDROOMS = 3; 
   double rent[FLOORS][BEDROOMS] = {{350, 390, 435}, 
				    {400, 440, 480},
				    {475, 530, 575},
				    {600, 650, 700},
				    {1000, 1075, 1150}}; 
   int floor;   
   int bedroom;
   string floorString;
   string bedroomString;
   int QUIT = 99;
				
   // Work done in the getReady() function
   cout << "Enter floor or 99 to quit: ";
   cin >> floor;
   while(floor != QUIT)
   {	
      // Work done in the determineRent() function
      cout << "Enter number of bedrooms: ";
      cin >> bedroom;
      cout << "Rent is $" << rent[floor][bedroom] << endl;
      cout << "Enter floor or 99 to quit: ";
      cin >> floor;		
   }
   // Work done in the finish() function
   cout << "End of program" << endl;
   return 0;
} // End of main() function


