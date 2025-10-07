# User Signup, Login, and Blog Application

This is a web application that allows **Patients** and **Doctors** to sign up, log in, and get redirected to their own dashboards.  
In addition, **Doctors** can create blog posts, and **Patients** can view them categorized by topic.

---

## Features

### User Management
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
- Dashboards display the signup details

### Blog System
- **Doctor Role:**
  - Can create new blog posts
  - Blog post fields:
    - Title
    - Image
    - Category (e.g., Mental Health, Heart Disease, COVID-19, Immunization)
    - Summary
    - Content
    - Draft option (save as draft)
  - Can view the list of their own posts
- **Patient Role:**
  - Can view all published blog posts (drafts hidden)
  - Blogs displayed **category-wise**
  - Each blog in the list shows:
    - Title
    - Image
    - Summary (truncated to 15 words)
    
---

## How it Works

### 1. Signup
- User selects role (Patient/Doctor)  
- Fills in all required fields  
- Password and Confirm Password must match  

### 2. Login
- User logs in with username and password  
- Redirected to the correct dashboard based on their role  

### 3. Dashboard
- Displays the user information entered at signup

### 4. Blog System
- **Doctor Dashboard:** Create, view, and manage blog posts  
- **Patient Dashboard:** Browse all published blogs by category  

---

## Technical Details
- Backend: Django
- Database: MySQL
- User Authentication: Django’s built-in auth system
- Blog images uploaded using Django’s `ImageField`
- Categories managed in a separate `Category` model
- Frontend uses HTML templates with Django template tags (no APIs required)
