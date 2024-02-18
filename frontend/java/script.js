let address = "";
let paidParkingValueAPI = true;
let maxParkingTimeValueAPI = 240;
let walkingTimeValueAPI = 2.0;


/*
Adds the functionality to bring up the filters menu when pressing the filter button
*/
filtersButton = document.querySelector('.filters-button');
filterMenu = document.querySelector('.filter-menu');

filtersButton.addEventListener('click', () => {
  filterMenu.classList.toggle('shown');
});


/*
Adds the ability to bring down the filters menu
*/
closeButton = document.querySelector('.close-button');
closeButton.addEventListener('click', () => {
    filterMenu.classList.toggle('shown');
});

/*
For The filters menu
*/

// JavaScript code to handle changes in filter values and update displayed values
walkingTimeRange = document.getElementById("walking-time");
walkingTimeValue1 = document.getElementById("walking-time-display");
walkingTimeValue = document.getElementById("walking-time-value");
walkingTimeRange.addEventListener("input", () => {
 walkingTimeValue.textContent = walkingTimeRange.value + " minutes";
});

maxParkingTimeRange = document.getElementById("max-parking-time");
maxParkingTimeValue1 = document.getElementById("max-parking-time-display");
maxParkingTimeValue = document.getElementById("max-parking-time-value");


maxParkingTimeRange.addEventListener("input", () => {
  hours = maxParkingTimeRange.value / 60;
  formattedHours = hours === 1 ? "1 hour" : hours + " hours";
 maxParkingTimeValue.textContent = formattedHours;
 
});

// Update paid parking display
paidParkingSelect = document.getElementById("paid-parking");
paidParkingValue = document.getElementById("paid-parking-value");
paidParkingSelect.addEventListener("change", () => {
 paidParkingValue.textContent = paidParkingSelect.value === "yes" ? "Yes" : "No";
 
});
 walkingTimeRange = document.getElementById("walking-time");
 walkingTimeDisplay = document.getElementById("walking-time-display");
walkingTimeRange.addEventListener("input", () => {
    walkingTimeDisplay.textContent = walkingTimeRange.value + " minutes";
    walkingTimeValueAPI = walkingTimeRange.value;
});

 maxParkingTimeRange = document.getElementById("max-parking-time");
 maxParkingTimeDisplay = document.getElementById("max-parking-time-display");
maxParkingTimeRange.addEventListener("input", () => {
     hours = maxParkingTimeRange.value / 60;
     formattedHours = hours === 1 ? "1 hour" : hours + " hours";
    maxParkingTimeDisplay.textContent = formattedHours;
    maxParkingTimeValueAPI = maxParkingTimeRange.value;
});

 paidParkingSelect = document.getElementById("paid-parking");
 paidParkingValue = document.getElementById("paid-parking-value");
paidParkingSelect.addEventListener("change", () => {
    paidParkingValue.textContent = paidParkingSelect.value === "yes" ? "Yes" : "No";
    paidParkingValueAPI = paidParkingSelect.value;
});


//Leaflet

// Create a map instance and set the view
var mymap = L.map('realMap').setView([51.505, -0.09], 13);

// Add a tile layer from OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(mymap);
 maxParkingTimeRange = document.getElementById("max-parking-time");
 maxParkingTimeValue1 = document.getElementById("max-parking-time-display");
 maxParkingTimeValue = document.getElementById("max-parking-time-value");


maxParkingTimeRange.addEventListener("input", () => {
   hours = maxParkingTimeRange.value / 60;
   formattedHours = hours === 1 ? "1 hour" : hours + " hours";
  maxParkingTimeValue.textContent = formattedHours;
});

// Function to handle search button click
function handleSearch() {
  var searchTerm = document.getElementById('searchInput').value;
  if (searchTerm.trim() !== '') {
      // Perform search operation with the search term (e.g., display results, zoom to location, etc.)
      address = searchTerm;

  } else {
      alert('Please enter a search term.');
  }
}

// Attach click event listener to search button
document.getElementById('search-button').addEventListener('click', handleSearch);

//Talking to backend
async function retrieveParking(/*address, paidParkingValue, maxParkingTimeValue, walkingTimeValue*/) {

  walkingTimeValueAPI = (walkingTimeValueAPI /15);

  walkingTimeValueAPI = parseFloat(walkingTimeValueAPI.toFixed(3));


  const data = {
      addressJSON: address,
      paidParkingValueJSON: paidParkingValueAPI,
      maxParkingTimeValueJSON: maxParkingTimeValueAPI,
      walkingTimeValueJSON: walkingTimeValueAPI
  };

  const response = await fetch('http://127.0.0.1:5000/get_coordinates', {
      method: 'POST',
      headers: {
          'Content-Type': 'application/json',
          'Accept': 'application/json'
      },
      body: JSON.stringify(data)
  });

  // Handle response here
  const result = await response.json();
  coordinate = result.coordinates[0];

  console.log(coordinate);
  
  if(coordinate == undefined)
    alert("Unfortunately no parking has been found")
  else
  {
    updateMap(coordinate);
    zoomToPin(map, coordinate[0], coordinate[1] * -1, 18);
  }

  return;

}
function updateMap(parkingCoords) {
  // Fetch the updated coordinates from the Flask route

          // Clear existing markers
          map.eachLayer(function (layer) {
              if (layer instanceof L.Marker) {
                  map.removeLayer(layer);
              }
          });

          // Add new markers based on the updated coordinates

         
         var marker = L.marker([parkingCoords[0], parkingCoords[1] * -1]).addTo(map);
         return;
}

function zoomToPin(map, latitude, longitude, zoomLevel) {
  map.setView([latitude, longitude], zoomLevel);
}






//walkingTimeValue
//maxParkingTimeValue
//paidParkingValue
//address