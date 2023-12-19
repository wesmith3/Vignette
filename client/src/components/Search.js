import React, { useState, useContext } from 'react';
import { AuthContext } from './Helpers/AuthProvider';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import MenuBar from './Helpers/MenuBar';
import Gallery from './Gallery';

function Search() {
  const { artworks } = useContext(AuthContext);
  const [searchQuery, setSearchQuery] = useState('');

  const filteredArtworks = artworks.filter((artwork) => {
    const lowerCaseQuery = searchQuery.toLowerCase();
    const lowerCaseUsername = artwork.user?.username?.toLowerCase() || '';
    const lowerCaseTitle = artwork.title?.toLowerCase() || ''; 

    const lowerCaseTags = (artwork.tags || []).flatMap((tag) => tag?.keyword?.toString().toLowerCase());
  
    return (
      lowerCaseUsername.includes(lowerCaseQuery) ||
      lowerCaseTitle.includes(lowerCaseQuery) ||
      lowerCaseTags.some((tag) => tag.includes(lowerCaseQuery))
    );
  });

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
              color: 'white',
            }}
            value={searchQuery}
            onChange={(e) => setSearchQuery(e.target.value)}
            placeholder="Search by username, title, or tags"
          />
        </Box>
      </div>
      <br />
      <br />
      <br />
      <Gallery artworks={filteredArtworks} />
    </>
  );
}

export default Search;
