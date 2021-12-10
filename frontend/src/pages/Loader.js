import React from "react";
import ReactLoading from "react-loading";

function Loader({ type, color, message }) {
  return (
    <div className="contentWrap">
      <div
        style={{
          position: "fixed",
          top: "75%",
          left: "50%",
          transform: "translate(-25%, -50%)",
          marginLeft: "auto",
          marginRight: "auto",
        }}
      >
        <div style={{ alignItems: "center" }}>
          <h2 style={{ fontSize: "20px", transform: "translate(-25%, -50%)" }}>
            {message}
          </h2>
        </div>
        <br />
        <ReactLoading type={type} color={color} height={"50%"} width={"50%"} />
      </div>
    </div>
  );
}

export default Loader;
