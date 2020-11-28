const $TIMER_DIV       = $('#timer_div');
const $BT_START        = $('#bt-start');
const $BT_CANCEL       = $('#bt-cancel');
const $BOARD_AND_TIMES = $('#board-and-times');

$(document).ready(function () {
  $BT_CANCEL.hide();
  selectToInitialTime();
  updateTime();
});
// let initial_time = 60;

let timer = function (duration) {
  let current = duration - 1000;
  let timer_id;
  return {
    start : function () {
      timer_id = setInterval(() => {

        $TIMER_DIV.text(`${current / 1000}s`);
        current -= 1000;
        if (current < 0) {
          console.log('this', this);
          this.cancel();
        }
      }, 1000);
      return timer_id;
    },
    cancel: function () {
      clearInterval(timer_id);
    }
  };
};

function selectToInitialTime(){
  $('#board-and-times').val(grid_size);
}

function updateTime() {
  // initial_time = time;
  $TIMER_DIV.text(`${initial_time}s`);
}

$BT_START.on('click', function () {
  t   = timer(initial_time * 1000);
  tid = t.start();
  $BT_START.hide();
  $BT_CANCEL.show();
  $BOARD_AND_TIMES.attr('disabled', 'disabled');
});

$BT_CANCEL.on('click', function () {
  window.location.href = `/?grid_size=${grid_size}`;
});

$BOARD_AND_TIMES.on('change', function () {
  const grid           = $(this).val();
  window.location.href = `/?grid_size=${grid}`;
});
