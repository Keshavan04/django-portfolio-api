# from rest_framework.decorators import api_view
# from rest_framework.response import Response


from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class= TaskSerializer

    












# # --- WAITER 1: The General Waiter (All Tasks) ---
# @api_view(['GET', 'POST'])
# def api_task_list(request):
#     if request.method == 'GET':
#         tasks = Task.objects.all()
#         serializer = TaskSerializer(tasks, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = TaskSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)


# # --- WAITER 2: The Specific Waiter (One Task at a time) ---
# @api_view(['GET', 'PUT', 'DELETE'])
# def api_task_detail(request, pk):
#     try:
#         task = Task.objects.get(pk=pk)
#     except Task.DoesNotExist:
#         return Response({"error": "Task not found"}, status=404)

#     if request.method == 'GET':
#         serializer = TaskSerializer(task)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = TaskSerializer(task, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         task.delete()
#         return Response({"message": "Task successfully deleted!"}, status=204)