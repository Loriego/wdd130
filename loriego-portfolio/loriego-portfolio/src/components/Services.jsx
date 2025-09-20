import React from "react";
import "./Services.css";

function Services() {
  return (
    <section className="services" id="services">
      <h2>My Services</h2>
      <div className="services-container">
        
        <div className="service-card">
          <h3>🌍 Web Development</h3>
          <p>
            Building modern, responsive, and user-friendly websites using
            React, HTML, CSS, and JavaScript.
          </p>
        </div>

        <div className="service-card">
          <h3>⚙️ Software Solutions</h3>
          <p>
            Developing custom software applications tailored to client needs,
            from simple tools to complex systems.
          </p>
        </div>

        <div className="service-card">
          <h3>🎨 Branding & Business Websites</h3>
          <p>
            Helping businesses establish their online presence with clean,
            professional websites and brand-focused designs.
          </p>
        </div>

      </div>
    </section>
  );
}

export default Services;
