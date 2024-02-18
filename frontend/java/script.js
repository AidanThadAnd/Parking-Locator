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
});

 maxParkingTimeRange = document.getElementById("max-parking-time");
 maxParkingTimeDisplay = document.getElementById("max-parking-time-display");
maxParkingTimeRange.addEventListener("input", () => {
     hours = maxParkingTimeRange.value / 60;
     formattedHours = hours === 1 ? "1 hour" : hours + " hours";
    maxParkingTimeDisplay.textContent = formattedHours;
});

 paidParkingSelect = document.getElementById("paid-parking");
 paidParkingValue = document.getElementById("paid-parking-value");
paidParkingSelect.addEventListener("change", () => {
    paidParkingValue.textContent = paidParkingSelect.value === "yes" ? "Yes" : "No";
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