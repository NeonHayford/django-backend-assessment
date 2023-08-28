# from django.test import TestCase
# from .views import CreateGroupView
# from .models import Group
# from rest_framework import HTTP_200_OK

# # Create your tests here.
# class CreateGroupViewTestCase(TestCase):
#     # Positive test case for successful group creation
#     def test_post(self):
#         request = self.factory.post('/groups/', {'group_name': 'Test Group'})
#         view = CreateGroupView.as_view()
#         response = view(request)
#         self.assertEqual(response.status_code, HTTP_200_OK)
#         self.assertEqual(Group.objects.count(), 1)
#         self.assertEqual(Group.objects.first().group_name, 'Test Group')


