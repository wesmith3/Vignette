import { useState } from 'react'
import { useNavigate } from 'react-router-dom';
import { Button, Form, Grid, Image, Message, Segment } from 'semantic-ui-react'
import { useFormik } from "formik";
import * as yup from "yup";
import AlertBar from './AlertBar'

function Login() {
  const navigate = useNavigate()
    const background = "././Gallery.jpg"
    const [alertMessage, setAlertMessage] = useState(null);
    const [snackType, setSnackType] = useState('');

  const formSchema = yup.object().shape({
    email: yup.string().email('Invalid email').required("Please enter an email."),
    password: yup.string().required("Please enter a password.").min(5)
  })
  
  const formik = useFormik({
    initialValues: {
      email: '',
      password: ''
    },
    validationSchema: formSchema,
    onSubmit: (values) => {
      fetch('/login', {
        method: 'POST',
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(values),
      })
      .then((res) => {
        if (res.status === 200) {
          navigate('/') 
        } else {
          setAlertMessage('Invalid user credentials.');
          setSnackType('error');
        }
      })
    }
  })


  return (
    <Grid textAlign='center' style={{ height: '105vh', backgroundImage: `url(${background})`, backgroundSize: 'cover', backgroundPosition: 'center'}} verticalAlign='middle'>
        <Grid.Column style={{ maxWidth: 450 }}>
            <Image src='././Logo.png' size='massive'/>
            <br />
            <Form onSubmit={formik.handleSubmit} id='formikLogin' size='large'>
                <Segment stacked>
                    <Form.Input
                        fluid
                        id='email'
                        type='text'
                        icon='user'
                        iconPosition='left'
                        placeholder='E-mail address'
                        onChange={formik.handleChange}
                        value={formik.values.email}
                    />
                    <Form.Input
                        fluid
                        icon='lock'
                        id='password'
                        iconPosition='left'
                        placeholder='Password'
                        type='password'
                        onChange={formik.handleChange}
                        value={formik.values.password}
                    />
                    <Button type='submit' color='black' fluid size='large'>
                        Login
                    </Button>
                    {alertMessage && (
                      <AlertBar
                        message={alertMessage}
                        setAlertMessage={setAlertMessage}
                        snackType={snackType}
                        handleSnackType={setSnackType}
                      />
                    )}
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