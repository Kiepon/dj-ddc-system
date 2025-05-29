from django.urls import path

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from .views import RecordCashList, RecordCashDetail


urlpatterns = [
    path('<int:pk>/', RecordCashDetail.as_view(), name="post_detail"),
    path('', RecordCashList.as_view(), name="post_list"),
    path('schema/', SpectacularAPIView.as_view(), name="schema"),
    path("schema/swagger-ui/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
]
