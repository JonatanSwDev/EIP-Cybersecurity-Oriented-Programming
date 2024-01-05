#include <iostream>
#include <fstream>
using namespace std;
/*
Created by Jonatan Gomez Garcia on 05-01-2024
*/

//Declare functions
void count();
int sum(int num1, int num2);

int main() {
    //Count
    count();
    cout << "2 + 5 = " << sum(2, 5) << endl;
    cout << "END" << endl;
    return 0;
}

////Initialize functions////
void count(){
    int count = 0;
    while(count <5){
        cout << "I count " << count << endl;
        count++;
    }
}

int sum(int num1, int num2){
    return num1 + num2;
}

