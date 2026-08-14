import os # importa o modulo os para manipulacao de caminhos de arquivos e diretorios
import cv2 # importa a biblioteca opencv para visao computacional e manipulacao de janelas
import numpy as np # importa a biblioteca numpy para operacoes matematicas e vetoriais
import sounddevice as sd # importa sounddevice para processamento e saida de audio em tempo real
import mediapipe as mp # importa o mediapipe para reconhecimento e rastreamento gestual
from mediapipe.tasks import python # importa as definicoes de tarefas em python do mediapipe
from mediapipe.tasks.python import vision # importa os modulos de visao computacional do mediapipe

# frequencias em hertz de cada nota musical
notas_musicais = {
    "C": 261.63,  "C#": 277.18, "Db": 277.18,
    "D": 293.66,  "D#": 311.13, "Eb": 311.13,
    "E": 329.63,  "F": 349.23,
    "F#": 369.99, "Gb": 369.99, "G": 392.00,
    "G#": 415.30, "Ab": 415.30, "A": 440.00,
    "A#": 466.16, "Bb": 466.16, "B": 493.88,
    "Cb": 246.94, "B#": 261.63, "Fb": 329.63, "E#": 349.23
}

# combinacao de notas que formam cada acorde
acordes = {
    # acordes maiores 
    "C": ["C", "E", "G"], "D": ["D", "F#", "A"], "E": ["E", "G#", "B"],
    "F": ["F", "A", "C"], "G": ["G", "B", "D"],  "A": ["A", "C#", "E"], "B": ["B", "D#", "F#"],

    # acordes menores 
    "Cm": ["C", "D#", "G"], "Dm": ["D", "F", "A"], "Em": ["E", "G", "B"],
    "Fm": ["F", "G#", "C"], "Gm": ["G", "A#", "D"], "Am": ["A", "C", "E"], "Bm": ["B", "D", "F#"],

    # acordes maiores com setima
    "C7": ["C", "E", "G", "A#"], "D7": ["D", "F#", "A", "C"], "E7": ["E", "G#", "B", "D"],
    "F7": ["F", "A", "C", "D#"], "G7": ["G", "B", "D", "F"], "A7": ["A", "C#", "E", "G"], "B7": ["B", "D#", "F#", "A"],

    # acordes menores com setima
    "Cm7": ["C", "D#", "G", "A#"], "Dm7": ["D", "F", "A", "C"], "Em7": ["E", "G", "B", "D"],
    "Fm7": ["F", "G#", "C", "D#"], "Gm7": ["G", "A#", "D", "F"], "Am7": ["A", "C", "E", "G"], "Bm7": ["B", "D", "F#", "A"],

    # acordes com alteracoes de sustenido e bemol
    "C#": ["C#", "F", "G#"], "C#m": ["C#", "E", "G#"], "C#7": ["C#", "F", "G#", "B"], "C#m7": ["C#", "E", "G#", "B"],
    "Db": ["Db", "F", "Ab"], "Dbm": ["Db", "E", "Ab"], "Db7": ["Db", "F", "Ab", "B"],
    "D#": ["D#", "G", "A#"], "D#m": ["D#", "F#", "A#"], "D#7": ["D#", "G", "A#", "C#"], "D#m7": ["D#", "F#", "A#", "C#"],
    "Eb": ["Eb", "G", "Bb"], "Ebm": ["Eb", "Gb", "Bb"], "Eb7": ["Eb", "G", "Bb", "Db"], "Ebm7": ["Eb", "Gb", "Bb", "Db"],
    "F#": ["F#", "A#", "C#"], "F#m": ["F#", "A", "C#"], "F#7": ["F#", "A#", "C#", "E"], "F#m7": ["F#", "A", "C#", "E"],
    "G#": ["G#", "C", "D#"], "G#m": ["G#", "B", "D#"], "G#7": ["G#", "C", "D#", "F#"], "G#m7": ["G#", "B", "D#", "F#"],
    "Ab": ["Ab", "C", "Eb"], "Abm": ["Ab", "B", "Eb"], "Ab7": ["Ab", "C", "Eb", "Gb"],
    "A#": ["A#", "D", "F"], "A#m": ["A#", "C#", "F"], "A#7": ["A#", "D", "F", "G#"], "A#m7": ["A#", "C#", "F", "G#"],
    "Bb": ["Bb", "D", "F"], "Bbm": ["Bb", "Db", "F"], "Bb7": ["Bb", "D", "F", "Ab"], "Bbm7": ["Bb", "Db", "F", "Ab"]
}

# taxa de amostragem padrao em hertz para o som
taxa_amostragem = 44100
# lista responsavel por armazenar as frequencias tocadas
frequencias_atuais = []
# variavel para preservar o alinhamento de fase entre blocos de audio
fase = 0.0

# funcao chamada pelo fluxo de audio para gerar e enviar sons
def retorno_chamada_audio(dados_saida, quadros, informacao_tempo, estado):
    # referencia a variavel global de fase para manter a onda continua
    global fase
    
    # verifica se nao ha notas ativas para reproduzir
    if not frequencias_atuais:
        # zera todo o buffer de saida, deixando sem som
        dados_saida[:] = 0.0
        # encerra a execucao da funcao
        return

    # calcula o vetor de tempo continuo para o bloco atual de audio
    t = (np.arange(quadros) + fase) / taxa_amostragem
    # incrementa a fase pelo numero de amostras processadas
    fase += quadros

    # inicializa o acumulador sonoro com zeros
    armazenador_temporario = np.zeros(quadros, dtype=np.float32)
    # itera pelas frequencias ativas somando as ondas senoidais
    for frequencia in frequencias_atuais:
        # adiciona a onda senoidal correspondente no acumulador
        armazenador_temporario += np.sin(2 * np.pi * frequencia * t)

    # normaliza a amplitude pelo numero de frequencias e ajusta o volume
    armazenador_temporario = (armazenador_temporario / len(frequencias_atuais)) * 0.3
    # grava o resultado final no primeiro canal da saida de audio
    dados_saida[:, 0] = armazenador_temporario.astype(np.float32)

# inicializa o fluxo de saida de audio mono com a funcao de callback
fluxo_audio = sd.OutputStream(channels=1, callback=retorno_chamada_audio, samplerate=taxa_amostragem)
# inicia a reproducao do fluxo de audio
fluxo_audio.start()

# localiza a pasta em que este arquivo de codigo esta salvo
diretorio_script = os.path.dirname(os.path.abspath(__file__))
# constroi o caminho completo para o modelo de deteccao de maos
caminho_modelo = os.path.join(diretorio_script, "hand_landmarker.task")

# abre o arquivo do modelo em modo de leitura binaria
with open(caminho_modelo, "rb") as f:
    # le os bytes do arquivo para carregar na memoria
    bytes_modelo = f.read()

# configura as opcoes basicas apontando para o buffer do modelo lido
opcoes_base = python.BaseOptions(model_asset_buffer=bytes_modelo)
# define as opcoes de execucao do detector de maos para modo imagem e duas maos
opcoes = vision.HandLandmarkerOptions(
    base_options=opcoes_base,
    running_mode=vision.RunningMode.IMAGE,
    num_hands=2
)
# instancia o detector de marcos da mao com as opcoes fornecidas
detector = vision.HandLandmarker.create_from_options(opcoes)

# funcao que analisa a posicao dos pontos da mao e determina dedos abertos ou fechados
def extrair_estado_dedos(pontos_referencia):
    # compara a ponta do indicador com a articulacao para checar se esta abaixado
    indicador_abaixado = pontos_referencia[8].y > pontos_referencia[6].y
    medio_abaixado     = pontos_referencia[12].y > pontos_referencia[10].y
    anelar_abaixado    = pontos_referencia[16].y > pontos_referencia[14].y
    minimo_abaixado    = pontos_referencia[20].y > pontos_referencia[18].y

    # calcula a distancia entre o polegar e a base do mindinho
    dist_ao_mindinho = np.hypot(pontos_referencia[4].x - pontos_referencia[17].x, pontos_referencia[4].y - pontos_referencia[17].y)
    # calcula a largura aproximada da regiao da palma
    largura_palma    = np.hypot(pontos_referencia[5].x - pontos_referencia[17].x, pontos_referencia[5].y - pontos_referencia[17].y)
    # define o polegar como fechado se estiver proximo da base da palma
    polegar_fechado  = dist_ao_mindinho < (largura_palma * 1.1)

    # retorna um dicionario com o estado booleano de cada dedo
    return {
        "polegar":   polegar_fechado,
        "indicador": indicador_abaixado,
        "medio":     medio_abaixado,
        "anelar":    anelar_abaixado,
        "minimo":    minimo_abaixado,
    }

# inicializa a captura de video usando a webcam padrao
captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# define o nome que sera exibido no topo da janela
nome_janela = "Instrumento Gestual"

# cria a janela de exibicao com suporte a redimensionamento
cv2.namedWindow(nome_janela, cv2.WINDOW_NORMAL)

# ajusta o tamanho inicial da janela para ocupar grande parte do monitor
cv2.resizeWindow(nome_janela, 1600, 900)

# posiciona a janela perto do canto superior esquerdo
cv2.moveWindow(nome_janela, 50, 50)

