// Inside TrackAndUpdateComponent.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import API_URL from './constants';
import './TrackAndUpdateComponent.css';

function TrackAndUpdateComponent() {
  const [data, setData] = useState([]);
  const [filterField, setFilterField] = useState('');
  const [filterValue, setFilterValue] = useState('');

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.post(`${API_URL}/track`, {
        [filterField]: filterValue,
      });

      setData(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleFilterFieldChange = (e) => {
    setFilterField(e.target.value);
  };

  const handleFilterValueChange = (e) => {
    setFilterValue(e.target.value);
  };

  const handleFilterSubmit = () => {
    fetchData();
  };

  const handleUpdate = () => {
    // Add logic to handle the update (send data to the backend)
    console.log('Updating data:', data);
  };

  return (
    <div className="track-container">
      <div className="filter-form">
        <h2>Filter Data</h2>
        <div>
          <label htmlFor="filterFieldInput">Filter Field:</label>
          <input
            type="text"
            id="filterFieldInput"
            value={filterField}
            onChange={handleFilterFieldChange}
          />
        </div>
        <div>
          <label htmlFor="filterValueInput">Filter Value:</label>
          <input
            type="text"
            id="filterValueInput"
            value={filterValue}
            onChange={handleFilterValueChange}
          />
        </div>
        <button onClick={handleFilterSubmit}>Submit</button>
      </div>

        <div className="filtered-data">
            <h2>Filtered Data:</h2>
            <table>
                <thead>
                    <tr>
                        <th>Field</th>
                        <th>Value</th>
                    </tr>
                </thead>
                <tbody>
                    {Object.entries(data).map(([key, value]) => (
                        <tr key={key}>
                            <td><strong>{key}</strong></td>
                            <td>{value}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            <button onClick={handleUpdate}>Update</button>
        </div>

    </div>
  );
}

export default TrackAndUpdateComponent;
