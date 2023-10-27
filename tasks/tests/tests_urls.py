from django.test import SimpleTestCase
from django.urls import resolve, reverse
from tasks.views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete

class TestUrls(SimpleTestCase):

    def test_tasks_list_url_resolves(self):
        url = reverse('tasks')

        self.assertEquals(resolve(url).func.view_class, TaskList)
    
    
    def test_task_detail_url_resolves(self):
        url = reverse('task', args=['id'])

        self.assertEquals(resolve(url).func.view_class, TaskDetail)


    def test_task_create_url_resolves(self):
        url = reverse('create-task')

        self.assertEquals(resolve(url).func.view_class, TaskCreate)
    

    def test_task_update_url_resolves(self):
        url = reverse('update-task', args=['id'])

        self.assertEquals(resolve(url).func.view_class, TaskUpdate)


    def test_task_delete_url_resolves(self):
        url = reverse('delete-task', args=['id'])

        self.assertEquals(resolve(url).func.view_class, TaskDelete)