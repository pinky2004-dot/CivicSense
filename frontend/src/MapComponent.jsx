import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';

// Celina, TX coordinates
const position = [33.3240, -96.7828];

const MapComponent = ({ issues }) => {
  return (
    <MapContainer center={position} zoom={13} style={{ height: '100vh', width: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {/* We will map over the issues and create markers here */}
      {issues.map((issue, index) => (
        <Marker key={index} position={[
            // For the demo, we'll generate slightly random positions around Celina
            position[0] + (Math.random() - 0.5) * 0.1,
            position[1] + (Math.random() - 0.5) * 0.1,
        ]}>
          <Popup>
            <b>{issue.priority} Priority</b><br />
            {issue.summary || issue.issue || issue.description || 'No summary available.'}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default MapComponent;