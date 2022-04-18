
from django.urls import path
from app_entrega1.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name = "Inicio"),
    path('about/', about_me, name = "Acerca de mi"),
    # Autores
    path('autores/', autores, name = "Autores"),
    path('autoresFormulario/', formulario_autores, name = "Formulario_Autores"),
    # Libros
    path('libros/lista/', LibrosList.as_view(), name = "Lista"),
    path('nuevo/', LibrosCreate.as_view(), name = "Crear"),
    path('<pk>/', LibrosDetail.as_view(), name = "Detalle"),
    path('editar/<pk>/', LibrosUpdate.as_view(), name = "Editar"),
    path('borrar/<pk>/', LibrosDelete.as_view(), name = "Eliminar"),
    # Busqueda
    path('librosBuscar/', buscar_libros, name = "Buscar_Libros"),
    # Login
    path('accounts/login', iniciar_sesion, name = "Login"),
    path('accounts/logout', LogoutView.as_view(template_name = 'app_entrega1/logout.html'), name = "Logout"),
    path('accounts/signup', registro, name = "Signup"),
    path('accounts/profile', editar_usuario, name = "Edit")
    ]
