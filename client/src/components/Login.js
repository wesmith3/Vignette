import React from 'react'
import { Button, Form, Grid, Image, Message, Segment } from 'semantic-ui-react'

function Login() {
    const background = "././Gallery.jpg"


  return (
    <Grid textAlign='center' style={{ height: '105vh', backgroundImage: `url(${background})`, backgroundSize: 'cover', backgroundPosition: 'center'}} verticalAlign='middle'>
        <Grid.Column style={{ maxWidth: 450 }}>
            <Image src='././Logo.png' size='massive'/>
            <br />
            <Form size='large'>
                <Segment stacked>
                    <Form.Input
                        fluid
                        icon='user'
                        iconPosition='left'
                        placeholder='E-mail address'
                    />
                    <Form.Input
                        fluid
                        icon='lock'
                        iconPosition='left'
                        placeholder='Password'
                        type='password'
                    />
                    <Button color='black' fluid size='large'>
                        Login
                    </Button>
                </Segment>
            </Form>
            <Message>
                New to us? <a href="/signup">Sign Up</a>
            </Message>
        </Grid.Column>
    </Grid>
  )
}

export default Login

