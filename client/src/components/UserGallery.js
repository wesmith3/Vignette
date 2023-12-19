import { useState, useEffect, useContext } from 'react';
import { AuthContext } from './Helpers/AuthProvider'
import { useParams } from 'react-router-dom';
import MenuBar from './Helpers/MenuBar';
import Gallery from './Gallery';
import ArtistModal from './ArtistModal';

function UserGallery() {
  const { username } = useParams()
  const { user } = useContext(AuthContext)
  const [artist, setArtist] = useState(null);
  const [artworks, setArtworks] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [isLoading, setIsLoading] = useState(true);

  const openModal = () => {
    setIsModalOpen(true);
  };

  const closeModal = () => {
    setIsModalOpen(false);
  };

  useEffect(() => {
    const fetchUserData = async () => {
      try {
        const allUsersResponse = await fetch('/users');
        const allUsersData = await allUsersResponse.json();
        const foundUser = allUsersData.find((u) => u.username === username);

        if (foundUser) {
          setArtist(foundUser)
          const userFollowing = user && foundUser.followers && foundUser.followers.some(follow => follow.follower_id === user.id);
          
          const artworksResponse = await fetch(`/users/${foundUser.id}/artworks`)
          const artworksData = await artworksResponse.json();
          if (userFollowing) {
            setArtworks(artworksData)
          } else {
            const previewArtworks = artworksData.filter((artwork) => artwork.preview === true);
            setArtworks(previewArtworks);
          }

        } else {
          console.error('User not found');
        }
      } catch (error) {
        console.error('Error fetching user data', error);
      } finally {
        setIsLoading(false);
      }
    };

    fetchUserData();
  }, [username]);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (!artist) {
    return null;
  }

  return (
    <>
      <MenuBar />
      <br />
      <div className='artist-plaque' onClick={openModal}>
        <div className='carved-text'>
          {artist.full_name}
          <br />
          @{artist.username}
          {isModalOpen && <ArtistModal artist={artist} onClose={closeModal} />}
        </div>
      </div>
      <br />
      <div>
        <br />
        <Gallery artworks={artworks} />
        <br />
      </div>
    </>
  );
}

export default UserGallery;
