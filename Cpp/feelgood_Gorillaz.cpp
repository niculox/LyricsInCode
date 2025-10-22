#include <iostream>
#include <chrono>   
#include <thread>   
#include <string>

using namespace std;

int main() {
    std::string line1 = "City's breaking down on a camel's back";
    std::string line2 = "They just have to go 'cause they don't know wack";
    std::string line3 = "So while you fill the streets, it's appealing to see";
    std::string line4 = "You won't get undercounted 'cause you're damned and free";
    std::string line5 = "You've got a new horizon, it's ephemeral style";
    std::string line6 = "A melancholy town where we never smile";
    std::string line7 = "And all I wanna hear is the message beep";
    std::string line8 = "My dreams, they got her kissing, 'cause I don't get sleep, no";

    for(int a = 0;a<line1.length();a++){
        cout<<line1[a];
        this_thread::sleep_for(chrono::milliseconds(50));
    }

    this_thread::sleep_for(chrono::milliseconds(800));

    cout<<endl;

    for(int b = 0;b<line2.length();b++){
        cout<<line2[b];
        this_thread::sleep_for(chrono::milliseconds(50));
    }

    this_thread::sleep_for(chrono::milliseconds(800));

    cout<<endl;

    for(int d = 0;d<line3.length();d++){
        cout<<line3[d];
        this_thread::sleep_for(chrono::milliseconds(50));
    }

    cout<<endl;

    for(int f = 0;f<line4.length();f++){
        cout<<line4[f];
        this_thread::sleep_for(chrono::milliseconds(40));
    }

    cout<<endl;

    for(int g = 0;g<line5.length();g++){
        cout<<line5[g];
        this_thread::sleep_for(chrono::milliseconds(50));
    }

    cout<<endl;

    for(int h = 0;h<line6.length();h++){
        cout<<line6[h];
        this_thread::sleep_for(chrono::milliseconds(50));
    }

    cout<<endl;

    for(int i = 0;i<line7.length();i++){
        cout<<line7[i];
        this_thread::sleep_for(chrono::milliseconds(50));
    }

    cout<<endl;

    for(int j = 0;j<line8.length();j++){
        cout<<line8[j];
        this_thread::sleep_for(chrono::milliseconds(50));
    }

    cout<<endl;
}


/*
    cout<<" o "<<endl;
    cout<<"(|)"<<endl;
    cout<<"/ |"<<endl<<endl;

    cout<<"(o "<<endl;
    cout<<" |)"<<endl;
    cout<<"/ |"<<endl<<endl;

    cout<<" o)"<<endl;
    cout<<"(| "<<endl;
    cout<<"/ |"<<endl<<endl;
*/