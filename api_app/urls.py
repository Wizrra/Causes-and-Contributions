from django.urls import path
from .views import CauseListCreateView, CauseDetailView, ContributeCreateView

urlpatterns = [
    path('causes/', CauseListCreateView.as_view(), name='causes-list-create'),
    path('causes/<uuid:id>/', CauseDetailView.as_view(), name='causes-detail'),
    # path('contribute/', ContributeCreateView.as_view(), name='causes-create'),
    path('causes/<uuid:id>/contribute/', ContributeCreateView.as_view(), name='causes-create')
]
