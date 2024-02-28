from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Careers


class CareersTestCase(APITestCase):
    def setUp(self):
        self.career = Careers.objects.create(username='testuser', title='testtitle', content='testcontent')


    def test_create_career_with_blank_fields(self):
        new_career = {'username': '', 'title': '', 'content': 'newcontent'}
        response = self.client.post(reverse('careers-list'), new_career)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data, {
            'username': ['This field may not be blank.'],
            'title': ['This field may not be blank.']
        })


    def test_create_new_career(self):
        new_career = {'username': 'newuser', 'title': 'newtitle', 'content': 'newcontent'}
        response = self.client.post(reverse('careers-list'), new_career)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Careers.objects.count(), 2)
        self.assertEqual(Careers.objects.get(username='newuser').title, 'newtitle')


    def test_get_careers(self):
        response = self.client.get(reverse('careers-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['username'], self.career.username)


    def test_update_careers_title_and_content_can_be_changed(self):
        new_title = 'newtitle'
        new_content = 'newcontent'
        response = self.client.patch(reverse('careers-detail', kwargs={'pk': self.career.pk}), {'title': new_title, 'content': new_content})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.career.refresh_from_db()
        self.assertEqual(self.career.title, new_title)
        self.assertEqual(self.career.content, new_content)


    def test_update_careers_names_cant_be_changed(self):
        response = self.client.patch(reverse('careers-detail', kwargs={'pk': self.career.pk}), {'username': 'newuser'})
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.career.refresh_from_db()
        self.assertEqual(self.career.username, 'testuser')


    def test_delete_career(self):
        response = self.client.delete(reverse('careers-detail', kwargs={'pk': self.career.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertRaises(Careers.DoesNotExist, Careers.objects.get, pk=self.career.pk)