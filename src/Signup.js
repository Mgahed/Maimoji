import React, { Component } from 'react'
import axios from 'axios'
import Button from '@material-ui/core/Button';
import CssBaseline from '@material-ui/core/CssBaseline';
import TextField from '@material-ui/core/TextField';
import FormControlLabel from '@material-ui/core/FormControlLabel';
import Checkbox from '@material-ui/core/Checkbox';
import Link from '@material-ui/core/Link';
import Grid from '@material-ui/core/Grid';
import Box from '@material-ui/core/Box';
import Typography from '@material-ui/core/Typography';
import Container from '@material-ui/core/Container';
import Avatar from '@material-ui/core/Avatar';
import { makeStyles } from '@material-ui/core/styles';



class Signup extends Component {

	constructor(props) {
		super(props)



		this.state = {
			FN: '',
			LN: '',
			mail: '',
			snum: '',
			spass: '',
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
			.post('https://maimoji.herokuapp.com/api/signup', this.state)
			.then(response => {
				console.log(response.data.boolean)
				var mgahd = response.data.boolean;
				if (mgahd === "True") {
					alert("Done");

				} else {
					alert("Error");
				}
				//document.getElementById("Demo").innerHTML = mgahd;

			})
			.catch(error => {
				console.log(error)
			})
	}

	render() {
		const useStyles = makeStyles(theme => ({
			paper: {
				marginTop: theme.spacing(8),
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
				marginTop: theme.spacing(3),
			},
			submit: {
				margin: theme.spacing(3, 0, 2),
			},
		}));


		const { FN } = this.state
		return (
<sss>
			<div>

				<div class="card text-center">
					<div class="card-header">
						<ul class="nav nav-pills card-header-pills">
							<li class="nav-item">
								<a class="nav-link" href="/" variant="body2">Home</a>
							</li>
							<li class="nav-item">
								<a class="nav-link active" href="/Signup" variant="body2">Signup</a>
							</li>
							<li class="nav-item">
								<a class="nav-link" href="/Signin" variant="body2">Signin</a>
							</li>
							
						</ul>
					</div>
				</div>

				<Container component="main" maxWidth="xs">
					<CssBaseline />
					<center><Avatar style={useStyles.Avatar}></Avatar> </center>
					<Typography component="h1" variant="h5">
						<center> <pre>Sign up

							</pre> </center>
					</Typography>
					<form onSubmit={this.submitHandler}>
						<Grid container spacing={2}>
							<Grid item xs={12} sm={6}>
								<TextField
									value={FN}
									autoComplete="fname"
									name="FN"
									variant="outlined"
									required
									fullWidth
									id="firstName"
									label="First Name"
									autoFocus
									onChange={this.changeHandler}
								/>
							</Grid>
							<Grid item xs={12} sm={6}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="lastName"
									label="Last Name"
									name="LN"
									autoComplete="lname"
									onChange={this.changeHandler}
								/>
							</Grid>
							<Grid item xs={12}>
								<TextField
									variant="outlined"
									required
									fullWidth
									id="email"
									label="Email Address"
									name="mail"
									autoComplete="email"
									onChange={this.changeHandler}
								/>
							</Grid>
							<Grid item xs={12}>
								<TextField
									variant="outlined"
									fullWidth
									id="Number"
									type="number"
									name="snum"
									label="Phone Number"
									autoComplete="number"
									onChange={this.changeHandler}
								/>
							</Grid>
							<Grid item xs={12}>
								<TextField
									variant="outlined"
									required
									fullWidth
									name="spass"
									label="Password"
									type="password"
									id="password"
									autoComplete="current-password"
									onChange={this.changeHandler}
								/>
							</Grid>
							<Grid item xs={12}>
								<FormControlLabel
									control={<Checkbox value="allowExtraEmails" color="primary" />}
									label="I want to receive inspiration, marketing promotions and updates via email."
								/>
							</Grid>
						</Grid>
						<Button
							type="submit"
							fullWidth
							variant="contained"
							color="primary"
						>
							Sign Up
          </Button>
						<Grid container justify="flex-end">
							<Grid item>
								<Link href="/Signin" variant="body2">
									Already have an account? Sign in
              </Link>
							</Grid>
						</Grid>
					</form>

					<Box mt={5}>

					</Box>
				</Container>

			</div>
			</sss>
		)
	}
}

export default Signup