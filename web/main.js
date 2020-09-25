async function displayPhoto() {
	let result = await eel.open_file()();

	document.querySelector('#image').src = result;
	document.querySelector('#image').style.transform = "rotate(0deg)";

	degrees = 0;
}

document.querySelector('.fa-camera').onclick = () => {
	displayPhoto();
}

// next or previous photo
async function next_or_prev(data) {
	let result = await eel.left_right(data)();

	document.querySelector('#image').src = result;
	document.querySelector('#image').style.transform = "rotate(0deg)";
			
	degrees = 0		
}

document.querySelector('.fa-chevron-left').onclick = () => { next_or_prev('left'); }
document.querySelector('.fa-chevron-right').onclick = () => { next_or_prev('right'); }

// photo rotation
degrees = 0;

document.querySelector('.fa-repeat').onclick = () => {
	document.querySelector('#image').style.transform = `rotate(${degrees + 90}deg)`;
	degrees += 90;
}

document.querySelector('.fa-undo').onclick = () => {
	document.querySelector('#image').style.transform = `rotate(${degrees - 90}deg)`;
	degrees -= 90;
}

// open my github
document.querySelector('#github').onclick = function(event)
{
	event.preventDefault();

	window.open(this.href)
}