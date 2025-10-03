// City coordinates
const cities = {
  "Cairo": [30.0444, 31.2357],
  "Tokyo": [35.6895, 139.6917],
  "Rio": [-22.9068, -43.1729],
  "Sydney": [-33.8688, 151.2093],
  "WashingtonDC": [38.9072, -77.0369]
};

let map; // store map reference

// Only initialize map when modal is shown
document.getElementById('mapModal').addEventListener('shown.bs.modal', function () {
  setTimeout(() => {
    if (!map) {
      map = L.map('map').setView([20, 0], 2); // world view

      // Tile layer
      L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '© OpenStreetMap contributors'
      }).addTo(map);

      // Add markers
      for (let city in cities) {
        let marker = L.marker(cities[city]).addTo(map).bindPopup(city);
        marker.on('click', function () {
          document.getElementById('city').value = city;
          bootstrap.Modal.getInstance(document.getElementById('mapModal')).hide();
        });
      }
    }
  }, 300);
});