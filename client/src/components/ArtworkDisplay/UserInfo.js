import { useEffect, useContext, useState } from 'react';
import { AuthContext } from '../Helpers/AuthProvider'
import { Button } from 'semantic-ui-react';
import Avatar from '@mui/material/Avatar';
import { Link } from 'react-router-dom';

function UserInfo({ artwork, user }) {
  const { following, setFollowing } = useContext(AuthContext)
  const [isFollowing, setIsFollowing] = useState(false)
  const isCurrentUser = user?.id === artwork.user_id;

  useEffect(() => {
    following.includes(artwork.user_id) && user.id !== artwork.user_id
      ? setIsFollowing(true)
      : setIsFollowing(false);
  }, [user, following, artwork.user_id]);
  
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
        const responseData = await response.json();
        setFollowing((prev) => [...prev, responseData.following_id]);
      } else {
        console.error('Failed to follow user');
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
        setFollowing((prevFollowing) =>
          prevFollowing.filter((id) => id !== followingId)
        );
      } else {
        console.error('Failed to unfollow user');
      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };
  

  return (
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <Avatar alt={artwork.user.full_name} src={artwork.user.profile_image} size='large' />
      <div
        style={{
          marginLeft: '10px',
          fontSize: '1.5em',
          display: 'flex',
          alignItems: 'center',
        }}
      >
        <Link to={`/${artwork.user.username}`}>
          <strong>@{artwork.user.username}</strong>
        </Link>
      </div>
      {isCurrentUser ? (
          null
        ) : (
          <Button
            color={isFollowing ? 'green' : 'blue'}
            icon={isFollowing ? 'check' : 'plus'}
            labelPosition='right'
            floated='right'
            onClick={() =>
              isFollowing ? handleUnfollow(artwork.user_id) : handleFollow(artwork.user_id)
            }
            content={isFollowing ? 'Following' : 'Follow'}
          />
        )}
    </div>
  );
}

export default UserInfo;
