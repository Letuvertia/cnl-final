import React from 'react';

function HelloMessage(props) {
  return (
    <div>
      <h1>Hello, {props.name}!</h1>
      <p>Welcome to your React application.</p>
    </div>
  );
}

export default HelloMessage;