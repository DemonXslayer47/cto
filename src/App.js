// App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import AuthPage from './components/AuthPage';
import CTOData from './components/CTOData';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<AuthPage />} />
          <Route path="/CTOData" element={<CTOData />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
