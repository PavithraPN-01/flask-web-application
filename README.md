# User Registry System

This project is a functional User Management API built with Python and the Flask framework. It allows for managing user data through standard RESTful methods and provides a set of introductory utility routes.

## Project Structure

### 1. flask-api.py (Introductory Routes)
This file serves as the entry point for understanding how Flask handles different types of data and routing. It contains:
* **Greeting Logic:** A homepage route that confirms a successful login.
* **Dynamic Routing:** A `/greet/<name>` endpoint that takes a variable from the URL and returns a personalized message.
* **Math Operations:** An `/add` endpoint that demonstrates how to process integers from a URL.
* **JSON Response Example:** A `/user` GET endpoint that shows how Python dictionaries are converted into JSON format (the standard language of APIs).

### 2. flask-methods.py (Full CRUD Logic)
This is the core of the registry system. It manages an in-memory list of users and supports:
* **GET /users:** Fetch the entire list of registered users.
* **POST /users:** Add a new user to the system.
* **PUT /users/<id>:** Update the name of an existing user.
* **DELETE /users/<id>:** Remove a user from the registry.

## API Testing with Postman
All API endpoints in this system have been verified and tested using **Postman**. 



**To test the PUT (Update) method in Postman:**
1. Set the request type to `PUT`.
2. Use the URL: `http://127.0.0.1:5000/users/1`.
3. Go to the **Body** tab, select **raw**, and set the format to **JSON**.
4. Enter the updated data:
   ```json
   {
       "name": "Updated User Name"
   }
