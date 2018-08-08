// =========CREATE PROMISE===========
let displayMapsFirst = new Promise((resolve, reject) => {
  setTimeout(function(){
    resolve('maps loaded');
    initMap()
  }, 250);
});

displayMapsFirst.then((successMessage) => {
  console.log('racetracks loaded' + successMessage);
  displayTracks()
});

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

let racetracks = [
  {
    name: 'Atlanta Motor Speedway',
    image: 'static/images/racetracks/atlanta.jpg',
    lat: 33.3868,
    lng: -84.3164,
  },
  {
    name: 'Auto Club Speedway',
    image: 'static/images/racetracks/auto_club_speedway.png',
    lat: 34.0888,
    lng: -117.5005,
  },
  {
    name: 'Bristol Motor Speedway',
    image: 'static/images/racetracks/bristol.png',
    lat: 36.5157,
    lng: -82.2570,
  },
  {
    name: 'Charlotte Motor Speedway',
    image: 'static/images/racetracks/charlotte_track.JPG',
    lat: 35.3515,
    lng: -80.6866,
  },
  {
    name: 'Daytona International Speedway',
    image: 'static/images/racetracks/daytona.jpg',
    lat: 29.2108,
    lng: -81.0228,
  },
  {
    name: 'Dover International Speedway',
    image: 'static/images/racetracks/dover.jpg',
    lat: 39.1899,
    lng: -75.5307,
  },
  {
    name: 'Kansas Speedway',
    image: 'static/images/racetracks/kansas_speedway.jpg',
    lat: 39.0997,
    lng: -94.5786,
  },
  {
    name: 'Las Vegas Motor Speedway',
    image: 'static/images/racetracks/las_vegas.jpg',
    lat: 36.2723,
    lng: -115.0103,
  },
  {
    name: 'Martinsville Speedway',
    image: 'static/images/racetracks/martinsville.jpg',
    lat: 36.6341,
    lng: -79.8517,
  },
  {
    name: 'Phoenix International Raceway',
    image: 'static/images/racetracks/phoenix.jpeg',
    lat: 33.3749,
    lng: -112.3112,
  },
  {
    name: 'Richmond International Raceway',
    image: 'static/images/racetracks/richmond.jpg',
    lat: 37.5924,
    lng: -77.4195,
  },
  {
    name: 'Talladega Superspeedway',
    image: 'static/images/racetracks/talladega.jpg',
    lat: 33.5670,
    lng: -86.0661,
  },
  {
    name: 'Texas Motor Speedway',
    image: 'static/images/racetracks/texas_motor.jpg',
    lat: 33.0373,
    lng: -97.2821,
  },
]

let trophy = "../static/images/trophy.png"

const displayTracks = () => {
  for(let i = 0; i < racetracks.length; i++) {
    let marker = new google.maps.Marker({
      map: map,
      title: racetracks[i].name,
      position: {
        lat: racetracks[i].lat,
        lng: racetracks[i].lng,
      },
      icon: {
        url: trophy,
        scaledSize: {height: 66, width: 55},
      }
    })
    let raceTrackInfoWindow = `<div id="content">
        <h2 id="firstHeading" class="firstHeading">${racetracks[i].name}</h2>
        <div id="bodyContent">'
        <img src="${racetracks[i].image}"/>
        </div>
        </div>`;
    let infowindow = new google.maps.InfoWindow({
      content: raceTrackInfoWindow
    });
    marker.addListener('mouseover', function() {
        infowindow.open(map, marker)
    })
    marker.addListener('mouseout', function() {
        infowindow.close(map, marker)
    })
  }
}

