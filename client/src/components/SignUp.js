import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import { Button, Form, Grid, Image, Message, Segment } from 'semantic-ui-react'
import { Formik } from 'formik'
import * as yup from 'yup'
import AlertBar from './Helpers/AlertBar'

function SignUp() {
  const navigate = useNavigate()
  const background = '././Gallery.jpg'
  const [alertMessage, setAlertMessage] = useState(null)
  const [snackType, setSnackType] = useState('')

  const signUpSchema = yup.object().shape({
    full_name: yup.string().min(5, 'Full name must be at least 5 characters long').max(150, 'Full name must be less than 150 characters long').required('Full Name is required'),
    username: yup.string().required('Username is required'),
    email: yup.string().email('Invalid email').required('Email is required'),
    password: yup.string().required('Password is required').min(5),
    location: yup.string(),
    bio: yup.string(),
  })

  const initialValues = {
    full_name: '',
    username: '',
    email: '',
    password: '',
    location: '',
    bio: '',
    profile_image: ''
  }

  const handleSubmit = async (values, { setSubmitting, setErrors }) => {
    try {
      await signUpSchema.validate(values, { abortEarly: false })

      const response = await fetch('/signup', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(values),
      })

      if (response.ok) {
        const userData = await response.json()
        
        console.log('User registered successfully:', userData)

        navigate('/')
      } else {
        const errorData = await response.json()
        console.error('Error from server:', errorData)
        setAlertMessage(errorData.message || 'Failed to register user.')
        setSnackType('error')
      }
    } catch (errors) {
      console.error('Validation errors:', errors.errors)
      setErrors(errors.errors.reduce((acc, error) => ({ ...acc, [error.path]: error.message }), {}))
      setAlertMessage('Please fix the highlighted fields.')
      setSnackType('error')
    } finally {
      setSubmitting(false)
    }
  }

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
        <Image src="././Logo.png" size="large" />
        <br />
        <Formik
          initialValues={initialValues}
          validationSchema={signUpSchema}
          onSubmit={handleSubmit}
        >
          {(formikProps) => (
            <Form onSubmit={formikProps.handleSubmit} id="formikSignUp" size="large">
              <Segment stacked>
                <Form.Group widths="two">
                  <Form.Input
                    fluid
                    id="full_name"
                    type="text"
                    icon="user"
                    iconPosition="left"
                    placeholder="Full Name"
                    onChange={formikProps.handleChange}
                    onBlur={formikProps.handleBlur}
                    value={formikProps.values.full_name}
                    error={formikProps.touched.full_name && formikProps.errors.full_name ? { content: formikProps.errors.full_name } : null}
                  />
                  <Form.Input
                    fluid
                    id="username"
                    type="text"
                    icon="user circle"
                    iconPosition="left"
                    placeholder="Username"
                    onChange={formikProps.handleChange}
                    onBlur={formikProps.handleBlur}
                    value={formikProps.values.username}
                    error={formikProps.touched.username && formikProps.errors.username ? { content: formikProps.errors.username } : null}
                  />
                </Form.Group>
                <Form.Input
                  fluid
                  id="email"
                  type="text"
                  icon="mail"
                  iconPosition="left"
                  placeholder="E-mail address"
                  onChange={formikProps.handleChange}
                  onBlur={formikProps.handleBlur}
                  value={formikProps.values.email}
                  error={formikProps.touched.email && formikProps.errors.email ? { content: formikProps.errors.email } : null}
                />
                <Form.Group widths="two">
                  <Form.Input
                    fluid
                    icon="lock"
                    id="password"
                    iconPosition="left"
                    placeholder="Password"
                    type="password"
                    onChange={formikProps.handleChange}
                    onBlur={formikProps.handleBlur}
                    value={formikProps.values.password}
                    error={formikProps.touched.password && formikProps.errors.password ? { content: formikProps.errors.password } : null}
                  />
                  <Form.Input
                    fluid
                    icon="location arrow"
                    id="location"
                    iconPosition="left"
                    placeholder="Location"
                    onChange={formikProps.handleChange}
                    onBlur={formikProps.handleBlur}
                    value={formikProps.values.location}
                    error={formikProps.touched.location && formikProps.errors.location ? { content: formikProps.errors.location } : null}
                  />
                </Form.Group>
                <Form.TextArea
                  id="bio"
                  control={Form.TextArea}
                  label="Bio"
                  placeholder="Tell us about yourself..."
                  onChange={formikProps.handleChange}
                  onBlur={formikProps.handleBlur}
                  value={formikProps.values.bio}
                  error={formikProps.touched.bio && formikProps.errors.bio ? { content: formikProps.errors.bio } : null}
                />
                <Button type="submit" color="black" fluid size="large">
                  Sign Up
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
          )}
        </Formik>
        <Message>
          Already have an account? <a href="/login">Click Here</a>
        </Message>
      </Grid.Column>
    </Grid>
  )
}

export default SignUp
