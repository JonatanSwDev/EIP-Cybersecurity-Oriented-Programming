#include <iostream>
using namespace std;
/*
Created by Jonatan Gomez Garcua on 04-01-2024
*/


int main() {
    int number = 13;
    double decimal = 3.14;
    bool ok = 0;
    char character = 'A';
    string sentence = "Hello World!";
    string userData = "";

    //Get data from User
    cout << "Type Something: ";
    cin >> userData;
    cout << "You have been typed " << userData << endl;

    cout << "Integer: " << number << endl;
    cout << "Decimal: " << decimal << endl;
    cout << "Boolean: " << ok << endl;
    cout << "Character: " << character << endl;
    cout << "String: " << sentence << endl;

    return 0;

}