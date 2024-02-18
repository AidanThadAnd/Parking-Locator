/*
Adds the functionality to bring up the filters menu when pressing the filter button
*/
const filtersButton = document.querySelector('.filters-button');
const filterMenu = document.querySelector('.filter-menu');

filtersButton.addEventListener('click', () => {
  filterMenu.classList.toggle('shown');
});


/*
Adds the ability to bring down the filters menu
*/
const closeButton = document.querySelector('.close-button');
closeButton.addEventListener('click', () => {
    filterMenu.classList.toggle('shown');
  });

/*
For The filters menu
*/

// JavaScript code to handle changes in filter values and update displayed values
const walkingTimeRange = document.getElementById("walking-time");
const walkingTimeValue = document.getElementById("walking-time-value");
  walkingTimeRange.addEventListener("input", () => {
    walkingTimeValue.textContent = walkingTimeRange.value + " minutes";
});

const maxParkingTimeRange = document.getElementById("max-parking-time");
const maxParkingTimeValue = document.getElementById("max-parking-time-value");
  maxParkingTimeRange.addEventListener("input", () => {
const hours = maxParkingTimeRange.value / 60;
const formattedHours = hours === 1 ? "1 hour" : hours + " hours";
    maxParkingTimeValue.textContent = formattedHours;
});

//Leaflet

// Create a map instance and set the view
var mymap = L.map('realMap').setView([51.505, -0.09], 13);

// Add a tile layer from OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '© OpenStreetMap contributors'
}).addTo(mymap);
