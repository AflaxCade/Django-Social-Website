# Social Website

This project is part of the "Django 4 By Example, Fourth Edition" book by Antonio Mele. The project demonstrates how to build a fully functional social networking website using Django 4. This social website allows users to create accounts, follow other users, share posts, comment on posts, and interact with the community.

## Project Description

The social website is a platform where users can connect with each other, share content, and engage in discussions. It includes features such as user authentication, profile management, following other users, creating and sharing posts, liking and commenting on posts, and receiving notifications.

## Features

- **User Authentication:** Users can register, log in, log out, change password, and reset password.
- **Profile Management:** Users can create and edit their profiles, including uploading profile pictures.
- **Follow System:** Users can follow and unfollow other users to see their posts in their feed.
- **Post Creation:** Users can create, edit, and delete posts.
- **Post Interaction:** Users can like and comment on posts.
- **Activity Stream:** Users can see a stream of activities, such as new posts from users they follow.
- **Notifications:** Users receive notifications for new followers, likes, and bookmarking images.

## Requirements

- Python 3.10 or higher
- Django 4.0
- Redis

## Libraries and Technologies Used

- **Django:** The web framework used to build the project.
- **SQLite:** The database used to store user and post data.
- **Pillow:** For handling image uploads.
- **django-allauth:** For handling user authentication, registration, and social logins.
- **django-activity-stream:** For generating the activity feed.
- **django-extensions:** For additional Django management commands and utilities.
- **easy-thumbnails:** For creating and managing image thumbnails.
- **Redis:** For caching and message brokering to improve performance and scalability.
- **JavaScript:** For enhancing the user experience on the front-end.
- **werkzeug:** A comprehensive WSGI web application library.
- **pyOpenSSL:** Python wrapper around a subset of the OpenSSL library's functionality.
- **cryptography:** Provides cryptographic recipes and primitives to Python developers.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/AflaxCade/social-website.git
```

2. Navigate to the project directory:

```bash
cd social-websit
```

3. Create a virtual environment:

```bash
python -m venv env
```

4. Activate the virtual environment:

- For Windows:

```bash
env\Scripts\activate
```

- For macOS and Linux:

```bash
source env/bin/activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Run the development server:

```bash
python manage.py runserver
```

Open your web browser and go to http://127.0.0.1:8000/account/

Or if you want bookmarklet functionality to bookmark content or image from other websites

```bash
python manage.py runserver_plus --cert-file cert.crt
```

Open your web browser and go to https://127.0.0.1:8000/account/ and Your browser will show a security warning because you are using a self-generated certificate instead
of a certificate trusted by a Certification Authority (CA). In this case, click on Advanced and then click on Proceed to 127.0.0.1 (unsafe).
