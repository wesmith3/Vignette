import { useContext, useEffect, useState } from 'react'
import { AuthContext } from './Helpers/AuthProvider'
import MenuBar from './Helpers/MenuBar'
import Gallery from './Gallery'
import AlertBar from './Helpers/AlertBar'

function Home() {
  const { artworks, setArtworks, user, setFollowing, following } = useContext(AuthContext)
  const [isDeleting, setIsDeleting] = useState(false)
  const [alertMessage, setAlertMessage] = useState(null)
  const [snackType, setSnackType] = useState('')
  
  useEffect(() => {
    if (user) {
      fetch(`/users/${user.id}/following`)
        .then((response) => response.json())
        .then((data) => {
          const followingIds = data.map(item => item.following_id);
          setFollowing(followingIds);
        })
        .catch((error) => {
          setAlertMessage(error)
          setSnackType('error')
        })
    }
  }, [user, setFollowing])


  const handleDelete = (artworkId) => {
    const deleteEndpoint = `/artworks/${artworkId}`

    fetch(deleteEndpoint, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    })
      .then((response) => {
        if (response.ok) {
          setArtworks((prevArtworks) =>
            prevArtworks.filter((artwork) => artwork.id !== artworkId)
          )
          setSnackType('success')
          setAlertMessage('Artwork deleted successfully')
        } else {
          setAlertMessage('Error deleting artwork')
        }
      })
      .catch((error) => {
        setSnackType('error')
        setAlertMessage('Error deleting artwork')
      })
      .finally(() => {
        setIsDeleting(true)
      })
  }


  const shuffledArtworks = [...artworks]

  for (let i = shuffledArtworks.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [shuffledArtworks[i], shuffledArtworks[j]] = [shuffledArtworks[j], shuffledArtworks[i]]
  }

  const followerArtworks = user
  ? shuffledArtworks.filter((artwork) => following.includes(artwork.user_id))
  : [];

  return (
    <>
      <MenuBar />
      <br />
      <Gallery artworks={followerArtworks} onDelete={handleDelete} />
      <br />
      <br />
      <AlertBar
        message={alertMessage}
        setAlertMessage={setAlertMessage}
        snackType={snackType}
        handleSnackType={setSnackType}
      />
    </>
  )
}

export default Home


