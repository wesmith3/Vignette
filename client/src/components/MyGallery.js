import * as React from 'react'
import Box from '@mui/material/Box';
import ImageList from '@mui/material/ImageList'
import ImageListItem from '@mui/material/ImageListItem'
import { useContext, useEffect, useState } from 'react'
import MenuBar from './MenuBar'
import ArtistModal from './ArtistModal'
import { AuthContext } from './AuthProvider'


const MyGallery = () => {
  const { user } = useContext(AuthContext)
  const [artworks, setArtworks] = useState([])
  const [isModalOpen, setIsModalOpen] = useState(false);

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  useEffect(() => {
    fetch(`/users/${user.id}/artworks`)
      .then(res => res.json())
      .then(data => {
        setArtworks(data)
      })
      .catch(err => console.log(err))
  }, [user.id])


  return (
    <>
      <MenuBar />
      <br />
      <div className='artist-plaque' onClick={openModal}>
        <div className='carved-text'>
        {user.full_name}
        <br />
        @{user.username}
        {isModalOpen && <ArtistModal user={user} onClose={closeModal} />}
        </div>
      </div>
      <br />
      <div>
        <Box sx={{ width: '100%' }}>
          <ImageList variant="woven" cols={3} gap={0}>
            {artworks.map((artwork) => (
              <ImageListItem key={artwork.id} sx={{ margin: 5 }}>
                <img className='artwork' src={artwork.image} alt={artwork.title} loading="lazy" />
              </ImageListItem>
            ))}
          </ImageList>
        </Box>
        <br />
      </div>
    </>
  )
}

export default MyGallery
