const getPreviewImageURL = async (fileData) => {
  if (!fileData) {
    return null;
  }

  const fr = new FileReader();

  return new Promise((resolve) => {
    fr.readAsDataURL(fileData);
    fr.onerror = () => {
      console.log("file data is wrong");
    };
    fr.onloadend = () => {
      resolve(fr.result);
    };
  });
};
export default getPreviewImageURL;
