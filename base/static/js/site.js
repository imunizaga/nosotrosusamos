/*global document: false */
/*global location: false */
/*global $: false */

$(document).ready(function () {
    "use strict";
    $('[data-toggle=offcanvas]').click(function () {
        $('.row-offcanvas').toggleClass('active');
    });

    $('a.list-group-item').removeClass('active');

    $('a.list-group-item.' + location.pathname.replace(/\//g, '')).addClass('active');
});
