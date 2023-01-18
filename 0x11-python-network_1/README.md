So we continue with python netwoking, the tasks are:

#0.Write a Python script that fetches https://alx-intranet.hbtn.io/status
#1.Write a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.
#2.Write a Python script that takes in a URL and an email, sends a POST request to the passed URL with the email as a parameter, and displays the body of the response (decoded in utf-8)
#3.Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response (decoded in utf-8).
#4.Write a Python script that fetches https://alx-intranet.hbtn.io/status
#5.Write a Python script that takes in a URL, sends a request to the URL and displays the value of the variable X-Request-Id in the response header
    You must use the packages requests and sys
    ou are not allow to import other packages than requests and sys
    The value of this variable is different for each request
    You don’t need to check script arguments (number and type)

#6.Write a Python script that takes in a URL and an email address, sends a POST request to the passed URL with the email as a parameter, and finally displays the body of the response.

    The email must be sent in the variable email
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to error check arguments passed to the script (number or type)

Please test your script in the sandbox provided, using the web server running on port 5000

#7.Write a Python script that takes in a URL, sends a request to the URL and displays the body of the response.

    If the HTTP status code is greater than or equal to 400, print: Error code: followed by the value of the HTTP status code
    You must use the packages requests and sys
    You are not allowed to import packages other than requests and sys
    You don’t need to check arguments passed to the script (number or type)

Please test your script in the sandbox provided, using the web server running on port 5000
#8.Write a Python script that takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.

    The letter must be sent in the variable q
    If no argument is given, set q=""
    If the response body is properly JSON formatted and not empty, display the id and name like this: [<id>] <name>
    Otherwise:
        Display Not a valid JSON if the JSON is invalid
        Display No result if the JSON is empty
    You must use the package requests and sys
    You are not allowed to import packages other than requests and sys
#9.Write a Python script that takes your GitHub credentials (username and password) and uses the GitHub API to display your id
