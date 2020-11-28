const $TIMER_DIV = $('#timer_div');
const $BT_START  = $('#bt-start');
const $BT_CANCEL = $('#bt-cancel');
let initial_time = 60;

$BT_CANCEL.hide();
$TIMER_DIV.text(`${initial_time}s`);

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

$BT_START.on('click', function () {
  t   = timer(60 * 1000);
  tid = t.start();
  $BT_START.hide();
  $BT_CANCEL.show();
  $BT_CANCEL.on('click', function () {
    // This works:
    // t.cancel();
    // $BT_START.show();
    // $BT_CANCEL.hide();

    // But I prefer this in this particular exercise:
    location.reload();
  });

});
