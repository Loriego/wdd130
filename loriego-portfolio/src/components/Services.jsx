import React from "react";
import "./Services.css";

function Services() {
  return (
    <section id="services" className="services">
      <h2>My Services</h2>
      <div className="service-cards">
        <div className="card">
          <h3>Web Development</h3>
          <p>
            I build responsive and modern websites using React, Vite, and
            Tailwind CSS to deliver fast, user-friendly experiences.
          </p>
        </div>
        <div className="card">
          <h3>Mobile Apps</h3>
          <p>
            I create Android applications with Java and React Native, giving
            businesses tools to reach users on the go.
          </p>
        </div>
        <div className="card">
          <h3>Software Solutions</h3>
          <p>
            I develop tailored software systems that solve real-world problems
            for individuals and companies.
          </p>
        </div>
      </div>
    </section>
  );
}

export default Services;
