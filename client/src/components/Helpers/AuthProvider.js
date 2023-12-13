import { createContext, useState, useEffect } from "react"

const getCookie = (name) => {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
};

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [artworks, setArtworks] = useState([]);
  const [users, setUsers] = useState([]);
  const [artToPurchase, setArtToPurchase] = useState(null);

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

  // useEffect(() => {
  //   const token = getAuthTokenFromCookie()
  //   console.log(token)
  //   if (token) {
  //     fetch('/me', {
  //       headers: {
  //         // 'Authorization': `Bearer ${token}`,
  //         'X-CSRF-TOKEN': getCookie('csrf_access_token')
  //       },
  //     })
  //       .then(response => {
  //         if (!response.ok) {
  //           if (response.status === 401) {
  //             // Handle unauthorized (token expired) - you might want to redirect to login
  //             console.error('Token expired');
  //           } else {
  //             throw new Error('Failed to fetch user information');
  //           }
  //         }
  //         return response.json();
  //       })
  //       .then(userData => {
  //         setUser(userData);
  //       })
  //       .catch(error => {
  //         console.error('Failed to fetch user information on page load', error);
  //       });
  //   }
  // }, []);
  useEffect(() => {
      fetch('/me', {
        headers: {
          // 'Authorization': `Bearer ${token}`,
          'X-CSRF-TOKEN': getCookie('csrf_access_token')
        },
      })
        .then(response => {
          if (!response.ok) {
            fetch('/refresh', {
              method: "POST",
              headers: {
                'X-CSRF-TOKEN': getCookie('csrf_refresh_token')
              }
          })
          .then(response => {
                    if (!response.ok) {
                        console.error('No Refresh Token');
                      } else {
                        return response.json()
                      }
                    })
          .catch(err => console.log(err))
          }
          else {
            response.json()
            .then(data => setUser(data))
          }
        })
        .then(userData => {
          setUser(userData)
          fetch("/artworks")
          .then(response => response.json())
          .then(data => setArtworks(data))
          .catch(err => console.log(err))
        })
        .catch(error => {
          console.error('Failed to fetch user information on page load', error);
        })
  }, [])

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
        artToPurchase,
        setArtToPurchase
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };
