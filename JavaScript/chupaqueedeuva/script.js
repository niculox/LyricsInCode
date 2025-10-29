const LYRICS = {
    line1: "Vem meu cajuzinho",
    line2: "Te dou muito carinho",
    line3: "Me dá seu coração", /**2x */
    line4: "Vem meu moranguinho",
    line5: "Te pego de jeitinho",
    line6: "Te encho de tesão",/**2x */
    line7: "Me deixa maluca",
    line8: "Tira o mel da fruta",
    line9: "Me mata de amor",/**2x */
    line1: "Me pega no colo",
    line11: "Me olha nos olhos",
    line12: "Me beija que é bom",/**2x */
    line13: "Na sua boca eu viro fruta",
    line14: "Chupa que é de uva",
    line15: "Chupa! Chupa",
}

const GIF = "https://i.pinimg.com/originals/24/da/59/24da59d9d50de9772aea99a7d65ea86f.gif";

const AUDIO_SRC = "./chupaqueedeuva.mpeg"; 

const IMAGES = {
    cajuzinho: "https://i.pinimg.com/736x/e7/0c/31/e70c312bc4cb2210c4e1696bfe9e6638.jpg",
    moranguinho: "https://i.pinimg.com/736x/cd/c0/73/cdc0734454bf7aad90e2729aa142d23f.jpg",
    carinho: "https://i.pinimg.com/1200x/18/eb/dc/18ebdc702431fc7b85a3110babf517fd.jpg",
    uva1: "https://i.pinimg.com/1200x/7a/38/e7/7a38e7207389f22a6a27f4e095807792.jpg",
    uva2: "https://i.pinimg.com/736x/05/b4/b1/05b4b103a4bce9d83d2fcfca8bdc3bfe.jpg",
    uva3: "https://i.pinimg.com/736x/e2/af/59/e2af591b70a89df1529a993b6c966223.jpg",
    maluca1: "https://i.pinimg.com/736x/65/13/bc/6513bcce3f1ecde8ee78f5a9e0dc8f93.jpg",
    maluca2: "https://i.pinimg.com/736x/de/5e/01/de5e01a00428bd0513ae1f8d2b9b7f41.jpg"
}

const body = document.body;
const botao = document.getElementById('som');
const line1 = document.getElementById('line1');
const line2 = document.getElementById('line2');
const gif = document.getElementById('gif');
const audio = new Audio(AUDIO_SRC);
audio.muted = true;

const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));

function typeLine(element, text, styleClass, speed = 30) {
    return new Promise(resolve => {
        element.className = `lyric-line ${styleClass}`;
        element.textContent = '';
        let i = 0;

        function addChar() {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(addChar, speed);
            } else {
                resolve(); 
            }
        }
        addChar();
    });
}

function showLine(element, text, styleClass) {
    element.className = `lyric-line ${styleClass}`;
    element.innerHTML = text;
}

function clearElements(...elements) {
    for (const el of elements) {
        if (el) el.innerHTML = '';
    }
}

function setBackground(bgClass) {
    body.className = bgClass;
}

function showGif(element, gifUrl) {
    element.innerHTML = `<img src="${gifUrl}" alt="Calcinha Preta">`;
}

botao.addEventListener('click', () => {
    botao.style.display = 'none'; 
    audio.muted = false; 

    runLyricSequence();
    
}, { once: true }); 

async function runLyricSequence() {
    try {

        await sleep(1000);
        showGif(gif, GIF);
        audio.play();

        
        
    } catch (error) {
        console.error("Erro na sequência de animação:", error);
    }
}
