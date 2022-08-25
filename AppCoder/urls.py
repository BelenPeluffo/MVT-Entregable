from django.urls import path
from AppCoder.views import curso, estudiantes, profesores, entregable

urlpatterns = [
    path('cursos/<nombre>/<camada>',curso),
    path('estudiantes/<nombre>/<apellido>/<email>',estudiantes),
    path('profesores/<nombre>/<apellido>/<email>/<profesion>',profesores),
    path('entregables/<nombre>/<fechaDeEntrega>/<entregado>',entregable),
]
