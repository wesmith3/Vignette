import React, { useContext, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Button, Image, Modal } from 'semantic-ui-react';
import MenuBar from '../Helpers/MenuBar';
import { AuthContext } from '../Helpers/AuthProvider';
import UserEditForm from './UserEditForm';

function Profile() {
  const { user, setUser } = useContext(AuthContext);
  const navigate = useNavigate();
  const [deleting, setDeleting] = useState(false);
  const [showConfirmationModal, setShowConfirmationModal] = useState(false);
  const [showImageEditModal, setShowImageEditModal] = useState(false);
  const [newProfileImage, setNewProfileImage] = useState(null);

  const handleDelete = async () => {
    try {
      setDeleting(true);
      const response = await fetch(`/users/${user.id}`, {
        method: 'DELETE',
      });
      if (response.ok) {
        navigate('/');
      } else {
        console.error('Failed to delete user');
      }
    } catch (error) {
      console.error('Error during user deletion:', error);
    } finally {
      setDeleting(false);
      setShowConfirmationModal(false);
    }
  };

  const openConfirmationModal = () => {
    setShowConfirmationModal(true);
  };

  const closeConfirmationModal = () => {
    setShowConfirmationModal(false);
  };

  const openImageEditModal = () => {
    setShowImageEditModal(true);
  };

  const closeImageEditModal = () => {
    setShowImageEditModal(false);
  };

  const handleProfileImageChange = (event) => {
    const file = event.target.files[0];
    if (file) {
      setNewProfileImage(URL.createObjectURL(file));
    }
  };

  const handleSaveProfileImage = async () => {
    try {
      // Assuming you have an API endpoint to update the user's profile picture
      const response = await fetch(`/users/${user.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ profile_image: newProfileImage }),
      });

      if (response.ok) {
        // Update the user's profile image in the local state
        setUser((prevUser) => ({ ...prevUser, profile_image: newProfileImage }));
        // Close the modal
        closeImageEditModal();
      } else {
        console.error('Failed to update profile image');
      }
    } catch (error) {
      console.error('Error during profile image update:', error);
    }
  };

  if (!user) {
    return null;
  }

  return (
    <div className="profile">
      <MenuBar />
      <br />
      <br />
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
        <Image src={newProfileImage || user.profile_image} className="account-image" alt="Profile" size="medium" circular />
        <Button className="edit-image" icon="edit outline" circular size="tiny" onClick={openImageEditModal} />
        <UserEditForm user={user} setUser={setUser} />
      </div>
      <br />
      <br />
      <br />
      <div className="delete-btn">
        <Button onClick={openConfirmationModal} fluid loading={deleting} negative>
          Delete Account
        </Button>
      </div>
      <br />
      <Modal open={showConfirmationModal} onClose={closeConfirmationModal} size="mini">
      </Modal>
      <Modal open={showImageEditModal} onClose={closeImageEditModal} size="mini">
        <Modal.Header>Edit Profile Image</Modal.Header>
        <Modal.Content>
          <input type="file" accept="image/*" onChange={handleProfileImageChange} />
        </Modal.Content>
        <Modal.Actions>
          <Button color="black" onClick={closeImageEditModal}>
            Cancel
          </Button>
          <Button positive onClick={handleSaveProfileImage} loading={deleting}>
            Save
          </Button>
        </Modal.Actions>
      </Modal>
    </div>
  );
}

export default Profile;


