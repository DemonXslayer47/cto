import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import API_URL from './constants'; // Import your API URL file
import './AuthPage.css';

const AuthPage = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    Name: '',
    ContactId: '',
    Email: '',
    Address: '',
    ZipCode: '',
    UserName: '',
    Password: '',
  });

  const handleInputChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSignup = async () => {
    try {
      const response = await fetch(`${API_URL}/register`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });
  
      const data = await response.json();
  
      if (data.issuccess) {
        // Successful signup, navigate to the '/update-track' route
        console.log('Signup successful');
        navigate('/update-track'); // Update the route as needed
      } else {
        console.error('Signup failed:', data.error);
      }
    } catch (error) {
      console.error('Error during signup:', error);
    }
  };
  
  const handleLogin = async () => {
    try {
      const response = await fetch(`${API_URL}/login`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      const data = await response.json();

      if (data.userId) {
        // Successful login, navigate to another page or perform an action
        console.log('Login successful');
        navigate('/update-track'); // Change '/dashboard' to your desired route
      } else {
        console.error('Login failed:', data.error);
      }
    } catch (error) {
      console.error('Error during login:', error);
    }
  };

  return (
    <div className="auth-container">
      <div className="auth-form">
        <h2>Signup</h2>
        <input
          type="text"
          name="Name"
          placeholder="Full Name"
          value={formData.Name}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="ContactId"
          placeholder="Contact ID"
          value={formData.ContactId}
          onChange={handleInputChange}
        />
        <input
          type="email"
          name="Email"
          placeholder="Email"
          value={formData.Email}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="Address"
          placeholder="Address"
          value={formData.Address}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="ZipCode"
          placeholder="Zip Code"
          value={formData.ZipCode}
          onChange={handleInputChange}
        />
        <input
          type="text"
          name="UserName"
          placeholder="UserName"
          value={formData.UserName}
          onChange={handleInputChange}
        />
        <input
          type="password"
          name="Password"
          placeholder="Password"
          value={formData.Password}
          onChange={handleInputChange}
        />
        <button onClick={handleSignup}>Signup</button>
      </div>

      <div className="auth-form">
        <h2>Login</h2>
        <input
          type="text"
          name="UserName"
          placeholder="Username"
          value={formData.UserName}
          onChange={handleInputChange}
        />
        <input
          type="password"
          name="Password"
          placeholder="Password"
          value={formData.Password}
          onChange={handleInputChange}
        />
        <button onClick={handleLogin}>Login</button>
      </div>
    </div>
  );
};

export default AuthPage;
