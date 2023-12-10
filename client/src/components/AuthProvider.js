import { createContext, useState } from 'react';

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [artworks, setArtworks] = useState([]);
  const [users, setUsers] = useState([])

  const login = (userData) => {
    setUser(userData);
  };

  const logout = () => {
    setUser(null);
  };

  return (
    <AuthContext.Provider value={{ user, setUser, login, logout, artworks, setArtworks, users, setUsers }}>
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };
