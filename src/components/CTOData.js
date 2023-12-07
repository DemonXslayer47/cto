// CTOData.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import API_URL from './constants';

const CTOData = () => {
  const [ctoData, setCTOData] = useState([]);
  const [editedData, setEditedData] = useState({});

useEffect(() => {
  // Fetch all CTO data from the backend when the component mounts
  axios.post(`${API_URL}/cto-data`)  // No specific parameters in the request
    .then(response => {
      // Check if the response.data is an array
      if (response.data && Array.isArray(response.data)) {
        setCTOData(response.data);
      } else {
        console.error('Invalid data structure in API response:', response.data);
      }
    })
    .catch(error => console.error('Error fetching CTO data', error));
}, []);

  

  const handleEdit = (field, value, index) => {
    // Update the editedData state when a field is edited
    setEditedData({
      ...editedData,
      [index]: {
        ...editedData[index],
        [field]: value,
      },
    });
  };

  const handleSave = () => {
    // Send the edited data to the backend to update the database
    axios.post(`${API_URL}/update`, { /* Add any required parameters */ })
      .then(response => {
        console.log('Update successful:', response.data);
        // Optionally, update the local state or show a success message
      })
      .catch(error => console.error('Error updating data', error));
  };

  return (
    <div>
      <h2>CTO Data</h2>
      <table>
        <thead>
          <tr>
            <th>Orig. Submit Date</th>
            <th>IRB Submit Date</th>
            <th>Pause Date</th>
            <th>Restart Date</th>
            <th>Est. Start Date</th>
            <th>eRS/WD</th>
            <th>IRB</th>
            <th>PI</th>
            <th>SC</th>
            <th>Dept</th>
            <th>Study Feasibility</th>
            <th>Sponsor / Protocol</th>
            <th>ICF</th>
            <th>IDE IND</th>
            <th>CTA</th>
            <th>SSM Fac</th>
            <th>SSM Pharm</th>
            <th>SSM RBR Approval</th>
            <th>CTO CA</th>
            <th>CTO Budget</th>
            <th>CTO IRB Check List</th>
            <th>CTO CTMS</th>
            <th>CTO/EPIC</th>
            <th>CTO WD Grant</th>
            <th>IRB Approval</th>
            <th>Status</th>
            <th>Type</th>
            <th>FY</th>
            <th>FQ</th>
            <th>CTO DO</th>
            <th>IRB DO</th>
            <th>Goal</th>
            <th>Rate</th>
            <th>Complete Date</th>
            <th>Project CTO TA</th>
            <th>Project IRB TA</th>
            <th>Which IRB</th>
            <th>Protocol Version & Date</th>
            <th>CTO Notes</th>
            <th>CTPI Notes</th>
            <th>CA Develop Start Date</th>
            <th>CA SSM Appr. / Final Date</th>
            <th>CA Dev / Final TA</th>
            <th>CA Submit / Start Dev TA</th>
            <th>CA Submit / Final TA</th>
            <th>Budget Neg Start Date</th>
            <th>Budget Final Date</th>
            <th>Budget Neg / Final TA</th>
            <th>Budget Submit / Final TA</th>
            <th>CTA Final Date</th>
            <th>CTA Submit / Final TA</th>
            <th>CTA FE Date</th>
            <th>CTA Final / FE TA</th>
            <th>Local IRB Review Complete</th>
            <th>CTO Checklist Rec'd</th>
            <th>IRB Ancillary Reviews Rec'd</th>
            <th>IRB Comments Sent</th>
            <th>IRB SAF Signed</th>
            <th>Final IRB Approval Date</th>
            <th>Local IRB Review Complete TA</th>
            <th>CTO Checklist Rec'd TA</th>
            <th>IRB Ancillary Reviews Rec'd TA</th>
            <th>IRB Comment Sent TA</th>
            <th>SIRB Approval TA</th>
          </tr>
        </thead>
        <tbody>
          {ctoData.map((row, index) => (
            <tr key={index}>
              <td>{row['Orig. Submit Date']}</td>
              <td>{row['IRB Submit Date']}</td>
              <td>{row['Pause Date']}</td>
              <td>{row['Restart Date']}</td>
              <td>{row['Est. Start Date']}</td>
              <td>{row['eRS/WD']}</td>
              <td>{row['IRB']}</td>
              <td>{row['PI']}</td>
              <td>{row['SC']}</td>
              <td>{row['Dept']}</td>
              <td>{row['Study Feasibility']}</td>
              <td>{row['Sponsor / Protocol']}</td>
              <td>{row['ICF']}</td>
              <td>{row['IDE IND']}</td>
              <td>{row['CTA']}</td>
              <td>{row['SSM Fac']}</td>
              <td>{row['SSM Pharm']}</td>
              <td>{row['SSM RBR Approval']}</td>
              <td>{row['CTO CA']}</td>
              <td>{row['CTO Budget']}</td>
              <td>{row['CTO IRB Check List']}</td>
              <td>{row['CTO CTMS']}</td>
              <td>{row['CTO/EPIC']}</td>
              <td>{row['CTO WD Grant']}</td>
              <td>{row['IRB Approval']}</td>
              <td>{row['Status']}</td>
              <td>{row['Type']}</td>
              <td>{row['FY']}</td>
              <td>{row['FQ']}</td>
              <td>{row['CTO DO']}</td>
              <td>{row['IRB DO']}</td>
              <td>{row['Goal']}</td>
              <td>{row['Rate']}</td>
              <td>{row['Complete Date']}</td>
              <td>{row['Project CTO TA']}</td>
              <td>{row['Project IRB TA']}</td>
              <td>{row['Which IRB']}</td>
              <td>{row['Protocol Version & Date']}</td>
              <td>{row['CTO Notes']}</td>
              <td>{row['CTPI Notes']}</td>
              <td>{row['CA Develop Start Date']}</td>
              <td>{row['CA SSM Appr. / Final Date']}</td>
              <td>{row['CA Dev / Final TA']}</td>
              <td>{row['CA Submit / Start Dev TA']}</td>
              <td>{row['CA Submit / Final TA']}</td>
              <td>{row['Budget Neg Start Date']}</td>
              <td>{row['Budget Final Date']}</td>
              <td>{row['Budget Neg / Final TA']}</td>
              <td>{row['Budget Submit / Final TA']}</td>
              <td>{row['CTA Final Date']}</td>
              <td>{row['CTA Submit / Final TA']}</td>
              <td>{row['CTA FE Date']}</td>
              <td>{row['CTA Final / FE TA']}</td>
              <td>{row['Local IRB Review Complete']}</td>
              <td>{row['CTO Checklist Recd']}</td>
              <td>{row['IRB Ancillary Reviews Recd']}</td>
              <td>{row['IRB Comments Sent']}</td>
              <td>{row['IRB SAF Signed']}</td>
              <td>{row['Final IRB Approval Date']}</td>
              <td>{row['Local IRB Review Complete TA']}</td>
              <td>{row['CTO Checklist Recd TA']}</td>
              <td>{row['IRB Ancillary Reviews Recd TA']}</td>
              <td>{row['IRB Comment Sent TA']}</td>
              <td>{row['SIRB Approval TA']}</td>
              {Object.keys(row).map((field) => (
                <td key={field}>
                   {editedData[index] && editedData[index][field] !== undefined ? (
                    <input
                    type="text"
                    value={editedData[index]?.[field] !== null ? editedData[index]?.[field] : ''}
                    onChange={(e) => handleEdit(field, e.target.value, index)}
                    />
                   ) : (
                    row[field]
                   )}
                </td>
                ))}
            </tr>
          ))}
        </tbody>
      </table>
      <button onClick={handleSave}>Save Changes</button>
    </div>
  );
};

export default CTOData;
