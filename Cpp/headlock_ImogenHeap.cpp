#include <iostream>
#include <chrono>   
#include <thread>   
#include <string>

const std::string RESET   = "\033[0m";
const std::string PRETO   = "\033[30m";
const std::string VERMELHO = "\033[31m";
const std::string VERDE   = "\033[32m";
const std::string AMARELO = "\033[33m";
const std::string AZUL    = "\033[34m";
const std::string MAGENTA = "\033[35m";
const std::string CIANO   = "\033[36m";

const std::string NEGRITO  = "\033[1m";
const std::string SUBLINHADO = "\033[4m";
const std::string INVERTER = "\033[7m";
const std::string ITALICO = "\033[3m";

const std::string BG_PRETO   = "\033[40m";
const std::string BG_VERMELHO = "\033[41m";
const std::string BG_VERDE   = "\033[42m";
const std::string BG_AMARELO = "\033[43m";
const std::string BG_AZUL    = "\033[44m";

using namespace std;

void LimparTela() {
#ifdef _WIN32 // Se estiver no Windows
    system("cls");
#else // Senão (Linux, Mac)
    system("clear");
#endif
}

void Letters(string text, int mseconds, int delay, const string& color){

    cout<<color;
    for (size_t i = 0; i < text.length(); i++) {
        cout << text[i] << flush;
        this_thread::sleep_for(chrono::milliseconds(mseconds));
    }
    cout<<RESET;

    this_thread::sleep_for(chrono::milliseconds(delay));

}

void LettersRainbow(string text, int mseconds, int delay){

    const string color[] = {VERMELHO, AMARELO, VERDE, CIANO, AZUL, MAGENTA};
    int countIndCor = 0;

    for(size_t i=0; i<text.length(); i++){
        cout<<color[countIndCor]<<text[i]<<RESET<<flush;
        this_thread::sleep_for(chrono::milliseconds(mseconds));
        countIndCor++;
        if(countIndCor > 5){
            countIndCor = 0;
        }
    }

    this_thread::sleep_for(chrono::milliseconds(delay));

}

void Headlock(string text, int mseconds, int delay){

    const string color[] = {VERMELHO, AMARELO, VERDE, CIANO, AZUL, MAGENTA};
    int countIndCor = 0;
    char espaco = ' ';

    for(size_t i=0; i<text.length(); i++){

        cout<<color[countIndCor]<<text[i]<<RESET<<flush<<endl;

        for(size_t j=0; j<=i; j++){
            cout<<espaco;
        }

        this_thread::sleep_for(chrono::milliseconds(mseconds));
        countIndCor++;

        if(countIndCor > 5){
            countIndCor = 0;
        }

    }

    this_thread::sleep_for(chrono::milliseconds(delay));

}

int main() {

    std::string line1 = "You say too late to start,";
    std::string line2 = "got your heart in a ";
    std::string line3 = "I don't believe any of it";
    std::string line4 = "You say too late to start, with your heart in a ";
    std::string line5 = "HEADLOCK";
    std::string line6 = "You know you're better than this";
    std::string line7 = "Afraid to start, got your heart in a ";

    LimparTela();
    Letters(line1, 65, 0, ITALICO);
    cout<<endl;
    Letters(line2, 60, 0, ITALICO);
    Letters(line5, 50, 1800, VERMELHO + ITALICO);
    cout<<endl;
    LettersRainbow(line3, 45, 1000);
    LimparTela();
    Letters(line4, 60, 0, ITALICO);
    cout<<endl;
    Headlock(line5, 100, 1500);
    cout<<endl;
    Letters(line6, 45, 1500, ITALICO + VERMELHO);
    LimparTela();
    Letters(line7, 65, 0, ITALICO);
    LettersRainbow(line5, 100, 1500);
    cout<<endl;
    Letters(line3, 70, 0, ITALICO + VERMELHO);
    LimparTela();
    Letters(line4, 70, 0, ITALICO + AMARELO);
    cout<<endl;
    Headlock(line5, 80, 1700);
    Letters(line6, 65, 0, ITALICO);

    return 0;

}
