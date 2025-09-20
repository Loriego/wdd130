import React from "react";
import Navbar from "./components/Navbar";
import Footer from "./components/Footer";
import About from "./components/About";
import Services from "./components/Services";
import "./App.css";
import heroImage from "./assets/loriego.jpg";

function App() {
  return (
    <div className="App">
      <Navbar />

      {/* Hero Section */}
      <section className="hero" id="home">
        <div className="hero-content">
          <h1>
            Hi, I’m <span>Loriego</span>
          </h1>
          <h2>Web Developer & Software Engineer</h2>
          <p>
            I help businesses and individuals build modern, responsive websites
            and software solutions.
          </p>
          <div className="hero-buttons">
            <a href="#portfolio" className="btn">
              View My Work
            </a>
            <a href="#contact" className="btn-outline">
              Hire Me
            </a>
          </div>
        </div>
        <div className="hero-image">
          <img src={heroImage} alt="Stallone Adu Baffour - Loriego" />
        </div>
      </section>

      {/* About Section */}
      <About />

      {/* Services Section */}
      <Services />

      <Footer />
    </div>
  );
}

export default App;
