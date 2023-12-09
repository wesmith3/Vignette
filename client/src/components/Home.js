import Box from '@mui/material/Box'
import ImageList from '@mui/material/ImageList'
import ImageListItem from '@mui/material/ImageListItem'
import { useEffect, useContext, useState } from 'react'
import { AuthContext } from './AuthProvider'
import MenuBar from './MenuBar'
import ArtworkModal from './ArtworkModal'

function Home({ onLoad }) {
  const { setArtworks, artworks } = useContext(AuthContext)
  const [ darkMode, isDarkMode ] = useState(false)
  const [selectedArtworkId, setSelectedArtworkId] = useState(null)


  
  const openModal = (artworkId) => {
    setSelectedArtworkId(artworkId);
  }

  const closeModal = () => {
    setSelectedArtworkId(null);
  }

  function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
  }
  
  useEffect(() => {
    fetch('/artworks')
      .then(res => res.json())
      .then(artworkData => {
        setArtworks(shuffleArray(artworkData))
        onLoad(shuffleArray(artworkData))
      })
      .catch(err => console.log(err))
  }, [])

  return (
    <>
      <MenuBar />
      <br />
      <div>
        <Box sx={{ width: '100%' }}>
          <ImageList variant="woven" cols={3} gap={0}>
            {artworks.map((artwork) => (
              <ImageListItem key={artwork.id} sx={{ margin: 5 }}>
                <img
                  className='artwork'
                  id={artwork.id}
                  src={artwork.image}
                  alt={artwork.title}
                  onClick={() => openModal(artwork.id)}
                />
                {selectedArtworkId === artwork.id && (
                  <ArtworkModal artwork={artwork} onClose={closeModal} />
                )}
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
