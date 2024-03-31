import React from 'react';

interface FoodDescriptionProps {
  description: string;
}

const FoodDescription: React.FC<FoodDescriptionProps> = ({ description }) => {
  return (
    <div className="container mt-4">
      <h2>Food Description</h2>
      <p>{description}</p>
    </div>
  );
};

export default FoodDescription;
