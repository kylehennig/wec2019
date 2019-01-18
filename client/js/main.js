let sF = 1;
let screenWidth = 1400*sF;
let screenHeight = 770*sF;

let app;
let sideLength;

function setup () {
    app = new PIXI.Application(screenWidth,screenHeight, {backgroundColor : 0x000000});
    document.body.appendChild(app.view);
    updateMap();

    app.ticker.add(delta => gameLoop(delta));
}

function gameLoop(delta) {


}

function updateMap (){

    sideCount = 30;
    let nodeWidth =25*sF;


    for(let i =0; i < sideCount; i ++){
        for(let j = 0; j < sideCount; j++){
            let rectangle = new PIXI.Graphics();
            rectangle.lineStyle(1, 0xc4c4c4, 0.5);
            rectangle.beginFill(0xFFFFFFF);
            rectangle.drawRect((screenWidth/4 + nodeWidth*i)*sF, (10 +nodeWidth*j)*sF, nodeWidth, nodeWidth);
            rectangle.endFill();
            app.stage.addChild(rectangle);
        }
    }
}

window.addEventListener("load", setup);
