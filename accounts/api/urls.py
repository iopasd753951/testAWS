from django.urls import path

# from .views import accountsDetailView, accountsListView, accountsCreateView, accountsDeleteView, accountsUpdateView
#
#
# urlpatterns = [
#     path('', accountsListView.as_view()),
#     path('create/', accountsCreateView.as_view()),
#     path('<pk>/update/', accountsUpdateView.as_view()),
#     path('<pk>/delete/', accountsDeleteView.as_view()),
#     path('<pk>', accountsDetailView.as_view()),
# ]

from accounts.api.views import AccountViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', AccountViewSet, basename='accounts')
urlpatterns = router.urls