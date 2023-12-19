import { createContext, useState, useEffect } from "react"
import { useNavigate } from 'react-router-dom'

const getCookie = (name) => {
  const value = `; ${document.cookie}`;
  const parts = value.split(`; ${name}=`);
  if (parts.length === 2) return parts.pop().split(';').shift();
};

const AuthContext = createContext();

const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [following, setFollowing] = useState([]);
  const [artworks, setArtworks] = useState([]);
  const [users, setUsers] = useState([]);
  const [artToPurchase, setArtToPurchase] = useState(null);
  const navigate = useNavigate()


  useEffect(() => {
      fetch('/me', {
        headers: {
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
                      fetch('/logout', {
                        method: 'DELETE',
                        headers: {
                          'Content-Type': 'application/json',
                        },
                      }).then((res) => {
                        if (res.ok) {
                        }
                      });
                      } else {
                        return response.json()
                      }
                    })
          .catch(err => console.log(err))
          }
          else {
            response.json()
            .then(data => {
              setUser(data)
            })
          }
        })
        .then(userData => {
          setUser(userData)
          fetch("/artworks")
          .then(response => response.json())
          .then(data => {
            setArtworks(data)
            fetch("/users")
            .then(response => response.json())
            .then(data => setUsers(data))
            .catch(err => console.log(err))
          })
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
        setArtToPurchase,
        following,
        setFollowing
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export { AuthContext, AuthProvider };
