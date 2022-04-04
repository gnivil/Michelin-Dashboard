// Adding tile layer
var streetmap = L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
  tileSize: 512,
  maxZoom: 18,
  zoomOffset: -1,
  id: "mapbox/streets-v11",
  accessToken: API_KEY
});
// var link = "/get_data"
// // Grabbing our GeoJSON data..
// d3.json(link).then(function(error, data) {
//   // See if we made connection with the data
//   console.log(data)
//   // L.geoJson(data).addTo(myMap);
// });


// DummyData: var three_stars = [
// {Restaurant_Name: 'Alinea',
// City: 'Chicago',
// Price_Range: '210 - 365 USD',
// Restauarant_Website: 'https://www.alinearestaurant.com/',
// Latitude: 41.913274,
// Longitude: -87.648174,
// Location: [41.913274, -87.648174]},
// {
//   Restaurant_Name: 'Kashiwaya',
//   City: 'Tokyo',
//   Price_Range: '13,000 - 43,000 JPY',
//   Restauarant_Website: 'https://jp-kashiwaya.com/senriyama/',
//   Latitude: 41.9110,
//   Longitude: -87.6349,
//   Location: [41.9110, -87.6349]
// }
// ];

// DummyData: var two_stars = [
//   {Restaurant_Name: 'Oriole',
//   City: 'Chicago',
//   Price_Range: '215 USD',
//   Restauarant_Website: 'https://www.oriolechicago.com/',
//   Latitude: 41.9761,
//   Longitude: -87.8169,
//   Location: [41.9761, -87.8169]},
//   {
//     Restaurant_Name: 'Smyth',
//     City: 'Chicago',
//     Price_Range: '225 - 280 USD',
//     Restauarant_Website: 'https://www.smythandtheloyalist.com/',
//     Latitude: 41.8850,
//     Longitude: -87.6606,
//     Location: [41.8850, -87.6606]
//   }
// ];



// An array which will be used to store created restaurant markers
var restmarkers_three = [];
var restmarkers_two = [];
var restmarkers = [];

var greenIcon = new L.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-green.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

var redIcon = new L.Icon({
  iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
  shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
  popupAnchor: [1, -34],
  shadowSize: [41, 41]
});

for (var i = 0; i < data_collection_3.length; i++) {
  var rest = data_collection_3[i];

  restmarkers_three.push(
    L.marker([rest.latitude, rest.longitude], { icon: greenIcon })
      .bindPopup("<h1>" + rest.name + "</h1> <br> " + rest.city + " " + "<br> Price Range: " + rest.price_range + " <br> Restaurant URL: " + rest.restaurant_website)
  )
};

for (var i = 0; i < data_collection_2.length; i++) {
  var rest_two = data_collection_2[i];

  restmarkers_two.push(
    L.marker([rest_two.latitude, rest_two.longitude], { icon: redIcon })
      .bindPopup("<h2>" + rest_two.name + "</h2> <br> " + rest_two.city + " " + "<br> Price Range: " + rest_two.price_range + " <br> Restaurant URL: " + rest_two.restaurant_website)
  )
};

for (var i = 0; i < data_collection.length; i++) {
  var rest_one = data_collection[i];

  restmarkers.push(
    L.marker([rest_one.latitude, rest_one.longitude])
      .bindPopup("<h3>" + rest_one.name + "</h3> <br> " + rest_one.city + " " + "<br> Price Range: " + rest_one.price_range + " <br> Restaurant URL: " + rest_one.restaurant_website)
  )
};

var cityLayer_three = L.layerGroup(restmarkers_three);
var cityLayer_two = L.layerGroup(restmarkers_two);
var cityLayer = L.layerGroup(restmarkers);


// Define variables for our tile layers
var outdoors = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "outdoors-v10",
  accessToken: API_KEY
});

var dark = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "dark-v10",
  accessToken: API_KEY
});

// Only one base layer can be shown at a time
var baseMaps = {
  Map: outdoors,
  Dark: dark
};

// Overlays that may be toggled on or off
var overlayMaps = {
  Three_Stars: cityLayer_three,
  Two_Stars: cityLayer_two,
  One_Star: cityLayer

};

function makeMap(lat, lon) {
  var myMap = L.map("map", {
    center: [lat, lon],
    zoom: 12,
    layers: [outdoors, cityLayer_two, cityLayer_three, cityLayer, streetmap]
  });
  return myMap
}

var myMap = centermap(60610);

// Select the button
var button = d3.select("#filter-btn")
// Select the form
var form = d3.select("#form");

// Select the button
var citybutton = d3.select("#city-btn")
// Select the form
var cityform = d3.select("#city-form");



// Create event handlers for clicking the button or pressing the enter key
button.on("click", runEnter);
form.on("submit", runEnter);
// function called runEnter
citybutton.on("click", runCityEnter);
cityform.on("submit", runCityEnter);

function runEnter() {
  // Prevent the page from refreshing
  d3.event.preventDefault();
  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#zipcode");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");
  //   ... // code to grab form
  //   ... // filter data to get lat lon for restaurant name
  //   makeMap(lat, lon)
  console.log(inputValue);
  centermap(inputValue)
}

function runCityEnter() {
  // Prevent the page from refreshing
  d3.event.preventDefault();
  // Select the input element and get the raw HTML node
  var inputElement = d3.select("#city");

  // Get the value property of the input element
  var inputValue = inputElement.property("value");

  console.log(inputValue);

  centercitymap(inputValue)
}


const data_sets = [].concat(data_collection, data_collection_2,data_collection_3)


function centercitymap(city) {
  var filteredData = data_sets.filter(object => object.city === city);
    // console.log(filteredData)
    var latitude = filteredData[0].latitude
    var longitude = filteredData[0].longitude

    if (typeof myMap != 'undefined') {
      myMap.remove()
    }

    myMap = makeMap(latitude, longitude);
    legend.addTo(myMap);
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);

  }
 
function centermap(zipcode) {



  baseurl = `https://maps.googleapis.com/maps/api/geocode/json?key=${google_api_key}&components=postal_code:`
  // console.log(baseurl)


  d3.json(baseurl + zipcode).then(function (geodata) {
    coordinates = geodata.results[0].geometry.location
    // console.log(coordinates)





    if (typeof myMap != 'undefined') {
      myMap.remove()
    }

    myMap = makeMap(coordinates.lat, coordinates.lng);
    legend.addTo(myMap);
    L.control.layers(baseMaps, overlayMaps).addTo(myMap);

  })
};
var legend = L.control({ position: 'bottomright' });

legend.onAdd = function (map) {

  var div = L.DomUtil.create('div', 'info legend');



  div.innerHTML +=
    '<i style="background:' + "green" + '"></i> ' + "Three Stars" +
    '<br>' + '<br>' + '<i style="background:' + "red" + '"></i> ' + "Two Stars" +
    '<br>' + '<br>' + '<i style="background:' + "blue" + '"></i> ' + "One Star"
    ;

  return div;
};



// Pass our map layers into our layer control
// Add the layer control to the map

;