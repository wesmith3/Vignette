import React from 'react'
import { Grid, Image, Form, Button, Message, Input, TextArea, Segment } from 'semantic-ui-react'
import { Formik } from 'formik'
import * as yup from 'yup'
function SignUp() {
    const background = "././Gallery.jpg"

    const signUpSchema = yup.object().shape({
        full_name: yup.string()
            .min(5, "Full name must be at least 5 chars long")
            .min(150, "Full name must be less than 150 chars long")
            .required("Full Name is required"),
        username: yup.string(),
        email: yup.string(),
        password: yup.string(),
    })

  return (
    <Grid textAlign='center' style={{ height: '105vh', backgroundImage: `url(${background})`, backgroundSize: 'cover', backgroundPosition: 'center'}} verticalAlign='middle'>
        <Grid.Column style={{ maxWidth: 450 }}>
            <Image src='././Logo.png' size='large'/>
            <br />
            <Form>
                <Segment>
                <Form.Group widths='two'>
                <Form.Field
                    id='full_name'
                    name='full_name'
                    icon='user'
                    iconPosition='left'
                    control={Input}
                    label='Full Name *'
                    placeholder='Full Name'
                    />
                <Form.Field
                    id='username'
                    name='username'
                    icon='user circle'
                    iconPosition='left'
                    control={Input}
                    label='Username *'
                    placeholder='Username'
                    />
                </Form.Group>
                <Form.Field
                    id='email'
                    name='email'
                    icon='mail'
                    iconPosition='left'
                    control={Input}
                    label='Email *'
                    placeholder='joe@schmoe.com'
                />
                <Form.Group widths='two'>
                <Form.Field
                    id='password'
                    name='password'
                    icon='lock'
                    iconPosition='left'
                    control={Input}
                    label='Password *'
                    placeholder='Password'
                    />
                <Form.Field
                    id='location'
                    name='location'
                    icon='location arrow'
                    iconPosition='left'
                    control={Input}
                    label='Location'
                    placeholder='Seattle, WA'
                    />
                </Form.Group>
                <Form.Field
                    id='bio'
                    name='bio'
                    control={TextArea}
                    label='Bio'
                    placeholder='Tell us about yourself...'
                />
                <Form.Field
                    fluid
                    size='large'
                    id='signup-btn'
                    control={Button}
                    content='Sign Up'
                    color='black'
                />
                </Segment>
            </Form>
            <Message>
                Already have an account? <a href='/login'>Click Here</a>
            </Message>
        </Grid.Column>
    </Grid>
  )
}

export default SignUp