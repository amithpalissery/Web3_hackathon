import React, { useState } from 'react';

function FundRequest({ wallet }) {
  const [amount, setAmount] = useState('');
  const [purpose, setPurpose] = useState('');

  const handleSubmitRequest = async (e) => {
    e.preventDefault();
    const response = await fetch('/create-request', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount, purpose })
    });
    const data = await response.json();
    console.log('Request Created:', data);
  };

  return (
    <form onSubmit={handleSubmitRequest}>
      <label>Amount Requested</label>
      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <label>Purpose</label>
      <input
        type="text"
        value={purpose}
        onChange={(e) => setPurpose(e.target.value)}
      />
      <button type="submit">Submit Request</button>
    </form>
  );
}

export default FundRequest;
