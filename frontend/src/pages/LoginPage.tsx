import { useState } from "react";
import { login } from "../api/client";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = async () => {
    await login(username, password);
    window.location.href = "/dashboard";
  };

  return (
    <div>
      <h2>Login</h2>
      <input value={username} onChange={e => setUsername(e.target.value)} />
      <input value={password} type="password" onChange={e => setPassword(e.target.value)} />
      <button onClick={handleSubmit}>Login</button>
    </div>
  );
}
