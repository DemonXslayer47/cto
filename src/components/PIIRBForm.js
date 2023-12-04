import React, { useState, useEffect } from 'react';
import axios from 'axios';
import API_URL from './constants';

function PIIRBForm() {
  const [piValue, setPIValue] = useState('');
  const [irbValue, setIRBValue] = useState(0);
  const [formValues, setFormValues] = useState([]);
  const [searchKey, setSearchKey] = useState('');
  const [selectedField, setSelectedField] = useState('PI'); // Default field for searching

  useEffect(() => {
    // Fetch data from the backend when the component mounts
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      const response = await axios.get(`${API_URL}/data`);
      setFormValues(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleSubmit = async () => {
    try {
      const response = await axios.post(`${API_URL}/data`, {
        PI: piValue,
        IRB: irbValue,
      });

      setFormValues(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleSearch = async () => {
    try {
      const response = await axios.get(`${API_URL}/data`, {
        params: {
          key: selectedField,
          value: searchKey,
        },
      });
      setFormValues(response.data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div>
      <div>
        <label htmlFor="piInput">PI:</label>
        <input
          type="text"
          id="piInput"
          value={piValue}
          onChange={(e) => setPIValue(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="irbInput">IRB:</label>
        <input
          type="number"
          id="irbInput"
          value={irbValue}
          onChange={(e) => setIRBValue(parseInt(e.target.value, 10))}
        />
      </div>
      <button onClick={handleSubmit}>Submit</button>

      <div>
        <h2>Search and Track:</h2>
        <div>
          <label htmlFor="searchKey">Search Key:</label>
          <select
            id="searchKey"
            value={selectedField}
            onChange={(e) => setSelectedField(e.target.value)}
          >
            <option value="PI">PI</option>
            <option value="IRB">IRB</option>
            {/* Add more options based on your data fields */}
          </select>
          <input
            type="text"
            value={searchKey}
            onChange={(e) => setSearchKey(e.target.value)}
          />
          <button onClick={handleSearch}>Search</button>
        </div>
        <table>
          <thead>
            <tr>
              <th>PI</th>
              <th>IRB</th>
              {/* Add more headers based on your data fields */}
            </tr>
          </thead>
          <tbody>
            {formValues.map((data) => (
              <tr key={data.id}>
                <td>{data.PI}</td>
                <td>{data.IRB}</td>
                {/* Add more cells based on your data fields */}
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default PIIRBForm;
