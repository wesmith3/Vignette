import { useState, useEffect } from 'react';
import { Button, Icon } from 'semantic-ui-react'
import CommentSection from './CommentSection';
import AlertBar from '../Helpers/AlertBar'

function Actions({ artwork, user, users, setIsEditing, onDelete, onClose, likes, setLikes, comments, setComments }) {
  const [liked, setLiked] = useState(false)
  const [showComments, setShowComments] = useState(false)
  const [alertMessage, setAlertMessage] = useState(null)
  const [snackType, setSnackType] = useState('')
  const isCurrentUserOwner = user && artwork.user_id === user.id

  
  const handleLike = async () => {
    const likeEndpoint = `/artworks/${artwork.id}/likes`;
    const method = liked ? 'DELETE' : 'POST';

    try {
      setLiked(!liked);
      setLikes((count) => (liked ? count - 1 : count + 1));

      const response = await fetch(likeEndpoint, {
        method: method,
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: user.id }),
      });

      if (!response.ok) {
        setLiked(liked);
        setLikes((count) => (liked ? count + 1 : count - 1));
        setAlertMessage('Error liking/unliking artwork')
        setSnackType("error")
      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  useEffect(() => {
    if (user && artwork.likes.some((like) => like.user_id === user.id)) {
      setLiked(true)
    }
  }, [user, artwork.likes])

  const handleDelete = async () => {
    try {
      onClose()
      onDelete(artwork.id)
    } catch (error) {
      console.error('Error deleting artwork from modal:', error)
    }
  }

  const handleEdit = () => {
    setIsEditing(true)
  }


  return (
    <>
            <Button
                color={liked ? 'red' : 'grey'}
                onClick={handleLike}
                icon={liked ? 'heart' : 'heart outline'}
                labelPosition='right'
                label={{
                  basic: true,
                  color: 'red',
                  pointing: 'left',
                  content: likes,
                }}
              />
              <Button
                color='blue'
                icon
                labelPosition='left'
                onClick={() => setShowComments(!showComments)}
                >
                <Icon name='comment' />
                {showComments ? 'Hide Comments' : `Comments (${comments.length})`}
              </Button>
              {isCurrentUserOwner ? (
                <>
                  <Button
                    color='red'
                    icon
                    floated='right'
                    labelPosition='left'
                    onClick={handleDelete}
                    >
                    <Icon name='trash' />
                    Delete Artwork
                  </Button>
                  <Button icon floated='right' labelPosition='left' onClick={handleEdit}>
                    <Icon name='edit' />
                    Edit Artwork
                  </Button>
                </>
              ) : (
                <form action={`/create-checkout-session/${artwork.id}`} method='POST'>
                  <Button floated='right' type='submit'>Checkout</Button>
                </form>
              )}
              {showComments && <CommentSection artwork={artwork} users={users} comments={comments} setComments={setComments} />}
              {alertMessage && (
              <AlertBar
                message={alertMessage}
                setAlertMessage={setAlertMessage}
                snackType={snackType}
                handleSnackType={setSnackType}
              />
            )}
          </>
  );
}

export default Actions;
