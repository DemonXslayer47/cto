import React, { useState } from 'react';
import API_URL from './constants';
import './UpdateTrackPage.css';
import { useNavigate } from 'react-router-dom';

const UpdateTrackPage = () => {
  const [updateData, setUpdateData] = useState({
    // Define fields for update
  });

  const [trackData, setTrackData] = useState({
    // Define fields for track
  });

  const handleUpdate = async () => {
    try {
      const response = await fetch(`${API_URL}/update`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updateData),
      });
      const result = await response.json();
      console.log(result); // Handle the response as needed
    } catch (error) {
      console.error('Error during update:', error);
    }
  };

  const handleTrack = async () => {
    try {
      const response = await fetch(`${API_URL}/track`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(trackData),
      });
      const result = await response.json();
      console.log(result); // Handle the response as needed
    } catch (error) {
      console.error('Error during track:', error);
    }
  };

  return (
    <div className="update-track-container">
      <div className="update-track-form">
        <h2>Update</h2>
        {/* Form fields for update go here */}
        <button onClick={handleUpdate}>Update</button>
      </div>
      <div className="update-track-form">
        <h2>Track</h2>
        {/* Form fields for track go here */}
        <button onClick={handleTrack}>Track</button>
      </div>
    </div>
  );
};

export default UpdateTrackPage;
