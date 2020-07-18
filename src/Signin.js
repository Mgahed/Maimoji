import React, { Component } from 'react'
import axios from 'axios'
import Avatar from '@material-ui/core/Avatar';
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Paper from '@material-ui/core/Paper';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { makeStyles } from '@material-ui/core/styles';


function Copyright() {
  return (
    <Typography variant="body2" color="textSecondary" align="center">
      {'Copyright © '}
      <Link color="inherit" href="https://material-ui.com/">
        Your Website
      </Link>{' '}
      {new Date().getFullYear()}
      {'.'}
    </Typography>
  );
}



class Signin extends Component {

  constructor(props) {
    super(props)



    this.state = {
      pass: '',
      number: '',
      mgahd: 'False'
    }
  }

  changeHandler = e => {
    this.setState({ [e.target.name]: e.target.value })
  }

  submitHandler = e => {
    e.preventDefault()
    console.log(this.state)
    axios
      .post('https://maimoji.herokuapp.com/api/login', this.state)
      .then(response => {
        console.log(response.data)
        var mgahd = response.data.boolean;

        if (mgahd === "True") {
          var mail = response.data.mail;
          var name = response.data.name;
          var num = response.data.number;
          var id = response.data.id;
          window.location.replace("http://localhost:3000/UserProfile")
        } else {
          alert("Error");
        }
        //document.getElementById("usermail").innerHTML = mail;
        sessionStorage.setItem("mail", mail);
        sessionStorage.setItem("name", name);
        sessionStorage.setItem("num", num);
        sessionStorage.setItem("id", id);

      })
      .catch(error => {
        console.log(error)
      })
  }

  render() {

    const useStyles = makeStyles(theme => ({
      root: {
        height: '100vh',
      },
      image: {
        backgroundImage: 'url(https://source.unsplash.com/1600x900/?emoji)',
        backgroundRepeat: 'no-repeat',
        backgroundColor:
          theme.palette.type === 'light' ? theme.palette.grey[50] : theme.palette.grey[900],
        backgroundSize: 'cover',
        backgroundPosition: 'center',
      },
      paper: {
        margin: theme.spacing(8, 4),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      },
      avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
      },
      form: {
        width: '100%',
        marginTop: theme.spacing(1),
      },
      submit: {
        margin: theme.spacing(3, 0, 2),
      },
    }));

 

    return (
      <div>

        <div class="card text-center">
          <div class="card-header">
            <ul class="nav nav-pills card-header-pills">
              <li class="nav-item">
                <a class="nav-link" href="/" variant="body2">Home</a>
              </li>
              <li class="nav-item">
                <a class="nav-link" href="/Signup" variant="body2">Signup</a>
              </li>
              <li class="nav-item">
                <a class="nav-link active" href="/Signin" variant="body2">Signin</a>
              </li>

            </ul>
          </div>
        </div>
        <center>
          <br></br>
          <br></br>
          <br></br>
          <br></br>
          <Grid >
            <CssBaseline />
            <Grid item xs={false} sm={4} md={7} className={useStyles.image} />
            <Grid item xs={12} sm={8} md={5} component={Paper} elevation={6} square>
              <div className={useStyles.paper}>
                <Avatar className={useStyles.avatar}>

                </Avatar>
                <Typography component="h1" variant="h5">
                  Sign in
          </Typography>
                <form onSubmit={this.submitHandler}>
                  <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    id="num"
                    label="Phone Number"
                    name="number"
                    autoComplete="num"
                    type="number"
                    autoFocus
                    onChange={this.changeHandler}
                  />
                  <TextField
                    variant="outlined"
                    margin="normal"
                    required
                    fullWidth
                    name="pass"
                    label="Password"
                    type="password"
                    id="password"
                    autoComplete="current-password"
                    onChange={this.changeHandler}
                  />
                  <FormControlLabel
                    control={<Checkbox value="remember" color="primary" />}
                    label="Remember me"
                  />
                  <Button
                    type="submit"
                    fullWidth
                    variant="contained"
                    color="primary"
                    className={useStyles.submit}
                  >
                    Sign In
            </Button>
                  <Grid container>
                    <Grid item xs>
                      <Link href="#" variant="body2">
                        Forgot password?
                </Link>
                    </Grid>
                    <Grid item>
                      <Link href="/Signup" variant="body2">
                        {"Don't have an account? Sign Up"}
                      </Link>
                    </Grid>
                  </Grid>
                  <Box mt={5}>
                    <Copyright />
                  </Box>
                </form>
              </div>
            </Grid>
          </Grid>
        </center>
      </div>
    )
  }
}

export default Signin



