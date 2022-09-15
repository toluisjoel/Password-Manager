from django.test import TestCase
from django.test.client import Client

from django.urls import reverse
from .models import SiteDetail, Website
from django.contrib.auth.models import User

# Create your tests here.


def create_website(website_link):
    user = User.objects.get(id=1)
    website = Website.objects.create(user=user, link=website_link)
    return website


def create_site_details(username, password, website):
    user = User.objects.get(id=1)
    SiteDetail.objects.create(
        user=user, website=website, username=username, password=password)
    return website.details.all()


class WebsiteIndexViewTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='john', password='smith')

    def test_no_website_exists(self):
        """
        If no website exist, an appropriate message is displayed.
        """
        self.client.login(username='john', password='smith')
        response = self.client.get(reverse('manager:home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No Sites Available')
        self.assertQuerysetEqual(response.context['websites'], [])

    def test_website_exists(self):
        """
        Websites created displays on the home page.
        """
        website = create_website('test.com')
        self.client.login(username='john', password='smith')
        response = self.client.get(reverse('manager:home'))
        self.assertQuerysetEqual(response.context['websites'], [website])

    def test_mutiple_website_exists(self):
        """
        The home page may display multiple website
        """
        website_1 = create_website('test.com')
        website_2 = create_website('test2.com')
        self.client.login(username='john', password='smith')
        response = self.client.get(reverse('manager:home'))
        self.assertQuerysetEqual(response.context['websites'], [website_2, website_1])

    def test_website_has_no_details(self):
        """
        Websites wihtout details does not displays on the home page.
        """
        website = create_website('test.com')
        self.client.login(username='john', password='smith')
        response = self.client.get(reverse('manager:home'))
        for site in response.context['websites']:
            self.assertQuerysetEqual(site.details.all(), [])

    def test_website_has_details(self):
        """
        Websites with details displays on the home page.
        """
        website = create_website('test.com')
        detail = create_site_details('thomas', 'joel', website)
        self.client.login(username='john', password='smith')
        response = self.client.get(reverse('manager:home'))
        for site in response.context['websites']:
            self.assertQuerysetEqual(site.details.all(), detail)
