import React from 'react';
import MenuBar from './MenuBar';
import { Icon, Table, Button } from 'semantic-ui-react'

function Profile() {


  return (
    <div className='profile'>
    <MenuBar />
    <br/>
    <br/>
    <Table className='account-table' celled striped size='large'>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell colSpan='3'>
            My Account <Button icon='edit outline'/>
            </Table.HeaderCell>
        </Table.Row>
      </Table.Header>

      <Table.Body>
          <Table.Row>
            <Table.Cell collapsing>Full Name</Table.Cell>
            <Table.Cell></Table.Cell>
          </Table.Row>
          <Table.Row>
            <Table.Cell>Username</Table.Cell>
            <Table.Cell></Table.Cell>
          </Table.Row>
          <Table.Row>
            <Table.Cell>Email</Table.Cell>
            <Table.Cell></Table.Cell>
          </Table.Row>
          <Table.Row>
            <Table.Cell>Bio</Table.Cell>
            <Table.Cell></Table.Cell>
          </Table.Row>
          <Table.Row>
            <Table.Cell>Location</Table.Cell>
            <Table.Cell></Table.Cell>
          </Table.Row>
        </Table.Body>
    </Table>

    <Table className='transaction-table' columns={4} celled size='large'>
    <Table.Header>
      <Table.Row>
        <Table.HeaderCell colSpan='4'>Transactions</Table.HeaderCell>
      </Table.Row>
    </Table.Header>

    <Table.Body>
      <Table.Row>
        <Table.Cell>
          <Icon name='calendar alternate outline'/>
          Date
          </Table.Cell>
        <Table.Cell>
          <Icon name='paint brush'/>
          Artwork
          </Table.Cell>
        <Table.Cell>
          <Icon name='user outline'/>
          Seller
          </Table.Cell>
        <Table.Cell>
          <Icon name='dollar'/>
          Amount Paid
          </Table.Cell>
      </Table.Row>
      <Table.Row>
        <Table.Cell></Table.Cell>
        <Table.Cell></Table.Cell>
        <Table.Cell></Table.Cell>
        <Table.Cell></Table.Cell>
      </Table.Row>
    </Table.Body>
  </Table>
    </div>
  );
}

export default Profile