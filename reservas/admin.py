from django.contrib import admin
from .models import ReservaVuelo, Venta, Pago

# Register your models here.
admin.site.register(ReservaVuelo)
admin.site.register(Venta)
admin.site.register(Pago)
