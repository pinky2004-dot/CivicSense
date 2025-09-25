// /frontend/src/App.jsx
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MapComponent from './MapComponent';
import './App.css'; // We'll create this file next for styling

function App() {
  const [issues, setIssues] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchIssues = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:8000/api/issues');
        setIssues(response.data);
        setError(null); // Clear any previous errors
      } catch (err) {
        console.error("Error fetching data from backend:", err);
        setError("Could not connect to the CivicSense AI backend. Is it running?");
      }
    };

    fetchIssues(); // Fetch immediately on load
    const intervalId = setInterval(fetchIssues, 15000); // Then poll every 15 seconds

    return () => clearInterval(intervalId); // Cleanup on component unmount
  }, []);

  return (
    <div className="App">
      <div className="header">
        <h1>CivicSense AI - Live Dashboard</h1>
        <p>Real-time Civic Issue Monitoring for Celina, TX</p>
      </div>
      {error && <div className="error-banner">{error}</div>}
      <MapComponent issues={issues} />
    </div>
  );
}

export default App;