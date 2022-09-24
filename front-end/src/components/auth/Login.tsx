import * as yup from "yup";

import {
  Button,
  Grid,
  Link,
  Paper,
  Stack,
  TextField,
  Typography,
} from "@mui/material";
import { Form, Formik, FormikValues } from "formik";

import { authenticateUser } from "../../api/user";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const navigate = useNavigate();

  const handleLogin = async (values: FormikValues) => {
    try {
      await authenticateUser(values);
    } catch (error) {
      console.error(error);
    } finally {
      navigate(-1);
    }
  };

  const initialValues: FormikValues = {
    username: "",
    password: "",
  };

  const validationSchema = yup.object({
    username: yup
      .string()
      .email("Enter a valid email")
      .required("Email is required"),
    password: yup.string().required("Password is required"),
  });

  return (
    <Formik
      initialValues={initialValues}
      onSubmit={handleLogin}
      validationSchema={validationSchema}
    >
      {({ values, handleChange, touched, errors, handleBlur }) => (
        <Form>
          <Grid container justifyContent="center" sx={{ my: 12 }}>
            <Paper elevation={1} sx={{ p: 5 }}>
              <Stack direction="column" spacing={2}>
                <Typography variant="h5" sx={{ mb: 3 }}>
                  Sign in to your account
                </Typography>
                <TextField
                  label="Email"
                  variant="outlined"
                  type="email"
                  name="username"
                  value={values.username}
                  onChange={handleChange}
                  error={touched.username && Boolean(errors.username)}
                  helperText={
                    touched.username && errors.username
                      ? `${errors.username}`
                      : undefined
                  }
                  onBlur={handleBlur}
                />
                <TextField
                  label="Password"
                  variant="outlined"
                  type="password"
                  name="password"
                  value={values.password}
                  onChange={handleChange}
                  error={touched.password && Boolean(errors.password)}
                  helperText={
                    touched.password && errors.password
                      ? `${errors.password}`
                      : undefined
                  }
                  onBlur={handleBlur}
                />
                <Link href="#" underline="hover" sx={{ pb: 4 }}>
                  Forgot your password?
                </Link>
                <Button sx={{ mt: 5 }} variant="contained" type="submit">
                  Log in
                </Button>
              </Stack>
            </Paper>
          </Grid>
        </Form>
      )}
    </Formik>
  );
};

export default Login;
