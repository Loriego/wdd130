import React from "react";
import "./Portfolio.css";

function Portfolio() {
  return (
    <section id="portfolio" className="portfolio">
      <h2>My Projects</h2>
      <div className="projects">
        <div className="project-card">
          <h3>Multi-Logistics Website</h3>
          <p>
            A responsive logistics company website built with React and Vite,
            featuring contact forms and service pages.
          </p>
          <a href="https://multi-logisticsghana.com" target="_blank" rel="noreferrer">
            View Project
          </a>
        </div>
        <div className="project-card">
          <h3>Meal Price Calculator</h3>
          <p>
            A Python project for BYU Pathway course that calculates meal prices
            with tax and tip. (Hosted on GitHub).
          </p>
          <a href="https://loriego.github.io/meal-price-calculator/" target="_blank" rel="noreferrer">
            View Project
          </a>
        </div>
        <div className="project-card">
          <h3>Portfolio Website</h3>
          <p>
            My personal portfolio showcasing my web and software development
            skills, built with React & Vite.
          </p>
          <a href="https://loriego.github.io/loriego-portfolio/" target="_blank" rel="noreferrer">
            View Project
          </a>
        </div>
      </div>
    </section>
  );
}

export default Portfolio;
