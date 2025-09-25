import React from 'react';

const InsightsPanel = ({ insights }) => {
  if (!insights || insights.length === 0) {
    return (
      <div className="insights-panel">
        <h3>Analyst Insights</h3>
        <p>No systemic insights generated yet. The Analyst is monitoring...</p>
      </div>
    );
  }

  return (
    <div className="insights-panel">
      <h3>Analyst Insights 🧠</h3>
      <ul>
        {insights.map((insight, index) => (
          <li key={index}>
            <strong>{insight.title}</strong>
            <p>{insight.summary}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default InsightsPanel;