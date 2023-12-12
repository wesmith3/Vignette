import { useState, useContext, useEffect } from 'react'
import { Image, Modal, Card, Button, Icon } from 'semantic-ui-react'
import Avatar from '@mui/material/Avatar'
import { Link } from 'react-router-dom';
import { AuthContext } from './Helpers/AuthProvider'
import CommentSection from './CommentSection'

function ArtworkModal({ onClose, artwork, onDelete }) {
  const { user, users, setCart, cart } = useContext(AuthContext);
  const [liked, setLiked] = useState(false);
  const [likeCount, setLikeCount] = useState(artwork.likes.length);
  const [showComments, setShowComments] = useState(false);
  const [isFollowing, setIsFollowing] = useState(false);
  const [isInCart, setIsInCart] = useState(false);
  const isCurrentUserOwner = user && artwork.user_id === user.id;

  const handleDelete = async () => {
    try {
      onClose()
      onDelete(artwork.id)
    } catch (error) {
      console.error('Error deleting artwork from modal:', error)
    }
  }

  useEffect(() => {
    if (user && artwork.likes.some((like) => like.user_id === user.id)) {
      setLiked(true)
    }
  }, [user, artwork.likes])

  const handleLike = async () => {
    const likeEndpoint = `/artworks/${artwork.id}/likes`
    const method = liked ? 'DELETE' : 'POST'

    try {
      const response = await fetch(likeEndpoint, {
        method: method,
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: user.id }),
      })

      if (response.ok) {
        setLiked(!liked)
        setLikeCount((count) => (liked ? count - 1 : count + 1))
      } else {
        console.error('Error liking/unliking artwork')
      }
    } catch (error) {
      console.error('Fetch error:', error)
    }
  }

  useEffect(() => {
    if (user && artwork.user.followers.some((follower) => follower.id === user.id)) {
      setIsFollowing(true);
    }
  }, [user, artwork.user.followers]);

  const handleAddToCart = () => {
    if (!isInCart) {
      setCart((prevCart) => {
        const currentCart = Array.isArray(prevCart) ? prevCart : [];
        return [...currentCart, artwork];
      });
      setIsInCart(true);
    }
  };

  const handleFollow = async (followingId) => {
    try {
      const response = await fetch(`/users/${user.id}/following`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ following_id: followingId }),
      });
  
      if (response.ok) {
        setIsFollowing(true)
      } else {
        // Handle error in following
        console.error('Error following user:', response.statusText);
      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  const handleUnfollow = async (followingId) => {
    try {
      const response = await fetch(`/users/${user.id}/follow`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ following_id: followingId }),
      });
  
      if (response.ok) {
        setIsFollowing(false)
      } else {
        console.error('Error unfollowing user:', response.statusText);
      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };
  
  

  return (
    <Modal onClose={onClose} open={true} className='artwork-modal' size='small' dimmer='blurring'>
  <Modal.Content>
    <Card fluid>
      <Card.Content>
        <div style={{ display: 'flex', alignItems: 'center' }}>
          <Avatar alt={user.full_name} src={artwork.user.profile_image} size='large' />
          <div style={{ marginLeft: '10px', fontSize: '1.5em', display: 'flex', alignItems: 'center' }}>
            <Link to={`/profile/${artwork.user.username}`}>
              <strong>@{artwork.user.username}</strong>
            </Link>
          </div>
          <Button
            color={isFollowing ? 'green' : 'blue'}
            icon={isFollowing ? 'check' : 'plus'}
            labelPosition='right'
            floated='right'
            onClick={() => (isFollowing ? handleUnfollow(artwork.user_id) : handleFollow(artwork.user_id))}
            content={isFollowing ? 'Following' : 'Follow'}
          />
        </div>
      </Card.Content>
      <Image src={artwork.image} wrapped ui={false} />
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
        {isCurrentUserOwner ? (
              <Button color='red' icon floated='right' labelPosition='left' onClick={handleDelete}>
                <Icon name='trash' />
                Delete Artwork
              </Button>
            ) : (
              <Button
                color={isInCart ? 'green' : 'black'}
                icon
                floated='right'
                labelPosition='left'
                onClick={handleAddToCart}
              >
                <Icon name={isInCart ? 'check' : 'shopping bag'} />
                {isInCart ? 'Added to Cart' : 'Add to Cart'}
              </Button>
            )}
        {showComments && <CommentSection artwork={artwork} users={users} />}
      </Card.Content>
    </Card>
  </Modal.Content>
</Modal>
  )
}

export default ArtworkModal