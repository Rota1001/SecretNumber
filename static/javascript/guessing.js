var colorList = []
var clicked = []
for(var i = 0; i < 25; i++){
    colorList[i] = 0;
}
function newTurn(){
    document.body.innerHTML = 
    "<div class=\"chessboard\">\
    <button onclick=\"onButtonClick(this)\", id=0></button>\
<button onclick=\"onButtonClick(this)\", id=1></button>\
<button onclick=\"onButtonClick(this)\", id=2></button>\
<button onclick=\"onButtonClick(this)\", id=3></button>\
<button onclick=\"onButtonClick(this)\", id=4></button>\
<button onclick=\"onButtonClick(this)\", id=5></button>\
<button onclick=\"onButtonClick(this)\", id=6></button>\
<button onclick=\"onButtonClick(this)\", id=7></button>\
<button onclick=\"onButtonClick(this)\", id=8></button>\
<button onclick=\"onButtonClick(this)\", id=9></button>\
<button onclick=\"onButtonClick(this)\", id=10></button>\
<button onclick=\"onButtonClick(this)\", id=11></button>\
<button onclick=\"onButtonClick(this)\", id=12></button>\
<button onclick=\"onButtonClick(this)\", id=13></button>\
<button onclick=\"onButtonClick(this)\", id=14></button>\
<button onclick=\"onButtonClick(this)\", id=15></button>\
<button onclick=\"onButtonClick(this)\", id=16></button>\
<button onclick=\"onButtonClick(this)\", id=17></button>\
<button onclick=\"onButtonClick(this)\", id=18></button>\
<button onclick=\"onButtonClick(this)\", id=19></button>\
<button onclick=\"onButtonClick(this)\", id=20></button>\
<button onclick=\"onButtonClick(this)\", id=21></button>\
<button onclick=\"onButtonClick(this)\", id=22></button>\
<button onclick=\"onButtonClick(this)\", id=23></button>\
<button onclick=\"onButtonClick(this)\", id=24></button>\
    </div>"
    $.ajax({
            url: "/data",
            method: "GET",
            dataType: "json",
            success: function(response){
                var data = response.data;
                colorList = response.colorList;
                for(var i = 0; i < 25; i++){
                    if(document.getElementById(i)){
                        document.getElementById(i).textContent = data[i];
                    }
                    console.log(colorList[i]);
                }
            },
            error: function(error){
                console.log(error);
            }
    })
    for(var i = 0; i < 25; i++){
        clicked[i] = 0;
    }
}


newTurn();


function onButtonClick(button){
    if(clicked[button.id])
        return;
    clicked[button.id] = 1;
    if(colorList[button.id] == 1){
        //red
        button.style.backgroundColor = "#c1121f";
        button.style.color = "#ffffff";
    }else if(colorList[button.id] == 0){
        //blue
        button.style.backgroundColor = "#003049";
        button.style.color = "#ffffff";
    }else if(colorList[button.id] == 2){
        button.style.backgroundColor = "#edf2f4";
    }else{
        button.style.backgroundColor = "#000000";
        button.style.color = "#ffffff";
    }
}
