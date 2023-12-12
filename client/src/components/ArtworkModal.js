import { useState, useContext, useEffect } from 'react'
import { Image, Modal, Card, Button, Icon } from 'semantic-ui-react'
import Avatar from '@mui/material/Avatar'
import { Link } from 'react-router-dom';
import { AuthContext } from './Helpers/AuthProvider'
import CommentSection from './CommentSection'

function ArtworkModal({ onClose, artwork, onDelete }) {
  const { user, users } = useContext(AuthContext)
  const [liked, setLiked] = useState(false)
  const [likeCount, setLikeCount] = useState(artwork.likes.length)
  const [showComments, setShowComments] = useState(false)
  const [isFollowing, setIsFollowing] = useState(false)
  const isCurrentUserOwner = user && artwork.user_id === user.id

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

  const handleFollow = async () => {
    // Implement logic to follow/unfollow the user
    // This will depend on your backend API and how you manage followers

    // Example:
    // Call your backend API to toggle follow status
    // Use setIsFollowing to update the state locally
    // You need to implement a corresponding API endpoint in your backend

    // const followEndpoint = `/users/${artwork.user.id}/follow`;
    // const method = isFollowing ? 'DELETE' : 'POST';
    // try {
    //   const response = await fetch(followEndpoint, {
    //     method: method,
    //     headers: {
    //       'Content-Type': 'application/json',
    //     },
    //     body: JSON.stringify({ user_id: user.id }),
    //   });
    //
    //   if (response.ok) {
    //     setIsFollowing(!isFollowing);
    //   } else {
    //     console.error('Error following/unfollowing user');
    //   }
    // } catch (error) {
    //   console.error('Fetch error:', error);
    // }
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
                  onClick={handleFollow}
                  content={isFollowing ? 'Following' : 'Follow'}
                  // style={{ marginLeft: '10px' }}
                />
            </div>
        </Card.Content>
          <Image src={artwork.image} wrapped ui={false} />
          <Card.Content>
            <Card.Header>{artwork.title}</Card.Header>
            <Card.Description>
              <p>
                {artwork.description}
              </p>
            <br />
              <p>
                <strong>Price:</strong> ${artwork.price}.00
              </p>
            </Card.Description>
            <br />
              <div>
              {artwork.tags.map((tag, index) => (
                <span key={index}><strong>#{tag.keyword}{index < artwork.tags.length - 1 ? ', ' : ''}</strong></span>
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
            <Button color='black' icon floated='right' labelPosition='left'>
              <Icon name='shopping bag' />
              Get Yours!
            </Button>
            {isCurrentUserOwner && (
              <Button color='red' icon floated='right' labelPosition='left' onClick={handleDelete}>
                <Icon name='trash' />
                Delete Artwork
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