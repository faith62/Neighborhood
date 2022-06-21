from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import NeighbourHood, UserProfile, Business, Post


# Create your tests here.

def test_home_page_status_code(self):
    url = reverse('home')
    response = self.client.get(url)
    self.assertEquals(response.status_code, 200)


class NeighbourhoodTestCase(TestCase):
    def setUp(self):
        self.user = User(username='brie', password='testpwsd123')
        self.user.save()
        self.profile = UserProfile(id=15, user=self.user, )
        # self.profile.create_profile()
        self.neighborhood = NeighbourHood(name='Test Neighbourhood', description='Test Description', admin=self.profile )
        # self.neighborhood.save()

    def tearDown(self):
        User.objects.all().delete()
        UserProfile.objects.all().delete()
        NeighborHood.objects.all().delete()
        self.user.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, UserProfile))

    def test_save_profile(self):
        self.profile.create_profile()
        after = UserProfile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_save_neighborhood(self):
        self.neighborhood.save()
        after = NeighborHood.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_neighbourhood(self):
        self.neighborhood.save()
        self.neighborhood.delete()
        after = NeighborHood.objects.all()
        self.assertTrue(len(after) == 0)

    def test_neighbourhood_name(self):
        self.assertEqual(self.neighborhood.name, 'Test Neighborhood')

    def test_neighbourhood_description(self):
        self.assertEqual(self.neighbuorhood.description, 'Test Description')

class BusinessTestCase(TestCase):
    def setUp(self):
        self.user = User(username='brie', password='testpwsd123')
        self.user.save()
        self.profile = UserProfile(id=17, user=self.user, )
        # self.profile.save()
        self.neighbourhood = NeighbourHood(name='Test Neighbourhood',
                                         description='Test Description')
        self.neighborhood.save()
        self.business = Business(name='Test Business', email="test@test.com", description='Test Description',
                                 neighbourhood=self.neighborhood )
        self.business.save()

    def tearDown(self):
        User.objects.all().delete()
        UserProfile.objects.all().delete()
        NeighbourHood.objects.all().delete()
        Business.objects.all().delete()
        self.user.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_business(self):
        self.business.save()
        after = Business.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_business(self):
        self.business.save()
        self.business.delete()
        after = Business.objects.all()
        self.assertTrue(len(after) == 0)

    def test_business_name(self):
        self.assertEqual(self.business.name, 'Test Business')

    def test_business_email(self):
        self.assertEqual(self.business.email, 'test@test.com')

    def test_business_description(self):
        self.assertEqual(self.business.description, 'Test Description')

    def test_business_neighbourhood(self):
        self.assertEqual(self.business.neighbourhood, self.neighbourhood)

    def test_business_user(self):
        self.assertEqual(self.business.user, self.profile)


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User(username='brie', password='testpwsd123')
        self.user.save()
        self.profile = UserProfile(id=17, user=self.user, )
        self.neighborhood = NeighbourHood(name='Test Neighbourhood',description='Test Description')
        self.neighbourhood.save()
        self.post = Post(title='Test Post', post='Test Content', user=self.profile, hood=self.neighbourhood, )
        self.post.save()

    def tearDown(self):
        User.objects.all().delete()
        UserProfile.objects.all().delete()
        Post.objects.all().delete()
        self.user.delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.post, Post))

    def test_save_post(self):
        self.post.save()

    def test_delete_post(self):
        self.post.save()

    def test_post_title(self):
        self.assertEqual(self.post.title, 'Test Post')

    def test_post_content(self):
        self.assertEqual(self.post.post, 'Test Content')

    def test_post_user(self):
        self.assertEqual(self.post.user, self.profile)

    def test_post_hood(self):
        self.assertEqual(self.post.hood, self.neighbourhood)


class ProfileTestCase(TestCase):
    def setUp(self):
        self.user = User(username='brie', password='testpwsd123')
        self.user.save()
        self.profile = UserProfile(id=17, user=self.user, )
        self.bio = "default bio"
        self.neighborhood = NeighbourHood(name='Test Neighbourhood', description='Test Description' )
        self.neighbourhood.save()

    def tearDown(self):
        User.objects.all().delete()
        UserProfile.objects.all().delete()
        NeighbourHood.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.profile, UserProfile))

    def test_save_profile(self):
        self.profile.create_profile()
        after = UserProfile.objects.all()
        self.assertTrue(len(after) > 0)

    def test_delete_profile(self):
        self.profile.create_profile()
        self.user.delete()
        after = UserProfile.objects.all()
        self.assertTrue(len(after) == 0)

    def test_profile_user(self):
        self.assertEqual(self.profile.user, self.user)

    def test_profile_neighbourhood(self):
        self.profile.neighbourhood = self.neighbourhood
        self.assertEqual(self.profile.neighbourhood, self.neighbourhood)

    def test_profile_image(self):
        self.assertEqual(self.profile.profile_pic, self.profile_pic)

    def test_profile_bio(self):
        self.assertEqual(self.profile.bio, self.bio)

    def test_profile_hood(self):
        self.profile.neighbourhood = self.neighbourhood
        self.assertEqual(self.profile.neighbourhood, self.neighbourhood)

    def test_profile_hood_name(self):
        self.profile.neighbourhood = self.neighbourhood
        self.assertEqual(self.profile.neighbourhood.name, self.neighbourhood.name)

    def test_profile_hood_description(self):
        self.profile.neighbourhood = self.neighbourhood
        self.assertEqual(self.profile.neighbourhood.description, self.neighbourhood.description)

    def test_profile_hood_police(self):
        self.profile.neighbourhood = self.neighbourhood
        self.assertEqual(self.profile.neighbourhood.police, self.neighbourhood.police)