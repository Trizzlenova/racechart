function getRaceDates(){
  axios.get('/api/standings')
  .then(function(response) {
    console.log(response.data.date)
    console.log(response.data.top15)
    for(let i = 0; i < response.data; i++) {
      let node = document.createElement("option");
      let textnode = document.createTextNode()
      node.appendChild(textnode);
      raceMenu.appendChild(node);
    }





  .then(function(response) {
    console.log(response.data.length)
    let info = [];
    for(let i = 0; i < response.data.length/2; i++) {
      let latis = parseFloat(response.data[i].gtfs_latitude);
      let longis = parseFloat(response.data[i].gtfs_longitude);
      let bartStation = response.data[i].name
      // console.log(response.data[i]);
      // console.log(station[i].abbr)
        // console.log(parseFloat(response.data.root.stations.station[i].gtfs_latitude) + " " + parseFloat(response.data.root.stations.station[i].gtfs_longitude))
      let marker = new google.maps.Marker({
        map: map,
        title: bartStation,
        position: {
          lat: latis,
          lng: longis,
        },
        icon: {
          // railway station by Artdabana@Design from the Noun Project
          url: "images/railroadBlk.svg",
          scaledSize: {height: 55, width: 55},
        }
      });
      // Finding Nearest Bart using distance formula
        let dlat = parseFloat(latis - lateral);
        let dlng = parseFloat(longis - longital);
        let distance = Math.sqrt(Math.pow(dlat ,2) + Math.pow(dlng, 2));
        info[i] = {bartStation: bartStation, lat: latis, lng: longis, distance: distance};
      };
      info.sort(findNearestBart);
      for(let j = 0; j < 1; j++) {
        console.log(info[j].bartStation);
        let node = document.createElement("option");
        let textnode = document.createTextNode(info[j].bartStation)
        node.appendChild(textnode);
        stationMenu.appendChild(node);
        callTravelTime(lateral, longital, info[j].lat, info[j].lng, stations);
      }
      // selectedVal(){
    })
  .catch(function(err){
    console.log(err)
  });
}
