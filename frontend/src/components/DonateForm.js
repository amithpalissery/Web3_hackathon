import React, { useState } from 'react';

function DonateForm({ setWallet }) {
  const [amount, setAmount] = useState('');

  const handleDonate = async (e) => {
    e.preventDefault();
    const response = await fetch('/donate', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ amount })
    });
    const data = await response.json();
    setWallet(data.wallet);
  };

  return (
    <form onSubmit={handleDonate}>
      <label>Amount to Donate</label>
      <input
        type="number"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />
      <button type="submit">Donate</button>
    </form>
  );
}

export default DonateForm;
