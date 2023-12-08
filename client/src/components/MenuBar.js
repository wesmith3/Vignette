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
import Badge from '@mui/material/Badge'
import MenuItem from '@mui/material/MenuItem'
import Menu from '@mui/material/Menu'
import MenuIcon from '@mui/icons-material/Menu'
import Avatar from '@mui/material/Avatar'
import ShoppingBagIcon from '@mui/icons-material/ShoppingBag'


function MenuBar() {
  const [anchorEl, setAnchorEl] = useState(null)
  const [isDrawerOpen, setIsDrawerOpen] = useState(false)
  const navigate = useNavigate()
  const { user } = useContext(AuthContext)

  const isMenuOpen = Boolean(anchorEl)

  const handleProfileMenuOpen = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleMenuClose = () => {
    setAnchorEl(null);
  };

  const handleSignOut = () => {
    fetch('/logout', {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    }).then((res) => {
      if (res.ok) {
        navigate('/login');
      }
    });
  };

  const menuId = 'primary-search-account-menu';
  const renderMenu = (
    <Menu
      anchorEl={anchorEl}
      anchorOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      id={menuId}
      keepMounted
      transformOrigin={{
        vertical: 'top',
        horizontal: 'right',
      }}
      open={isMenuOpen}
      onClose={handleMenuClose}
    >
      <MenuItem onClick={() => {navigate("/")}}>My Gallery</MenuItem>
      <MenuItem onClick={() => {navigate("/profile")}}>My Account</MenuItem>
      <MenuItem onClick={handleSignOut}>Sign Out</MenuItem>
    </Menu>
  )

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
              onClick={() => setIsDrawerOpen(true)} // Open the drawer
              sx={{ mr: 2 }}
            >
              <MenuIcon />
            </IconButton>
        <Box sx={{ flexGrow: 1 }}>
          <Image src="././Logo.png" alt="logo" size="small" padded centered/>
        </Box>
          <Box >
            <IconButton
              size="large"
              color="inherit"
            >
              <Badge badgeContent={2} color="error">
                <ShoppingBagIcon 
                size="large"
                />
              </Badge>
            </IconButton>
            <IconButton
              size="large"
              edge="end"
              aria-label="account of current user"
              aria-controls={menuId}
              aria-haspopup="true"
              onClick={handleProfileMenuOpen}
              color="inherit"
            >
              <Avatar 
                alt={user.full_name}
                src={user.profile_image} 
                size="large"
                />
            </IconButton>
          </Box>
        </Toolbar>
      </AppBar>
      {renderMenu}
      <Drawer
          anchor="left"
          className='drawer'
          open={isDrawerOpen}
          onClose={() => setIsDrawerOpen(false)}
          PaperProps={{
            sx: {
              width: '15%',
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
            <ListItem button onClick={() => navigate('/')}>
              Home
            </ListItem>
            <br />
            <br />
            <ListItem button onClick={() => navigate('/profile')}>
              Explore
            </ListItem>
            <br />
            <br />
            <ListItem button onClick={handleSignOut}>
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
            <ListItem button onClick={() => navigate("/profile")}>
              My Gallery
            </ListItem>
            <ListItem button onClick={() => navigate("/profile")}>
              My Account
            </ListItem>
            <ListItem button onClick={handleSignOut}>
              Sign Out
            </ListItem>
          </List>
        </Drawer>
    </Box>
    </>
  );
}

export default MenuBar