import React, { useState, useContext } from 'react'
import { Image, Modal, Grid, Card, Button, Icon, Comment, Form, Header } from 'semantic-ui-react'
import { AuthContext } from './AuthProvider'
import { formatDistanceToNow } from 'date-fns'

function ArtworkModal({ onClose, artwork }) {
  const { user } = useContext(AuthContext)
  const [liked, setLiked] = useState(false)
  const [likeCount, setLikeCount] = useState(artwork.likes.length)
  const [showComments, setShowComments] = useState(false)

  const handleLike = () => {
    const likeEndpoint = `/artworks/${artwork.id}/likes`
    const method = liked ? 'DELETE' : 'POST'

    fetch(likeEndpoint, {
      method: method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ user_id: user.id }),
    })
      .then((response) => {
        if (response.ok) {
          setLiked(!liked)
          setLikeCount((count) => (liked ? count - 1 : count + 1))
        } else {
          console.error('Error liking/unliking artwork')
        }
      })
      .catch((error) => {
        console.error('Fetch error:', error)
      })
  }

  return (
    <Modal onClose={onClose} open={true} className='artwork-modal' size='small' dimmer='true'>
      <Modal.Content>
        <Card fluid>
          <Image src={artwork.image} wrapped ui={false} />
          <Card.Content>
            <Card.Header>{artwork.title}</Card.Header>
            <Card.Description>
              <p>
                <strong>Description:</strong> {artwork.description}
              </p>
              <p>
                <strong>Price:</strong> ${artwork.price}.00
              </p>
            </Card.Description>
          </Card.Content>
          <Card.Content extra>
            <Button
              color={liked ? 'red' : 'grey'}
              onClick={handleLike}
              icon={liked ? 'heart' : 'heart outline'}
              labelPosition='right'
              label={{
                basic: true,
                color: 'red',
                pointing: 'left',
                content: likeCount.toString(),
              }}
            />
            <Button color='blue' icon labelPosition='left' onClick={() => setShowComments(!showComments)}>
              <Icon name='comment' />
              {showComments ? 'Hide Comments' : 'Show Comments'}
            </Button>
            <Button color='black' icon floated='right' labelPosition='left'>
              <Icon name='cart' />
              Add to Cart
            </Button>
            {showComments && (
              <Comment.Group>
                <Header as='h3' dividing>
                  Comments
                </Header>
                {artwork.comments.map((comment) => (
                  <Comment key={comment.id}>
                    {/* <Comment.Avatar src={comment.user.profile_image} /> */}
                    <Comment.Content>
                      {/* <Comment.Author as='a'>{comment.user.username}</Comment.Author> */}
                      <Comment.Metadata>
                        <div>{formatDistanceToNow(new Date(comment.created_at), { addSuffix: true })}</div>
                      </Comment.Metadata>
                      <Comment.Text>{comment.content}</Comment.Text>
                      <Comment.Actions>
                        <Comment.Action>Reply</Comment.Action>
                      </Comment.Actions>
                    </Comment.Content>
                  </Comment>
                ))}
                <Form reply>
                  <Form.TextArea rows={2} />
                  <Button content='Add Reply' labelPosition='left' icon='edit' primary />
                </Form>
              </Comment.Group>
            )}
          </Card.Content>
        </Card>
      </Modal.Content>
    </Modal>
  )
}

export default ArtworkModal
