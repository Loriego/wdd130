import { Truck, Package, Phone, Mail, Globe } from "lucide-react";

function App() {
  return (
    <div className="font-sans text-gray-900">
      {/* Navbar */}
      <nav className="flex justify-between items-center px-6 py-4 bg-gradient-to-r from-blue-700 to-blue-500 shadow-lg sticky top-0 z-50">
        <h1 className="text-2xl font-extrabold text-white tracking-wide">
          Multi-Logistics Ghana
        </h1>
        <div className="space-x-6 hidden md:flex">
          <a href="#services" className="text-white hover:text-yellow-300">
            Services
          </a>
          <a href="#about" className="text-white hover:text-yellow-300">
            About
          </a>
          <a href="#contact" className="text-white hover:text-yellow-300">
            Contact
          </a>
        </div>
      </nav>

      {/* Hero Section */}
      <header className="bg-gradient-to-br from-blue-600 via-blue-500 to-blue-400 flex flex-col items-center justify-center text-center h-[80vh] px-4 text-white">
        <h2 className="text-4xl md:text-6xl font-extrabold drop-shadow-lg">
          Reliable Freight, Import & Export Solutions
        </h2>
        <p className="mt-4 text-lg max-w-2xl">
          Moving goods across the globe with speed, safety, and trust.
        </p>
        <a
          href="#contact"
          className="mt-6 px-8 py-3 bg-yellow-400 text-blue-900 font-semibold rounded-full shadow-lg hover:bg-yellow-300 transition"
        >
          Request a Quote
        </a>
      </header>

      {/* Services */}
      <section id="services" className="px-6 py-20 bg-gray-50">
        <h3 className="text-3xl font-bold text-center mb-12 text-blue-700">
          Our Core Services
        </h3>
        <div className="grid md:grid-cols-3 gap-10 max-w-6xl mx-auto">
          <div className="p-8 bg-white rounded-2xl shadow-xl hover:shadow-2xl border-t-4 border-blue-600">
            <Truck className="w-12 h-12 text-blue-600 mb-4" />
            <h4 className="text-xl font-semibold mb-3">Freight Forwarding</h4>
            <p className="text-gray-600">
              Comprehensive freight solutions for import and export by air, sea,
              and land.
            </p>
          </div>
          <div className="p-8 bg-white rounded-2xl shadow-xl hover:shadow-2xl border-t-4 border-yellow-400">
            <Package className="w-12 h-12 text-yellow-500 mb-4" />
            <h4 className="text-xl font-semibold mb-3">Customs Clearance</h4>
            <p className="text-gray-600">
              Fast, efficient customs handling ensuring smooth flow of your
              shipments.
            </p>
          </div>
          <div className="p-8 bg-white rounded-2xl shadow-xl hover:shadow-2xl border-t-4 border-green-500">
            <Globe className="w-12 h-12 text-green-600 mb-4" />
            <h4 className="text-xl font-semibold mb-3">Global Network</h4>
            <p className="text-gray-600">
              International partnerships that guarantee your goods reach any
              destination.
            </p>
          </div>
        </div>
      </section>

      {/* About */}
      <section id="about" className="px-6 py-20 bg-gradient-to-r from-blue-50 to-blue-100">
        <h3 className="text-3xl font-bold text-center mb-10 text-blue-800">
          About Multi-Logistics Ghana
        </h3>
        <p className="max-w-3xl mx-auto text-center text-lg text-gray-700">
          At <span className="font-bold text-blue-700">Multi-Logistics Ghana</span>, 
          we specialize in providing reliable, cost-effective, and transparent logistics solutions. 
          With years of experience in freight forwarding, customs clearance, and supply chain management, 
          we ensure your cargo gets where it needs to be — on time, every time.
        </p>
      </section>

      {/* Contact */}
      <section id="contact" className="px-6 py-20 bg-white">
        <h3 className="text-3xl font-bold text-center mb-12 text-blue-700">
          Get in Touch
        </h3>
        <div className="grid md:grid-cols-2 gap-12 max-w-4xl mx-auto">
          <div className="flex items-start space-x-4 bg-blue-50 p-6 rounded-xl shadow">
            <Phone className="w-7 h-7 text-blue-600" />
            <div>
              <h4 className="font-semibold text-blue-800">Phone</h4>
              <p className="text-gray-700">+233 24 744 0127</p>
            </div>
          </div>
          <div className="flex items-start space-x-4 bg-yellow-50 p-6 rounded-xl shadow">
            <Mail className="w-7 h-7 text-yellow-500" />
            <div>
              <h4 className="font-semibold text-yellow-600">Email</h4>
              <p className="text-gray-700">info@multilogisticsghana.com</p>
            </div>
          </div>
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gradient-to-r from-blue-700 to-blue-900 text-white py-6 text-center">
        © {new Date().getFullYear()} Multi-Logistics Ghana. All rights reserved.
      </footer>
    </div>
  );
}

export default App;