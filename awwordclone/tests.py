from django.test import TestCase
from .models import Profile, Project

# Create your tests here.

class ProfileTestClass(TestCase):
    #Set up method
    def setUp(self):
        self.new_profile =Profile(title="food for good life",image="image.jpeg",description="this is to test if it can work",link = "https://github.com/shureim/Instagram-Website/tree/master/insta")

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.new_profile,Profile))

    #Testing Save Method
    def test_save_method(self):
        self.new_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)

    def test_delete_method(self):
        self.new_profile.save_profile()
        self.new_profile.delete_profile()
