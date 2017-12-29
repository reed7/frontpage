$(function() {
    $("#qa_list button").hover(
        function() { $(this).animate({backgroundColor: "rgba(0, 0, 0, .1)"}, 80)},
        function() { $(this).animate({backgroundColor: "rgba(0, 0, 0, 0)"}, 80)}
    );

    $("#qa_list a").hover(
        function() { $(this).animate({backgroundColor: "rgba(0,104,183,.2)"}, 80)},
        function() { $(this).animate({backgroundColor: "rgba(0, 0, 0, 0)"}, 80)}
    );

    $("#how_contact").click(function() {
        $('html, body').animate({scrollTop: $(document).height()}, 'slow');
    });

    $("#contact_bar svg").hover(
        function() { $(this).animate({backgroundColor: "rgba(0, 0, 0, .3)"}, 80)},
        function() { $(this).animate({backgroundColor: "rgba(0, 0, 0, 0)"}, 80)}
    );

    $("#portrait").hover(
        function() { $(this).attr('src', color_portrait) },
        function() { $(this).attr('src', bw_portrait) }
    );

    $("#show_autox").click(function() {
        $(".mask").show("blind", 300);
        $('.photo-box').css({
            'padding-top': ($(window).height() - 470)/2 // vertical center
        });
        $('.photo-box').show("blind", 400);

        $('.photo-box').bind('click', function(){
            $('.mask').hide("blind", 200);
            $(this).hide("blind", 200);
        });
     });

    $(window).resize(function(event) {

    });
});