import React from 'react';
import HelloMessage from './HelloMessage';  // Assuming HelloMessage.js is in the same directory

function App() {
  return (
    <div>
      <HelloMessage name="World" />  // Pass "World" as the name prop
    </div>
  );
}

export default App;