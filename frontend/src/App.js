import React, { useState, useEffect } from 'react';
import DonateForm from './components/DonateForm';
import FundRequest from './components/FundRequest';
import Voting from './components/Voting';

function App() {
  const [wallet, setWallet] = useState(null);
  const [requests, setRequests] = useState([]);
  
  useEffect(() => {
    fetchRequests();
  }, []);

  const fetchRequests = async () => {
    const response = await fetch('/api/get-requests');
    const data = await response.json();
    setRequests(data);
  };

  return (
    <div className="App">
      <h1>Crowdfunding Transparency App</h1>
      {!wallet ? (
        <DonateForm setWallet={setWallet} />
      ) : (
        <>
          <FundRequest wallet={wallet} />
          <Voting requests={requests} wallet={wallet} />
        </>
      )}
    </div>
  );
}

export default App;
