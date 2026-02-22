import React from 'react';
import { useQuery } from 'react-query';

export default function Home() {
  const { data, error, isLoading } = useQuery('fetchPersonalization', fetchPersonalization);

  if (isLoading) return <p>Loading...</p>;
  if (error) return <p>Error loading data</p>;
  
  return (
    <div className="p-4">
      <h1 className="text-2xl font-bold">Personalized Content</h1>
      <p>{data.content}</p>
    </div>
  );

  async function fetchPersonalization() {
    const response = await fetch('/api/personalization');
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  }
}