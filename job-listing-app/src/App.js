import React, { useState } from "react";
import Header from "./components/Header";
import JobSearchBar from "./components/JobSearchBar";
import JobFilters from "./components/JobFilters";
import JobList from "./components/JobList";
import '@fortawesome/fontawesome-free/css/all.min.css';

const App = () => {
  const [view, setView] = useState("home");
  const [searchTerm, setSearchTerm] = useState(""); 
  const [filters, setFilters] = useState({
    jobType: "Job type",
    workplace: "Workplace",
    country: "Country or timezone",
    seniority: "Seniority",
  }); 

  const handleSearch = (term) => {
    setSearchTerm(term);
  };

  const handleFilterChange = (newFilters) => {
    setFilters(newFilters);
  };

  const renderContent = () => {
    switch (view) {
      case "home":
        return (
          <div className="relative bg-gradient-to-r from-blue-800 via-blue-600 to-blue-400 min-h-screen flex items-center justify-center text-white">
            <div className="absolute inset-0 bg-opacity-50 bg-cover bg-center" style={{ backgroundImage: "url('https://source.unsplash.com/1920x1080/?career,technology')" }}></div>
            <div className="relative z-10 text-center max-w-4xl">
              <h1 className="text-5xl font-extrabold mb-6">
                Welcome to <span className="text-yellow-400">JobPortal</span>
              </h1>
              <p className="text-lg leading-relaxed mb-8">
                Discover thousands of opportunities to find the career of your dreams. 
                JobPortal connects you with the best job offers across the globe.
              </p>
              <button
                onClick={() => setView("jobs")}
                className="px-8 py-4 bg-yellow-400 text-blue-900 font-bold rounded-full hover:bg-yellow-500 transition shadow-lg"
              >
                Explore Jobs
              </button>
            </div>
          </div>
        );
      case "jobs":
        return (
          <div className="container mx-auto px-4 py-6">
            <JobSearchBar onSearch={handleSearch} />
            <JobFilters onFilterChange={handleFilterChange} />
            <JobList searchTerm={searchTerm} filters={filters} />
          </div>
        );
      default:
        return null;
    }
  };

  return (
    <div className="bg-gray-100 min-h-screen">
      <Header />
      {renderContent()}
    </div>
  );
};

export default App;
