from django.urls import path

from user.views.user_insert import UserInsertView
from user.views.user_select import UserSelectView

urlpatterns = [
    path("insert", UserInsertView.as_view({'post': 'create'})),
    path("login", UserSelectView.as_view({'post': 'login'})),
]
