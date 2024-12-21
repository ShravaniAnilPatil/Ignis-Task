import React from "react";

const JobFilters = ({ onFilterChange }) => {
  const handleFilterChange = (e) => {
    const { name, value } = e.target;
    onFilterChange((prevFilters) => ({
      ...prevFilters,
      [name]: value,
    }));
  };

  return (
    <div className="flex space-x-4 py-4 mb-6">
      <select
        name="jobType"
        className="px-4 py-2 border rounded-lg"
        onChange={handleFilterChange}
      >
        <option>Job type</option>
        <option>Full-time</option>
        <option>Part-time</option>
      </select>
      <select
        name="workplace"
        className="px-4 py-2 border rounded-lg"
        onChange={handleFilterChange}
      >
        <option>Workplace</option>
        <option>Remote</option>
        <option>On-site</option>
      </select>
      <select
        name="country"
        className="px-4 py-2 border rounded-lg"
        onChange={handleFilterChange}
      >
        <option>Country or timezone</option>
        <option>USA</option>
        <option>Europe</option>
      </select>
      <select
        name="seniority"
        className="px-4 py-2 border rounded-lg"
        onChange={handleFilterChange}
      >
        <option>Seniority</option>
        <option>Junior</option>
        <option>Mid-level</option>
        <option>Senior</option>
      </select>
    </div>
  );
};

export default JobFilters;
