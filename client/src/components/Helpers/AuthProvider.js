import { createContext, useState, useEffect } from "react"

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [artworks, setArtworks] = useState([]);
  const [users, setUsers] = useState([]);
  const [cart, setCart] = useState([]);

 const getAuthTokenFromCookie = () => {
    const name = "access_token_cookie=";
    const decodedCookie = decodeURIComponent(document.cookie);
    const cookieArray = decodedCookie.split(';');
  
    for(let i = 0; i < cookieArray.length; i++) {
      let cookie = cookieArray[i].trim();
      if (cookie.indexOf(name) == 0) {
        return cookie.substring(name.length, cookie.length);
      }
    }
  
    return null;
  };

  useEffect(() => {
    const token = getAuthTokenFromCookie();
    console.log(token)
  
    if (token) {
      fetch('/me', {
        headers: {
          'Authorization': `Bearer ${token}`,
        },
      })
        .then(response => {
          if (!response.ok) {
            if (response.status === 401) {
              // Handle unauthorized (token expired) - you might want to redirect to login
              console.error('Token expired');
            } else {
              throw new Error('Failed to fetch user information');
            }
          }
          return response.json();
        })
        .then(userData => {
          setUser(userData);
        })
        .catch(error => {
          console.error('Failed to fetch user information on page load', error);
        });
    }
  }, []);

  const login = (userData) => {
    setUser(userData);
  };

  const logout = () => {
    setUser(null);
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        setUser,
        login,
        logout,
        artworks,
        setArtworks,
        users,
        setUsers,
        cart,
        setCart,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };
