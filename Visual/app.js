
const width= 700;
let followX= 1000000;
let followY= 500000;
let time = 1;
const coordinates = window.coordinates;
let timeSpeed = 1;
let log = false;
let log2 = false;
let starsArray= [];
let moon;
let sun;
let earth;
let JWST1;
let JWST2;
let Days;
let speed;
let freeze = 3;
let freezeindex = 0;


var s = 1;  
function ZoomUp(){
    timeSpeed ++;
}
function ZoomDown(){
    freeze ++;
}

function Stop(){
    timeSpeed =0;
}




function preload() {
    moon=document.getElementById('moon');
    moon.style.position = "absolute";
    sun =document.getElementById('sun'); 
    sun.style.position = "absolute";
    earth=document.getElementById('earth'); 
    earth.style.position = "absolute";
    JWST1 = document.getElementById('jwst1');
    JWST1.style.position = "absolute";
    JWST2 = document.getElementById('jwst2');
    JWST2.style.position = "absolute";

    
    Days = document.getElementById('days');
    Days.style.position = "absolute";
    Days.style.left = width*2 + 30;
    Days.style.top = 30;
    speed = document.getElementById('speed');
    speed.style.position = "absolute";
    speed.style.left = width*2 + 30;
    speed.style.top = 60;
}



function setup() {
    createCanvas(width * 2 , width ); 
    buttonUp = createButton('+');
    buttonUp.position(10, width + 19);
    buttonUp.style("width",  "30px");
    buttonUp.mousePressed(ZoomUp);
    
    buttonDown = createButton('-');
    buttonDown.position(40, width + 19);
    buttonDown.style("width",  "30px");
    buttonDown.mousePressed(ZoomDown);

    
    buttonStop = createButton('stop');
    buttonStop.position(70, width + 19);
    buttonStop.style("width", "50px");
    buttonStop.mousePressed(Stop);
    starsArray = stars();


    
}


function stars(){
    let count = Math.random() * 500 + 500;
    let starsPos=[];
    for(let i=0;i<count;i++){
        let x = Math.random() * width * 2; 
        let y = Math.random() * width * 2; 
        starsPos.push({x,y});
    }

    return starsPos;
}




function draw() {
    if(freezeindex >= freeze){
    let l2 = L2({x:coordinates[time].x_earth,y:coordinates[time].y_earth});
    background(0);
    sun.style.top = width / 2;
    
    sun.style.left =  3 * width / 2;
    earth.style.top = width / 2;
    earth.style.left  = width / 2;
    
    rect(width,0,10,width*2);
    for(let i=0 ; i < starsArray.length;i++){
        stroke(255); 
        point(starsArray[i].x,starsArray[i].y);
        noStroke();

    }
    followX = Max({x:coordinates[time].x_jw,y:coordinates[time].y_jw},{x:coordinates[time].x_earth,y:coordinates[time].y_earth},{x:coordinates[time].x_moon,y:coordinates[time].y_moon})/width;
    for(let i=0 ;i < time - 1; i++){
            stroke(0, 0, 150); 
            line(Relative(coordinates[i].x_jw - coordinates[i].x_earth) ,Relative(coordinates[i].y_jw - coordinates[i].y_earth),Relative(coordinates[i+1].x_jw - coordinates[i+1].x_earth),Relative(coordinates[i+1].y_jw - coordinates[i+1].y_earth));
            noStroke();
            // stroke(150, 0, 0); 
            //  line(Relative(coordinates[i].x_moon - coordinates[i].x_earth),Relative(coordinates[i].y_moon - coordinates[i].y_earth),Relative(coordinates[i+1].x_moon - coordinates[i+1].x_earth),Relative(coordinates[i+1].y_moon - coordinates[i+1].y_earth));
            // noStroke();
    }
    JWST1.style.left =Relative(coordinates[time-1].x_jw - coordinates[time-1].x_earth) ;
    JWST1.style.top =Relative(coordinates[time-1].y_jw - coordinates[time-1].y_earth) ;
    moon.style.left=Relative(coordinates[time-1].x_moon - coordinates[time-1].x_earth);
    moon.style.top=Relative(coordinates[time-1].y_moon - coordinates[time-1].y_earth);

    if(time-2 > 0)
        speed.innerText = parseInt( Math.sqrt((coordinates[time-1].x_jw - coordinates[time-2].x_jw)*(coordinates[time-1].x_jw - coordinates[time-2].x_jw)  + 
        (coordinates[time-1].y_jw - coordinates[time-2].y_jw)*(coordinates[time-1].y_jw - coordinates[time-2].y_jw) )/(365 *24 /5000) ) + " km/h"
    if( Relative(l2.x - coordinates[time].x_earth) < width){
        fill(255);
        ellipse(Relative(l2.x - coordinates[time].x_earth),Relative(l2.y - coordinates[time].y_earth),4,4);
        text("L2",Relative(l2.x - coordinates[time].x_earth) + 10,Relative(l2.y - coordinates[time].y_earth) + 10);
        noStroke();
    }


    
    //l2.x / followY + 3/2*width, l2.y / followY + width/2,8,8);
  
    for(let i=0 ;i < time - 1; i++){
        stroke(0, 0, 150); 
        line(coordinates[i].x_jw / followY + 3/2*width,coordinates[i].y_jw/ followY + width /2 ,
            coordinates[i+1].x_jw/ followY + 3/2*width ,coordinates[i+1].y_jw/ followY + width /2);
        noStroke();
       
        // stroke(150, 0, 0); 
        // line(coordinates[i].x_moon / followY + 3/2*width,coordinates[i].y_moon / followY + width /2,
        //     coordinates[i+1].x_moon / followY + 3/2*width,coordinates[i+1].y_moon / followY+ width /2);
        // noStroke();
        stroke(0, 150, 0);
        line(coordinates[i].x_earth / followY + 3/2*width,coordinates[i].y_earth / followY + width /2,
            coordinates[i+1].x_earth / followY + 3/2*width,coordinates[i+1].y_earth / followY + width /2);
        noStroke();
    } 
    JWST2.style.left =coordinates[time-1].x_jw / followY + 3/2*width ;
    JWST2.style.top =coordinates[time-1].y_jw/ followY + width /2 ;
    stroke(255, 0 , 0);
    ellipse(l2.x  / followY + 3/2*width,l2.y / followY + width /2  ,1,1)
    noStroke();
    fill(255);
    text("Earth",width/2+10, width/2-10);
    text("JWST",Relative(coordinates[time-1].x_jw - coordinates[time-1].x_earth)+10, Relative(coordinates[time-1].y_jw - coordinates[time-1].y_earth)-10);
    text("JWST",coordinates[time-1].x_earth / followY + 3/2*width + 10,coordinates[time-1].y_earth / followY + width /2 + 10);
    text("Moon",Relative(coordinates[time-1].x_moon - coordinates[time-1].x_earth)+10, Relative(coordinates[time-1].y_moon - coordinates[time-1].y_earth)+10);
    text("Sun",width*3/2+12, width/2-12);
    noStroke();
    Days.innerText= parseInt(time *365/5000) + " days";
    if(followX > 20000) moon.style.visibility = "hidden"; 
    
    time +=timeSpeed;
    freezeindex=0;
    }
    else
        freezeindex++;
    if(time > coordinates.length -1) time= coordinates.length;

}



function Max(J,E,M){
    let x = [Math.abs(J.x-E.x),Math.abs(M.x-E.x),Math.abs(J.x-M.x) ];
    let y = [Math.abs(J.y-E.y),Math.abs(M.y-E.y),Math.abs(J.y-M.y)];
    //return Math.max.apply(null, [Math.max.apply(null, y),Math.max.apply(null, x)]) * 3 ;
    return  4000000;
}

function Relative(coordinate){
    return parseInt((coordinate/followX) + width/2);
}

function L2({x,y}){
    let tnA= y/x;
    let x1;
    if(x<0)
    x1 = -Math.sqrt(1500000 * 1500000/(1+tnA*tnA));
    else
    x1 =  Math.sqrt(1500000 * 1500000/(1+tnA*tnA));
    let y1 = x1*tnA;
    return {x:x+x1,y:y+y1};
}
