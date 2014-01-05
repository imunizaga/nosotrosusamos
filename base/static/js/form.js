var $datePicker = $('.date-picker');
if ($datePicker.datepicker) {
  $datePicker.datepicker({
    format: "dd/mm/yyyy",
    language: "es"
  });
}

$('.model-form input:text').addClass('form-control');

$('select').not('.filtered').select2({
  width: "95%"
});
