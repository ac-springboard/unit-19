let timer = function(duration) {
	let current     = duration;
	let timer_id;
	const timer_div = document.getElementById('timer_div');
	return {
		start: function () {
			timer_id = setInterval(() => {

				timer_div.innerText = `${current/1000}s`;
				current -= 1000
				if ( current < 0 ){
					console.log( 'this', this )
					this.stop();
				}
			}, 1000);
			return timer_id;
		},
		stop : function(){
			clearInterval(timer_id);
		}
	};
};

t = timer(60*1000);
console.log(t)
tid = t.start();
console.log( 'tid', tid)
