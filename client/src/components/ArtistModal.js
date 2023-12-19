import { Image, Modal } from 'semantic-ui-react'

function ArtistModal({ onClose, artist }) {
  return (
    <Modal
      onClose={onClose}
      open={true}
      className='artist'
    >
      <Modal.Content image>
        <Image size='huge' src={artist.profile_image} circular />
        <Modal.Description>
          <p>
            <strong>Name:</strong> {artist.full_name}
          </p>
          <p>
            <strong>Username:</strong> @{artist.username}
          </p>
          <p>
            <strong>Bio:</strong> {artist.bio}
          </p>
          <p>
            <strong>Based In:</strong> {artist.location}
          </p>
        </Modal.Description>
      </Modal.Content>
    </Modal>
  )
}

export default ArtistModal
