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
