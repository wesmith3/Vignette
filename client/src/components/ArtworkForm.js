import React from 'react';
import { Field, ErrorMessage, Formik, Form } from 'formik';
import { Button } from 'semantic-ui-react';
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
    <Formik
      initialValues={initialValues}
      validationSchema={validationSchema}
      onSubmit={handleSubmit}
    >
      <Form className='artwork-form'>
        <div>
          <label>Title:</label>
          <Field type='text' name='title' />
          <ErrorMessage name='title' component='div' />
        </div>
        <div>
          <label>Description:</label>
          <Field as='textarea' name='description' />
          <ErrorMessage name='description' component='div' />
        </div>
        <div>
          <label>Image URL:</label>
          <Field type='text' name='image' />
          <ErrorMessage name='image' component='div' />
        </div>
        <div>
          <label>Tags (comma-separated):</label>
          <Field type='text' name='tags' />
          <ErrorMessage name='tags' component='div' />
        </div>
        <div>
          <label>Price:</label>
          <Field type='number' name='price' />
          <ErrorMessage name='price' component='div' />
        </div>
        <div>
          <label>Preview:</label>
          <Field type='checkbox' name='preview' />
          <ErrorMessage name='preview' component='div' />
        </div>
        <Button type='submit'>Create Artwork</Button>
        <Button type='button' onClick={onCancel}>
          Cancel
        </Button>
      </Form>
    </Formik>
  );
};

export default ArtworkForm;

