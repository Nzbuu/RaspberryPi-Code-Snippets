var main = function() {
// insert code here
var vis = d3.select('#visualisation'),
    WIDTH = 1000,
    HEIGHT = 500,
    MARGINS = {
      top: 20,
      right: 20,
      bottom: 20,
      left: 50
    }

xRange = d3.scale.linear().range([MARGINS.left, WIDTH - MARGINS.right]).domain([d3.min(lineData, function(d) {
      return d.time;
}), d3.max(lineData, function(d) {
      return d.time;
    })]);
yRange = d3.scale.linear().range([HEIGHT - MARGINS.top, MARGINS.bottom]).domain([d3.min(lineData, function(d) {
      return d.temperature;
    }), d3.max(lineData, function(d) {
      return d.temperature;
    })]);

xAxis = d3.svg.axis()
      .scale(xRange)
      .tickSize(5)
      .tickSubdivide(true),

yAxis = d3.svg.axis()
      .scale(yRange)
      .tickSize(5)
      .orient('left')
      .tickSubdivide(true);
 
vis.append('svg:g')
  .attr('class', 'time axis')
  .attr('transform', 'translate(0,' + (HEIGHT - MARGINS.bottom) + ')')
  .call(xAxis);
 
vis.append('svg:g')
  .attr('class', 'temperature axis')
  .attr('transform', 'translate(' + (MARGINS.left) + ',0)')
  .call(yAxis);

 // Xlabel 
vis.append("text")
  .attr("class", "x label")
  .attr("text-anchor", "middle")
  .attr("x", WIDTH/2)
  .attr("y", HEIGHT-1)
  .text("Time [h]");

vis.append("text")
  .attr("class", "y label")
  .attr("text-anchor", "middle")
  .attr("x", -HEIGHT/2)
  .attr("y", 6)
  .attr("dy", ".75em")
  .attr("transform", "rotate(-90)")
  .text("Temperature [degC]");

// Line Plot
/*var lineFunc = d3.svg.line()
  .x(function(d) {
    return xRange(d.time);
  })
  .y(function(d) {
    return yRange(d.temperature);
  })
  .interpolate('linear');

 vis.append('svg:path')
  .attr('d', lineFunc(lineData))
  .attr('stroke', '#2E64FE')
  .attr('stroke-width', 2)
  .attr('fill', 'none'); */

// Data points plot
var point = vis.append('svg:g')
.attr("class", "line-point");

point.selectAll('circle')
.data(lineData)
.enter().append('circle')
.attr("cx", function(d) { return xRange(d.time) })
.attr("cy", function(d) { return yRange(d.temperature) })
.attr("r", 1)
.style("fill", '#2E64FE')
.style("stroke", '#2E64FE');    
}

$(document).ready(main);


