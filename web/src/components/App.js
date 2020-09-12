import React from "react";
import ImageUpload from "./ImageUpload/ImageUpload";

const App = () => {
  return (
    <div
      style={{
        display: "flex",
        width: window.innerWidth,
        height: window.innerHeight,
        justifyContent: "center",
        alignItems: "center",
      }}
    >
      <ImageUpload />
    </div>
  );
};
export default App;
