import { Formik, Field, Form, ErrorMessage } from 'formik';
import { useState } from 'react';

export default function SignupForm() {
  const [showFirstName, setShowFirstName] = useState(true);

  const validateFirstName = value => {
    let errorMessage;
    if (!value) {
      errorMessage = 'Enter a first name';
    }
    return errorMessage;
  };

  const validateEmail = value => {
    let errorMessage;
    if (!/^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$/i.test(value)) {
      errorMessage = 'Invalid email address';
    }
    return errorMessage;
  };

  return (
    <>
      <label htmlFor="showFirstName">Show First Name</label>
      <input 
        type="checkbox" 
        id="showFirstName" 
        onChange={() => { setShowFirstName(!showFirstName); }} 
        checked={showFirstName}
      />
      <Formik
        initialValues={{ firstName: '', lastName: '', email: '' }}
        onSubmit={(values) => {
          console.log(values);
        }}
      >
        <Form>
          {showFirstName && (
            <>
              <label htmlFor="firstName">First Name</label>
              <Field name="firstName" type="text" validate={validateFirstName} />
              <ErrorMessage name="firstName" />
            </>
          )}

          <label htmlFor="lastName">Last Name</label>
          <Field name="lastName" type="text" />
          <ErrorMessage name="lastName" />

          <label htmlFor="email">Email Address</label>
          <Field name="email" type="email" validate={validateEmail} />
          <ErrorMessage name="email" />

          <button type="submit">Submit</button>
        </Form>
      </Formik>
    </>
  );
};
