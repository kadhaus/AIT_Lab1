from django.conf.urls import url,include
from task1.views import ViewWithText, ViewWithEquation, ViewWithGraphics,drawGraphic



urlpatterns = [
    url(r'^reverse$', ViewWithText.as_view()),
    url(r'^equation$', ViewWithEquation.as_view()),
    url(r'^graphics$', ViewWithGraphics.as_view()),
    url(r'^draw$', drawGraphic),
    url(r'^$', ViewWithEquation.as_view()),
]