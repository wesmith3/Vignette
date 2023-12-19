import { useState, useContext, useEffect } from 'react'
import { Image, Modal, Card } from 'semantic-ui-react'
import { AuthContext } from '../Helpers/AuthProvider'
import EditForm from './EditForm'
import UserInfo from './UserInfo'
import Actions from './Actions'

function ArtworkModal({ onClose, artwork, onDelete }) {
  const { user, users } = useContext(AuthContext)
  const [isEditing, setIsEditing] = useState(false)
  const [comments, setComments] = useState([])
  const [likes, setLikes] = useState([])
  const [isLiked, setIsLiked] = useState(false)

useEffect(() => {
  fetch(`/artworks/${artwork.id}/comments`)
    .then(res => res.json())
    .then(comments => {
      setComments(comments)
      fetch(`/artworks/${artwork.id}/likes`)
        .then(res => res.json())
        .then(likes => {
          setLikes([...likes])
          const userExists = user && likes.some(like => like.user_id === user.id)
          if (userExists) {
            setIsLiked(true);
          }
        })
        })
    .catch(err => console.log(err));
}, []);



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
              <div><strong>Tags:</strong></div>
              <div>
                {artwork.tags.map((tag, index) => (
                  <span key={index}>
                    #{tag.keyword}
                    {index < artwork.tags.length - 1 ? ', ' : ''}
                  </span>
                ))}
              </div>
            </Card.Content>
            <Card.Content extra>
              <Actions
                artwork={artwork}
                user={user}
                users={users}
                setIsEditing={setIsEditing}
                onDelete={onDelete}
                onClose={onClose}
                likes={likes}
                isLiked={isLiked}
                setIsLiked={setIsLiked}
                setLikes={setLikes}
                comments={comments}
                setComments={setComments}
              />
            </Card.Content>
          </Card>
        )}
      </Modal.Content>
    </Modal>
  )
}

export default ArtworkModal
