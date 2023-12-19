import { useContext, useState }from 'react'
import { useNavigate } from 'react-router-dom'
import { AuthContext } from './AuthProvider'
import AppBar from '@mui/material/AppBar'
import Drawer from '@mui/material/Drawer'
import List from '@mui/material/List'
import ListItem from '@mui/material/ListItem'
import Box from '@mui/material/Box'
import Toolbar from '@mui/material/Toolbar'
import IconButton from '@mui/material/IconButton'
import { Image } from 'semantic-ui-react'
import MenuIcon from '@mui/icons-material/Menu'
import Avatar from '@mui/material/Avatar'


function MenuBar() {
  const [isDrawerOpen, setIsDrawerOpen] = useState(false)
  const navigate = useNavigate()
  const { user} = useContext(AuthContext)

  const handleSignOut = () => {
    fetch('/logout', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    }).then((res) => {
      if (res.ok) {
        navigate('/');
      }
    });
  };

  return (
    <>
    <Box sx={{ flexGrow: 1 }}>
      <AppBar position="static" className="menu-bar" sx={{ height: '70px' }}>
        <Toolbar>
        <IconButton
              size="large"
              edge="start"
              color="inherit"
              aria-label="open drawer"
              onClick={() => setIsDrawerOpen(true)}
              sx={{ mr: 2 }}
            >
              <MenuIcon />
            </IconButton>
        <Box sx={{ flexGrow: 1 }}>
          <Image src="././Logo.png" alt="logo" size="small" centered/>
        </Box>
        </Toolbar>
      </AppBar>
      <Drawer
          anchor="left"
          className='drawer'
          open={isDrawerOpen}
          onClose={() => setIsDrawerOpen(false)}
          PaperProps={{
            sx: {
              width: '18%',
              padding: '15px',
              backgroundColor: 'black',
              color: "white",
              textAlign: 'center',
              fontFamily: 'cursive',
              fontSize: '45px',
              fontWeight: 'bold'
            },
          }}
        >
          <List>
            <br />
            <br />
            <ListItem className='menu-item' button onClick={() => navigate('/home')}>
              Home
            </ListItem>
            <br />
            <br />
            <ListItem className='menu-item' button onClick={() => navigate('/explore')}>
              Explore
            </ListItem>
            <br />
            <br />
            <ListItem className='menu-item' button onClick={() => navigate('/search')}>
              Search
            </ListItem>
          </List>
          <List 
          sx={{ 
            position: 'absolute', 
            bottom: '0', 
            width: '100%',
            fontSize: "25px"
          }}
          >
            <ListItem className='menu-item' button onClick={() => navigate("/my_gallery")}>
              My Gallery
            </ListItem>
            <ListItem className='menu-item' button onClick={() => navigate("/profile")}>
              My Account
            </ListItem>
            <ListItem className='menu-item' button onClick={handleSignOut}>
              Sign Out
              {user && (
                <IconButton
                  size="small"
                  edge="end"
                  aria-label="account of current user"
                  color="inherit"
                >
                  <Avatar alt={user.full_name} src={user.profile_image} size="large" />
                </IconButton>
              )}
                </ListItem>
          </List>
        </Drawer>
    </Box>
    </>
  );
}

export default MenuBar