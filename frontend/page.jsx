
'use client';
import { useState } from 'react';

export default function Home() {
  const [from, setFrom] = useState('Madrid');
  const [to, setTo] = useState('Barcelona');
  const [date, setDate] = useState('2025-07-15');
  const [result, setResult] = useState('');

  const search = async () => {
    const res = await fetch(`http://localhost:8000/search?from_city=${from}&to_city=${to}&date=${date}`);
    const data = await res.json();
    setResult(data.result);
  };

  return (
    <main className="p-10">
      <h1 className="text-2xl font-bold mb-4">Comparador de Viajes</h1>
      <div className="flex gap-4 mb-4">
        <input value={from} onChange={e => setFrom(e.target.value)} placeholder="Desde" className="border p-2" />
        <input value={to} onChange={e => setTo(e.target.value)} placeholder="Hasta" className="border p-2" />
        <input type="date" value={date} onChange={e => setDate(e.target.value)} className="border p-2" />
        <button onClick={search} className="bg-blue-500 text-white px-4 py-2">Buscar</button>
      </div>
      <pre className="bg-gray-100 p-4">{result}</pre>
    </main>
  );
}
