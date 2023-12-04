import React, { useState } from 'react';
import axios from 'axios';
import API_URL from './constants';

function PIIRBForm() {
  const [piValue, setPIValue] = useState('');
  const [irbValue, setIRBValue] = useState(0); 
  const [formValues, setFormValues] = useState({});

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
        <h2>Form Values:</h2>
        <pre>{JSON.stringify(formValues, null, 2)}</pre>
      </div>
    </div>
  );
}

export default PIIRBForm;
