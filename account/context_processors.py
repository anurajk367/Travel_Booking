
from account.models import Intrested
# from django.contrib.auth.models import User



def intrested_count(request):
    if request.user.is_authenticated:

        cnt=Intrested.objects.filter(user=request.user).count()
        return {'count':cnt}
    else:
        return{"count":0}
