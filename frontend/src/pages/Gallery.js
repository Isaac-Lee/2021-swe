import React, { useEffect, useState } from "react";
import Header from "../components/Header";
import { USER_SERVER } from "../config";
import axios from "axios";
import { useHistory } from "react-router";

const Gallery = () => {
  const [imgList, setImgList] = useState([]);

  useEffect(() => {
    if (window.localStorage.getItem("isAuth") === "true") {
      getImages();
    }
  }, []);

  const getImages = async () => {
    console.log("하이");
    try {
      const response = axios.get(`${USER_SERVER}/satellite/api/showGallery`);
      console.log(response);
      // if (response.data.success) {
      //   //history.push(`/`);
      //   const realData = response.data.images;
      //   setImgList(realData);
      //   console.log(realData[0]);
      // }
    } catch (error) {
      alert(error);
    }
  };

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
