const JobCard = ({ job }) => {
    return (
      <div className="bg-white p-4 shadow rounded-lg flex justify-between items-center">
        <div>
          <p className="text-sm text-gray-500">{job.time}</p>
          <h3 className="text-lg font-bold">{job.title}</h3>
          <p className="text-sm text-gray-700">{job.company}</p>
          <p className="text-sm text-green-600">{job.type}</p>
        </div>
        <div className="text-right">
          <p className="text-sm text-gray-700">{job.salary}</p>
        </div>
      </div>
    );
  };
  
  export default JobCard;
  