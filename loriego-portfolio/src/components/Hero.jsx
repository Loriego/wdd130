import React from "react";
import heroImage from "../assets/loriego.jpg";
import "./Hero.css";

function Hero() {
  return (
    <section id="home" className="hero">
      <div className="hero-content">
        <h1>Hi, I’m <span className="highlight">Loriego</span></h1>
        <h2>Web Developer & Software Engineer</h2>
        <p>
          I build modern, responsive websites and software solutions that help 
          businesses and individuals succeed online.
        </p>
        <div className="hero-buttons">
          <a href="#portfolio" className="btn primary">View My Work</a>
          <a href="#contact" className="btn secondary">Hire Me</a>
        </div>
      </div>
      <div className="hero-image">
        <img src={heroImage} alt="Loriego" />
      </div>
    </section>
  );
}

export default Hero;
