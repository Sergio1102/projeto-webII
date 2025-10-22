from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.listarEventos, name='listarEventos'),
    path('eventos/', views.listarEventos, name='listarEventos_explicit'),
    path('evento/<int:id>/', views.detalharEvento, name='detalharEvento'),
    path('evento/novo/', views.criarEvento, name='criarEvento'),
    path('evento/<int:id>/editar/', views.atualizarEvento, name='atualizarEvento'),
    path('evento/<int:id>/apagar/', views.apagarEvento, name='apagarEvento'),
    path('evento/<int:id>/inscrever/', views.inscrever_evento, name='inscrever_evento'),
    
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    
    path('locais/', views.listarLocais, name='listarLocais'),
    path('local/novo/', views.criarLocal, name='criarLocal'),    
    path('local/<int:id>/editar/', views.atualizarLocal, name='atualizarLocal'),   
    path('local/<int:id>/apagar/', views.apagarLocal, name='apagarLocal'),
    
    path('palestrantes/', views.listarPalestrantes, name='listarPalestrantes'),
    path('palestrante/novo/', views.criarPalestrante, name='criarPalestrante'),
    path('palestrante/<int:id>/editar/', views.atualizarPalestrante, name='atualizarPalestrante'),    
    path('palestrante/<int:id>/apagar/', views.apagarPalestrante, name='apagarPalestrante'),

    path('categorias/', views.listarCatEventos, name='listarCatEventos'),
    path('categoria/novo/', views.criarCatEvento, name='criarCatEvento'),
    path('categoria/<int:id>/editar/', views.atualizarCatEvento, name='atualizarCatEvento'),
    path('categoria/<int:id>/apagar/', views.apagarCatEvento, name='apagarCatEvento'),

    path('', include('django.contrib.auth.urls')), 
    path('register/', views.register, name='register'),
]