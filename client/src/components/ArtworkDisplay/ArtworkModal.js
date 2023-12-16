import { useState, useContext } from 'react'
import { Image, Modal, Card } from 'semantic-ui-react'
import { AuthContext } from '../Helpers/AuthProvider'
import EditForm from './EditForm'
import UserInfo from './UserInfo'
import Actions from './Actions'

function ArtworkModal({ onClose, artwork, onDelete }) {
  const { user, users } = useContext(AuthContext)
  const [isEditing, setIsEditing] = useState(false)


  return (
    <Modal onClose={onClose} open={true} className='artwork-modal' size='small' dimmer='blurring'>
      <Modal.Content>
        {isEditing ? (
          <EditForm artwork={artwork} setIsEditing={setIsEditing}/>
        ) : (
          <Card fluid>
            <Card.Content>
             <UserInfo artwork={artwork} user={user}/>
            </Card.Content>
            <div className="watermark-container">
              <div className="watermark">Vignette</div>
              <Image src={artwork.image} />
            </div>
            <Card.Content>
              <Card.Header>{artwork.title}</Card.Header>
              <Card.Description>
                <p>{artwork.description}</p>
                <br />
                <p>
                  <strong>Price:</strong> ${artwork.price}.00
                </p>
              </Card.Description>
              <br />
              <div>
                {artwork.tags.map((tag, index) => (
                  <span key={index}>
                    <strong>#{tag.keyword}</strong>
                    {index < artwork.tags.length - 1 ? ', ' : ''}
                  </span>
                ))}
              </div>
            </Card.Content>
            <Card.Content extra>
              <Actions artwork={artwork} user={user} users={users} setIsEditing={setIsEditing} onDelete={onDelete} onClose={onClose}/>
            </Card.Content>
          </Card>
        )}
      </Modal.Content>
    </Modal>
  )
}

export default ArtworkModal
