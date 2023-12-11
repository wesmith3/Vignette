import Box from '@mui/material/Box'
import ImageList from '@mui/material/ImageList'
import ImageListItem from '@mui/material/ImageListItem'
import { useState } from 'react'
import ArtworkModal from './ArtworkModal'

function Gallery({ artworks }) {
    const [selectedArtworkId, setSelectedArtworkId] = useState(null)

    const openModal = (artworkId) => {
        setSelectedArtworkId(artworkId);
      }
    
      const closeModal = () => {
        setSelectedArtworkId(null);
      }

      
    
  return (
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
  )
}

export default Gallery
