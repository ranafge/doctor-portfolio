from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404, render
from django.utils.decorators import method_decorator
from django_ratelimit.decorators import ratelimit
from .models import Appointment
from .serializers import AppointmentSerializer

@method_decorator(ratelimit(key="ip", rate="10/h", method="POST", block=True), name="post")
class AppointmentCreateView(CreateAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            return Response(
                {"success": True, "message": "অ্যাপয়েন্টমেন্ট সফলভাবে জমা হয়েছে!", "id": obj.id},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"success": False, "errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

class AppointmentDetailView(RetrieveAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer

def print_appointment(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk)
    return render(request, "appointments/print.html", {"appointment": appointment})
