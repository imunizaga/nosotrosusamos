/*global categoryData: false */
/*global tagData: false */

(function () {
  'use strict';
  // Load the Visualization API and the piechart package.
  google.load('visualization', '1.0', {'packages': ['corechart']});

  // Callback that creates and populates a data table,
  // instantiates the pie chart, passes in the data and
  // draws it.
  function drawChart() {

    // Create the data table.
    var data,
      $charts,
      $chartDiv,
      category,
      chart,
      i,
      j,
      options,
      rowData,
      tag;

    $charts = $('.charts');
    // iterate over all categories
    for (i = 0; i < categoryData.length; i += 1) {
      category = categoryData[i];

      data = new google.visualization.DataTable();

      data.addColumn('string', 'Tag');
      data.addColumn('number', 'Entrevistas');

      rowData = [];
      for (j = 0; j < tagData.length; j += 1) {
        tag = tagData[j];
        if (tag.categories.indexOf(category.id) >= 0) {
          rowData.push([tagData[j].title, tagData[j].num_interviews]);
        }
      }

      data.addRows(rowData);

      $chartDiv = $('<div></div>');
      $charts.append($chartDiv);
      // Set chart options
      options = {
        'title': category.title,
        'width': 400,
        'height': 300
      };

      // Instantiate and draw our chart, passing in some options.
      chart = new google.visualization.PieChart($chartDiv[0]);
      chart.draw(data, options);
    }
  }

  // Set a callback to run when the Google Visualization API is loaded.
  google.setOnLoadCallback(drawChart);
}());
