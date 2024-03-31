import React, { useState } from 'react';

const FileUpload: React.FC = () => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files.length > 0) {
      setSelectedFile(event.target.files[0]);
    }
  };

  const handleSubmit = () => {
    // Handle file upload logic
    if (selectedFile) {      
      console.log('Selected file:', selectedFile);
    }
  };

  return (
    <div className="container mt-4">
      <div className="input-group">
        <input type="file" className="form-control" onChange={handleFileChange} />
        <div className="input-group-append">
          <button className="btn btn-primary" type="button" onClick={handleSubmit}>Upload</button>
        </div>
      </div>
    </div>
  );
};

export default FileUpload;
