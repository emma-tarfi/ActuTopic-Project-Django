from django.contrib import admin

from user.models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'city', 'phone', 'avatar')

    def user_info(self, obj):
        return obj.description

    def get_queryset(self, request):
        queryset = super(ProfileAdmin, self).get_queryset(request)
        queryset = queryset.order_by('-phone', 'user')
        return queryset

    user_info.short_description = 'Info'


admin.site.register(Profile, ProfileAdmin)