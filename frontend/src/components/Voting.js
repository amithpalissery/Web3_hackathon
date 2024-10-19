import React from 'react';

function Voting({ requests, wallet }) {
  const handleVote = async (requestId, vote) => {
    const response = await fetch('/vote', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ requestId, vote })
    });
    const data = await response.json();
    console.log('Vote Submitted:', data);
  };

  return (
    <div>
      <h2>Vote on Fund Requests</h2>
      {requests.map((request, index) => (
        <div key={index}>
          <p>{request.purpose}</p>
          <button onClick={() => handleVote(request.id, true)}>Approve</button>
          <button onClick={() => handleVote(request.id, false)}>Reject</button>
        </div>
      ))}
    </div>
  );
}

export default Voting;
