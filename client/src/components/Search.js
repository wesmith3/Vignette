import { useContext } from 'react'
import { AuthContext } from './AuthProvider'
import Box from '@mui/material/Box';
import ImageList from '@mui/material/ImageList'
import ImageListItem from '@mui/material/ImageListItem'
import TextField from '@mui/material/TextField';
import MenuBar from './MenuBar';

function Search() {
  const { artworks } = useContext(AuthContext);


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
          <br />
          <br />
          <br />
          <div>
            <Box sx={{ width: '100%' }}>
              <ImageList variant="woven" cols={3} gap={0}>
                {artworks.map((artwork) => (
                  <ImageListItem key={artwork.id} sx={{ margin: 5 }}>
                    <img className='artwork' src={artwork.image} alt={artwork.title} />
                  </ImageListItem>
                ))}
              </ImageList>
            </Box>
            <br />
          </div>
    </>
  );
}

export default Search;


