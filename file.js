function search(files) {
  function findFile(currentPath, currentFiles) {
    for (let key in currentFiles) {
      let newPath = currentPath === '' ? key : `${currentPath}/${key}`;
      let value = currentFiles[key];

      if (typeof value === 'string') {
      
        return newPath;
      } else if (typeof value == 'object' && value !== null) {
    
        let result = findFile(newPath, value);
        if (result) {
          return result;
        }
      }
    }
    return null; 
  }

  let filePath = findFile('', files);

  if (filePath) {
    return filePath;
  } else {
    throw new Error("No file found in the filesystem.");
  }
}