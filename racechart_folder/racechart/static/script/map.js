// =========MAP DISPLAY===========

let map = new google.maps.Map(document.getElementById('map'), {
  center: {lat: 39, lng: -95},
  zoom: 4.5
});

// =========RACE LOCATION===========

// let locations = [];
// const displayTracks = () => {
//   for(let i = 0; i < raceData.length; i++) {
//     locations.push(raceData[i]['track'])
//     console.log(track)
//     let marker = new google.maps.Marker({
//       map: map,
//       title: track,
//       position: {lat: 37.7749, lng: -122.4194},
//       icon: {
//         url: "images/car_point.png",
//         scaledSize: {height: 55, width: 55},
//       }
//     })
//   }
//   console.log(locations)
// }

// displayTracks()

// console.log(locations)


// console.log()

displayShit()
