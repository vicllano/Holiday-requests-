Employee Holiday Requests

Purpose:

The web app will receive holiday requests from employees, store them in a MYSQL database, query all holiday request records and present them to employees for view and managers for approval.

Description: 

Initialize the MYSQL database 
Create database Model pto_requests
Define pto_requests table columns
Create the database pto_requests table within the application context
Create route decorators
Accept an Employee's name and other holiday request details from the form on index.html
Create variables from form inputs
Assign variables to the database table
If form input values are missing
	return error and pass it to index.html
If start_date is greater than end_date 
	return date_error and pass it to index.html
If there is a problem adding to the database 
	return other_error and pass it to index.html
Else
	Push record to database
	Return confirmation and pass it to submitted.html

Query all records in database table, order by date_created and store it in all_requests
Return all_requests and pass it into manager.html

When a record's update button is clicked in manager.html pass the record's id to the url
Query record from database with the id passed from the url and store it in update
create variables from the data stored in update 
return variables and pass them into approvals.html
When submit button is clicked assign update.status the new value from the form dropdown in approvals.html
If there is a problem updating the database 
	return string message
Else
	Push updated record to database
	Query all records in database table, order by date_created and store it in all_requests
	Return all_requests and confirmation and pass them into manager.html

Query all records in database table, order by date_created and store it in request_status
Return request_status and pass ir into request_status.html

Pre-requisites: 

1. Requires access to MYSQL
2. Requires the creation of a database named requests
3. Requires the creation and activation of a virtual environment
4. Requires the installation of modules in requrements.txt

Landing Page
<img width="1284" alt="Screenshot 2023-02-12 at 8 04 01 PM" src="https://user-images.githubusercontent.com/73876124/218367827-4d7f3a08-0c11-4e8b-8d02-ca6a2d7af9ea.png">

Request Submission Confirmation
<img width="1285" alt="Screenshot 2023-02-12 at 8 09 11 PM" src="https://user-images.githubusercontent.com/73876124/218368428-a1bcf930-073c-4dc6-82f3-d225d382abbe.png">

Manager Approval Page
<img width="1286" alt="Screenshot 2023-02-12 at 8 10 20 PM" src="https://user-images.githubusercontent.com/73876124/218368551-e5719fb3-1187-4e51-a8c9-44b91319fa85.png">

Status Update Page
<img width="1279" alt="Screenshot 2023-02-12 at 8 13 39 PM" src="https://user-images.githubusercontent.com/73876124/218368905-3644f214-ffc9-402f-b3a4-be0aca2cc887.png">

Update Succesful
<img width="1281" alt="Screenshot 2023-02-12 at 8 14 03 PM" src="https://user-images.githubusercontent.com/73876124/218368946-a776c502-9673-4369-ad13-d68cddf8fa3e.png">

All Fields Required Error
<img width="1277" alt="Screenshot 2023-02-12 at 8 15 38 PM" src="https://user-images.githubusercontent.com/73876124/218369103-1b8e28fa-2629-42c2-be97-c931647fe3f4.png">

Adjust Dates Error
<img width="1285" alt="Screenshot 2023-02-12 at 8 17 12 PM" src="https://user-images.githubusercontent.com/73876124/218369290-4f56d24d-fc27-480b-9812-c7041323e439.png">






