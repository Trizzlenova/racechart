// function getRaceDates(){
//   axios.get('/api/standings')
//   .then(function(response) {
//     for(let i = 0; i < response.data; i++) {
//       let node = document.createElement("option");
//       let textnode = document.createTextNode()
//       node.appendChild(textnode);
//       raceMenu.appendChild(node);
//     }

// on selection, generateData() and createGraph

const driverSelected = () => {
  createGraph(generateData());
}

const raceData = [];

const getRaces = () => {
  axios.get('/api/races')
  .then(function(response) {
    raceData.push(response.data)
  })
}

getRaces();

console.log(raceData)

const createGraph = (data) => {
  // set the dimensions and margins of the graph
  var margin = {top: 20, right: 20, bottom: 30, left: 50},
      width = 666 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;

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
  var svg = d3.select("div").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform",
            "translate(" + margin.left + "," + margin.top + ")");

  // format the data
  // data.forEach(function(d) {
  //   d.date = parseTime(d.date);
  //   d.rank = +d.rank;
  // });

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
}

let driverInfo = [];

const getResults = () => {
  axios.get(`/api/results/`)
  .then(function(response) {
    for (let i= 0; i < response.data.length; i++) {
      driverInfo.push(response.data[i])
    }
  })
}

getResults();

console.log(driverInfo)

const getId = (driverId) => {
  let data = [];
  selectedDriver = driverId[driverId.selectedIndex].id;
  $('div').empty();

  for(let i = 0; i < driverInfo.length; i++) {
    if (selectedDriver == driverInfo[i].driver) {
      raceData[0].forEach((raceInfo) => {
        let position = driverInfo[i].position
        if(raceInfo.id === driverInfo[i].race) {
          console.log(raceInfo.start_time);
          let year = parseInt(raceInfo.start_time.substring(0, 4));
          // console.log(year)
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

