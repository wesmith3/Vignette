import Box from '@mui/material/Box';
import ImageList from '@mui/material/ImageList'
import ImageListItem from '@mui/material/ImageListItem'
import { useContext, useEffect, useState } from 'react'
import MenuBar from './MenuBar'

function Home() {
  const [artworks, setArtworks] = useState([])
  
  useEffect(() => {
    fetch('/artworks')
      .then(res => res.json())
      .then(data => {
        setArtworks(data)
      })
      .catch(err => console.log(err))
  }, [])

  console.log(artworks)

  return (
    <>
      <MenuBar />
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
  )
}

export default Home
