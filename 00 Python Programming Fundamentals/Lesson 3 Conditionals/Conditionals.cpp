#include <iostream>
using namespace std;
/*
Created by Jonatan Gomez Garcia on 04-01-2024
*/


int main() {
int userData;

cout << "Input the number 2: ";
cin >> userData;


   if(userData == 2){
    //First condition is true
    cout << "Thanks for input the number 2" << endl;
   } else if (userData < 0)
    //Second condition is true
    cout << "You have been inputted a negative number" << endl;
   else {
    //If both condition are false
    cout << "Case not supported by condition" << endl;
   }

    return 0;
}