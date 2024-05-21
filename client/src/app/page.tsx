'use client'
import { useState, ChangeEvent, FormEvent } from 'react';
import axios from 'axios';
require('dotenv').config()

export default function Home() {
  const [firstName, setFirstName] = useState<string>('');
  const [lastName, setLastName] = useState<string>('');
  const [email, setEmail] = useState<string>('');
  const [resume, setResume] = useState<File | null>(null);
  const [message, setMessage] = useState<string>('');

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    const formData = new FormData();
    formData.append('first_name', firstName);
    formData.append('last_name', lastName);
    formData.append('email', email);
    formData.append('resume', resume!);

    try {
      await axios.post(`${process.env.NEXT_PUBLIC_API_URL}/leads`, formData);
      setMessage('Lead submitted successfully!');
    } catch (error) {
      setMessage('Error submitting lead.');
    }
  };

  return (
    <div>
      <h1>Submit a Lead</h1>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="First Name"
          value={firstName}
          onChange={(e: ChangeEvent<HTMLInputElement>) => setFirstName(e.target.value)}
          required
        />
        <input
          type="text"
          placeholder="Last Name"
          value={lastName}
          onChange={(e: ChangeEvent<HTMLInputElement>) => setLastName(e.target.value)}
          required
        />
        <input
          type="email"
          placeholder="Email"
          value={email}
          onChange={(e: ChangeEvent<HTMLInputElement>) => setEmail(e.target.value)}
          required
        />
        <input
          type="file"
          onChange={(e: ChangeEvent<HTMLInputElement>) => setResume(e.target.files![0])}
          required
        />
        <button type="submit">Submit</button>
      </form>
      <p>{message}</p>
    </div>
  );
}
