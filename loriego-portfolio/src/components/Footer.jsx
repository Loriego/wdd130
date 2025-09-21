import React from "react";
import "./Footer.css";

function Footer() {
  return (
    <footer className="footer">
      <p>© {new Date().getFullYear()} Loriego. All rights reserved.</p>
      <p>
        Built with ❤️ using React & Vite |{" "}
        <a href="mailto:info@multi-logisticsghana.com">info@multi-logisticsghana.com</a>
      </p>
    </footer>
  );
}

export default Footer;
