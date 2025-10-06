# User Signup and Login Application

This is a simple web application that allows **Patients** and **Doctors** to sign up, log in, and get redirected to their own dashboards.  
After logging in, the user will see a basic dashboard showing the details they entered during signup.

---

## Features

- Two types of users:
  - Patient
  - Doctor
- Signup form with the following fields:
  - First Name
  - Last Name
  - Profile Picture
  - Username
  - Email
  - Password & Confirm Password (with match check)
  - Address (line1, city, state, pincode)
- Login system
- After login, users are redirected to their respective dashboards
- Dashboards simply display the signup details

---

## How it works

1. **Signup**  
   - User chooses if they are a Patient or Doctor  
   - Fills in all the required fields  
   - Password and Confirm Password must match  

2. **Login**  
   - User logs in with username and password  
   - Depending on the role (Patient/Doctor), the app redirects to the correct dashboard  

3. **Dashboard**  
   - Shows the user information entered at the time of signup  

---
