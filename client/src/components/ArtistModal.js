import { Image, Modal } from 'semantic-ui-react'

function ArtistModal({ onClose, user }) {
  return (
    <Modal
      onClose={onClose}
      open={true}
      className='artist'
    >
      <Modal.Content image>
        <Image size='huge' src={user.profile_image} circular />
        <Modal.Description>
          <p>
            <strong>Name:</strong> {user.full_name}
          </p>
          <p>
            <strong>Username:</strong> @{user.username}
          </p>
          <p>
            <strong>Bio:</strong> {user.bio}
          </p>
          <p>
            <strong>Based Out Of:</strong> {user.location}
          </p>
        </Modal.Description>
      </Modal.Content>
    </Modal>
  )
}

export default ArtistModal
