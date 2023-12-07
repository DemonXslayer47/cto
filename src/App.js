// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AuthPage from './components/AuthPage';
import UpdateTrackPage from './components/UpdateTrackPage';
import TrackAndUpdateComponent from './components/TrackAndUpdateComponent';  // Import the new component
import CTOData from './components/CTOData';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/update-track" element={<UpdateTrackPage />} />
          <Route path="/track" element={<TrackAndUpdateComponent />} />  {/* Add the new route */}
          <Route path="/" element={<AuthPage />} />
          <Route path="/CTOData" element={<CTOData />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
