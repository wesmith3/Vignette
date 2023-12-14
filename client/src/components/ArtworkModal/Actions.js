import { useState, useEffect } from 'react';
import { Button, Icon } from 'semantic-ui-react'
import CommentSection from './CommentSection';

function Actions({ artwork, user, users, setIsEditing, onDelete, onClose }) {
  const [liked, setLiked] = useState(false)
  const [likeCount, setLikeCount] = useState(artwork.likes.length)
  const [showComments, setShowComments] = useState(false)
  const [comments, setComments] = useState([])
  const isCurrentUserOwner = user && artwork.user_id === user.id

  useEffect(() => {
    fetch(`/artworks/${artwork.id}/comments`)
      .then((res) => res.json())
      .then((data) => setComments(data))
      .catch((err) => console.log(err))
  }, [])

  useEffect(() => {
    if (user && artwork.likes.some((like) => like.user_id === user.id)) {
      setLiked(true)
    }
  }, [user, artwork.likes])

  const handleLike = async () => {
    const likeEndpoint = `/artworks/${artwork.id}/likes`;
    const method = liked ? 'DELETE' : 'POST';
  
    try {
      const response = await fetch(likeEndpoint, {
        method: method,
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: user.id }),
      });
  
      if (response.ok) {
        setLiked(!liked);
        setLikeCount((count) => (liked ? count - 1 : count + 1));
      } else {
        console.error('Error liking/unliking artwork');
      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  }

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
                  content: likeCount.toString(),
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
          </>
  );
}

export default Actions;
