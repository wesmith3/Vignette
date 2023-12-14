import { useContext, useState, useEffect } from 'react';
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

  if (!user) {
    // Render a loading state or return null until user data is available
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
        <Image src={user.profile_image} className="account-image" alt="Profile" size="medium" circular />
        <Button className="edit-image" icon="edit outline" circular size="tiny" />
        <UserEditForm user={user} setUser={setUser} />
      </div>
      <br />
      <br />
      {/* <TransactionsTable user={user} /> */}
      <br />
      <div className="delete-btn">
        <Button onClick={openConfirmationModal} fluid loading={deleting} negative>
          Delete Account
        </Button>
      </div>
      <br />
      <Modal open={showConfirmationModal} onClose={closeConfirmationModal} size="mini">
        <Modal.Header>Confirm Deletion</Modal.Header>
        <Modal.Content>
          <p>
            Are you sure you want to delete your account?
            You will no longer have access to any of your account or related information!
          </p>
        </Modal.Content>
        <Modal.Actions>
          <Button color="black" onClick={closeConfirmationModal}>
            Cancel
          </Button>
          <Button negative onClick={handleDelete} loading={deleting}>
            Delete
          </Button>
        </Modal.Actions>
      </Modal>
    </div>
  );
}

export default Profile;

