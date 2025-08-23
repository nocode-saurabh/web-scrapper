const config = {
    // Use environment variables or different URLs for development/production
    API_URL: process.env.NODE_ENV === 'production' 
      ? 'https://your-backend-url.com'  // Replace with your actual backend URL
      : 'http://localhost:4000'
  };
  
  export default config;