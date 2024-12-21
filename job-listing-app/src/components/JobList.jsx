import React, { useState, useEffect } from "react";
import { fetchJobs } from "../services/api";

const JobList = ({ searchTerm, filters }) => {
  const [jobs, setJobs] = useState([]);
  const [filteredJobs, setFilteredJobs] = useState([]);
  const [expandedJobId, setExpandedJobId] = useState(null);

  useEffect(() => {
    const loadJobs = async () => {
      const jobData = await fetchJobs();
      setJobs(jobData);
    };

    loadJobs();
  }, []);

  useEffect(() => {
    const filterJobs = () => {
      let filtered = [...jobs];

      if (searchTerm) {
        filtered = filtered.filter((job) =>
          job.title.toLowerCase().includes(searchTerm.toLowerCase())
        );
      }
      if (filters.jobType !== "Job type") {
        filtered = filtered.filter((job) => job.employment_type === filters.jobType);
      }
      if (filters.workplace !== "Workplace") {
        filtered = filtered.filter((job) => job.location_type === filters.workplace);
      }
      if (filters.country !== "Country or timezone") {
        filtered = filtered.filter((job) => job.location === filters.country);
      }
      if (filters.seniority !== "Seniority") {
        filtered = filtered.filter((job) => job.seniority === filters.seniority);
      }

      setFilteredJobs(filtered);
    };

    filterJobs();
  }, [searchTerm, filters, jobs]);

  const toggleJobDetails = (jobId) => {
    setExpandedJobId(expandedJobId === jobId ? null : jobId);
  };

  return (
    <div className="job-list container mx-auto p-6">
      {filteredJobs.length > 0 ? (
        filteredJobs.map((job) => (
          <div
            key={job.id}
            className="job-card bg-white p-6 border rounded-lg shadow-lg mb-6"
          >
            <h2 className="text-2xl font-bold text-blue-800 mb-2">{job.title}</h2>
            <p className="text-gray-600 text-sm mb-4">{job.company_name}</p>

            <div className="grid grid-cols-2 gap-4 text-gray-700 text-sm">
              <div className="flex items-center">
                <i className="fas fa-briefcase text-blue-500 mr-2"></i>
                <span>Employment Type: {job.employment_type}</span>
              </div>
              <div className="flex items-center">
                <i className="fas fa-map-marker-alt text-red-500 mr-2"></i>
                <span>
                  Location: {job.location} ({job.location_type})
                </span>
              </div>
              <div className="flex items-center">
                <i className="fas fa-dollar-sign text-green-500 mr-2"></i>
                <span>Salary: {job.salary || "Not specified"}</span>
              </div>
              <div className="flex items-center">
                <i className="fas fa-calendar-alt text-yellow-500 mr-2"></i>
                <span>Posted Date: {job.posted_date}</span>
              </div>
              <div className="flex items-center">
                <i className="fas fa-clock text-purple-500 mr-2"></i>
                <span>Modified: {job.modified_date}</span>
              </div>
            </div>

            <button
              onClick={() => toggleJobDetails(job.id)}
              className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
            >
              {expandedJobId === job.id ? "Hide Details" : "View Details"}
            </button>

            {expandedJobId === job.id && (
              <div className="mt-4">
                <div className="my-4">
                  <strong>Skills:</strong>
                  <p className="text-gray-500">{job.skills}</p>
                </div>
                <div className="my-4">
                  <strong>Job Description:</strong>
                  <p className="text-gray-700 leading-relaxed">{job.job_description}</p>
                </div>
              </div>
            )}
          </div>
        ))
      ) : (
        <p className="text-center text-gray-600 text-lg">No jobs found...</p>
      )}
    </div>
  );
};

export default JobList;
