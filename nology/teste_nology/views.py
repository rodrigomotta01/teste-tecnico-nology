from django.shortcuts import get_object_or_404, render
from django.views.generic import CreateView, ListView
from django.urls import reverse_lazy
from .models import Compra
from .forms import CompraForm
from .utils import get_ip

from .cashback_nology import Cliente, ClienteVIP
# Create your views here.

class criar_compra_view(CreateView):
    model = Compra
    form_class = CompraForm
    template_name = 'compra_create.html'
    success_url = reverse_lazy('listar_compras')

    def form_valid(self, form):
        compra = form.save(commit=False)
        valor_compra = compra.valor_compra
        compra.ip_cliente = get_ip(self.request)
        if compra.tipo_cliente == 'comum':
            cashback = Cliente.calc_cashback(valor_compra, 0)
        else:
            cashback = ClienteVIP.calc_cashback(valor_compra, 0)
        compra.cashback = cashback
        compra.save()
        return super().form_valid(form)
    
class listar_compras_view(ListView):
    model = Compra
    template_name = 'compra_list.html'
    context_object_name = 'compras'

    def get_queryset(self):
        ip = get_ip(self.request)
        return Compra.objects.filter(ip_cliente=ip)
