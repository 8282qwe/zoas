from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'persons', views.PersonViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('zoas-api/participation/', views.ParticipationViewSet),
    path('zoas-api/stt-view/', views.SttViewSet),
    path('zoas-api/summary-view/', views.SummaryViewSet),
    path('zoas-api/join/', views.joinViewSet),
]

