//Width and height
var w = 500;
var h = 250;
var barPadding = 1;


//Create SVG element
var svg = d3.select("#d3_demo_1")
			.append("svg")
			.attr("width", w)
			.attr("height", h);


$("#bn_d3_demo_1").click(function() {	

	//generate an array with length 30, number range from 15 to 30
	var dataset = [];
	/*var dataset = [ 5, 10, 13, 19, 21, 25, 22, 18, 15, 13,
					11, 12, 15, 20, 18, 17, 16, 18, 23, 25 ];*/
	for (var i = 0; i < 25; i++) {
		dataset.push(Math.round(Math.random()*15 + 15));
	}

	svg.selectAll("rect")
	   .data(dataset)
	   .enter()
	   .append("rect")
	   .attr("x", function(d, i) {
	   		return i * (w / dataset.length);
	   })
	   .attr("y", function(d) {
	   		return h - (d * 4);
	   })
	   .attr("width", w / dataset.length - barPadding)
	   .attr("height", function(d) {
	   		return d * 4;
	   })
	   .attr("fill", function(d) {
			return "rgb(0, 0, " + (d * 10) + ")";
	   });

	svg.selectAll("text")
	   .data(dataset)
	   .enter()
	   .append("text")
	   .text(function(d) {
	   		return d;
	   })
	   .attr("text-anchor", "middle")
	   .attr("x", function(d, i) {
	   		return i * (w / dataset.length) + (w / dataset.length - barPadding) / 2;
	   })
	   .attr("y", function(d) {
	   		return h - (d * 4) + 14;
	   })
	   .attr("font-family", "sans-serif")
	   .attr("font-size", "11px")
	   .attr("fill", "white");	
});
		
		