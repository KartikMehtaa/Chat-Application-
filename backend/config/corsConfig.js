// corsConfig.js
const allowedOrigins = [
    "http://localhost:8081", 
    "https://chat-application-30lh.onrender.com"
  ];
  
  const corsOptions = {
    origin: function (origin, callback) {
      if (!origin || allowedOrigins.includes(origin)) {
        callback(null, true);
      } else {
        callback(new Error("Not allowed by CORS"));
      }
    },
    credentials: true
  };
  
  module.exports = corsOptions;
  