import { useContext } from 'react'
import { AuthContext } from './Helpers/AuthProvider'
import MenuBar from './MenuBar'
import Gallery from './Gallery'

function Home() {
  const { artworks } = useContext(AuthContext);

  return (
    <>
      <MenuBar />
      <br />
      <Gallery artworks={artworks}/>
    </>
  )
}

export default Home
