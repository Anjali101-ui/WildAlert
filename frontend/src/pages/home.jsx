import React from 'react';
import { useNavigate } from 'react-router-dom';
import animalsImage from '../assets/assets/animals.jpg';
import facebook from '../assets/assets/fb.jpeg';
import insta from '../assets/assets/insta.jpeg';
import twitter from '../assets/assets/twitter.jpeg';

const HomePage = () => {
  const navigate = useNavigate();

  const handleLoginClick = () => {
    navigate('/login');
  };

  const handleProfileClick = () => {
    // Directly go to tracking for demo
    navigate('/tracking');
  };

  return (
    <div className="font-outfit min-h-screen flex flex-col bg-black text-white overflow-x-hidden w-[100vw]">

      {/* Header */}
      <header className="bg-black justify-between items-center fixed top-0 left-0 z-30 w-[100vw]">
        <div className="px-12 py-6 flex justify-between items-center">
          <div className="text-4xl font-extrabold text-white">
            Wild<span className="text-red-500">Alert</span>
          </div>

          <nav className="flex space-x-8">
            <a href="#" className="text-gray-300 hover:text-red-500 text-lg">Home</a>
            <a href="#about" className="text-gray-300 hover:text-red-500 text-lg">About</a>
            <a href="#contact" className="text-gray-300 hover:text-red-500 text-lg">Contact</a>
            <button
              onClick={handleProfileClick}
              className="text-gray-300 hover:text-red-500 text-lg"
            >
              Profile
            </button>
          </nav>
        </div>
      </header>

      {/* Main */}
      <main className="w-[100vw] m-0 p-0">

        {/* Hero Section */}
        <section
          className="py-32 bg-cover bg-center relative w-[100vw]"
          style={{ backgroundImage: `url(${animalsImage})` }}
        >
          <div className="absolute inset-0 bg-black opacity-50"></div>

          <div className="max-w-7xl mx-auto text-center relative z-10 px-8">
            <h1 className="text-5xl font-extrabold mb-6 text-white">
              Real-Time Wild Animal Detection & Alerts
            </h1>

            <p className="mb-8 text-gray-200 text-lg max-w-2xl mx-auto">
              Stay safe with instant notifications when wild animals are detected near your area.
            </p>

            <div className="flex gap-6 justify-center">
              <button
                className="text-white bg-red-500 px-8 py-3 rounded-full font-semibold hover:bg-red-400 text-lg"
                onClick={handleLoginClick}
              >
                Get Started
              </button>

              <button
                className="text-white border border-white px-8 py-3 rounded-full font-semibold hover:border-red-500 hover:text-red-500 text-lg"
                onClick={handleLoginClick}
              >
                Log In
              </button>
            </div>
          </div>
        </section>

        {/* About */}
        <section id="about" className="py-24 bg-gray-900 text-white w-screen">
          <div className="max-w-5xl mx-auto px-8 text-center">
            <h2 className="text-6xl font-bold mb-6">About WildAlert</h2>
            <p className="text-xl leading-relaxed">
              WildAlert monitors CCTV feeds and detects wildlife in real-time.
              AI analysis helps assess risk levels and notify communities instantly.
            </p>
          </div>
        </section>

        {/* Testimonials */}
        <section id="contact" className="py-24 bg-black w-screen">
          <div className="max-w-7xl mx-auto px-8">
            <div className="text-center mb-12">
              <h2 className="text-5xl font-bold text-white">What Our Users Say</h2>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-3 gap-12">
              <div className="bg-gray-900 text-white rounded-lg p-8 shadow-lg">
                <p className="italic mb-4 text-lg">
                  "WildAlert saved us from a bear sighting near our home!"
                </p>
                <p className="font-bold text-lg">- John</p>
              </div>

              <div className="bg-red-500 text-white rounded-lg p-8 shadow-lg">
                <p className="italic mb-4 text-lg">
                  "As a ranger, this helps keep visitors safe."
                </p>
                <p className="font-bold text-lg">- Emily</p>
              </div>

              <div className="bg-gray-900 text-white rounded-lg p-8 shadow-lg">
                <p className="italic mb-4 text-lg">
                  "I feel safer knowing I’ll get instant alerts."
                </p>
                <p className="font-bold text-lg">- Priya</p>
              </div>
            </div>
          </div>
        </section>

      </main>

      {/* Footer */}
      <footer className="bg-gray-900 text-gray-300 py-16 w-screen">
        <div className="max-w-7xl mx-auto px-8 flex justify-between items-center">
          <div>
            <h6 className="font-bold text-white text-xl mb-4">
              Wild<span className="text-red-500">Alert</span>
            </h6>
            <div className="flex space-x-4">
              <img src={facebook} alt="Facebook" className="w-8 h-8" />
              <img src={twitter} alt="Twitter" className="w-8 h-8" />
              <img src={insta} alt="Instagram" className="w-8 h-8" />
            </div>
          </div>

          <div className="text-lg text-gray-400">
            © 2026 WildAlert. All rights reserved.
          </div>
        </div>
      </footer>

    </div>
  );
};

export default HomePage;
