import styled from "styled-components";
import BlankTop from "../components/BlankTop";
import Button from "../components/Button";
import React, { useState } from "react";
import { useEffect } from "react";
import { useHistory, Link } from "react-router-dom";
import axios from "axios";
import { USER_SERVER } from "../config";
import Header from "../components/Header";
import logo from "../logos/login-logo.PNG";

const Fix = styled.div`
  background-color: #f5f6f7;
  text-align: center;
  height: 93vh;
`;

const Wrapper = styled.div`
  width: 50%;
  display: inline-block;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  margin-top: 45px;
  margin-bottom: 0;
  padding-bottom: 0;
`;

const GrayCard = styled.div`
  width: 610px;
  margin-bottom: 30px;
  margin-left: auto;
  margin-right: auto;
  font-family: "NanumSquare";
  padding: 2vw 2vw 2vw 2vw;
  text-align: center;
`;

const Input = styled.input`
  width: 450px;
  height: 50px;
  background-color: #ffffff;
  margin-top: 20px;
  margin-bottom: 20px;
  font-family: "NanumSquare";
  font-size: 20px;
`;

const Login = () => {
  const history = useHistory();
  const [info, setInfo] = useState({
    id: "",
    password: "",
  });

  const clear = async () => {
    setInfo({ id: "", password: "" });
  };

  const onInputChange = async (e) => {
    const { name, value } = e.target;
    setInfo({
      ...info,
      [name]: value,
    });
  };

  const formSubmit = async (evt) => {
    evt.preventDefault();
    if (info.id === "" || info.password === "") {
      alert("아이디와 비밀번호를 다 입력하십시오.");
    } else {
      try {
        const response = await axios.post(
          `${USER_SERVER}/user/api/login`,
          info
        );
        if (response.data.success) {
          window.localStorage.setItem("isAuth", "true");
          history.push(`/`);
          alert("로그인 되었습니다.");
        } else {
          if (response.data.message === "아이디중복") {
            alert("회원가입 되어있지 않은 아이디입니다.");
          } else {
            alert("비밀번호가 맞지 않습니다.");
          }
        }
      } catch (error) {
        //alert(error.response.data.message);
      }
    }
  };

  useEffect(() => {}, [info]);

  return (
    <Fix>
      <BlankTop DesktopMargin="3" TabletMargin="3" MobileMargin="1" />
      <Header />
      <Wrapper>
        <BlankTop DesktopMargin="3" TabletMargin="3" MobileMargin="1" />
        <img
          style={{
            width: "260px",
            marginLeft: "auto",
            marginRight: "auto",
          }}
          src={logo}
          alt="로고"
        />
        <GrayCard>
          <form>
            <Input
              placeholder="  아이디"
              name="id"
              value={info.id}
              onChange={onInputChange}
            />
            <Input
              style={{ fontFamily: "Roboto" }}
              type="password"
              placeholder="  비밀번호"
              name="password"
              value={info.password}
              onChange={onInputChange}
            />

            <Button
              width="460"
              height="55"
              font="20"
              background="#000080"
              color="#ffffff"
              marginLeft="auto"
              marginRight="auto"
              marginTop="20"
              onClick={formSubmit}
            >
              로그인
            </Button>
            <br />
            <br />
            <br />
            <br />

            <Link
              to="/signup"
              style={{
                fontSize: "20px",
                color: "#000000",
                marginTop: "40px",
                marginBottom: "0px",
              }}
            >
              회원가입
            </Link>
          </form>
        </GrayCard>
      </Wrapper>
    </Fix>
  );
};
export default Login;
