    
window.onload = function () {
  
  var on_mouse_over = function() {
  
      this.className = this.className + " hovered";
    };
   
 var on_mouse_out = function() {
      
  this.className = this.className.replace( /(?:^|\s) hovered(?!\S)/g , '');
 
   }
    
var items = document.getElementsByTagName('li');

    for(var i = 0; i < items.length; i++) {
  
    items[i].addEventListener('mouseover', on_mouse_over);

    items[i].addEventListener('mouseout', on_mouse_out);
 
   }


document.getElementById('color').onclick = changeColor;
var currentColor="red";

function changeColor(){
       if(currentColor=="red"){

     document.body.style.color="green";
     currentColor="green";
}else {
document.body.style.color="red";
currentColor="red";
}
return currentColor;
}

};
