# from django.test import TestCase

# # Create your tests here.
# import unittest
# from django.contrib.auth.models import User
# from rest_framework.authtoken.models import Token
# from rest_framework.test import APIRequestFactory, force_authenticate
# from .views import LogoutView

# class LogoutViewTestCase(unittest.TestCase):
#     def setUp(self):
#         self.factory = APIRequestFactory()
#         self.view = LogoutView.as_view()
#         self.user = User.objects.create_user(username='testuser', password='testpassword')
#         self.token = Token.objects.create(user=self.user)

#     def test_positive_logout(self):
#         # Positive test case: User successfully logs out
#         request = self.factory.post('/logout/')
#         force_authenticate(request, user=self.user, token=self.token)
#         response = self.view(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data, {'detail': 'Successfully logged out.'})

#     def test_negative_logout_unauthenticated(self):
#         # Negative test case: User is not authenticated
#         request = self.factory.post('/logout/')
#         response = self.view(request)
#         self.assertEqual(response.status_code, 401)
#         self.assertEqual(response.data, {'detail': 'Authentication credentials were not provided.'})

#     def test_negative_logout_invalid_token(self):
#         # Negative test case: User provides an invalid token
#         request = self.factory.post('/logout/')
#         force_authenticate(request, user=self.user, token='invalid_token')
#         response = self.view(request)
#         self.assertEqual(response.status_code, 401)
#         self.assertEqual(response.data, {'detail': 'Invalid token.'})

#     def test_error_logout_invalid_method(self):
#         # Error test case: User tries to use an invalid HTTP method
#         request = self.factory.get('/logout/')
#         force_authenticate(request, user=self.user, token=self.token)
#         response = self.view(request)
#         self.assertEqual(response.status_code, 405)
#         self.assertEqual(response.data, {'detail': 'Method "GET" not allowed.'})

#     def test_edge_logout_multiple_authentication_classes(self):
#         # Edge test case: View has multiple authentication classes
#         request = self.factory.post('/logout/')
#         force_authenticate(request, user=self.user, token=self.token)
#         response = self.view(request)
#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data, {'detail': 'Successfully logged out.'})

# if __name__ == '__main__':
#     unittest.main()