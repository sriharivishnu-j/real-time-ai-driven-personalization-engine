import type { NextPage } from 'next';
import Head from 'next/head';

const Home: NextPage = () => {
  return (
    <div className="container mx-auto">
      <Head>
        <title>AI Personalization Engine</title>
      </Head>
      <main>
        <h1 className="text-3xl font-bold">
          Welcome to the AI-Driven Personalization Engine
        </h1>
      </main>
    </div>
  );
};

export default Home;