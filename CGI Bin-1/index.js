console.log("running")

function onInsert(){
    document.getElementById("insert").checked = true;
}
function onRetrieve(){
    document.getElementById("retrieve").checked = true;
}
function onBlear(){
    document.getElementById("clear").checked = true;
}
function onDigest(){
    document.getElementById("digest").checked = true;
}
function onInspect(){
    document.getElementById("inspect").checked = true;
}


var bgColors=["yellow", "lightblue", "lightgreen", "pink"]

var insertBgCounter=0;
function insertBg(){
    document.getElementById('insert-div').style.backgroundColor = bgColors[insertBgCounter];
    if(insertBgCounter<3){
        insertBgCounter++;
    }else{
        insertBgCounter = 0;
    }
}

var retrieveBgCounter=0;
function retrieveBg(){
    document.getElementById('retrieve-div').style.backgroundColor = bgColors[retrieveBgCounter];
    if(retrieveBgCounter<3){
        retrieveBgCounter++;
    }else{
        retrieveBgCounter = 0;
    }
}

var clearBgCounter=0;
function clearBg(){
    document.getElementById('clear-div').style.backgroundColor = bgColors[clearBgCounter];
    if(clearBgCounter<3){
        clearBgCounter++;
    }else{
        clearBgCounter = 0;
    }
}

var digestBgCounter=0;
function digestBg(){
    document.getElementById('digest-div').style.backgroundColor = bgColors[digestBgCounter];
    if(digestBgCounter<3){
        digestBgCounter++;
    }else{
        digestBgCounter = 0;
    }
}

var inspectBgCounter=0;
function inspectBg(){
    document.getElementById('inspect-div').style.backgroundColor = bgColors[inspectBgCounter];
    if(inspectBgCounter<3){
        inspectBgCounter++;
    }else{
        inspectBgCounter = 0;
    }
}