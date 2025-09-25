import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import { highPriorityIcon, mediumPriorityIcon, lowPriorityIcon } from './icons';

const position = [33.3240, -96.7828];

const getPriorityIcon = (priority) => {
  switch (priority?.toLowerCase()) {
    case 'high':
      return highPriorityIcon;
    case 'medium':
      return mediumPriorityIcon;
    case 'low':
      return lowPriorityIcon;
    default:
      return lowPriorityIcon;
  }
};

const MapComponent = ({ issues }) => {
  return (
    <MapContainer center={position} zoom={13} style={{ height: '100vh', width: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {issues.map((issue) => {
        const summary = issue.summary || issue.issue || issue.description || issue.details || 'No summary available.';
        
        return (
          <Marker 
            key={issue.original_id} 
            position={issue.location}
            icon={getPriorityIcon(issue.priority)}
          >
            <Popup>
              <div style={{fontWeight: 'bold', textTransform: 'uppercase'}}>{issue.priority || 'N/A'} Priority</div>
              {summary}
            </Popup>
          </Marker>
        );
      })}
    </MapContainer>
  );
};

export default MapComponent;