import React, { useState, useEffect } from 'react';
import axios from 'axios';
import MapComponent from './MapComponent';
import InsightsPanel from './InsightsPanel'; // Import our new component
import './App.css';

function App() {
  // I now need to manage two pieces of state
  const [issues, setIssues] = useState([]);
  const [insights, setInsights] = useState([]);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchState = async () => {
      try {
        // API endpoint /api/state
        const response = await axios.get('http://127.0.0.1:8000/api/state');

        console.log("API Response Data:", response.data);
        
        // Set both issues and insights from the response object
        setIssues(response.data.active_issues || []);
        setInsights(response.data.generated_insights || []);
        
        setError(null);
      } catch (err) {
        console.error("Error fetching data from backend:", err);
        setError("Could not connect to the CivicSense AI backend. Is it running?");
      }
    };

    fetchState(); // Fetch immediately on load
    const intervalId = setInterval(fetchState, 15000); // Poll every 15 seconds

    return () => clearInterval(intervalId);
  }, []);

  console.log("Current Component State:", { issues, insights });

  return (
    <div className="App">
      <div className="header">
        <h1>CivicSense - Live Dashboard</h1>
        <p>Real-time Civic Issue Monitoring</p>
      </div>
      
      {/* Add the new InsightsPanel to UI */}
      <InsightsPanel insights={insights} />
      
      {error && <div className="error-banner">{error}</div>}
      
      {/* The MapComponent now only receives the issues */}
      <MapComponent issues={issues} />
    </div>
  );
}

export default App;