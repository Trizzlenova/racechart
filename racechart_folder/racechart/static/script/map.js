// =========MAP DISPLAY===========

// let map = new google.maps.Map(document.getElementById('map'), {
//   center: {lat: 39, lng: -95},
//   zoom: 4.5
// });

// =========RACETRACK LOCATION===========

let geocoder = new google.maps.Geocoder();
let address;
let track
const displayTracks = () => {
  for(let i = 0; i < raceData.length; i++) {
    track = raceData[i]['track']
    address = track
    geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': address }, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        let marker = new google.maps.Marker({
          map: map,
          title: raceData[i]['track'],
          position:
              {
                lat: results[0].geometry.location.lat(),
                lng: results[0].geometry.location.lng(),
              },
          icon: {
            url: "../static/images/car_point.png",
            scaledSize: {height: 30, width: 50},
          }
        })
      }
    });
  }
}

// const displayTracks = () => {
//   for(let i = 0; i < raceData.length; i++) {
//     track = raceData[i]['track']
//     geocoder.geocode({
//     'latLng': event.latLng
//   }, function(results, status) {
//     if (status == google.maps.GeocoderStatus.OK) {
//       if (results[0]) {
//         alert(results[0].formatted_address);
//       }
//     }
//   });
// }


