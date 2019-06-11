
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
	""" para completar el perfil """
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		if not request.user.is_anonymous:
				profile = request.user.profile
				if not profile.picture or not profile.biography:
					if request.path not in [reverse('users:update'), reverse('users:logout')] and not request.path.startswith('/admin/'):
						return redirect ('update')


		response = self.get_response(request)
		return response