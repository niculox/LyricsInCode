#include <iostream>
#include <chrono>   
#include <thread>   
#include <string>

using namespace std;

void Letters(string text, int mseconds, int delay){

    for(int i=0;i<text.length();i++){
        cout<<text[i];
        this_thread::sleep_for(chrono::milliseconds(mseconds));
    }
    this_thread::sleep_for(chrono::milliseconds(delay));

    cout<<endl;

}

int main() {
    std::string line1 = "City's breaking down on a camel's back";
    std::string line2 = "They just have to go 'cause they don't know wack";
    std::string line3 = "So while you fill the streets, it's appealing to see";
    std::string line4 = "You won't get undercounted 'cause you're damned and free";
    std::string line5 = "You've got a new horizon, it's ephemeral style";
    std::string line6 = "A melancholy town where we never smile";
    std::string line7 = "And all I wanna hear is the message beep";
    std::string line8 = "My dreams, they got her kissing, 'cause I don't get sleep, no";

    Letters(line1, 60, 800);
    Letters(line2, 50, 800);
    Letters(line3, 40, 800);
    Letters(line4, 40, 800);
    Letters(line5, 60, 800);
    Letters(line6, 50, 800);
    Letters(line7, 50, 800);
    Letters(line8, 50, 800);

    return 0;

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