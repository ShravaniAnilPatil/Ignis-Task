import axios from "axios";

const API_URL = "http://127.0.0.1:8000/api/jobs/";

export const fetchJobs = async () => {
  try {
    const response = await axios.get(API_URL);
    return response.data;
  } catch (error) {
    if (error.code === "ERR_NETWORK") {
      console.error("Backend server is not reachable. Please check the server.");
    } else {
      console.error("Error fetching jobs:", error);
    }
    return [];
  }
};
