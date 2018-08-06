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

let geocoder = new google.maps.Geocoder();
let address;
let track;

let car = "../static/images/car.png"
let trophy = "../static/images/trophyflag.png"
let marker;

const displayTracks = () => {
  for(let i = 0; i < raceData.length; i++) {
    track = raceData[i]['track']
    address = track
    geocoder = new google.maps.Geocoder();
    geocoder.geocode( { 'address': address }, function(results, status) {
      if (status == google.maps.GeocoderStatus.OK) {
        console.log(raceData[i]['track'])
        let marker = new google.maps.Marker({
          map: map,
          title: raceData[i]['track'],
          position:
              {
                lat: results[0].geometry.location.lat(),
                lng: results[0].geometry.location.lng(),
              },
          icon: {
            url: trophy,
            // scaledSize: {height: 70, width: 60},
          }
        });
        marker.addListener('mouseover', function() {
            marker.setIcon(car);
        })
        marker.addListener('mouseout', function() {
            marker.setIcon(trophy);
        })
      }
    });
  }
}


