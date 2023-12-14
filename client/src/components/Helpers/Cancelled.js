import React from 'react'
import MenuBar from './MenuBar'
import { Image } from 'semantic-ui-react'

function Cancelled() {
  return (
    <>
    <MenuBar />
    <br />
    <div className='cancel-message'>
    <Image src="../Cancelled.png" size='medium' centered/>
    <br />
    <h1>Oh no! Something went wrong!</h1>
    <h1>Your payment was cancelled!</h1>
    <h3>Click <a href="/home">here</a> to enjoy more art</h3>
    </div>
    </>
  )
}

export default Cancelled
