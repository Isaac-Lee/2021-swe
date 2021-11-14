import React, { useState } from "react";
import { useHistory } from "react-router";
import Header from "../components/Header";
import "./MainPage.css";

const MainPage = () => {
  const history = useHistory();
  const [searchInfo, setSearchInfo] = useState({
    keyword: "전층 오존",
    shooting_period: "",
    shooting_time: "",
    title: "",
    font: "",
    latitude_font: "",
    longitude_font: "",
  });

  const keywordList = ["전층 오존", "자외선 지수", "에어로졸"];
  const fontWeightList = ["20px", "15px", "10px"];
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
          <select
            name="keyword"
            onChange={onInputChange}
            value={searchInfo.keyword}
          >
            {keywordList.map((item) => (
              <option value={item} key={item}>
                {item}
              </option>
            ))}
          </select>
        </div>
        <div className="title">
          <p>제목 입력</p>
          <input
            type="text"
            placeholder="  제목"
            name="title"
            value={searchInfo.title}
            onChange={onInputChange}
          ></input>
        </div>
        <p id="font">폰트 크기</p>
        <div className="font">
          <div className="font-title">
            <p>제목</p>
            <select
              name="font"
              onChange={onInputChange}
              value={searchInfo.font}
            >
              {fontWeightList.map((item) => (
                <option value={item} key={item}>
                  {item}
                </option>
              ))}
            </select>
          </div>
          <div className="font-latitude">
            <p>위도</p>
            <select
              name="latitude_font"
              onChange={onInputChange}
              value={searchInfo.latitude_font}
            >
              {fontWeightList.map((item) => (
                <option value={item} key={item}>
                  {item}
                </option>
              ))}
            </select>
          </div>
          <div className="font-longitude">
            <p>경도</p>
            <select
              name="longitude_font"
              onChange={onInputChange}
              value={searchInfo.longitude_font}
            >
              {fontWeightList.map((item) => (
                <option value={item} key={item}>
                  {item}
                </option>
              ))}
            </select>
          </div>
        </div>
      </div>
      <div className="resultImage"></div>
    </div>
  );
};

export default MainPage;
