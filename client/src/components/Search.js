import React from 'react';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import MenuBar from './MenuBar';

function Search() {
  return (
    <>
      <MenuBar />
      <div style={{ display: 'flex', justifyContent: 'center' }}>
        <Box
          sx={{
            width: '60%',
            maxWidth: '100%',
            display: 'flex',
            flexDirection: 'column',
            alignItems: 'center',
            marginTop: '5%',
          }}
        >
          <TextField
            fullWidth
            className='search-bar'
            sx={{
              backgroundColor: 'black',
              color: 'white',
              // borderRadius: '25px',
              '& input': {
                color: 'white',
                border: 'none', // Remove the border
                outline: 'none', // Remove the outline
              },
              '& input:focus': {
                border: 'none', // Remove the border on focus
                outline: 'none', // Remove the outline on focus
              },
            }}
          />
        </Box>
      </div>
    </>
  );
}

export default Search;


