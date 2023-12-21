import React, { useState, useContext } from 'react';
import { AuthContext } from './Helpers/AuthProvider';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import Tabs from '@mui/material/Tabs';
import Tab from '@mui/material/Tab';
import MenuBar from './Helpers/MenuBar';
import Gallery from './Gallery';

function Search() {
  const { user, artworks } = useContext(AuthContext);
  const [searchQuery, setSearchQuery] = useState('');
  const [selectedUserTab, setSelectedUserTab] = useState(null);

  // Extract unique users from filtered artworks
  const uniqueUsers = Array.from(
    new Set(
      artworks
        .filter((artwork) => {
          const lowerCaseQuery = searchQuery.toLowerCase();
          const lowerCaseUsername = artwork.user?.username?.toLowerCase() || '';
          return lowerCaseUsername.includes(lowerCaseQuery);
        })
        .map((artwork) => artwork.user?.username)
    )
  );

  const isUserFollowing = (artwork) => {
    return user?.id && artwork.user?.followers.includes(user.id);
  };

  const filteredArtworks = artworks.filter((artwork) => {
    const lowerCaseQuery = searchQuery.toLowerCase();
    const lowerCaseUsername = artwork.user?.username?.toLowerCase() || '';
    const lowerCaseTitle = artwork.title?.toLowerCase() || '';

    const lowerCaseTags = (artwork.tags || []).flatMap((tag) =>
      tag?.keyword?.toString().toLowerCase()
    );

    return (
      (selectedUserTab === null || lowerCaseUsername === selectedUserTab) &&
      (lowerCaseUsername.includes(lowerCaseQuery) ||
        lowerCaseTitle.includes(lowerCaseQuery) ||
        lowerCaseTags.some((tag) => tag.includes(lowerCaseQuery)) ||
        (artwork.preview || isUserFollowing(artwork)))
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
            placeholder='Search by username, title, or tags'
          />
        </Box>
      </div>
      <br />
      {uniqueUsers.length > 0 && (
        <Tabs
          value={selectedUserTab}
          onChange={(_, newValue) => setSelectedUserTab(newValue)}
          indicatorColor='primary'
          textColor='primary'
          centered
        >
          <Tab label='All' value={null} />
          {uniqueUsers.map((user, index) => (
            <Tab key={index} label={user} value={user} />
          ))}
        </Tabs>
      )}
      <br />
      <Gallery artworks={filteredArtworks} />
    </>
  );
}

export default Search;