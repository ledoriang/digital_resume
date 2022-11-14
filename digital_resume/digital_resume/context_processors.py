from django.contrib.auth.models import User

def project_context(request):
    # return {
    #     'user': request.user,
    #     'users': User.objects.all(),
    # }

    context = {
        'me': User.objects.first(),
    }

    return context