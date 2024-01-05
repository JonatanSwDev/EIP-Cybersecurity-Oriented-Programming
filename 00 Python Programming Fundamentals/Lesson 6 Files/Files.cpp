#include <iostream>
#include <fstream>
using namespace std;
/*
Created by Jonatan Gomez Garcia on 05-01-2024
*/

int main() {
    ifstream fileIn;
    ofstream fileOut;
    string word = "";
    string text = "";

    //Process to read word by word
    fileIn.open("Text to read.txt");
    if (fileIn.is_open()){
        fileIn >> word;
        cout << "Word: " << word << endl;
        fileIn >> word;
        cout << "Word: " << word << endl << endl;
        
    }
    fileIn.close();
    
    //Process to read line by line
    fileIn.open("Text to read.txt");
    if (fileIn.is_open()){
        while(getline(fileIn, text)){
                cout << text <<  endl;
            }
    }

    //Process to write
    fileOut.open("Text to write.txt");
    if (fileOut.is_open()){
        fileOut << "I am writting into the Text to write.txt";
    }
    fileOut.close();


    return 0;
}