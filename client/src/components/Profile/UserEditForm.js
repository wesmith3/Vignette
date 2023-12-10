import { Table, Input, Button } from 'semantic-ui-react'
import { useState } from 'react'

function UserEditForm({ user }) {
    const [editMode, setEditMode] = useState(false)
    const [editedUser, setEditedUser] = useState({ ...user });

    function formattedDate(date) {
        return new Date(date).toLocaleDateString('en-US', {
          year: '2-digit',
          month: '2-digit',
          day: '2-digit',
        })
      }
    
    
      const handleEditClick = () => {
        setEditMode(true);
      };
    
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
            setEditMode(false);
          } else {
            console.error('Update unsuccessful');
          }
        } catch (error) {
          console.error(error);
        }
      };
    
      const handleCancelClick = () => {
        setEditMode(false);
        setEditedUser({ ...user });
      };
    
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
        );
      };
    
      const mappedUserInfoRows = () => {
        if (editMode) {
          // Render editable form fields when in edit mode
          return (
            <>
              <Table.Row>
                <Table.Cell className='table-header' collapsing>
                  Full Name
                </Table.Cell>
                <Table.Cell>
                  <Input defaultValue={user.full_name} />
                </Table.Cell>
              </Table.Row>
              <Table.Row>
                <Table.Cell className='table-header' collapsing>
                  Username
                </Table.Cell>
                <Table.Cell>
                  <Input defaultValue={user.username} />
                </Table.Cell>
              </Table.Row>
              <Table.Row>
                <Table.Cell className='table-header' collapsing>
                  Email
                </Table.Cell>
                <Table.Cell>
                  <Input defaultValue={user.email} />
                </Table.Cell>
              </Table.Row>
              <Table.Row>
                <Table.Cell className='table-header' collapsing>
                  Bio
                </Table.Cell>
                <Table.Cell>
                  <Input defaultValue={user.bio} />
                </Table.Cell>
              </Table.Row>
              <Table.Row>
                <Table.Cell className='table-header' collapsing>
                  Based In
                </Table.Cell>
                <Table.Cell>
                  <Input defaultValue={user.location} />
                </Table.Cell>
              </Table.Row>
              
            </>
          )
        } else {
          
          return (
            <>
              <Table.Row>
                  <Table.Cell className='table-header' collapsing>
                    Full Name
                    </Table.Cell>
                  <Table.Cell>{user.full_name}</Table.Cell>
                </Table.Row>
                <Table.Row>
                  <Table.Cell className='table-header'>
                    Username
                    </Table.Cell>
                  <Table.Cell>{user.username}</Table.Cell>
                </Table.Row>
                <Table.Row>
                  <Table.Cell className='table-header'>
                    Email
                    </Table.Cell>
                  <Table.Cell>{user.email}</Table.Cell>
                </Table.Row>
                <Table.Row>
                  <Table.Cell className='table-header'>
                    Bio
                    </Table.Cell>
                  <Table.Cell>{user.bio}</Table.Cell>
                </Table.Row>
                <Table.Row>
                  <Table.Cell className='table-header'>
                    Based In
                    </Table.Cell>
                  <Table.Cell>{user.location}</Table.Cell>
                </Table.Row>
                <Table.Row>
                  <Table.Cell className='table-header'>
                    Joined
                    </Table.Cell>
                  <Table.Cell>{formattedDate(user.created_at)}</Table.Cell>
                </Table.Row>
            </>
          )
        }
      }

  return (
    <Table className='account-table' celled striped size='large'>
          <Table.Header>
            <Table.Row>
              <Table.HeaderCell colSpan='2'>
                My Account {renderEditButton()}
              </Table.HeaderCell>
            </Table.Row>
          </Table.Header>

          <Table.Body>{mappedUserInfoRows()}</Table.Body>
        </Table>
  )
}

export default UserEditForm
