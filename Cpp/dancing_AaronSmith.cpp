#include <iostream>
#include <chrono>   
#include <thread>   

using namespace std;

int main() {

    std::cout << "All the time" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(1400));

    std::cout << "My baby, you on my mind" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(2000));

    std::cout << "And I don't know why" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(2000));

    std::cout << "Yeah, but the feeling is fine" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(2500));

    std::cout << "Can't you see?" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(1500));

    std::cout << "Yo' honey you are for me, oh" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(2500));

    std::cout << "We were meant to be" << std::endl;
    std::this_thread::sleep_for(std::chrono::milliseconds(4000));

}
