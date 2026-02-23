import React from 'react';
import { useQuery } from 'react-query';

const fetchPersonalizationData = async () => {
  const response = await fetch('/api/personalization');
  if (!response.ok) throw new Error('Network response was not ok');
  return response.json();
};

const HomePage: React.FC = () => {
  const { data, error, isLoading } = useQuery('personalizationData', fetchPersonalizationData);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold">Personalization Engine</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
};

export default HomePage;