let sF = 1;
let screenWidth = 1000*sF;
let screenHeight = 700*sF;

let app;
let sideLength;

function setup () {
    app = new PIXI.Application(screenWidth,screenHeight, {backgroundColor : 0x000000});
    document.body.appendChild(app.view);
    updateMap();

    //app.ticker.add(delta => gameLoop(delta));
}

function gameLoop(delta) {


}

function updateMap (){

    sideCount = 1;
    let nodeWidth = 10;



    for(let i =0; i < sideCount; i ++){
        for(let j = 0; i < sideCount; j++){
            let rectangle = new PIXI.Graphics();
            rectangle.lineStyle(4, 0xFF0000, 1);
            rectangle.beginFill(0xFF0000);
            rectangle.drawRect(nodeWidth*i, nodeWidth*j, nodeWidth, nodeWidth);
            rectangle.endFill();
            app.stage.addChild(rectangle);
        }
    }
}

window.addEventListener("load", setup);
