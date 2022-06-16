from django.test import TestCase
import pkg_resources
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class ImageTestCase(TestCase):
    '''
    Test class to test the behavior of the image model
    '''
    def setUp(self):
        '''
        setup method that will run before every test
        '''
        # Creating a new user and saving
        self.new_user = User(username = 'testUser', email = 'test@gmail.com',password = 'pass123')
        self.new_user.save()

        # Creating a new profile and saving it
        self.new_profile = Profile(id = 1, user = self.new_user, bio = 'testtesttest')
        self.new_profile.save()

        # Creating a new image and saving it
        self.new_image = Image(id = 1, name = 'testImg', caption = 'test caption', profile = self.new_profile)
        self.new_image.save()

    def test_instance(self):
        '''
        test_instance to test if the object has been instanciated properly
        '''
        self.assertTrue(isinstance(self.new_image, Image))

    def test_delete_img(self):
        Image.delete_image(self.new_image.id)
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)

class ProfileTestClass(TestCase):
    '''
    Test class to test the behavior of the profile class
    '''

    # Set up method
    def setUp(self):
        '''
        setup method that will run before every test
        '''
        # Creating a new user and saving it
        self.new_user = User(username = 'test', password = 'pass123', email = 'test@gmail.com')
        self.new_user.save()

        # Creating a new profile and saving it
        self.new_profile = Profile(id = 1, user = self.new_user, bio = 'testtesttest')
        self.new_profile.save()

    def test_instance(self):
        '''
        Method to test if the new_profile object is an instance of the Profile model
        '''
        self.assertTrue(self.new_profile, Profile)

    def test_delete_profile(self):
        Profile.delete_profile(self.new_profile.id)
        saved_profiles = Profile.objects.all()
        self.assertTrue(len(saved_profiles) == 0)

# class MyInstaClone(TestCase):
#     '''
#     Test class to run tests checking on the behaviour of the entire app
#     '''
#     def setUpTestUser(cls):
#         '''
#         setUp method to set up the default user with an id
#         '''
#         cls.obj_id = User.objects.create(
#             username = 'testUser'
#             email = 'test@gmail.com'
#             password = 'pass123'
#         ).pk

#     def setUp(self):
#         '''
#         setUp method to run before every test
#         '''
#         self.new_user = User.objects.create(
#             username = 'weps'
#             email = 'weps@gmail.com'
#             password = 'pass4321'
#         )
#         login = self.client.login(username = 'weps', password = '4321')

#         self.new_profile = Profile.objects.get