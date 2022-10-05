from tasks.viewsets import TaskViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tasks', TaskViewSet)

#url/task