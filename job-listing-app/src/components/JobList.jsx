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

  const getModifiedDate = (postedDate, modifiedDate) => {
    if (modifiedDate) return modifiedDate;
  
    const posted = new Date(postedDate);
    const now = new Date();
    const fallbackModified = new Date(posted.getTime() + 24 * 60 * 60 * 1000);
    const finalModified = fallbackModified > now ? now : fallbackModified;
  
    return finalModified.toISOString().split("T")[0];
  };
  
  return (
    <div className="job-list container mx-auto p-6">
      {filteredJobs.length > 0 ? (
        filteredJobs.map((job) => (
          <div
            key={job.id}
            className="job-card bg-white p-6 border rounded-xl shadow-md mb-6 transition duration-300 ease-in-out hover:shadow-lg hover:border-blue-500"
          >
            <h2 className="text-2xl font-semibold text-blue-700 mb-2">
              {job.title}
            </h2>
            <p className="text-gray-500 text-sm mb-4">{job.company_name}</p>

            <div className="grid grid-cols-2 gap-4 text-gray-600 text-sm">
              <div className="flex items-center">
                <i className="fas fa-briefcase text-blue-500 mr-2"></i>
                <span>{job.employment_type}</span>
              </div>
              <div className="flex items-center">
                <i className="fas fa-map-marker-alt text-red-500 mr-2"></i>
                <span>
                  {job.location} ({job.location_type})
                </span>
              </div>
              <div className="flex items-center">
                <i className="fas fa-dollar-sign text-green-500 mr-2"></i>
                <span>{job.salary || "Not specified"}</span>
              </div>
              <div className="flex items-center">
                <i className="fas fa-calendar-alt text-yellow-500 mr-2"></i>
                <span>{job.posted_date}</span>
              </div>
              <div className="flex items-center">
                <i className="fas fa-clock text-purple-500 mr-2"></i>
                <span>{getModifiedDate(job.posted_date, job.modified_date)}</span>
              </div>
            </div>

            <button
              onClick={() => toggleJobDetails(job.id)}
              className="mt-4 px-4 py-2 bg-gradient-to-r from-blue-500 to-indigo-500 text-white rounded-lg hover:from-blue-600 hover:to-indigo-600 transition focus:outline-none focus:ring focus:ring-indigo-300"
            >
              {expandedJobId === job.id ? "Hide Details" : "View Details"}
            </button>

            {expandedJobId === job.id && (
              <div className="mt-4 bg-gray-100 p-4 rounded-lg">
                <div className="my-4">
                  <strong className="block text-blue-800">Skills:</strong>
                  <p className="text-gray-700">{job.skills}</p>
                </div>
                <div className="my-4">
                  <strong className="block text-blue-800">Job Description:</strong>
                  <p className="text-gray-800 leading-relaxed">
                    {job.job_description}
                  </p>
                </div>
              </div>
            )}
          </div>
        ))
      ) : (
        <p className="text-center text-gray-500 text-lg">No jobs found...</p>
      )}
    </div>
  );
};

export default JobList;
