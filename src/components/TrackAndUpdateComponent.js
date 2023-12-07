import React, { useState, useEffect, useCallback } from 'react';
import axios from 'axios';
import API_URL from './constants';
import './TrackAndUpdateComponent.css';

function TrackAndUpdateComponent() {
  const [data, setData] = useState([]);
  const [filterField, setFilterField] = useState('');
  const [filterValue, setFilterValue] = useState('');

  const fetchData = useCallback(async () => {
    try {
      const response = await axios.post(`${API_URL}/track`, {
        [filterField]: filterValue,
      });

      // Convert object to an array of key-value pairs
      const dataArray = Object.entries(response.data).map(([key, value]) => ({ key, value }));

      setData(dataArray || []);
    } catch (error) {
      console.error('Error fetching data:', error);
      // You might want to set an error state or display a message to the user
    }
  }, [filterField, filterValue]);

  useEffect(() => {
    fetchData();
  }, [fetchData]); // Add fetchData to the dependency array

  const handleFilterFieldChange = (e) => {
    setFilterField(e.target.value);
  };

  const handleFilterValueChange = (e) => {
    setFilterValue(e.target.value);
  };

  const handleFilterSubmit = () => {
    fetchData();
  };

  const handleUpdate = async () => {
    try {
      // Add logic to handle the update (send data to the backend)
      const response = await axios.post(`${API_URL}/update`, { updatedData: data });
      console.log('Update response:', response.data);
    } catch (error) {
      console.error('Error updating data:', error);
    }
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
              {Object.keys(data[0] || {}).map((key) => (
                <th key={key}>{key}</th>
              ))}
            </tr>
          </thead>
          <tbody>
            {data.map((row, index) => (
              <tr key={index}>
                {Object.values(row).map((value, index) => (
                  <td key={index}>{value}</td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>
        <button onClick={handleUpdate} disabled={!data.length}>
          Update
        </button>
      </div>
    </div>
  );
}

export default TrackAndUpdateComponent;
