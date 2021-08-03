(function ($) {
    $(document).ready(function () {
      
        $('img').each(function () {
            var $el = $(this),
                s = $el.attr('src'),
                sRx = /^[\/data\/]+/igm;
            if (sRx.test(s)) {
                s = 'http:' + s;
                $el.attr('src',s);
            }
        });
       
    });
})(jQuery);

