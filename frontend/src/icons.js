import L from 'leaflet';

// We'll use simple URLs to generate colored circle icons.
// This is a neat trick to avoid needing actual image files.
const createCircleIcon = (color) => {
  const svg = `
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="32" height="32">
      <circle cx="12" cy="12" r="10" fill="${color}" stroke="white" stroke-width="2"/>
    </svg>
  `;
  const url = `data:image/svg+xml;base64,${btoa(svg)}`;
  return L.icon({
    iconUrl: url,
    iconSize: [32, 32],
    iconAnchor: [16, 16],
    popupAnchor: [0, -16],
  });
};

export const highPriorityIcon = createCircleIcon('#d9534f'); // Red
export const mediumPriorityIcon = createCircleIcon('#f0ad4e'); // Yellow/Orange
export const lowPriorityIcon = createCircleIcon('#5bc0de'); // Blue