import React, { useState, useContext } from 'react'
import { Comment, Header, Form, Button } from 'semantic-ui-react'
import { formatDistanceToNow } from 'date-fns'
import { AuthContext } from './Helpers/AuthProvider'

function CommentSection({ artwork, users, onUpdateComments }) {
  const { user } = useContext(AuthContext)
  const [newComment, setNewComment] = useState('')

  const handleAddComment = async () => {
    try {
      const response = await fetch(`/artworks/${artwork.id}/comments`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_id: user.id, content: newComment }),
      })

      if (response.ok) {
        const updatedArtwork = await response.json()
        onUpdateComments(updatedArtwork.comments)
        setNewComment('')
      } else {
        console.error('Error adding comment')
      }
    } catch (error) {
      console.error('Fetch error:', error)
    }
  }

  const handleDeleteComment = async (commentId) => {
    try {
      const response = await fetch(`/comments/${commentId}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
      })

      if (response.ok) {
        // Fetch updated artwork data or update state accordingly
        onUpdateComments(artwork.comments.filter((comment) => comment.id !== commentId))
      } else {
        console.error('Error deleting comment')
      }
    } catch (error) {
      console.error('Fetch error:', error)
    }
  }

  const renderComments = () => {
    return (
      <Comment.Group>
        <Header as='h3' dividing>
          Comments
        </Header>
        {artwork.comments.map((comment) => {
          const commentUser = users.find((u) => u.id === comment.user_id)

          return (
            <Comment key={comment.id}>
              <Comment.Avatar src={commentUser ? commentUser.profile_image : ''} />
              <Comment.Content>
                <Comment.Author as='a'>@{commentUser ? commentUser.username : 'Unknown User'}</Comment.Author>
                <Comment.Metadata>
                  <div>{formatDistanceToNow(new Date(comment.created_at), { addSuffix: true })}</div>
                </Comment.Metadata>
                <Comment.Text>{comment.content}</Comment.Text>
                {user && user.id === comment.user_id && (
                  <Comment.Actions>
                    <Comment.Action onClick={() => handleDeleteComment(comment.id)}>Delete</Comment.Action>
                  </Comment.Actions>
                )}
              </Comment.Content>
            </Comment>
          )
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
    )
  }

  return <>{renderComments()}</>
}

export default CommentSection
