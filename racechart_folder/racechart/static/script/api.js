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
  })
}
