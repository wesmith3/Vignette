import { useContext, useState } from 'react'
import { AuthContext } from './Helpers/AuthProvider'
import MenuBar from './Helpers/MenuBar'
import Gallery from './Gallery'
import AlertBar from './Helpers/AlertBar'

function Home() {
  const { artworks, setArtworks } = useContext(AuthContext)
  const [isDeleting, setIsDeleting] = useState(false)
  const [alertMessage, setAlertMessage] = useState(null);
  const [snackType, setSnackType] = useState('');

  const handleDelete = (artworkId) => {
    const deleteEndpoint = `/artworks/${artworkId}`;
  
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
          );
          setSnackType('success');
          setAlertMessage('Artwork deleted successfully');
        } else {
          setAlertMessage('Error deleting artwork');
        }
      })
      .catch((error) => {
        setSnackType('error');
        setAlertMessage('Error deleting artwork');
      })
      .finally(() => {
        setIsDeleting(true);
      });
  };

  return (
    <>
      <MenuBar />
      <br />
      <Gallery artworks={artworks} onDelete={handleDelete} />
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
