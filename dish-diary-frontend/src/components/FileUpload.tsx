import React, { useState } from 'react';
import axios from 'axios';

export interface FoodEntry {
  id: number;
  description: string;
  imageUrl: string;
}

interface FileUploadProps {
  onUploadSuccess: (newEntry: FoodEntry) => void; // Callback function to handle upload success
}

const FileUpload: React.FC<FileUploadProps> = ({ onUploadSuccess }) => {
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const handleFileChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    if (event.target.files && event.target.files.length > 0) {
      setSelectedFile(event.target.files[0]);
    }
  };

  const handleSubmit = async () => {
    if (selectedFile) {
      const formData = new FormData();
      formData.append('file', selectedFile);

      try {
        const response = await axios.post('http://127.0.0.1:5000/upload', formData, {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        });
        console.log(response.data);
        onUploadSuccess(response.data); // Trigger the callback function with the new entry
      } catch (error) {
        console.error('Error uploading file:', error);
      }
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
