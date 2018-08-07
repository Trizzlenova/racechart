// =========MAP DISPLAY===========

let map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 39, lng: -95},
    zoom: 4.5,
    styles: styles['customMap']
  });
}

let styles = {
  customMap: [
    {
      elementType: 'geometry',
      stylers: [{color: '#02549E'}]
    },
    {
      elementType: 'labels.icon',
      stylers: [{visibility: 'off'}]
    },
    {
      elementType: 'labels.text.fill',
      stylers: [{visibility: 'off'}]
    },
    {
      elementType: 'labels.text.stroke',
      stylers: [{visibility: 'off'}]
    },
    {
        "featureType": "administrative",
        "elementType": "geometry.stroke",
        "stylers": [
            {
                "weight": 1.4
            },
            {
                "color": "#ffffff"
            }
        ]
    },
    {
      featureType: 'administrative.land_parcel',
      elementType: 'labels.text.fill',
      stylers: [{color: '#bdbdbd'}]
    },
    {
      featureType: 'poi',
      elementType: 'geometry',
      stylers: [{color: '#eeeeee'}]
    },
    {
      featureType: 'poi',
      elementType: 'labels.text.fill',
      stylers: [{color: '#757575'}]
    },
    {
      featureType: 'poi.park',
      elementType: 'geometry',
      stylers: [{color: '#e5e5e5'}]
    },
    {
      featureType: 'poi.park',
      elementType: 'labels.text.fill',
      stylers: [{color: '#9e9e9e'}]
    },
    {
      featureType: 'road',
      elementType: 'geometry',
      stylers: [{color: '#ffffff'}]
    },
    {
      featureType: 'road.arterial',
      elementType: 'labels.text.fill',
      stylers: [{color: '#757575'}]
    },
    {
      featureType: 'road.highway',
      elementType: 'geometry',
      stylers: [{color: '#dadada'}]
    },
    {
      featureType: 'road.highway',
      elementType: 'labels.text.fill',
      stylers: [{color: '#616161'}]
    },
    {
      featureType: 'road.local',
      elementType: 'labels.text.fill',
      stylers: [{color: '#9e9e9e'}]
    },
    {
      featureType: 'transit.line',
      elementType: 'geometry',
      stylers: [{color: '#e5e5e5'}]
    },
    {
      featureType: 'transit.station',
      elementType: 'geometry',
      stylers: [{color: '#eeeeee'}]
    },
    {
      featureType: 'water',
      elementType: 'geometry',
      stylers: [{color: '#00ffff'}]
    },
    {
      featureType: 'water',
      elementType: 'labels.text.fill',
      stylers: [{color: '#BC2021'}]
    }
  ]
}

// =========RACETRACK LOCATION===========

let raceTracks = [
{
name: 'Auto Club Speedway',
image: 'static/images/auto_club_speedway.png',
lat: 34.0888,
lng: -117.5005,
},
// {
// name: 'Auto Club Speedway',
// image: 'static/images/auto_club_speedway.png',
// lat: 34.0888,
// lng: -117.5005,
// }
]

let car = "../static/images/car.png"
let trophy = "../static/images/trophyflag.png"

const displayTracks = () => {
  console.log(raceTracks[0].lng)
  let marker = new google.maps.Marker({
    map: map,
    title: raceTracks[0].name,
    position: {
      lat: raceTracks[0].lat,
      lng: raceTracks[0].lng,
    },
    icon: {
      url: trophy,
      // scaledSize: {height: 55, width: 55},
    }
  })
    let contentString = `<div id="content">
            <h2 id="firstHeading" class="firstHeading">${raceTracks[0].name}</h2>
            <div id="bodyContent">'
            <img src="${raceTracks[0].image}"/>
            </div>
            </div>`;
        let infowindow = new google.maps.InfoWindow({
          content: contentString
        });
        marker.addListener('mouseover', function() {
            infowindow.open(map, marker)
        })
        marker.addListener('mouseout', function() {
            infowindow.close(map, marker)
        })
}




// let geocoder = new google.maps.Geocoder();
// let address;
// let track;

// let marker;

// const displayTracks = () => {
//   for(let i = 0; i < raceData.length; i++) {
//     track = raceData[i]['track']
//     address = track
//     geocoder = new google.maps.Geocoder();
//     geocoder.geocode( { 'address': address }, function(results, status) {
//       if (status == google.maps.GeocoderStatus.OK) {
//         console.log(raceData[i]['track'])
//         let marker = new google.maps.Marker({
//           map: map,
//           title: raceData[i]['track'],
//           position:
//               {
//                 lat: results[0].geometry.location.lat(),
//                 lng: results[0].geometry.location.lng(),
//               },
//           icon: {
//             url: trophy,
//           }
//         });
//         var contentString = '<div id="content">'+
//             '<h2 id="firstHeading" class="firstHeading">Charlotte Speedway</h2>'+
//             '<div id="bodyContent">'+
//             '<img src="static/images/charlotte_track.JPG"/>'+
//             '</div>'+
//             '</div>';
//         var infowindow = new google.maps.InfoWindow({
//           content: contentString
//         });
//         marker.addListener('mouseover', function() {
//             infowindow.open(map, marker)
//         })
//         marker.addListener('mouseout', function() {
//             infowindow.close(map, marker)
//         })
//       }
//     });
//   }
// }


