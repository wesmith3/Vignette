import React from 'react';
import { useNavigate } from 'react-router-dom'
import Drawer from '@mui/material/Drawer'
import List from '@mui/material/List'
import { Button } from 'semantic-ui-react'

const ShoppingCartDrawer = ({ isCartOpen, setIsCartOpen }) => {
    const navigate = useNavigate()
    
  return (
    <Drawer
      anchor="right"
      className='cart'
      open={isCartOpen}
      onClose={() => setIsCartOpen(false)}
      PaperProps={{
        sx: {
          width: '15%',
          padding: '15px',
          backgroundColor: 'black',
          color: 'white',
          textAlign: 'center',
          fontFamily: 'cursive',
          fontSize: '16px',
          fontWeight: 'bold',
        },
      }}
    >
      <div>
        <h1 className='cart-header'>My Cart</h1>
        {/* Your cart items and details go here */}
        <ul>
          <li>Product 1</li>
          <li>Product 2</li>
          {/* Add more items as needed */}
        </ul>
        <List 
          sx={{ 
            position: 'absolute', 
            bottom: '0', 
            width: '100%',
            fontSize: "25px"
          }}>
        <p><strong className='total'>Total:</strong> $100.00</p>
        <Button className='checkout-btn' onClick={() => navigate("/checkout")}>Checkout</Button>
        </List>
      </div>
    </Drawer>
  );
};

export default ShoppingCartDrawer;
