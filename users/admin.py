from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from django.contrib.auth.models import User 
from users.models import Profile

# Register your models here.
 

class ProfileAdmin(admin.ModelAdmin):
	"""docstring for ProfileAdmin"""

	list_display = ('user', 'phone_number', 'website', 'picture')
	list_display_links = ('user', 'phone_number')
	serch_fields = (
		'user__email',
		'user__username'
		'user__firt_name',
		'user__last_name',
		'phone_number'
		)

	list_filter =(
		'user__is_active',
		'user__is_staff',
		'created',
		'modified'
	)

	fieldsets = (
		('Profile', {
			'fields': (('user', 'picture'),)
			}),
		('Extra info', {
			'fields':(
				('website', 'phone_number'),
				('biography')
			)
			}),
		('Meta data',{
			'fields': (('created', 'modified'),), 
			})
	)

	readonly_fields = ('created', 'modified',)


class ProfileInline(admin.StackedInline):

		model = Profile
		can_delete = False
		verbose_name_plural = 'Profiles'


class UserAdmin(BaseUserAdmin):
	"""docstring for UserAdmin"""

	inlines = (ProfileInline,)
	
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Profile)