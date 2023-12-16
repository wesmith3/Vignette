import { useState, useEffect } from 'react';
import { Button, Icon } from 'semantic-ui-react'
import CommentSection from './CommentSection';

function Actions({ artwork, user, users, setIsEditing, onDelete, onClose }) {
  const [liked, setLiked] = useState(false);
  const [likes, setLikes] = useState([]);
  const [showComments, setShowComments] = useState(false);
  const [comments, setComments] = useState([]);
  const [loadingLikes, setLoadingLikes] = useState(true);
  const [loadingComments, setLoadingComments] = useState(true);
  const isCurrentUserOwner = user && artwork.user_id === user.id;

  useEffect(() => {
    const fetchComments = async () => {
      try {
        const res = await fetch(`/artworks/${artwork.id}/comments`);
        const data = await res.json();
        setComments(data);
      } catch (error) {
        console.log('Error fetching comments:', error);
      } finally {
        setLoadingComments(false);
      }
    };

    if (showComments && loadingComments) {
      fetchComments();
    }
  }, [artwork.id, showComments, loadingComments]);

  useEffect(() => {
    const fetchLikes = async () => {
      try {
        const res = await fetch(`/artworks/${artwork.id}/likes`);
        const data = await res.json();
        setLikes(data);
  
        // Set liked based on whether the current user has already liked the artwork
        if (user && data.some((like) => like.user_id === user.id)) {
          setLiked(true);
        }
      } catch (error) {
        console.log('Error fetching likes:', error);
      } finally {
        setLoadingLikes(false);
      }
    };
  
    fetchLikes();
  }, [artwork.id, user]);

  const handleLike = async () => {
    const likeEndpoint = `/artworks/${artwork.id}/likes`;
    const method = liked ? 'DELETE' : 'POST';

    try {
      // Optimistic update
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
        // Revert changes on failure
        setLiked(liked);
        setLikes((count) => (liked ? count + 1 : count - 1));
        console.error('Error liking/unliking artwork');
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
                  content: loadingLikes ? '...' : likes.length,
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
