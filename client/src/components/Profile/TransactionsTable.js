import { useEffect, useState } from 'react'
import { Icon, Table } from 'semantic-ui-react'

function TransactionsTable({ user }) {
    const [transactions, setTransactions] = useState([])

    function formattedDate(date) {
        return new Date(date).toLocaleDateString('en-US', {
          year: '2-digit',
          month: '2-digit',
          day: '2-digit',
        })
      }

      useEffect(() => {
        fetch(`/users/${user.id}/transactions`)
          .then(res => res.json())
          .then(data => {
            setTransactions(data)
          })
          .catch(err => console.log(err))
      }, [user.id])

      const mappedTransactions = () => {
        return transactions.map(transaction => (
          <Table.Row key={transaction.id}>
            <Table.Cell>
              {formattedDate(transaction.created_at)}
            </Table.Cell>
            <Table.Cell>
              "{transaction.artwork.title}"
            </Table.Cell>
            <Table.Cell>
              {transaction.buyer_id === user.id ? 'Bought from' : 'Sold to'}:{' '}
              {transaction.buyer_id === user.id
                ? transaction.seller_id
                : transaction.buyer_id}
            </Table.Cell>
            <Table.Cell>
              ${transaction.amount_paid}
            </Table.Cell>
          </Table.Row>
        ))
      }


  return (
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
  )
}

export default TransactionsTable
