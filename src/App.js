import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AuthPage from './components/AuthPage';
import UpdateTrackPage from './components/UpdateTrackPage';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/update-track" element={<UpdateTrackPage />} />
          <Route path="/" element={<AuthPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
