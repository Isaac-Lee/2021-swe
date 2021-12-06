import React, { useState } from "react";
import { useHistory } from "react-router";
import Header from "../components/Header";
import DatePicker from "react-datepicker";
import "./MainPage.css";
import "react-datepicker/dist/react-datepicker.css";
import { ko } from "date-fns/esm/locale";
import { USER_SERVER } from "../config";
import axios from "axios";

const MainPage = () => {
  const history = useHistory();
  const [searchInfo, setSearchInfo] = useState({
    keyword: "대기보정",
    shooting_period: new Date(),
    shooting_time_start: "00:00",
    shooting_time_end: "00:00",
    title: "",
    font: "20px",
    latitude_font: "20px",
    longitude_font: "20px",
  });
  const [images, setImages] = useState([]);
  const [imgSrc, setImgSrc] = useState(null);
  const [clickNum, setClickNum] = useState(0);

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
    console.log(value);
  };

  const clickSearchBtn = async (e) => {
    if (window.localStorage.getItem("isAuth") === "true") {
      try {
        const response = await axios.post(
          `${USER_SERVER}/satellite/api/createImage`,
          searchInfo
        );
        if (response.data.success) {
          history.push(`/`);
          const realData = response.data.images;
          setImages(realData);

          //setImgSrc(realData[{ clickNum }].url);
          //window.location.replace("/");
        }
      } catch (error) {
        alert(error);
      }
    } else {
      alert("로그인이 필요합니다.");
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
      <p id="title">위성영상 전시</p>
      <div className="condition">
        <div className="search_btn">
          <button onClick={clickSearchBtn}>검색</button>
        </div>
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
        <div className="second-line">
          <div className="font-title">
            <p>제목 폰트 크기</p>
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
            <p>위도 폰트 크기</p>
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
            <p>경도 폰트 크기</p>
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
      <div className="result_image">
        {images.map((img) => (
          <img src={img.url} key={img.url} alt="위성사진" />
        ))}
      </div>
      <div className="table">
        <table>
          <tbody>
            <tr>
              {images.map((img) => (
                <td
                  style={{
                    border: "1px solid black",
                  }}
                  key={img.url}
                ></td>
              ))}
            </tr>
          </tbody>
        </table>
      </div>
      <div className="save_btn">
        <button>저장</button>
      </div>
    </div>
  );
};

export default MainPage;
