import React, { useEffect, useState } from "react";
import Header from "../components/Header";
import { USER_SERVER } from "../config";
import axios from "axios";
import { useHistory } from "react-router";
import "./Gallery.css";

const Gallery = () => {
  const [imgList, setImgList] = useState([]);
  const [checkImgs, setCheckImgs] = useState([]);

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
      if (response.data.success) {
        //history.push(`/`);
        const realData = response.data.images;
        setImgList(realData);
        console.log(realData[0]);
      }
    } catch (error) {
      alert(error);
    }
  };

  const checkBtn = (checked, id) => {
    if (checked) {
      setCheckImgs([...checkImgs, id]);
      console.log("체크됨");
    } else {
      // 체크 해제
      setCheckImgs(checkImgs.filter((el) => el !== id));
      console.log("체크취소");
    }
  };

  const makeATag = (url) => {
    const a = document.createElement("a");
    a.href = url;
    a.download = `${url}.jpg`;
    document.body.appendChild(a);
    a.click();
    setTimeout((_) => {
      window.URL.revokeObjectURL(url);
    }, 60000);
    a.remove();
  };

  const clickDownloadBtn = () => {
    if (checkImgs.length > 0) {
      checkImgs.forEach((url) => makeATag(url));
    } else {
      alert("체크된 것이 없습니다.");
    }
  };

  const clickDeleteBtn = async () => {
    if (checkImgs.length > 0) {
      try {
        const response = await axios.post(
          `${USER_SERVER}/satellite/api/deleteImage`,
          checkImgs
        );
        if (response.data.success) {
          alert("삭제되었습니다.");
        }
      } catch (error) {
        alert(error.response.data.message);
      }
    } else {
      alert("체크된 것이 없습니다.");
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
        <div className="tableArea">
          <thead>
            <tr>
              <td>선택</td>
              <td>이미지 제목</td>
              <td>영상 타이틀</td>
              <td>영상 촬영 날짜</td>
            </tr>
          </thead>
          <tbody>
            {imgList.map((img, i) => (
              <tr>
                <td className={i}>
                  <input
                    type="checkbox"
                    id={img.url}
                    onChange={(e) => {
                      checkBtn(e.currentTarget.checked, img.url);
                    }}
                    checked={checkImgs.includes(img.url) ? true : false}
                  />
                </td>
                <td className={i}>{img.title}</td>
                <td className={i}>{img.url}</td>
                <td className={i}>{img.shooting_peroid}</td>
              </tr>
            ))}
          </tbody>
        </div>
        <div>
          <button onClick={clickDownloadBtn}>저장</button>
        </div>
        <div>
          <button onClick={clickDeleteBtn}>삭제</button>
        </div>
      </div>
    </div>
  );
};

export default Gallery;
