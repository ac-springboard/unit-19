const cv          = document.getElementById('timer_canvas');
const cp          = document.getElementById('timer');
const ct          = cv.getContext("2d");
let cw = cp.clientWidth * 0.9;
let ch = cp.clientHeight * 0.9;
console.log( cw, ch );
cv.setAttribute('width', cw + 'px');
cv.setAttribute('height', cw + 'px')

const cx          = cw / 2;
const cy          = cw / 2 ;
const cr          = cw / 4;
let angIni        = 0;
let angDes        = Math.PI * 2 / 60;
let timer_counter = 59;
let fillDelta     = 255 / 60;
let r             = 0;
let g             = 255;
let b             = 0;
// ct.fillRect(0, 0, 300, 300);
ct.beginPath();
ct.arc(cy, cx, cr, 0, Math.PI * 2);
// ct.fillStyle = 'rgba( 6, 6, 6, 0.5)';
ct.fillStyle = 'lightyellow';
ct.fill();
ct.strokeStyle = 'rgba(0, 255, 0, 0.5 )';
ct.lineWidth   = 50;
ct.font        = '30px Arial bolder';
ct.stroke();
ct.fillText(timer_counter, cx - 15, cy + 15);
// ct.fillStyle = '#00ff00';
// ct.fill();
const seti = setInterval(function () {

	ct.beginPath();
	// ct.moveTo(cx, cy);
	ct.arc(cx, cy, cr, angIni - 0.05, angIni + angDes + 0.05);
	// ct.lineTo(cx, cy);
	ct.lineWidth   = 51;
	ct.strokeStyle = '#800000';
	ct.stroke();

	// ct.fillStyle = 'rgba( 6, 6, 6, 0.5)';
	ct.fillStyle = 'lightyellow';
	ct.fillRect(cx - 30, cy - 20, 60, 40);
	// ct.clearRect( cx - 20, cy - 20, 60 , 40);

	ct.fillStyle = 'rgb( ' + r + ', ' + g + ', ' + b + ' )';
	r += fillDelta;
	g -= fillDelta;
	ct.fillText(timer_counter + 's', cx - 15, cy + 10);

	// ct.fillStyle = '#ffffff';
	// ct.fill();
	timer_counter -= 1;
	angIni += angDes;
	if (timer_counter < 0) {
		clearInterval(seti);
	}
}, 125);
