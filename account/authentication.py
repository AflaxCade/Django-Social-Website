from django.contrib.auth.models import User
from account.models import Profile
import requests
from django.core.files.base import ContentFile
from urllib.parse import urlparse, unquote
import os

class EmailAuthBackend:
    """
    Authenticate using an e-mail address.
    """
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except (User.DoesNotExist, User.MultipleObjectsReturned):
            return None
        
    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
        


def create_profile(backend, user, response, *args, **kwargs):
    """
    Create user profile for social authentication and save the social profile picture.
    """
    profile, created = Profile.objects.get_or_create(user=user)
    
    # Handle Google OAuth2
    if backend.name == 'google-oauth2':
        picture_url = response.get('picture')
    
    # Handle Twitter OAuth
    elif backend.name == 'twitter':
        picture_url = response.get('profile_image_url_https')
        if picture_url:
            # Change Twitter profile image URL to get the original size
            picture_url = picture_url.replace('_normal', '')

    # Handle GitHub OAuth
    elif backend.name == 'github':
        picture_url = response.get('avatar_url')

    if picture_url:
        # Download the image
        r = requests.get(picture_url)
        if r.status_code == 200:
            # Parse the filename and add an appropriate extension
            parsed_url = urlparse(picture_url)
            filename = os.path.basename(unquote(parsed_url.path))
            filename, ext = os.path.splitext(filename)
            if ext.lower() not in ['.jpg', '.jpeg', '.png']:
                ext = '.jpg'  # Default to .jpg if no valid extension
            profile.photo.save(f'{filename}{ext}', ContentFile(r.content), save=True)
