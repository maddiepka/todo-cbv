from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from .models import Task

# Create your tests here.

class TaskTestCase(TestCase):
    def setUp(self):

        self.user = User.objects.create_user(username='testuser', password='12345')
        self.client = Client()      
    
    def test_status_code(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
    
    def test_no_tasks(self):
        """
        If no tasks exist, an approriate message is displayed.
        """
        response = self.client.get(reverse('tasks'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No tasks to do!")
        self.assertQuerySetEqual(response.context['tasks'], [])
    
    def test_are_tasks(self):
        """
        If tasks exist, list of tasks is displayed
        """


        task1 = Task.objects.create(title='do loundry', user=self.user)
        task2 = Task.objects.create(title="do homework", user=self.user)
        response = self.client.get(reverse('tasks'))

        self.assertEqual(response.status_code, 200)
        self.assertQuerySetEqual(list(response.context['tasks']), [task1, task2])



