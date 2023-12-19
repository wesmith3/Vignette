import React from 'react';
import { Field, ErrorMessage, Formik, Form } from 'formik';
import { Button, Form as SemanticForm, Input, TextArea, Checkbox } from 'semantic-ui-react';
import * as Yup from 'yup';

const ArtworkForm = ({ onSubmit, onCancel }) => {
  const initialValues = {
    title: '',
    description: '',
    image: '',
    tags: '',
    price: '',
    preview: false,
  };

  const validationSchema = Yup.object({
    title: Yup.string().required('Title is required'),
    description: Yup.string().required('Description is required'),
    image: Yup.string().url('Invalid URL').required('Image URL is required'),
    tags: Yup.string(),
    price: Yup.number().positive('Price must be a positive number').required('Price is required'),
    preview: Yup.boolean().required('Preview is required'),
  });

  const handleSubmit = (values, { resetForm, setSubmitting }) => {
    console.log('Form values:', values);
    onSubmit(values);
    resetForm();
    setSubmitting(false);
  };

  return (
    <Formik initialValues={initialValues} validationSchema={validationSchema} onSubmit={handleSubmit}>
      <Form className='artwork-form'>
        <SemanticForm.Field>
          <label>Title:</label>
          <Field as={Input} type='text' name='title' />
          <ErrorMessage name='title' component='div' />
        </SemanticForm.Field>
        <SemanticForm.Field>
          <label>Description:</label>
          <Field as={TextArea} name='description' />
          <ErrorMessage name='description' component='div' />
        </SemanticForm.Field>
        <SemanticForm.Field>
          <label>Image URL:</label>
          <Field as={Input} type='text' name='image' />
          <ErrorMessage name='image' component='div' />
        </SemanticForm.Field>
        <SemanticForm.Field>
          <label>Tags (comma-separated):</label>
          <Field as={Input} type='text' name='tags' />
          <ErrorMessage name='tags' component='div' />
        </SemanticForm.Field>
        <SemanticForm.Field>
          <label>Price:</label>
          <Field as={Input} type='number' name='price' />
          <ErrorMessage name='price' component='div' />
        </SemanticForm.Field>
        <SemanticForm.Field>
          <label>Public:</label>
          <Field as={Checkbox} type='radio' name='preview' />
          <ErrorMessage name='preview' component='div' />
        </SemanticForm.Field>
        <Button type='submit'>Create Artwork</Button>
        <Button type='button' onClick={onCancel}>
          Cancel
        </Button>
      </Form>
    </Formik>
  );
};

export default ArtworkForm;

