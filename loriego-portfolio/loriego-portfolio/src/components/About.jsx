import React from "react";
import "./About.css";

function About() {
  return (
    <section className="about" id="about">
      <h2>About Me</h2>
      <div className="about-content">
        <div className="about-text">
          <p>
            Hi 👋, I’m <strong>Stallone Adu Baffour</strong>, also known as{" "}
            <span className="highlight">Loriego</span>. I’m a passionate{" "}
            <strong>Web Developer & Software Engineer</strong> from Ghana,
            currently studying at <strong>Brigham Young University (BYU)</strong>.
          </p>
          <p>
            With experience in building websites, applications, and digital
            solutions, I specialize in creating modern, responsive, and
            user-friendly platforms. My goal is to help businesses and
            individuals grow by bringing their ideas online.
          </p>
          <p>
            💡 Areas I work with: React, JavaScript, HTML, CSS, Node.js,
            WordPress, and more.
          </p>
        </div>

        <div className="skills">
          <h3>My Skills</h3>
          <ul>
            <li>⚡ React & JavaScript</li>
            <li>⚡ HTML5 & CSS3</li>
            <li>⚡ Node.js & Express</li>
            <li>⚡ WordPress Development</li>
            <li>⚡ UI/UX Design</li>
          </ul>
        </div>
      </div>
    </section>
  );
}

export default About;
