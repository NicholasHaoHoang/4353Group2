<a href="https://codecov.io/gh/NicholasHaoHoang/4353Group2" > 
 <img src="https://codecov.io/gh/NicholasHaoHoang/4353Group2/branch/main/graph/badge.svg?token=5EF2Y2MROP"/> 
</a>
<h1>
^Click to view Coverage Report
</h1>

This will be the final group project of 4353 for Singh.

Assignment 2:
In this assignment you will build the front end for the web application that you designed in assignment 1. 
Remember, we are only building front end in this assignment.

Additional Details:
Front end must include following components:
- Login (Allow Client to register if not a client yet)
- Client Registration (Initially only username and Password)
- Client Profile Management (After client registers they should login first to complete the profile). Following fields will be on Profile page / form:
	- Full Name (50 characters, required)
	- Address 1 (100 characters, required)
	- Address 2 (100 characters, optional)
	- City (100 characters, required)
	- State (Drop Down, selection required) DB will store 2 character state code
	- Zipcode (9 characters, at least 5 character code required)
	
- Fuel Quote Form with following fields: (We are not building pricing module yet)
	- Gallons Requested (numeric, required)
	- Delivery Address (Non-editable, comes from client profile)
	- Delivery Date (Calender, date picker)
	- Suggested Price / gallon (numeric non-editable, price will be calculated by Pricing Module - we are not building pricing module yet)
	- Total Amount Due (numeric non-editable, calculated (gallons * price))
	
- Fuel Quote History
	- Tabular display of all client quotes in the past. All fields from Fuel Quote are displayed.

- You should have validations in place for required fields, field types, and field lengths. 

- NOTE: Only provide a word / pdf doc. You should use GitHub for your group collaboration and code.

Answer these questions:
1. Provide link to GitHub repository for TAs to view the code? (1 point)
2. Discuss if your design and development methodology has changed since assignment 1 and why? (1 point)
3. List what front end technologies you are using and why. List who is responsible of doing what in your group? (2 points)
4. Provide screen shots of your front end, each page? (5 points)
5. IMPORTANT: list who did what within the group. TAs should be able to validate in GitHub, otherwise team members who didn't contribute will receive a ZERO. (1 point)

ASSIGNMENT 3:
In this assignment you will build the back end for the web application that you designed in assignment 1. 
Remember, we are only building back end in this assignment.


Description: 
Same as assignment 1.

Additional Details:

Back end must include following components/modules:



- Login module
- Client Profile Management module
- Fuel Quote module, includes list of quote history for a client.
- Pricing module. Only create a class. You will implement this in last assignment.

Important deliverables:
- You should have validations in place for required fields, field types, and field lengths in backend code as well. 
- All backend code should be covered by unit tests. Code coverage should be grater than 80%. 
- Research how to run the code coverage reports. Each IDE has plugins to generate reports. Here are few pointers. https://stackify.com/code-coverage-tools/
- All front end should be connected to back end. Form data should be populated from backend. Backend should receive data from front end, validate, and prepare it to persist to DB.
- WE ARE NOT IMPLEMENTING DB yet. For this assignment you can hard code the values.

NOTE: Only provide a word / pdf doc. You should use GitHub for your group collaboration and code.

Answer these questions:
1. Provide link to GitHub repository for TAs to view the code. Code should include unit tests.(5 points)
2. List what backend technologies you are using and why? (2 points)
3. IMPORTANT: list who did what within the group. TAs should be able to validate in GitHub, otherwise team members who didn't contribute will receive a ZERO.
 
Fill in this table, provide as much details possible:

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
Assignment 4:
Due July 24th
In this assignment you will create the database and connect it to your web application.

Description: 
Same as assignment 1.

Additional Details:




Database must include following tables:
- UserCredentials (ID & password), password should be encrypted.
- ClientInformation
- FuelQuote
- Any additional tables you feel, like States.

Important deliverables:
- You should have validations in place for required fields, field types, and field lengths. 
- Backend should retrieve data from DB and display it to front end.
- Form data should be populated from backend. Backend should receive data from front end, validate, and persist to DB.
- Any new code added should be covered by unit tests. Keep code coverage above 80%.

- NOTE: Only provide a word / pdf doc. You should use GitHub for your group collaboration and code.

Answer these questions:
1. Provide link to GitHub repository for TAs to view the code.(5 points)
2. Provide SQL statements to create database.(3 points)
3. Rerun the code coverage report and provide it. (2 points)
4. IMPORTANT: list who did what within the group. TAs should be able to validate in GitHub, otherwise team members who didn't contribute will receive a ZERO.

What to turn in: 
- Only soft copy uploaded to BlackBoard before due date. 
- DO NOT SUBMIT CODE to BlackBoard. 
- Only one submission per group.
- No extensions.
- All group members must contribute equally.

