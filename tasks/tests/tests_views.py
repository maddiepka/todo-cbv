from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

from tasks.models import Task

import datetime


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser',
                                             password='12345')
        self.task1 = Task.objects.create(
            title='task1',
            user=self.user
        )
        self.tasks_list_url = reverse('tasks')
        self.task_detail_url = reverse('task', args=[self.task1.id])
    

    def test_tasks_list_GET(self):
        response = self.client.get(path=self.tasks_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/tasks.html')


    def test_task_detail_GET(self):
        response = self.client.get(self.task_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task.html')


    def test_task_create_GET(self):
        response = self.client.get(reverse('create-task'))

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'tasks/task_form.html')


    def test_task_create_POST(self):

        response = self.client.post(reverse('create-task'), data={
            'title': 'task2',
            'user': self.user,
        })
        print (response.context['form'].errors)
