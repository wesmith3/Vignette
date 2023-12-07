import { useContext, useEffect, useState } from 'react';
import MenuBar from './MenuBar';
import { AuthContext } from './AuthProvider';
import { Icon, Table, Button, Image } from 'semantic-ui-react';
import Badge from '@mui/material/Badge';
import NotificationsIcon from '@mui/icons-material/Notifications';

function Profile() {
  const { user } = useContext(AuthContext);
  const [transactions, setTransactions] = useState([]);

  function formattedDate(date) {
    return new Date(date).toLocaleDateString('en-US', {
      year: '2-digit',
      month: '2-digit',
      day: '2-digit',
    });
  }

  useEffect(() => {
    fetch(`/users/${user.id}/transactions`)
      .then(res => res.json())
      .then(data => {
        setTransactions(data);
      })
      .catch(err => console.log(err));
  }, [user.id]);

  const mappedTransactions = () => {
    return transactions.map(transaction => (
      <Table.Row key={transaction.id}>
        <Table.Cell>
          {formattedDate(transaction.created_at)}
        </Table.Cell>
        <Table.Cell>
          {transaction.artwork_id}
        </Table.Cell>
        <Table.Cell>
          {transaction.buyer_id === user.id ? 'Bought from' : 'Sold to'}:{' '}
          {transaction.buyer_id === user.id
            ? transaction.seller_id
            : transaction.buyer_id}
        </Table.Cell>
        <Table.Cell>
          {transaction.amount_paid}
        </Table.Cell>
      </Table.Row>
    ));
  };

  return (
    <div className='profile'>
      <MenuBar />
      <br />
      <br />
      <div
        style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
        }}
      >
          <Image src={user.profile_image} className='account-image' alt='Profile' size='medium' circular>
          </Image>
            <Button icon='edit outline' circular size='tiny'/>
        <Table className='account-table' celled striped size='large'>
          <Table.Header>
            <Table.Row>
              <Table.HeaderCell colSpan='2'>
                My Account <Button icon='edit outline' />
              </Table.HeaderCell>
            </Table.Row>
          </Table.Header>

          <Table.Body>
            <Table.Row>
              <Table.Cell className='table-header' collapsing>Full Name</Table.Cell>
              <Table.Cell>{user.full_name}</Table.Cell>
            </Table.Row>
            <Table.Row>
              <Table.Cell className='table-header'>Username</Table.Cell>
              <Table.Cell>{user.username}</Table.Cell>
            </Table.Row>
            <Table.Row>
              <Table.Cell className='table-header'>Email</Table.Cell>
              <Table.Cell>{user.email}</Table.Cell>
            </Table.Row>
            <Table.Row>
              <Table.Cell className='table-header'>Bio</Table.Cell>
              <Table.Cell>{user.bio}</Table.Cell>
            </Table.Row>
            <Table.Row>
              <Table.Cell className='table-header'>Based In</Table.Cell>
              <Table.Cell>{user.location}</Table.Cell>
            </Table.Row>
            <Table.Row>
              <Table.Cell className='table-header'>Joined</Table.Cell>
              <Table.Cell>{formattedDate(user.created_at)}</Table.Cell>
            </Table.Row>
          </Table.Body>
        </Table>
      </div>

      <Table className='transaction-table' columns={4} celled size='large'>
        <Table.Header>
          <Table.Row>
            <Table.HeaderCell>
              <Icon name='calendar alternate outline' />
              Date
            </Table.HeaderCell>
            <Table.HeaderCell>
              <Icon name='paint brush' />
              Artwork
            </Table.HeaderCell>
            <Table.HeaderCell>
              <Icon name='user outline' />
              Buyer/Seller
            </Table.HeaderCell>
            <Table.HeaderCell>
              <Icon name='dollar' />
              Amount Paid
            </Table.HeaderCell>
          </Table.Row>
        </Table.Header>

        <Table.Body>{mappedTransactions()}</Table.Body>
      </Table>
      <br />
      <br />
    </div>
  );
}

export default Profile;