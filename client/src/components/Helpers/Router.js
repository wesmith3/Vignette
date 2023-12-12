import { useContext } from "react";
import { Routes, Route } from "react-router-dom";
import { AuthProvider, AuthContext } from "./AuthProvider";
import Error from "./Error";
import Login from "../Login";
import Profile from '../Profile/Profile'
import UserGallery from '../UserGallery'
import Signup from "../SignUp";
import Search from "../Search";
import Home from "../Home";
import MyGallery from "../MyGallery";
import Loading from "./Loading";
import Checkout from "../Transaction/Checkout"

function Router() {
  const { login, setArtworks, setUsers, setUser } = useContext(AuthContext);
  return (
    <AuthProvider>
      <Routes>
        <Route
          path="/profile"
          element={
          <Profile 
              onLoad={(editedUser) => {
              setUser(editedUser)
          }}
            />
          }
        />
        <Route path="/signup" element={<Signup />} />
        <Route path="/checkout" element={<Checkout />} />
        <Route path="/profile/:username" element={<UserGallery />} />
        <Route path="/search" element={<Search />} />
        <Route 
          path="/loading"
          element={
            <Loading
              onLoad={(artworkData, userData) => {
                setArtworks(artworkData);
                setUsers(userData);
            }}
            />
          }
        />
        <Route path="/my_gallery" element={<MyGallery />} />
        <Route
          path="/home"
          element={
            <Home
              onLoad={(artworkData, userData) => {
                setArtworks(artworkData);
                setUsers(userData);
              }}
            />
          }
        />
        <Route
          path="/"
          element={<Login onLogin={(userData) => login(userData)} />}
        />
        <Route path="*" element={<Error />} />
      </Routes>
    </AuthProvider>
  );
}

export default Router;
