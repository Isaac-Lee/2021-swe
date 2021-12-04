import React from "react";
import Header from "../components/Header";
import { USER_SERVER } from "../config";
import axios from "axios";

const Gallery = () => {
  return (
    <div
      style={{
        backgroundColor: "#FEFEFE",
        width: "100vw",
        minHeight: "88vh",
        marginTop: "80px",
        zIndex: "0",
      }}
      className="window"
    >
      <div className="nav">
        <Header />
      </div>
    </div>
  );
};

export default Gallery;
