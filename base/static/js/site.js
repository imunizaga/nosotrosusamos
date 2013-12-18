/*global document: false */
/*global location: false */
/*global $: false */

$(document).ready(function () {
    "use strict";
    $('[data-toggle=offcanvas]').click(function () {
        $('.row-offcanvas').toggleClass('active');
    });

    $('a.list-group-item').removeClass('active');

    var slug = location.pathname.replace(/\//g, '');
    if (slug !== "") {
        $('a.list-group-item.' + slug).addClass('active');
    }
});
