import { useContext } from 'react'
import MenuBar from '../MenuBar'
import { AuthContext } from '../Helpers/AuthProvider'
import { Button, Image } from 'semantic-ui-react'
import TransactionsTable from './TransactionsTable'
import UserEditForm from './UserEditForm'

function Profile() {
  const { user } = useContext(AuthContext)

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
        <Button className='edit-image' icon='edit outline' circular size='tiny'/>
        <UserEditForm user={user}/>
      </div>

      <TransactionsTable user={user}/>
      <br />
      <br />
    </div>
  )
}

export default Profile
