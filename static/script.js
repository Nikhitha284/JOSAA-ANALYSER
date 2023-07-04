 // Fetch data from the backend API
 function fetchData() {
  fetch('/api/seat-allotments/')
    .then(response => response.json())
    .then(data => {
      // Process the fetched data
      if (data && data.length > 0) {
        const parsedData = JSON.parse(data);
        displayData(parsedData);
      } else {
        console.error('No data available');
        // Handle empty data case
      }
    })
    .catch(error => {
      console.error('Error:', error);
      // Handle error case
    });
}

// Display the fetched data on the frontend
function displayData(data) {
  const container = document.getElementById('data-container');
  container.innerHTML = '';

  // Example: Display seat allotment data in a table
  const table = document.createElement('table');
  const tableHead = document.createElement('thead');
  const tableBody = document.createElement('tbody');

  // Create table header row
  const headerRow = document.createElement('tr');
  const headerColumns = Object.keys(data[0].fields);

  headerColumns.forEach(column => {
    const th = document.createElement('th');
    th.textContent = column;
    headerRow.appendChild(th);
  });

  tableHead.appendChild(headerRow);
  table.appendChild(tableHead);

  // Create table body rows
  data.forEach(item => {
    const row = document.createElement('tr');
    const columns = Object.values(item.fields);

    columns.forEach(column => {
      const td = document.createElement('td');
      td.textContent = column;
      row.appendChild(td);
    });

    tableBody.appendChild(row);
  });

  table.appendChild(tableBody);
  container.appendChild(table);
}

// Call the fetchData function when the page is loaded
window.addEventListener('DOMContentLoaded', fetchData);

