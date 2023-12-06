import React from 'react';
import MenuBar from './MenuBar';
import { Icon, Table } from 'semantic-ui-react'

function Profile() {


  return (
    <div className='profile'>
    <MenuBar />
    <Table className='account-table' celled striped size='large'>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell colSpan='3'>My Account</Table.HeaderCell>
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
        <Table.Cell>Date</Table.Cell>
        <Table.Cell>Artwork</Table.Cell>
        <Table.Cell>Seller</Table.Cell>
        <Table.Cell>Amount Paid</Table.Cell>
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