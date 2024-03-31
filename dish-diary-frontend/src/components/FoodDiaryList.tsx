import React from 'react';

const FoodDiaryList: React.FC = () => {
  // Dummy data for now
  const foodEntries = [
    { id: 1, description: 'Breakfast - Eggs and Toast', imageUrl: 'https://example.com/food1.jpg' },
    { id: 2, description: 'Lunch - Salad', imageUrl: 'https://example.com/food2.jpg' },
    // Add more entries as needed
  ];

  return (
    <div className="container mt-4">
      <h2>Food Diary</h2>
      <ul className="list-group">
        {foodEntries.map((entry) => (
          <li key={entry.id} className="list-group-item">
            <img src={entry.imageUrl} alt={entry.description} className="img-fluid mr-3" style={{ maxWidth: '100px' }} />
            <span>{entry.description}</span>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FoodDiaryList;
