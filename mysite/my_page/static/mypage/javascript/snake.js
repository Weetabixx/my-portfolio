var head = [25,25]
var snake = [[25,26],[25,27],[25,28],[25,29]];
var direction = "N";
var nextDirection = 'N';
var gameOngoing = true;
var score = 0;
var apple = [20,15];

var canvas = document.getElementById("myCanvas");
var ctx = canvas.getContext("2d");
ctx.fillStyle = "#000000";

function sleeps(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

document.onkeydown = keyPress;
drawApple();
gameTick();

async function gameTick(){
    while(gameOngoing){
        var newHead = [];
        newHead[0] = head[0];
        newHead[1] = head[1];
        snake.push(newHead);
        if(!eatApple()){
            var tail = snake.shift();
            deleteTail(tail);
        }
        await sleeps(100);
        direction = nextDirection;
        move();
        drawHead();
        checkColision();
    }
}

function checkColision(){
    var xPos = head[0];
    var yPos = head[1];
    if(xPos > 50 || xPos < 0 || yPos > 50 || yPos < 0){
        gameOngoing = false;
    }
    var arrayLength = snake.length;
    for (var i = 0; i < arrayLength; i++) {
        if(head[0] === snake[i][0] && head[1] === snake[i][1]){
            gameOngoing = false;
        }
    }
}

function eatApple(){
    var xPos = head[0];
    var yPos = head[1];
    if(xPos === apple[0] && yPos === apple[1]){
        apple[0] = Math.floor(Math.random() * 50);
        apple[1] = Math.floor(Math.random() * 50);
        drawApple();
        return true;
    }
    return false;
}

function drawApple(){
    var xPos = apple[0];
    var yPos = apple[1];
    xPos = xPos * 10;
    yPos = yPos * 10;
    ctx.fillStyle = "#990000";
    ctx.fillRect(xPos, yPos, 10, 10);
}

function drawHead(){
    var xPos = head[0];
    var yPos = head[1];
    xPos = xPos * 10;
    yPos = yPos * 10;
    ctx.fillStyle = "#000000";
    ctx.fillRect(xPos, yPos, 10, 10);
}

function deleteTail(tail){
    var xPos = tail[0];
    var yPos = tail[1];
    xPos = xPos * 10;
    yPos = yPos * 10;
    ctx.fillStyle = "#ffffff";
    ctx.fillRect(xPos, yPos, 10, 10);
}

function move(){
    var oldHead = head;
    switch (direction) {
        case 'N':
            head[1] = oldHead[1] - 1;
            break;
        case 'E':
            head[0] = oldHead[0] + 1;
            break;
        case 'S':
            head[1] = oldHead[1] + 1;
            break;
        case 'W':
            head[0] = oldHead[0] - 1;
            break;
        
        default:
            // code
    }
}

function keyPress(event){
    var x = event.which || event.keyCode;
    console.log(x);
    switch (x) {
        case 38:
            if(direction !== 'S'){
                nextDirection = 'N';
            }
            break;
        case 39:
            if(direction !== 'W'){
                nextDirection = 'E';
            }
            break;
        case 40:
            if(direction !== 'N'){
                nextDirection = 'S';
            }
            break;
        case 37:
            if(direction !== 'E'){
                nextDirection = 'W';
            }
            break;
        
        default:
            // code
    }
}
