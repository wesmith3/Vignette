import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import MenuBar from './Helpers/MenuBar';
import Gallery from './Gallery';
import ArtistModal from './ArtistModal';

function UserGallery() {
  const { username } = useParams();
  const [user, setUser] = useState(null);
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
          setUser(foundUser);

          const artworksResponse = await fetch(`/users/${foundUser.id}/artworks`);
          const artworksData = await artworksResponse.json();
          setArtworks(artworksData);
        } else {
          console.error('User not found');
        }
      } catch (error) {
        console.error('Error fetching user data', error);
      } finally {
        setIsLoading(false); // Set loading to false regardless of success or error
      }
    };

    fetchUserData();
  }, [username]);

  if (isLoading) {
    // Display loading spinner or message while fetching data
    return <div>Loading...</div>;
  }

  if (!user) {
    // If there's no user, display nothing
    return null;
  }

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
        <br />
        <Gallery artworks={artworks} />
        <br />
      </div>
    </>
  );
}

export default UserGallery;
