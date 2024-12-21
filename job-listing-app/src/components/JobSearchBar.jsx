import React, { useState } from "react";

const JobSearchBar = ({ onSearch }) => {
  const [searchTerm, setSearchTerm] = useState("");

  const handleInputChange = (e) => {
    setSearchTerm(e.target.value);
    onSearch(e.target.value);
  };

  return (
    <div className="bg-white p-4 shadow rounded-lg flex items-center space-x-4 mb-6">
      <input
        type="text"
        value={searchTerm}
        onChange={handleInputChange}
        placeholder="Search by job title"
        className="flex-1 px-4 py-2 border rounded-lg"
      />
      <button
        className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600"
        onClick={() => onSearch(searchTerm)}
      >
        Search
      </button>
    </div>
  );
};

export default JobSearchBar;

  