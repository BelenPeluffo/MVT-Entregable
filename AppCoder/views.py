from django.shortcuts import render
from AppCoder.models import Curso,Estudiante,Profesor,Entregable

# Create your views here.
def curso(request,nombre,camada):
    context={
        "nombre":nombre,
        "camada":camada,
    }
    curso=Curso(nombre=nombre,camada=camada)
    curso.save()
    return render(request,'AppCoder/cursos.html',context)

def estudiantes(request,nombre,apellido,email):
    context={
        "nombre":nombre,
        "apellido":apellido,
        "email":email,
    }
    estudiante=Estudiante(nombre=nombre,apellido=apellido,email=email)
    estudiante.save()
    return render(request,'AppCoder/estudiantes.html',context)

def profesores(request,nombre,apellido,email,profesion):
    context={
        "nombre":nombre,
        "apellido":apellido,
        "email":email,
        "profesion":profesion,
    }
    profesor=Profesor(nombre=nombre,apellido=apellido,email=email,profesion=profesion)
    profesor.save()
    return render(request,'AppCoder/profesores.html',context)

def entregable(request,nombre,fechaDeEntrega,entregado):
    context={
        "nombre":nombre,
        "fechaDeEntrega":fechaDeEntrega,
        "entregado":entregado,
    }
    entregable=Entregable(nombre=nombre,fechaDeEntrega=fechaDeEntrega,entregado=entregado)
    entregable.save()
    return render(request,'AppCoder/entregables.html',context)