import React, { useState } from "react";
import { useHistory } from "react-router";
import Header from "../components/Header";
import "./MainPage.css";

const MainPage = () => {
  const history = useHistory();
  const [searchInfo, setSearchInfo] = useState({
    keyword: "",
    shooting_period: "",
    shooting_time: "",
    title: "",
    font: "",
    latitude_font: "",
    longitude_font: "",
  });

  const onInputChange = async (e) => {
    const { name, value } = e.target;
    setSearchInfo({
      ...searchInfo,
      [name]: value,
    });
  };

  return (
    <div
      style={{
        backgroundColor: "#f5f6f7",
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
      <p id="title">위성영상 전시</p>
      <div className="condition">
        <div className="keyword">
          <p>키워드 검색</p>
          <input
            type="text"
            placeholder="  키워드"
            name="keyword"
            value={searchInfo.keyword}
            onChange={onInputChange}
          ></input>
        </div>
        <div className="shootingPeriod">
          <p>촬영 기간</p>
          <select>
            <option key="banana" value="banana">
              바나나
            </option>
            <option key="apple" value="apple">
              사과
            </option>
            <option key="orange" value="orange">
              오렌지
            </option>
          </select>
        </div>
      </div>
      <div className="resultImage"></div>
    </div>
  );
};

export default MainPage;
