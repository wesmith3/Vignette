import { useContext } from 'react';
import { Routes, Route } from 'react-router-dom'
import { AuthProvider, AuthContext } from './AuthProvider'
import Error from './Error';
import Login from './Login';
import Profile from './Profile';
import Signup from './SignUp';
import Home from './MenuBar';

function Router() {
  const { login } = useContext(AuthContext);
  return (
    <AuthProvider>
      <Routes>
        <Route path="/profile" element={<Profile />} />
        <Route path="/signup" element={<Signup />} />
        <Route
          path="/login"
          element={<Login onLogin={(userData) => login(userData)} />}
        />
        <Route path="/" element={<Home />} />
        {/* <Route path="" element={<Error />} /> */}
      </Routes>
    </AuthProvider>
  );
}

export default Router;
