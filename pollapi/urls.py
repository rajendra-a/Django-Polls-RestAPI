from django.urls import path
from rest_framework.routers import DefaultRouter



from .views import *
from .apiviews import *
from .genericapiviews import *


router = DefaultRouter()
router.register("polls", PollViewSet, basename="polls")



urlpatterns = [
    #function based urls
    # path("polls/", polls_list, name="polls"),
    # path("polls/<int:pk>/", poll_detail, name="poll_detail"),

    #class based urls with APIViews
    path("poll_list/", PollList.as_view(), name="poll_list"),
    path("poll_list/<int:pk>/", POllDetail.as_view(), name="poll_in_detail"),

    # #class base urls with generics
    # path("polls_list/", PollsList.as_view(), name="polls_list"),
    # path("polls_detail/<int:pk>/", PollsDetail.as_view(), name="polls_detail"),

    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choices"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),

    path("users/", UserCreate.as_view(), name="user_create"),
    path("login/", LoginView.as_view(), name="login"),
  

]

urlpatterns += router.urls