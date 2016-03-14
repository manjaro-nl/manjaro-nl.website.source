 $(document).ready(function() {
    $("a[href='#top']").click(function() {
        $("html, body").animate({ scrollTop: 0 }, "slow");
        return false;
    });

    $(window).scroll(function(){
         if ($(this).scrollTop() > 200) {
             $('.btn-scroll-to-top').fadeIn();
         } else {
             $('.btn-scroll-to-top').fadeOut();
         }
    });
});
