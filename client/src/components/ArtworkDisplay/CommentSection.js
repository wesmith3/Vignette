import { useState, useContext } from 'react';
import { Comment, Header, Form, Button } from 'semantic-ui-react';
import { AuthContext } from '../Helpers/AuthProvider';
import Avatar from '@mui/material/Avatar';

function CommentSection({ artwork, users, comments, setComments }) {
  const { user } = useContext(AuthContext);
  const [newComment, setNewComment] = useState('');


  const handleAddComment = async () => {
    try {
      const response = await fetch(`/artworks/${artwork.id}/comments`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: user.id, content: newComment }),
      });

      if (response.ok) {
        const newCommentData = await response.json();
        setComments([...comments, newCommentData]);
        setNewComment('')
      } else {
        console.error('Error adding comment');
      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  const handleDeleteComment = async (commentId) => {
    try {
      const response = await fetch(`/comments/${commentId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      });

      if (response.ok) {
        const updatedComments = comments.filter((comment) => comment.id !== commentId);
        setComments(updatedComments)
      } else {
        console.error('Error deleting comment');
      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  const renderComments = () => {
    return (
      <Comment.Group>
        <Header as='h3' dividing>
          Comments
        </Header>
        {comments.map((comment) => {
          const commentUser = users.find((u) => u.id === comment.user_id);

          return (
            <Comment key={comment.id}>
              <Avatar alt={commentUser.full_name} src={commentUser.profile_image} />
              <Comment.Content>
                <Comment.Author as='a'>@{commentUser ? commentUser.username : 'Unknown User'}</Comment.Author>
                <Comment.Text>{comment.content}</Comment.Text>
                {user && user.id === comment.user_id && (
                  <Comment.Actions>
                    <Comment.Action onClick={() => handleDeleteComment(comment.id)}>Delete</Comment.Action>
                  </Comment.Actions>
                )}
              </Comment.Content>
            </Comment>
          );
        })}
        <Form reply>
          <Form.TextArea
            style={{ maxHeight: '40px' }}
            value={newComment}
            onChange={(e) => setNewComment(e.target.value)}
          />
          <Button content='Add Comment' labelPosition='left' size='small' icon='edit' primary onClick={handleAddComment} />
        </Form>
      </Comment.Group>
    );
  };

  return <>{renderComments()}</>;
}

export default CommentSection;

