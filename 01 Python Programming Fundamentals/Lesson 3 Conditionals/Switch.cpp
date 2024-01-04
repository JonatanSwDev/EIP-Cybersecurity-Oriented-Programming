#include <iostream>
using namespace std;
/*
Created by Jonatan Gomez Garcua on 04-01-2024
*/


int main() {
int userData;

cout << "Input a number: ";
cin >> userData;

switch(userData){
    case 0:
        cout << "Cero" << endl;
        break;
    case 1:
        cout << "One" << endl;
        break;
    case 2:
        cout << "Two" << endl;
        break;
    default:
        cout << "Case not supported by condition" << endl;
        break;
}
}