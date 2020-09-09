// When size is submitted by the user, call makeGrid()
//When user clicks on submit button,we need to add listener to mouse click for submit button and use the stored values to create a table of height* width.
//Event is being triggered when submit button is pressed,on this event grid is to be created.  


var canvas=document.getElementById('pixelCanvas');
var size=document.getElementById('sizePicker');
var color=document.getElementById('colorPicker');



//event triggered on submit button

size.addEventListener('submit',function(event){
	event.preventDefault();

	var height=document.getElementById('inputHeight').value;
	var width=document.getElementById('inputWidth').value;
	makeGrid(height,width); //function called
});

//Defining grid function

function makeGrid(height,width) {

	var row,cell;
	canvas.innerHTML="";
for (var i = 0; i < height; i++) 
	{
	row=canvas.insertRow(i);
		for(var j=0; j < width; j++)
		{
		cell=row.insertCell(j);
		console.log(color.value);
		cell.addEventListener('click',function(event){
	this.style.backgroundColor=color.value;
	console.log('Mouse clicked');
	});
		cell.addEventListener('dblclick',function(event){
	this.style.backgroundColor="";
	console.log('Mouse clicked');
	});
			}
	}
	

};



