import { useContext } from "react";
import { Routes, Route } from "react-router-dom";
import { AuthContext } from "./AuthProvider";
import Error from "./Error";
import Login from "../Login";
import Profile from '../Profile/Profile'
import UserGallery from '../UserGallery'
import Signup from "../SignUp";
import Search from "../Search";
import Home from "../Home";
import MyGallery from "../MyGallery";
import Loading from "./Loading";
import { Elements } from '@stripe/react-stripe-js';
import { loadStripe } from '@stripe/stripe-js';
const stripePubKey = "pk_test_51OLr7qJxYeOx9Zwqcf5BNOofHBJ34Q47JC5eaMAXQD114sULFriIbEB3UEiaK4WX0cNrbsxcfiAuaOJuY9Rkg7vM00qbJy1vOB"

function Router() {
  const { login, setArtworks, setUsers, setUser, cart } = useContext(AuthContext);
  return (
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
  );
}

export default Router;
