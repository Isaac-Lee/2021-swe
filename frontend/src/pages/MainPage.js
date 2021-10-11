import React from "react";
import Header from "../components/Header";

const MainPage = () => {
  return (
    <div
      style={{
        backgroundColor: "#f5f6f7",
        width: "100vw",
        minHeight: "88vh",
        marginTop: "80px",
        zIndex: "0",
      }}
    >
      <div className="nav">
        <Header />
      </div>
    </div>
  );
};

export default MainPage;
