$(document).ready(function() {
    var navItems = $("#nav-links");
    var trans = 150;

    // Resize Window
    $(window).on('resize', function() {
        var win = $(window);
        if (win.width() > 700) {        // desktop
            navItems.show();
        } else {                        // mobile
            navItems.hide();
            $("#burger-1").animate({margin: '3px 0px'}, 0);
            $("#burger-3").animate({margin: '3px 0px'}, 0);
        }
    });

    // Click Burger
    $("#burger").click(function() {
        if ($(navItems).is(":hidden")) {
            $("#burger-1").animate({margin: '0px 0px 6px 0px'}, trans);
            $("#burger-3").animate({margin: '6px 0px 0px 0px'}, trans);
            navItems.slideDown(200);
        } else {
            $("#burger-1").animate({margin: '3px 0px'}, trans);
            $("#burger-3").animate({margin: '3px 0px'}, trans);
            navItems.slideUp(200);
        }
    });

});
