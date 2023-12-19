import { useContext, useState } from 'react';
import { AuthContext } from './Helpers/AuthProvider';
import { loadStripe } from '@stripe/stripe-js';
import { Elements } from '@stripe/react-stripe-js';
import Box from '@mui/material/Box';
import ImageList from '@mui/material/ImageList';
import ImageListItem from '@mui/material/ImageListItem';
import ArtworkModal from './ArtworkDisplay/ArtworkModal';
import MenuBar from './Helpers/MenuBar';

const stripePubKey = "pk_test_51OLr7qJxYeOx9Zwqcf5BNOofHBJ34Q47JC5eaMAXQD114sULFriIbEB3UEiaK4WX0cNrbsxcfiAuaOJuY9Rkg7vM00qbJy1vOB";

function Gallery({ onDelete }) {
  const [selectedArtworkId, setSelectedArtworkId] = useState(null);
  const { artworks, user } = useContext(AuthContext);

  const openModal = (artworkId) => {
    setSelectedArtworkId(artworkId);
  };

  const closeModal = () => {
    setSelectedArtworkId(null);
  };

  const isUserFollowing = (artwork) => {
    return user?.id && artwork.user?.followers.includes(user.id);
  };

  return (
    <>
    <MenuBar />
    <br />
    <Box sx={{ width: '100%' }}>
      <ImageList variant="woven" cols={3} gap={0}>
        {artworks.map((artwork) => (
          (isUserFollowing(artwork) || artwork.preview) && (
            <ImageListItem key={artwork.id} sx={{ margin: 5 }}>
              <img
                className="artwork"
                id={artwork.id}
                src={artwork.image}
                alt={artwork.title}
                onClick={() => openModal(artwork.id)}
                />
              {selectedArtworkId === artwork.id && (
                <Elements stripe={loadStripe(stripePubKey)}>
                  <ArtworkModal
                    artwork={artwork}
                    onClose={closeModal}
                    onDelete={onDelete}
                    />
                </Elements>
              )}
            </ImageListItem>
          )
        ))}
      </ImageList>
    </Box>
    </>
  );
}

export default Gallery;
