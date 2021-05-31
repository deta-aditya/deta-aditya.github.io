import React from 'react';
import { NavBar } from './components/NavBar'
import { BannerSection } from './components/BannerSection'
import { ExperienceSection } from './components/ExperienceSection'
import './App.css';

function App() {
  return (
    <div className="App">
      <NavBar />
      <main className="main-content">
        <BannerSection />
        <ExperienceSection />
      </main>
    </div>
  );
}

export default App;
