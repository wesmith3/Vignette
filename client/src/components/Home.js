import { useContext } from 'react'
import { AuthContext } from './AuthProvider'
import MenuBar from './MenuBar'

function Home() {
  const { user } = useContext(AuthContext);
  console.log(user)

  return (
    <div>
      <MenuBar />
    </div>
  )
}

export default Home
