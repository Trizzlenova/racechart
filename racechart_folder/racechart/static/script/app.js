// Grab data from api.js
getRaces();
getResults();

const createGraph = (data) => {
  // set the dimensions and margins of the graph
  var margin = {top: 20, right: 20, bottom: 30, left: 50},
      width = 700 - margin.left - margin.right,
      height = 400 - margin.top - margin.bottom;

  // parse the date / time
  var parseTime = d3.timeParse("%m/%d/%Y");

  // set the ranges
  var x = d3.scaleTime().range([0, width]);
  var y = d3.scaleLinear().range([height, 0]);

  // define the line
  var valueline = d3.line()
      .x(function(d) { return x(d.date); })
      .y(function(d) { return y(d.rank); });

  // append the svg obgect to the body of the page
  // appends a 'group' element to 'svg'
  // moves the 'group' element to the top left margin
  var svg = d3.select("#graphed").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");


  // Scale the range of the data
  x.domain(d3.extent(data, function(d) { return d.date; }));
  y.domain([0, d3.max(data, function(d) { return d.rank; })]);

  // Add the valueline path.
  svg.append("path")
    .data([data])
    .attr("class", "line")
    .attr("d", valueline);

  // Add the X Axis
  svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));

  // Add the Y Axis
  svg.append("g")
      .call(d3.axisLeft(y));
  svg.append("text")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", ".71em")
      .style("text-anchor", "end")
      .text("Finishing Position");
}

const getId = (driverId) => {
  let data = [];
  selectedDriver = driverId[driverId.selectedIndex].id;
  $('#graphed').empty();

  for(let i = 0; i < driverInfo.length; i++) {
    if (selectedDriver == driverInfo[i].driver) {
      raceData.forEach((raceInfo) => {
        let position = driverInfo[i].position
        if(raceInfo.id === driverInfo[i].race) {
          let year = parseInt(raceInfo.start_time.substring(0, 4));
          let month = parseInt(raceInfo.start_time.substring(5, 7));
          let day = parseInt(raceInfo.start_time.substring(8, 10));
          let startDate = month + '/' + day + '/' + year;
          let parseTime = d3.timeParse("%m/%d/%Y");
          startDate = parseTime(startDate);
          data.push({'date': startDate, 'rank': position});
        }
      })
      data.forEach(function(d) {
        d.rank = +d.rank;
      });
    };
  }
  createGraph(data);
}
