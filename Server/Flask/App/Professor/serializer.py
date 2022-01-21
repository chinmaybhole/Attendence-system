from App import api

prof_login_parser = api.parser()
prof_login_parser.add_argument("userid",location = "headers", help= "Enter your userid", required = "True")
prof_login_parser.add_argument("passw",location = "headers", help= "Enter your password", required = "True")

auth_failures = {
	401 : "Credentials Incorrect",
    404 : "User not found",
    500 : "Internal Server Error"
}

