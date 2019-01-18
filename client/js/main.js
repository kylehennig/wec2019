window.addEventListener("load", main);

function main() {
let startButton = document.querySelector(".settings #start");
startButton.addEventListener("click", setup);

let sF = 1;
let screenWidth = 1400*sF;
let screenHeight = 770*sF;

let app;
let sideLength;
let sideCount;
let nodeWidth;
let rectangles = [];

/**
 * Reads size from html select element and sets global sideCount
 */
function setSize() {
  let selectElement = document.querySelector(".settings select");
  let sizeString = selectElement.value;
  console.log(sizeString);

  if (sizeString == "small") {
    sideCount = 10;
  } else if (sizeString == "medium") {
    sideCount = 20;
  } else if (sizeString == "large") {
    sideCount = 30;
  } else {
    console.log("Unrecognized size option from html");
  }
}

function setup () {
    setSize();
    app = new PIXI.Application(screenWidth,screenHeight, {backgroundColor : 0x000000});
    document.body.appendChild(app.view);
    createMap();
    //updateMap();

    app.ticker.add(delta => gameLoop(delta));
}

function gameLoop(delta) {
    drawMap();
}

function createMap() {
    nodeWidth =25*sF;

    for(let i =0; i < sideCount; i ++){
        let column = [];
        for(let j = 0; j < sideCount; j++){
            let rectangle = new PIXI.Graphics();
            rectangle.lineStyle(1, 0xc4c4c4, 0.5);
            rectangle.beginFill(0xFFFFFFF);
            rectangle.drawRect((screenWidth/4 + nodeWidth*i)*sF, (10 +nodeWidth*j)*sF, nodeWidth, nodeWidth);
            // rectangle.x = (screenWidth/4 + nodeWidth*i)*sF;
            // rectangle.y = (10 +nodeWidth*j)*sF;
            rectangle.endFill();
	    rectangle.interactive = true;
	    rectangle.on("pointerdown", () => { updateRect(rectangle,i,j); });
	    column.push(rectangle);
            app.stage.addChild(rectangle);
        }
        rectangles.push(column);
    }
    console.log(rectangles);
}

function updateRect(rectangle,arrayX,arrayY) {
  let oldX = rectangle.x;
  let oldY = rectangle.y;

  let visible = false;
  let number = false;
  let bomb = false;
  let newRect;
  if(!visible){
      if(number) {
          rectangle.clear();
          rectangle.lineStyle(1, 0xc4c4c4, 0.5);
          rectangle.beginFill(0x00FF00);
          rectangle.drawRect((screenWidth/4 + nodeWidth*arrayX)*sF, (10 +nodeWidth*arrayY)*sF, nodeWidth, nodeWidth);
          rectangle.endFill();

      }else if (bomb){
          rectangle.clear();
          rectangle.lineStyle(1, 0xc4c4c4, 0.5);
          rectangle.beginFill(0x00FF00);
          rectangle.drawRect((screenWidth/4 + nodeWidth*arrayX)*sF, (10 +nodeWidth*arrayY)*sF, nodeWidth, nodeWidth);
          rectangle.endFill();


      } else {
          rectangle.clear();
          rectangle.lineStyle(1, 0xc4c4c4, 0.5);
          rectangle.beginFill(0x00FF00);
          rectangle.drawRect((screenWidth/4 + nodeWidth*arrayX)*sF, (10 +nodeWidth*arrayY)*sF, nodeWidth, nodeWidth);
          rectangle.endFill();
      }
      visible = true;
  }
}

function drawMap(){
    for(let i = 0; i < sideCount; i++){
        for( let j= 0; j< sideCount; j++){
            app.stage.addChild(rectangles[i][j]);
        }
    }
}

} // main
