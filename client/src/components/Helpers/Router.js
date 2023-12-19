import { useContext } from "react";
import { Routes, Route } from "react-router-dom";
import { AuthContext } from "./AuthProvider";
import Error from "./Error";
import Login from "../Login";
import Profile from '../Profile/Profile'
import UserGallery from '../UserGallery'
import Signup from "../SignUp";
import Search from "../Search";
import Explore from "../Explore";
import Home from "../Home";
import MyGallery from "../Profile/MyGallery";
import Loading from "./Loading";
import Success from "./Success";
import Cancelled from "./Cancelled";
function Router() {
  const { login, setArtworks, setUsers, setUser, user } = useContext(AuthContext);
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
        <Route path="/:username" element={<UserGallery user={user}/>} />
        <Route path="/search" element={<Search />} />
        <Route path="/explore" element={<Explore />} />
        <Route path="/success" element={<Success />} />
        <Route path="/cancelled" element={<Cancelled />} />
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
