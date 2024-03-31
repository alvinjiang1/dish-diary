import React from 'react';
import './App.css';
import FileUpload from './components/FileUpload';
import FoodDiaryList from './components/FoodDiaryList';

const App: React.FC = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Food Diary App</h1>
        <FileUpload />
        <FoodDiaryList />
      </header>
    </div>
  );
};

export default App;
