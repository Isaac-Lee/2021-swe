import React, { useState } from "react";
import { useHistory } from "react-router";
import Header from "../components/Header";
import DatePicker from "react-datepicker";
import "./MainPage.css";
import "react-datepicker/dist/react-datepicker.css";
import { ko } from "date-fns/esm/locale";

const MainPage = () => {
  const history = useHistory();
  const [searchInfo, setSearchInfo] = useState({
    keyword: "전층 오존",
    shooting_period: new Date(),
    shooting_time_start: "",
    shooting_time_end: "",
    title: "",
    font: "",
    latitude_font: "",
    longitude_font: "",
  });

  const keywordList = ["대기보정", "에어로졸 광학 두께", "엽록소농도"];
  const fontWeightList = ["20px", "15px", "10px"];
  const timeList = [
    "00:00",
    "01:00",
    "02:00",
    "03:00",
    "04:00",
    "05:00",
    "06:00",
    "07:00",
    "08:00",
    "09:00",
    "10:00",
    "11:00",
    "12:00",
    "13:00",
    "14:00",
    "15:00",
    "16:00",
    "17:00",
    "18:00",
    "19:00",
    "20:00",
    "21:00",
    "22:00",
    "23:00",
    "24:00",
  ];
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
        <div className="first-line">
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
        </div>
        <div className="second-line">
          <div className="shooting_period">
            <p>촬영 날짜</p>
            <DatePicker
              locale={ko}
              dateFormat="yyyy/MM/dd"
              selected={searchInfo.shooting_period}
              onChange={(date) =>
                setSearchInfo({ ...searchInfo, shooting_period: date })
              }
            ></DatePicker>
          </div>
          <div className="shooting_time">
            <p>촬영 시간</p>
            <select
              name="shooting_time_start"
              onChange={onInputChange}
              value={searchInfo.shooting_time_start}
            >
              {timeList.map((item) => (
                <option value={item} key={item}>
                  {item}
                </option>
              ))}
            </select>
            <span>~</span>
            <select
              name="shooting_time_end"
              onChange={onInputChange}
              value={searchInfo.shooting_time_end}
            >
              {timeList.map((item) => (
                <option value={item} key={item}>
                  {item}
                </option>
              ))}
            </select>
          </div>
        </div>
        <div className="third-line">
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
        <div className="search_btn">
          <button>검색</button>
        </div>
      </div>
      <div className="result_image"></div>
      <div className="save_btn">
        <button>저장</button>
      </div>
    </div>
  );
};

export default MainPage;
