import { useState, useContext } from 'react'
import { useNavigate } from 'react-router-dom'
import { Button, Form, Grid, Image, Message, Segment } from 'semantic-ui-react'
import { useFormik } from 'formik'
import * as yup from 'yup'
import AlertBar from './Helpers/AlertBar'
import { AuthContext } from './Helpers/AuthProvider'

function Login({ onLogin }) {
  const navigate = useNavigate()
  const background = '././Gallery.jpg'
  const [alertMessage, setAlertMessage] = useState(null)
  const [snackType, setSnackType] = useState('')
  const { login } = useContext(AuthContext)

  const formSchema = yup.object().shape({
    email: yup.string().email('Invalid email').required('Please enter an email.'),
    _password: yup.string().required('Please enter a password.').min(5),
  })

  const formik = useFormik({
    initialValues: {
      email: '',
      _password: '',
    },
    validationSchema: formSchema,
    onSubmit: async (values) => {
      try {
        const response = await fetch('/login', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(values),
        })

        if (response.ok) {
          const userData = await response.json()
          onLogin(userData)
          login(userData)
          navigate('/loading')
        } else {
          const errorData = await response.json()
          console.error('Error from server:', errorData)
          setAlertMessage(errorData.message || 'Invalid user credentials.')
          setSnackType('error')
        }
      } catch (error) {
        console.error(error.message)
        setAlertMessage('An unexpected error occurred.')
        setSnackType('error')
      }
    },
  })

  return (
    <Grid
      textAlign="center"
      style={{
        height: '105vh',
        backgroundImage: `url(${background})`,
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      }}
      verticalAlign="middle"
    >
      <Grid.Column style={{ maxWidth: 450 }}>
        <Image src="././Logo.png" size="massive" />
        <br />
        <Form onSubmit={formik.handleSubmit} id="formikLogin" size="large">
          <Segment stacked>
            <Form.Input
              fluid
              id="email"
              type="text"
              icon="user"
              iconPosition="left"
              placeholder="E-mail address"
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              value={formik.values.email}
              error={formik.touched.email && formik.errors.email ? { content: formik.errors.email } : null}
            />
            <Form.Input
              fluid
              icon="lock"
              id="_password"
              iconPosition="left"
              placeholder="Password"
              type="password"
              onChange={formik.handleChange}
              onBlur={formik.handleBlur}
              value={formik.values._password}
              error={
                formik.touched._password && formik.errors._password
                  ? { content: formik.errors._password }
                  : null
              }
            />
            <Button type="submit" color="black" fluid size="large">
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