import express from "express";
import dotenv from "dotenv";
import connectDb from "./config/databaseConnect.js";
import cookieParser from "cookie-parser";
import authRouter from "./routes/authRoutes.js";
import cors from "cors";
const corsOptions = require("./config/corsConfig.js");
import userRouter from "./routes/getCurrentUser.js";
import messageRouter from "./routes/messageRoute.js";
import { app, server } from "./socket.io/socket.io.js";

dotenv.config();
const port = process.env.PORT || 5000;
app.use(cookieParser());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(cors(corsOptions));  // corsConfig.js'den gelen corsOptions'u kullanarak CORS yapılandırması yapıyoruz.
app.use(
  cors({
    origin: "*",   // sab allow
    credentials: true,
  })
);
app.use("/auth", authRouter);
app.use("/user", userRouter);
app.use("/message", messageRouter);

connectDb().then(() => {
  server.listen(port, () => {
    console.log(`Server listening on ${port}`);
  });
});
