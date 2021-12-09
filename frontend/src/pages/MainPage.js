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
    keyword: "AC",
    shooting_period: new Date(),
    shooting_time_start: "00:00",
    shooting_time_end: "00:00",
    title: "untitled",
    font: "20",
    latitude_font: "20",
    longitude_font: "20",
  });
  const [images, setImages] = useState([]);
  const [clickNum, setClickNum] = useState(0);
  const [clickedImage, setClickedImage] = useState([]);
  const [isSearch, setIsSearch] = useState(false);

  const keywordValue = ["AC", "AOD", "Chl"];
  const keywordList = ["대기보정", "에어로졸 광학 두께", "엽록소농도"];
  const fontWeightList = ["20", "15", "10"];
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

  // 검색버튼
  const clickSearchBtn = async (e) => {
    if (window.localStorage.getItem("isAuth") === "true") {
      setIsSearch(true);
      try {
        const response = await axios.post(
          `${USER_SERVER}/satellite/api/createImage`,
          searchInfo
        );
        if (response.data.success) {
          history.push(`/`);
          const realData = response.data.images;
          setImages(realData);
          setClickedImage(realData[0]);
          console.log(realData[0]);

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

  // table 버튼 클릭시 이벤트
  const clickTable = (index, e) => {
    //e.target.style.backgroundColor = "grey";
    setClickNum(index);
    setClickedImage(images[index]);
    console.log(images[index]);
    //alert("버튼 클릭됨!" + index);
  };

  // 이미지 클릭했을 때 이미지의 src 불러오기
  const hi = (e) => {
    alert(e.target.src);
    console.log(clickedImage);
  };

  // 저장 버튼 클릭 함수
  const clickSaveBtn = async (e) => {
    if (window.localStorage.getItem("isAuth") === "true") {
      if (isSearch === "true") {
        try {
          const response = await axios.post(
            `${USER_SERVER}/satellite/api/saveImage`,
            clickedImage
          );
          if (response.data.success) {
            alert("갤러리에 저장되었습니다.");
          }
        } catch (error) {
          alert(error.response.data.message);
        }
      } else {
        alert("검색을 먼저 해주십시오");
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
              {keywordList.map((item, i) => (
                <option value={keywordValue[`${i}`]} key={item}>
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
              {timeList.map((item, i) => (
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
      <div className="save_btn">
        <button onClick={clickSaveBtn}>저장</button>
      </div>
      <div className="table">
        <table>
          <tbody>
            <tr
              style={{
                border: "1px solid black",
              }}
            >
              {images.map((img, i) => (
                <td key={i} onClick={(e) => clickTable(i, e)}>
                  <button>{images[`${i}`].shooting_time}</button>
                </td>
              ))}
            </tr>
          </tbody>
        </table>
      </div>
      <div className="result_image">
        {images.length > 0 ? (
          <>
            {images[clickNum].url === null ? (
              <></>
            ) : (
              <img src={images[clickNum].url} onClick={hi} alt="위성사진" />
            )}
          </>
        ) : (
          <></>
        )}
      </div>
    </div>
  );
};

export default MainPage;
