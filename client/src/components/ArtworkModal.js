import { useState, useContext, useEffect } from 'react'
import { Image, Modal, Grid, Card, Button, Icon, Comment, Form, Header } from 'semantic-ui-react'
import { AuthContext } from './AuthProvider'
import { formatDistanceToNow } from 'date-fns'

function ArtworkModal({ onClose, artwork }) {
  const { user, users } = useContext(AuthContext)
  const [liked, setLiked] = useState(false)
  const [likeCount, setLikeCount] = useState(artwork.likes.length)
  const [showComments, setShowComments] = useState(false)

  useEffect(() => {
    // Check if the current user's ID is in the likes array
    if (user && artwork.likes.some((like) => like.user_id === user.id)) {
      setLiked(true);
    }
  }, [user, artwork.likes]);

  const handleLike = () => {
    const likeEndpoint = `/artworks/${artwork.id}/likes`;
    const method = liked ? 'DELETE' : 'POST';

    fetch(likeEndpoint, {
      method: method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ user_id: user.id }),
    })
      .then((response) => {
        if (response.ok) {
          setLiked(!liked);
          setLikeCount((count) => (liked ? count - 1 : count + 1));
        } else {
          console.error('Error liking/unliking artwork');
        }
      })
      .catch((error) => {
        console.error('Fetch error:', error);
      });
  };

  return (
    <Modal onClose={onClose} open={true} className='artwork-modal' size='small' dimmer='blurring'>
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
              {showComments ? 'Hide Comments' : `Comments (${artwork.comments.length})`}
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
                {artwork.comments.map((comment) => {
                  const commentUser = users.find((u) => u.id === comment.user_id);

                  return (
                    <Comment key={comment.id}>
                      <Comment.Avatar src={commentUser ? commentUser.profile_image : ''} />
                      <Comment.Content>
                        <Comment.Author as='a'>@{commentUser ? commentUser.username : 'Unknown User'}</Comment.Author>
                        <Comment.Metadata>
                          <div>{formatDistanceToNow(new Date(comment.created_at), { addSuffix: true })}</div>
                        </Comment.Metadata>
                        <Comment.Text>{comment.content}</Comment.Text>
                        <Comment.Actions>
                          <Comment.Action>Reply</Comment.Action>
                        </Comment.Actions>
                      </Comment.Content>
                    </Comment>
                  );
                })}
                <Form reply>
                  <Form.TextArea style={{ maxHeight: '40px' }} />
                  <Button content='Add Comment' labelPosition='left' size='small' icon='edit' primary />
                </Form>
              </Comment.Group>
            )}
          </Card.Content>
        </Card>
      </Modal.Content>
    </Modal>
  );
}

export default ArtworkModal
