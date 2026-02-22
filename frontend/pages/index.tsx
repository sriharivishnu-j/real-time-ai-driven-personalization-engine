import { useQuery } from 'react-query';

export default function Home() {
  const { data, error, isLoading } = useQuery('fetchData', fetchData);

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error: {error.message}</div>;

  return (
    <div className="container mx-auto">
      <h1 className="text-2xl font-bold">Personalized Content</h1>
      <div>{JSON.stringify(data)}</div>
    </div>
  );

  async function fetchData() {
    const response = await fetch('/api/personalized-content');
    if (!response.ok) throw new Error('Network response was not ok');
    return response.json();
  }
}