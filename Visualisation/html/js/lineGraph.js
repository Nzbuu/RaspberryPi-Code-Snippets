var main = function() {

  var myurl = 'http://127.0.0.1:8080/data'; // for local calls only


  $.ajax({
    url: myurl
  }).done(function(data){
    draw(reshape(data));
  })

 
 function reshape(data){
    // ...
    data = JSON.parse(data);

    data = _.chain(data.time).zip(data.values).map(function(a){ return {x: a[0], y: a[1] };}).value();
    //data = _.zip(data.time, data.values);

    return [
      {
        values: data,      //values - represents the array of {x,y} data points
        key: 'Temperature Data', //key  - the name of the series.
        color: '#ff7f0e',  //color - optional: choose your own line color.
        area: false
      }
    ];
  };
  var formatter = function (d){
    console.log(d);
    return d3.time.format('%Hh %d %b ') (new Date(1000 * d)); // convert linux epoch time to milliseconds

  };

 function draw(data){
    nv.addGraph(function() {
        var chart = nv.models.lineWithFocusChart();

        //Format x-axis labels with custom function.
        chart.xAxis.tickFormat(formatter).axisLabel('Time');
        chart.x2Axis.tickFormat(formatter).axisLabel('Time');

        // y-axis labels
        chart.yAxis.tickFormat(d3.format(',.1f')).axisLabel('Temperature [degC]');
        chart.y2Axis.tickFormat(d3.format(',.1f'));        

        d3.select('#chart svg')
        .datum(data)
        .call(chart);



        
        nv.utils.windowResize(chart.update);
        return chart;
    });  
  };
};

$(document).ready(main);


