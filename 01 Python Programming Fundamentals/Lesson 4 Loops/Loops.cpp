#include <iostream>
using namespace std;
/*
Created by Jonatan Gomez Garcua on 05-01-2024
*/


int main() {
    //Mainly intended for searches
    int count = 0;
    bool found = false;
    while(count < 5 && !found){
        cout << "Round number while loop " << count << endl;
        
        //Exit condition
        if (count == 3){ 
            found = true; 
            cout << "3 is found " << endl;
        }

        count ++;
    }

    //Mainly intended for go over
    for(int i = 0; i < 5; i++){
        cout << "Round number for loop " << i << endl;
    }

        count = 0;
        found = false;
    do{
        cout << "Round number do-while loop " << count << endl;
        //Exit condition
        if (count == 3){ 
            found = true; 
            cout << "3 is found " << endl;
        }

        count ++;
    } while (count < 5 && !found);

    return 0;
}