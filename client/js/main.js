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

    client.join(sideCount).then((res) => {
        if (res.success) {
	    console.log("Successfully joined game");
            app.ticker.add(delta => gameLoop(delta));
        } else {
	    console.log("Failed to join");
	}
    });
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
	    rectangle.on("pointerdown", () => { onClick(rectangle,i,j); });
	    column.push({
	        graphic: rectangle,
	        x: i,
	        y: j,
	        visited: false,
	        adjacent: 0,
	        basin: false,
	        revealed: false,
	    });
            app.stage.addChild(rectangle);
        }
        rectangles.push(column);
    }
    console.log(rectangles);
}

function onClick (rectangle,i,j){
    // Send request
    client.move(i,j).then((res) => {
        if(res.success) {
            console.log("move success");
            requestMap();
        } else {
            console.log("move failed");
        }
        }


    )
}

async function requestMap (){
    // Updates map from server data
    let board;
    let res = await client.board();
    if(res.success) {
        board = res.board;
    } else {
        console.log("Failed to retrieve map");
        return
    }
    for(let i = 0; i < sideCount; i++){
        for( let j= 0; j< sideCount; j++){
            rectangles[i][j].visited = board [i][j].visited;
            rectangles[i][j].adjacent = board [i][j].adjacent;
            rectangles[i][j].basin = board [i][j].basin;

        }
    }

}

function drawMap(){
    // Redraws the map
    for(let i = 0; i < sideCount; i++){
        for( let j= 0; j< sideCount; j++){
            if (rectangles[i][j].visited && rectangle[i][j].revealed) {
                if( rectangles[i][j].basin){
                    rectangles[i][j].graphic.clear();
                    rectangles[i][j].graphic.lineStyle(1, 0xc4c4c4, 0.5);
                    rectangles[i][j].graphic.beginFill(0xFF0000); //Red if basin
                    rectangles[i][j].graphic.drawRect((screenWidth/4 + nodeWidth*arrayX)*sF, (10 +nodeWidth*arrayY)*sF, nodeWidth, nodeWidth);
                    rectangles[i][j].graphic.endFill();
                    app.stage.addChild(rectangles[i][j].graphic);

                } else {
                    rectangles[i][j].graphic.clear();
                    rectangles[i][j].graphic.lineStyle(1, 0xc4c4c4, 0.5);
                    rectangles[i][j].graphic.beginFill(0x00FF00); //Green if not basin
                    rectangles[i][j].graphic.drawRect((screenWidth/4 + nodeWidth*arrayX)*sF, (10 +nodeWidth*arrayY)*sF, nodeWidth, nodeWidth);
                    rectangles[i][j].graphic.endFill();
                    app.stage.addChild(rectangles[i][j].graphic);

                    if(rectangles[i][j].adjacent != 0) {
                        console.log(rectangles[i][j].adjacent);
                    }
                }
            }
        }
    }
}

} // main
