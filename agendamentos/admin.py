from django.contrib import admin
from .models import Cliente, Servico, agendamento
# Register your models here.

# Registro de modelos 
admin.site.register(Cliente)
admin.site.register(Servico)
admin.site.register(agendamento)
