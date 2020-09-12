import React, { useCallback, useState } from "react";
import getPreviewImageURL from "./utils/getPreviewImageURL";
import "./ImageUpload.css";

const ImageUpload = () => {
  const [imageData, setImageData] = useState(null);
  const [fileName, setFileName] = useState("");
  const [previewImage, setPreviewImage] = useState(null);
  const [responseMessage, setResponseMessage] = useState("");

  const handleUploadImage = useCallback(
    (event) => {
      event.preventDefault();
      if (!imageData) {
        return;
      }

      const data = new FormData();
      data.append("file", imageData);
      data.append("filename", fileName);

      fetch("http://localhost/rest/image", {
        method: "POST",
        body: data,
      })
        .then((res) => res.json())
        .then((data) => setResponseMessage(data.message));
    },
    [imageData, fileName, setResponseMessage]
  );

  const onChangeFile = useCallback(
    (event) => {
      setFileName(event.target.files[0].name);
      setImageData(event.target.files[0]);
      getPreviewImageURL(event.target.files[0]).then((imgURL) =>
        setPreviewImage(imgURL)
      );
    },
    [setImageData, setPreviewImage, setFileName]
  );

  return (
    <div>
      <div
        style={{
          display: "flex",
          width: 300,
          height: 300,
          borderWidth: 5,
          borderColor: "black",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        {previewImage && (
          <img
            src={previewImage}
            alt="previewImg"
            style={{ width: "100%", height: "100%" }}
          />
        )}
      </div>
      <form
        onSubmit={handleUploadImage}
        style={{
          display: "flex",
          flexDirection: "row",
          width: 300,
          justifyContent: "center",
        }}
      >
        <div className="filebox">
          <label for="imageInput">이미지 선택</label>
          <input
            type="file"
            accept="image/*"
            id="imageInput"
            onChange={onChangeFile}
          />
        </div>
        <button className="uploadButton">이미지 업로드</button>
      </form>
      {responseMessage && <div>{responseMessage}</div>}
    </div>
  );
};
export default ImageUpload;
