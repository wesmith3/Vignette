import React from 'react'
import MenuBar from './MenuBar'
import { Image } from 'semantic-ui-react'

function Success() {
  return (
    <>
    <MenuBar />
    <br />
    <div className='success-message'>
    <Image src="../Success.jpg" size='medium' circular centered/>
    <h1>Thank you!</h1>
    <h1>Your payment was successful!</h1>
    <h3>Click <a href="/home">here</a> to enjoy more art</h3>
    </div>
    </>
  )
}

export default Success
