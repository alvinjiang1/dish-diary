import React from 'react';
import './App.css';
import FileUpload, { FoodEntry } from './components/FileUpload'; // Import FileUpload component
import FoodDiaryList from './components/FoodDiaryList'; // Import FoodDiaryList component

const App: React.FC = () => {
  const handleUploadSuccess = (newEntry: FoodEntry) => {
    // Handle successful upload here
    console.log('New entry:', newEntry);
  };

  return (
    <div className="App">
      <header className="App-header">
      <h1>Food Diary App</h1>        
        <FoodDiaryList />
      </header>
    </div>
   );
  };
  
  export default App;