const width= 600;
let followX= 1000000;
let followY= 1000000;
let time = 1;
const coordinates = window.coordinates;
let log = false;
let log2 = false;

var s = 1;  
function ZoomUp(){
    pridlijeniye -=100000;
}
function ZoomDown(){
    pridlijeniye +=100000;
}




function setup() {
    createCanvas(width * 2 +100, width * 2 +100); 
    buttonUp = createButton('+');
    buttonUp.position(width + 19, 19);
    buttonUp.mousePressed(ZoomUp);
    
    buttonDown = createButton('-');
    buttonDown.position(width + 19, 40);
    buttonDown.mousePressed(ZoomDown);
}







function draw() {
    background(255);
    followX = Max({x:coordinates[time].x_jw,y:coordinates[time].y_jw},{x:coordinates[time].x_earth,y:coordinates[time].y_earth},{x:coordinates[time].x_moon,y:coordinates[time].y_moon},
        {x:coordinates[time+1].x_jw,y:coordinates[time+1].y_jw},{x:coordinates[time+1].x_earth,y:coordinates[time+1].y_earth},{x:coordinates[time+1].x_moon,y:coordinates[time+1].y_moon})/width;
    for(let i=0 ;i < time - 1; i++){
            stroke(0, 0, 150); 
            line(Relative(coordinates[i].x_jw - coordinates[i].x_earth) ,Relative(coordinates[i].y_jw - coordinates[i].y_earth),Relative(coordinates[i+1].x_jw - coordinates[i+1].x_earth),Relative(coordinates[i+1].y_jw - coordinates[i+1].y_earth));
            noStroke();
            stroke(150, 0, 0); 
            line(Relative(coordinates[i].x_moon - coordinates[i].x_earth),Relative(coordinates[i].y_moon - coordinates[i].y_earth),Relative(coordinates[i+1].x_moon - coordinates[i+1].x_earth),Relative(coordinates[i+1].y_moon - coordinates[i+1].y_earth));
            noStroke();
    }


    for(let i=0 ;i < time - 1; i++){
        stroke(0, 0, 150); 
        line(coordinates[i].x_jw / 1000000 + 3/2*width,coordinates[i].y_jw/ 1000000 + width /2 ,
            coordinates[i+1].x_jw/ 1000000 + 3/2*width ,coordinates[i+1].y_jw/ 1000000 + width /2);
        noStroke();
        stroke(150, 0, 0); 
        line(coordinates[i].x_moon / 1000000 + 3/2*width,coordinates[i].y_moon / 1000000 + width /2,
            coordinates[i+1].x_moon / 1000000 + 3/2*width,coordinates[i+1].y_moon / 1000000+ width /2);
        noStroke();
        
        line(coordinates[i].x_earth / 1000000 + 3/2*width,coordinates[i].y_earth / 1000000 + width /2,
            coordinates[i+1].x_earth / 1000000 + 3/2*width,coordinates[i+1].y_earth / 1000000 + width /2);
}

    time++;
    if(time > coordinates.length -1) time= coordinates.length;

}



function Max(J,E,M){
    let x = [Math.abs(J.x-E.x),Math.abs(M.x-E.x),Math.abs(J.x-M.x) ];
    let y = [Math.abs(J.y-E.y),Math.abs(M.y-E.y),Math.abs(J.y-M.y)];
    return Math.max.apply(null, [Math.max.apply(null, y),Math.max.apply(null, x)]) * 3 ;
}

function Relative(coordinate){
    return parseInt((coordinate/followX) + width/2);
}


