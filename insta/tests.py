from django.test import TestCase
from .models import *

# Create your tests here.
class ImageTestCase(TestCase):
    '''
    Test class to test the behavior of the image model
    '''
    def setUp(self):
        '''
        setup method that will run before every test
        '''
        self.user = User.objects.create(
            username = 'test',
            email = 'test@gmail.com',
            password = 'test123'
        )
        Image.objects.create(
            name='test_img',
            image = 'http://res.cloudinary.com/de2vfftjr/image/upload/v1654235259/qf1yv11zbyhuiabihpas.jpg',
            caption = 'test_caption',
            user = self.user
        )

class ProfileTestClass(TestCase):
    '''
    Test class to test the behavior of the profile class
    '''

    # Set up method
    def setUp(self):
        '''
        setup method that will run before every test
        '''
        # Creating a new location and saving it
        self.new_profile = Profile(bio = 'testing')
        self.new_profile.save_profile()