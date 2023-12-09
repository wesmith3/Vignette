import { useContext } from 'react';
import { Routes, Route } from 'react-router-dom'
import { AuthProvider, AuthContext } from './AuthProvider'
import Error from './Error';
import Login from './Login';
import Profile from './Profile';
import Signup from './SignUp';
import Search from './Search';
import Home from './Home';
import MyGallery from './MyGallery'

function Router() {
  const { login, setArtworks } = useContext(AuthContext);
  return (
    <AuthProvider>
      <Routes>
        <Route path="/profile" element={<Profile />} />
        <Route path="/signup" element={<Signup />} />
        <Route path="/search" element={<Search />} />
        <Route path="/my_gallery" element={<MyGallery />} />
        <Route path="/home" element={<Home onLoad={(artworkData) => setArtworks(artworkData)}/>} />
        <Route
          path="/"
          element={<Login onLogin={(userData) => login(userData)} />}
        />
        {/* <Route path="" element={<Error />} /> */}
      </Routes>
    </AuthProvider>
  );
}

export default Router;
