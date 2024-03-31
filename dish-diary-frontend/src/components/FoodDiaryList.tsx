import React, { useState, useEffect } from 'react';
import axios from 'axios';
import FileUpload, { FoodEntry } from './FileUpload';

const FoodDiaryList: React.FC = () => {
  const [foodEntries, setFoodEntries] = useState<FoodEntry[]>([]);

  useEffect(() => {
    const fetchFoodDiary = async () => {
      try {
        const response = await axios.get('http://127.0.0.1:5000/food-diary');
        setFoodEntries(response.data);
      } catch (error) {
        console.error('Error fetching food diary:', error);
      }
    };

    fetchFoodDiary();
  }, []);
  const handleUploadSuccess = (newEntry: FoodEntry) => {
    setFoodEntries([newEntry, ...foodEntries]);
  };
  
  return (
    <div className="container mt-4">
      <h2>Food Diary</h2>
      <FileUpload onUploadSuccess={handleUploadSuccess} />
      <ul className="list-group">
        {foodEntries.map((entry, index) => ( // Add index as a fallback key
          <li key={entry.id || index} className="list-group-item">
            <div className="d-flex align-items-center">
              <img src={entry.imageUrl} alt={entry.description} className="img-fluid mr-3" style={{ maxWidth: '100px' }} />      
              <span style={{ color: 'black' }}>{entry.description}</span>        
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FoodDiaryList;
