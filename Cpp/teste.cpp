#include <iostream>
#include <chrono>
#include <thread>
#include <cstdlib> // Para system()

// Função para limpar a tela de forma portável
void LimparTela() {
#ifdef _WIN32 // Se estiver no Windows
    system("cls");
#else // Senão (Linux, Mac)
    system("clear");
#endif
}

int main() {
    int posicao = 0;
    int direcao = 1; // 1 = direita, -1 = esquerda
    int larguraTela = 40;

    while (true) { // Loop infinito de animação
        LimparTela();

        // 1. Desenha os espaços antes do objeto
        for (int i = 0; i < posicao; ++i) {
            std::cout << " ";
        }

        // 2. Desenha o objeto
        std::cout << "o";

        // 3. Imprime uma quebra de linha
        std::cout << std::endl;

        // 4. Atualiza a posição
        posicao += direcao;

        // 5. Verifica as bordas
        if (posicao >= larguraTela) {
            direcao = -1; // Inverte a direção
        } else if (posicao <= 0) {
            direcao = 1; // Inverte a direção
        }

        // 6. Pausa (framerate)
        std::this_thread::sleep_for(std::chrono::milliseconds(50));
    }

    return 0;
}