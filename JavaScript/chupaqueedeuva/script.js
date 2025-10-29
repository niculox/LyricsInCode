const LYRICS = {
    line1: "Vem meu",
    line2: "Te dou muito",
    line3: "Me dá seu coração", /**2x */
    line4: "Vem meu ",
    line5: "Te pego de jeitinho",
    line6: "Te encho de ",/**2x */
    line7: "Me deixa maluca",
    line8: "Tira o mel da fruta",
    line9: "Me mata de amor",/**2x */
    line10: "Me pega no colo",
    line11: "Me olha nos olhos",
    line12: "Me beija que é bom",/**2x */
    line13: "Na sua boca eu viro fruta",
    line14: "Chupa que é de",
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
    maluca1: "https://i.pinimg.com/736x/65/13/bc/6513bcce3f1ecde8ee78f5a9e0dc8f93.jpg",
    maluca2: "https://i.pinimg.com/736x/de/5e/01/de5e01a00428bd0513ae1f8d2b9b7f41.jpg"
}

const BODY = document.body;
const BOTAO = document.getElementById('som');
const LINE1 = document.getElementById('line1');
const LINE2 = document.getElementById('line2');
const IMG = document.getElementById('img');
const GIFS = document.getElementById('gif');
const AUDIO = new Audio(AUDIO_SRC);
AUDIO.muted = true;

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
    BODY.className = bgClass;
}

function showGif(element, gifUrl) {
    element.innerHTML = `<img src="${gifUrl}" alt="Chupa que é de uva">`;
}

function showImage(element, imgUrl){
    element.innerHTML = `<img src="${imgUrl}" alt="imagenzinha">`;
}

BOTAO.addEventListener('click', () => {
    BOTAO.style.display = 'none'; 
    AUDIO.muted = false; 

    runLyricSequence();
    
}, { once: true }); 

async function runLyricSequence() {
    try {

        await sleep(1000);
        showGif(GIFS, GIF);
        AUDIO.play();

        await sleep(16000);
        clearElements(GIFS);
        setBackground('bg-dark');

        await sleep(100);
        setBackground('bg-light');
        showLine(LINE1, LYRICS.line1, 'style-dark-on-light');

        await sleep(500);
        clearElements(LINE1);
        setBackground('bg-orange');
        showImage(IMG, IMAGES.cajuzinho);

        await sleep(1000);
        clearElements(IMG);
        setBackground('bg-light');
        showLine(LINE1, LYRICS.line2, 'style-dark-on-light');

        await sleep(800);
        clearElements(LINE1);
        showImage(IMG, IMAGES.carinho);

        await sleep(1200);
        clearElements(IMG);
        typeLine(LINE1, LYRICS.line3, 'style-red-emphasis', 35);

        await sleep(2000);
        clearElements(LINE1);
        setBackground('bg-pink');
        typeLine(LINE1, LYRICS.line3, 'style-basic-size', 35)

        await sleep(1800);
        clearElements(LINE1);
        setBackground('bg-light')
        showLine(LINE1, LYRICS.line4, 'style-dark-on-light');

        await sleep(1000);
        clearElements(LINE1);
        showImage(IMG, IMAGES.moranguinho);

        await sleep(800);
        clearElements(IMG);
        showLine(LINE1, LYRICS.line5, 'style-dark-on-light');

        await sleep(2000);
        clearElements(IMG);
        setBackground('bg-dark');
        showLine(LINE1, LYRICS.line6, 'style-light-on-dark');

        await sleep(500);
        clearElements(LINE1);
        setBackground('bg-light');
        showImage(IMG, IMAGES.maluca1);

        await sleep(1000);
        clearElements(IMG);
        showLine(LINE1, LYRICS.line6, 'style-dark-on-light');

        await sleep(700);
        clearElements(LINE1);
        showImage(IMG, IMAGES.maluca2);

        await sleep(1500);
        clearElements(IMG);
        typeLine(LINE1, LYRICS.line7, 'style-dark-on-light', 35);

        await sleep(1700);
        clearElements(IMG);
        setBackground('bg-orange');
        showLine(LINE1, LYRICS.line8, 'style-dark-on-light');

        await sleep(1500);
        clearElements(LINE1);
        setBackground('bg-dark');
        showLine(LINE1, LYRICS.line9, 'style-light-on-dark');

        await sleep(2000);
        setBackground('bg-purple');
        showLine(LINE2, LYRICS.line9, 'style-red-emphasis');

        await sleep(2300);
        clearElements(LINE1, LINE2);
        setBackground('bg-dark');
        typeLine(LINE1, LYRICS.line10, 'style-light-on-dark', 40);

        await sleep(1800);
        clearElements(LINE1);
        typeLine(LINE1, LYRICS.line11, 'style-light-on-dark', 40);

        await sleep(2000);
        clearElements(LINE1);
        setBackground('bg-purple');
        showLine(LINE1, LYRICS.line12, 'style-light-on-dark');

        await sleep(1500);
        setBackground('bg-orange');
        showLine(LINE2, LYRICS.line12, 'style-red-emphasis');

        await sleep(1300);
        clearElements(LINE1, LINE2);
        setBackground('bg-red');
        await sleep(100);
        setBackground('bg-white');
        await sleep(100);
        setBackground('bg-pink');
        await sleep(100);
        setBackground('bg-orange');
        await sleep(100);
        setBackground('bg-purple');
        await sleep(100);
        setBackground('bg-black');

        await sleep(500);
        showLine(LINE1, LYRICS.line13, 'style-red-emphasis');

        await sleep(2000);
        clearElements(LINE1);
        setBackground('bg-purple');
        showLine(LINE1, LYRICS.line14, 'style-light-on-dark');

        await sleep(1200);
        clearElements(LINE1);
        setBackground('bg-light');
        showImage(IMG, IMAGES.uva1);

        await sleep(1000);
        clearElements(IMG);
        setBackground('bg-red');
        showLine(LINE1, LYRICS.line15, 'style-light-on-dark');

        await sleep(2000);
        clearElements(LINE1);
        setBackground('bg-pink');
        showLine(LINE1, LYRICS.line14, 'style-light-on-dark');

        await sleep(500);
        clearElements(LINE1);
        setBackground('bg-light');
        showImage(IMG, IMAGES.uva2);

        await sleep(1300);
        clearElements(IMG);
        showGif(GIFS, GIF);
        
    } catch (error) {
        console.error("Erro na sequência de animação:", error);
    }
}
