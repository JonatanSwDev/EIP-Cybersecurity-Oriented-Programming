#include <iostream>
using namespace std;
/*
Created by Jonatan Gomez Garcia on 05-01-2024
*/

const int MAX = 10;
typedef int tNumbers[MAX];

int main() {
    tNumbers numbersEven;
    tNumbers numbersOdd;

    numbersEven[0] = 0;
    numbersEven[1] = 2;
    numbersEven[2] = 4;
    numbersEven[3] = 6;
    numbersOdd[0] = 1;
    numbersOdd[1] = 3;
    numbersOdd[2] = 5;
    numbersOdd[3] = 7;

    for(int i = 0; i < 4; i++){
        cout << "Even number " << numbersEven[i] << endl; 
        cout << "Odd number " << numbersOdd[i] << endl; 
    }

   
    return 0;
}