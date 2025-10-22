#include <iostream>
#include <chrono>   // Para durações de tempo
#include <thread>   // Para a função sleep_for

using namespace std;

int main() {
    setlocale(LC_ALL, "pt_BR.UTF-8");
    std::cout << "Eu caminhei com a luz do sol" << std::endl;

    // Pausa a execução por 3 segundos
    std::this_thread::sleep_for(std::chrono::milliseconds(3500));

    std::cout << "Iluminei igual o dia" << std::endl;

    // Pausa a execução por 500 milissegundos (meio segundo)
    std::this_thread::sleep_for(std::chrono::milliseconds(3500));

    std::cout << "Eu vi o amor virar o mal" << std::endl;

    std::this_thread::sleep_for(std::chrono::seconds(4));

    std::cout << "E mesmo assim não me escondia" << std::endl;

    std::this_thread::sleep_for(std::chrono::milliseconds(2500));

    std::cout << "Covardes," << std::endl;

    std::this_thread::sleep_for(std::chrono::milliseconds(1000));

    std::cout << "Falo pros covardes" << std::endl;

    std::this_thread::sleep_for(std::chrono::milliseconds(1800));

    std::cout << "Que suas vontades" << std::endl;

    std::this_thread::sleep_for(std::chrono::milliseconds(1500));

    std::cout << "Não ferem quem tem FÉ" << std::endl;

    std::this_thread::sleep_for(std::chrono::seconds(1));

    return 0;
}
