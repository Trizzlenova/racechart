let raceData = [];
const getRaces = () => {
  axios.get('/api/races')
  .then(function(response) {
    for (let i= 0; i < response.data.length; i++) {
      raceData.push(response.data[i])
    }
  })
}

let driverInfo = [];
const getResults = () => {
  axios.get(`/api/results/`)
  .then(function(response) {
    for (let i= 0; i < response.data.length; i++) {
      driverInfo.push(response.data[i])
    }
    initMap()
  })
}

function queueFunction(milliseconds, runFunction) {
  var start = new Date().getTime();
  for (var i = 0; i < 1e7; i++) {
    if ((new Date().getTime() - start) > milliseconds){
      break;
    }
  }
  runFunction
  console.log(runFunction + ' is running!')
}
