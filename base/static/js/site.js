/*global document: false */
/*global $: false */

$(document).ready(function () {
    "use strict";
    $('[data-toggle=offcanvas]').click(function () {
        $('.row-offcanvas').toggleClass('active');
    });
});
