$(document).ready(() => {
  // code comes here
  $(window).scroll(function () {
    var scroll = $(document).scrollTop();

    if (scroll > 100) {
      $("#navigation").addClass("shadow-sm");
    } else {
      $("#navigation").removeClass("shadow-sm");
    }
  });
});
