# Social Website

This project is part of the "Django 4 By Example, Fourth Edition" book by Antonio Mele. The project demonstrates how to build a fully functional social networking website using Django 4. This social website allows users to create accounts, follow other users, share posts, comment on posts, and interact with the community.

## Project Description

The social website is a platform where users can connect with each other, share content, and engage in discussions. It includes features such as user authentication, profile management, following other users, creating and sharing posts, liking and commenting on posts, and receiving notifications.

## Features

- **User Authentication:** Users can register, log in, log out, change password, and reset password.
- **Social Login:** Users can authenticate using social accounts (e.g., Google, Twitter and Github) in addition to email-based authentication.
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

## Redis intallation Using Docker

### Installing Docker

1. **Download Docker**: Visit [Docker's official website](https://www.docker.com/get-started) and download Docker for your operating system.
   
2. **Install Docker**: Follow the installation instructions for your operating system.

3. **Verify Installation**: Open a terminal or command prompt and run the following command to verify Docker installation:

```bash
docker --version
```

### Pulling and Running Redis

1. **Pull Redis Image**: Open a terminal or command prompt and execute the following command to pull the latest Redis image from Docker Hub:

```bash
docker pull redis
```

2. **Run Redis Container**: Once the image is downloaded, start a Redis container by running:

```bash
docker run -it --rm --name redis -p 6379:6379 redis
```

## Application Snapshots

![Login](https://github.com/AflaxCade/social-website/blob/main/Snapshots/login.png)

# Note

To enable social login functionality, you need to add your own API keys and secrets for Google, Twitter, and GitHub in the `settings.py` file. These values are currently set as empty strings:

## Google API
```python
***REMOVED*** = ''  # Google Client ID
***REMOVED*** = ''  # Google Client Secret
```

## Twitter API
```python
SOCIAL_AUTH_TWITTER_KEY = ''  # Google Client ID
SOCIAL_AUTH_TWITTER_SECRET = ''  # Google Client Secret
```

## GitHub API
```python
SOCIAL_AUTH_GITHUB_KEY = ''  # Google Client ID
SOCIAL_AUTH_GITHUB_SECRET = ''  # Google Client Secret
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or additions.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project is based on the "Django 4 By Example, Fourth Edition" book by Antonio Mele. Special thanks to the author for providing such a comprehensive guide to building web applications with Django.
