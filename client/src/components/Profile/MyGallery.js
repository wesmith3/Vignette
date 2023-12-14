import { useState, useContext, useEffect } from 'react';
import { Button, Popup } from 'semantic-ui-react';
import MenuBar from '../Helpers/MenuBar';
import Gallery from '../Gallery';
import ArtistModal from '../ArtistModal';
import { AuthContext } from '../Helpers/AuthProvider';
import ArtworkForm from './ArtworkForm';
import AlertBar from '../Helpers/AlertBar';

const MyGallery = () => {
  const { user, setArtworks } = useContext(AuthContext);
  const [artworks, setArtworksLocal] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);
  const [isFormVisible, setIsFormVisible] = useState(false);
  const [alertMessage, setAlertMessage] = useState(null);
  const [snackType, setSnackType] = useState('');

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

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

  const handleArtworkSubmit = (values) => {
    const tagsArray = values.tags.split(',').map(tag => tag.trim());
  
    fetch(`/users/${user.id}/artworks`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ ...values, tags: tagsArray }),
    })
      .then((res) => {
        if (!res.ok) {
          throw new Error('Error submitting artwork');
        }
        return res.json();
      })
      .then((data) => {
        setArtworksLocal((prevArtworks) => [...prevArtworks, data]);
        setIsFormVisible(false);
        setSnackType('success');
        setAlertMessage('Artwork created successfully');
      })
      .catch((error) => {
        setSnackType('error');
        setAlertMessage(error.message);
      });
  };

  useEffect(() => {
    if (user) {
      fetch(`/users/${user.id}/artworks`)
        .then((res) => res.json())
        .then((data) => {
          setArtworksLocal(data);
          setIsDeleting(false);
        })
        .catch((err) => console.log(err));
    }
  }, [user, isFormVisible, isDeleting]);

  if (!user) {
    return null;
  }

  return (
    <>
      <MenuBar />
      <br />
      <Popup
        content='Add New Artwork'
        position='left center'
        trigger={
          <Button
            className='add-artwork-btn'
            color='black'
            icon='add'
            circular
            floated='right'
            onClick={() => setIsFormVisible(true)}
          />
        }
      />
      {isFormVisible && (
        <>
          <ArtworkForm onSubmit={handleArtworkSubmit} onCancel={() => setIsFormVisible(false)} />
        </>
      )}
        <AlertBar
          message={alertMessage}
          setAlertMessage={setAlertMessage}
          snackType={snackType}
          handleSnackType={setSnackType}
        />
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
        <br />
        <Gallery artworks={artworks} onDelete={handleDelete} />
        <br />
      </div>
    </>
  );
};

export default MyGallery;