# loop principal de execucao enquanto a camera permanecer aberta
while captura.isOpened():
    # le o proximo quadro capturado pela camera
    sucesso, quadro = captura.read()
    # encerra o loop caso haja falha na leitura da imagem
    if not sucesso:
        break

    # inverte horizontalmente a imagem para criar o espelhamento
    quadro = cv2.flip(quadro, 1)
    # extrai a altura e a largura do quadro de video
    altura, largura, _ = quadro.shape

    # converte a representacao de cores do opencv bgr para rgb
    quadro_rgb = cv2.cvtColor(quadro, cv2.COLOR_BGR2RGB)
    # encapsula os dados da imagem no formato aceito pelo mediapipe
    imagem_mediapipe = mp.Image(image_format=mp.ImageFormat.SRGB, data=quadro_rgb)
    # executa o modelo de deteccao de maos sobre o quadro atual
    resultado_deteccao = detector.detect(imagem_mediapipe)

    # define os estados padrao dos dedos da mao como abertos
    dedos_esq = {"polegar": False, "indicador": False, "medio": False, "anelar": False, "minimo": False}
    dedos_dir = {"polegar": False, "indicador": False, "medio": False, "anelar": False, "minimo": False}

    # verifica se foram encontrados pontos de maos na deteccao
    if resultado_deteccao.hand_landmarks:
        # percorre cada mao identificada na cena
        for pontos_referencia in resultado_deteccao.hand_landmarks:
            # extrai a coordenada horizontal do pulso
            pulso_x = pontos_referencia[0].x

            # se o pulso estiver no lado esquerdo da tela processa como mao esquerda
            if pulso_x < 0.5:
                # extrai o estado dos dedos da mao esquerda
                dedos_esq = extrair_estado_dedos(pontos_referencia)
            # caso contrario processa como mao direita
            else:
                # extrai o estado dos dedos da mao direita
                dedos_dir = extrair_estado_dedos(pontos_referencia)

    # inicializa a nota base como vazia
    nota_base = None

    # extrai as variaveis booleanas de cada dedo da mao esquerda
    p_e = dedos_esq["polegar"]
    i_e = dedos_esq["indicador"]
    m_e = dedos_esq["medio"]
    a_e = dedos_esq["anelar"]
    min_e = dedos_esq["minimo"]

    # verifica se o dedao esquerdo esta fechado para ativar a nota base
    if p_e:
        # combinacao correspondente a nota si
        if not i_e and not m_e and a_e and min_e:
            nota_base = "B"
        elif not i_e and m_e and a_e and min_e:
            nota_base = "A"
        elif i_e and m_e and a_e and min_e:
            nota_base = "G"
        elif i_e and m_e and a_e and not min_e:
            nota_base = "F"
        elif i_e and m_e and not a_e and not min_e:
            nota_base = "E"
        elif i_e and not m_e and not a_e and not min_e:
            nota_base = "D"
        elif not i_e and not m_e and not a_e and not min_e:
            nota_base = "C"

    # inicializa a variavel do texto a ser exibido
    texto_exibicao = " "
    # inicializa a lista de frequencias correspondentes ao acorde
    novas_frequencias = []

    # se houver uma nota base detectada calcula as variacoes da mao direita
    if nota_base:
        # extrai as variaveis booleanas de cada dedo da mao direita
        p_d = dedos_dir["polegar"]
        i_d = dedos_dir["indicador"]
        m_d = dedos_dir["medio"]
        a_d = dedos_dir["anelar"]
        min_d = dedos_dir["minimo"]

        # divide a frequencia pela metade se o polegar direito estiver fechado
        multiplicador_oitava = 0.5 if p_d else 1.0
        # define o sufixo de texto indicando mudanca de oitava
        texto_oitava = " (3)" if p_d else ""

        # inicializa o modificador de acidente musical
        acidente = ""
        # define bemol se indicador e medio estiverem abaixados
        if i_d and m_d:
            acidente = "b"
        # define sustenido se apenas o indicador estiver abaixado
        elif i_d:
            acidente = "#"

        # anelar direito define o modo menor
        eh_menor   = a_d
        # minimo direito adiciona a setima
        com_setima = min_d

        # monta o acordeconcatenando de acordo as características detectadas na mao direita
        chave_acorde = f"{nota_base}{acidente}"
        if eh_menor:
            chave_acorde += "m"
        if com_setima:
            chave_acorde += "7"

        # busca as notas do acorde no dicionario
        if chave_acorde in acordes:
            # recupera a lista de notas individuais do acorde
            notas_acorde = acordes[chave_acorde]
            # calcula as frequencias ajustadas com base no multiplicador de oitava
            novas_frequencias = [notas_musicais[n] * multiplicador_oitava for n in notas_acorde]
            # formata o texto contendo informacoes do acorde
            texto_exibicao = f"{chave_acorde}{texto_oitava} - ({' '.join(notas_acorde)})"
        else:
            # caso a combinacao nao exista no dicionario, exibe simbolos de interrogacao
            texto_exibicao = f"???"

    # atualiza a variavel de frequencias em execucao
    frequencias_atuais = novas_frequencias

    # define a cor do texto no padrao bgr
    cor_texto = (101, 38, 98)

    # define a escala do tamanho da fonte
    escala_fonte = 0.85
    # define a espessura do traco da fonte
    espessura_fonte = 1
    # calcula a largura e altura do texto para posicionamento preciso
    (largura_texto, altura_texto), _ = cv2.getTextSize(texto_exibicao, cv2.FONT_HERSHEY_SIMPLEX, escala_fonte, espessura_fonte)
    # calcula a posicao horizontal para centralizar o texto
    posicao_x = (largura - largura_texto) // 2
    # calcula a posicao vertical para fixar o texto proximo a borda inferior
    posicao_y = altura - 40
    # desenha o texto centralizado na parte inferior do quadro
    cv2.putText(quadro, texto_exibicao, (posicao_x, posicao_y), cv2.FONT_HERSHEY_SIMPLEX, escala_fonte, cor_texto, espessura_fonte)
    # exibe o quadro processado na janela configurada
    cv2.imshow(nome_janela, quadro)

    # aguarda tecla por um milissegundo e encerra o programa se q for pressionado
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# para a transmissao de audio
fluxo_audio.stop()
# fecha a conexao do fluxo de som
fluxo_audio.close()
# libera os recursos da webcam
captura.release()
# fecha todas as janelas do opencv
cv2.destroyAllWindows()
