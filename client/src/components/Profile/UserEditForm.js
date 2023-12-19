import { useState } from 'react'
import { Table, Input, Button } from 'semantic-ui-react'

function UserEditForm({ user, setUser }) {
  const [editMode, setEditMode] = useState(false)
  const [editedUser, setEditedUser] = useState({ ...user })

  const formattedDate = (date) => {
    return new Date(date).toLocaleDateString('en-US', {
      year: '2-digit',
      month: '2-digit',
      day: '2-digit',
    })
  }

  const handleEditClick = () => {
    setEditMode(true)
  }

  const handleSaveClick = async () => {
    try {
      const { id, created_at, ...updatedUserData } = editedUser;

      const response = await fetch(`/users/${user.id}`, {
        method: 'PATCH',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedUserData),
      });

      if (response.ok) {
        setUser(editedUser)
        setEditMode(false)
      } else {
        console.error('Update unsuccessful');
      }
    } catch (error) {
      console.error(error);
    }
  };

  const handleCancelClick = () => {
    setEditMode(false)
    setEditedUser({ ...user })
  }

  const handleInputChange = (field, value) => {
    setEditedUser((prevUser) => ({
      ...prevUser,
      [field]: value,
    }))
  }

  const renderEditButton = () => {
    return (
      <Button.Group>
        {editMode ? (
          <>
            <Button positive icon='check' onClick={handleSaveClick} />
            <Button.Or />
            <Button negative icon='close' onClick={handleCancelClick} />
          </>
        ) : (
          <Button icon='edit outline' onClick={handleEditClick} />
        )}
      </Button.Group>
    )
  }

  const renderUserInfoRows = () => {
    const userInfoFields = ['full_name', 'username', 'email', 'bio', 'location']

    return userInfoFields.map((field) => (
      <Table.Row key={field}>
        <Table.Cell className='table-header' collapsing>
          {field === 'full_name' ? 'Full Name' : field.charAt(0).toUpperCase() + field.slice(1)}
        </Table.Cell>
        <Table.Cell>
          {editMode ? (
            <Input
              value={editedUser[field]}
              onChange={(e) => handleInputChange(field, e.target.value)}
            />
          ) : (
            user[field]
          )}
        </Table.Cell>
      </Table.Row>
    ))
  }

  const renderJoinedRow = () => {
    return (
      <Table.Row>
        <Table.Cell className='table-header'>Joined</Table.Cell>
        <Table.Cell>{formattedDate(user.created_at)}</Table.Cell>
      </Table.Row>
    )
  }

  return (
    <Table className='account-table' celled striped size='large'>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell colSpan='2'>My Account {renderEditButton()}</Table.HeaderCell>
        </Table.Row>
      </Table.Header>

      <Table.Body>
        {renderUserInfoRows()}
        {!editMode && renderJoinedRow()}
      </Table.Body>
    </Table>
  )
}

export default UserEditForm
