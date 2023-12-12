import React from 'react';
import { useNavigate } from 'react-router-dom';
import Drawer from '@mui/material/Drawer'
import MUIList from '@mui/material/List'; // Alias for @mui/material List
import { Button, Image, List } from 'semantic-ui-react';

const ShoppingCartDrawer = ({ isCartOpen, setIsCartOpen, cart }) => {
  const navigate = useNavigate();

  return (
    <Drawer
    anchor="right"
    className='cart'
    open={isCartOpen}
    onClose={() => setIsCartOpen(false)}
    PaperProps={{
      sx: {
        width: '20%',
        padding: '15px',
        // backgroundColor: 'black',
        // color: 'white',
        textAlign: 'center',
        fontFamily: 'cursive',
        fontSize: '16px',
        fontWeight: 'bold',
      },
    }}
    >
    <div>
        <h1 className='cart-header'>My Cart</h1>
      <List celled >
        {cart.map((item) => (
          <List.Item key={item.id}>
            <Image avatar src={item.image} />
            <List.Content>
              <List.Header as='a'>{item.title}</List.Header>
              <List.Description>${(item.price / 100).toFixed(2)}</List.Description>
            </List.Content>
          </List.Item>
        ))}
      </List>
      <MUIList
        sx={{
          position: 'absolute',
          bottom: '0',
          width: '100%',
          fontSize: '25px',
        }}
      >
        <p>
          <strong className='total'>Total:</strong> ${cart.reduce((acc, item) => acc + item.price / 100, 0).toFixed(2)}
        </p>
        <Button className='checkout-btn' onClick={() => navigate('/checkout')}>
          Checkout
        </Button>
      </MUIList>
    </div>
    </Drawer>
  );
};

export default ShoppingCartDrawer;

