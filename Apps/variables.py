from .models import Cliente
from _datetime import datetime, date, timedelta
clientes=Cliente.objects.all()
clientes_vencidos=[]
proximos=[]
vencidos=0
for c in clientes:
    fecha=date(c.fechafirma.year+c.periodo,c.fechafirma.month, c.fechafirma.day)
    time=fecha-date.today()
    if time.days<=0:
        clientes_vencidos.append(c)
    if 0<time.days<=30:
        proximos.append(c)
vencidos=len(clientes_vencidos)+len(proximos)
def data_templates(request):
    return {
        'clientes_vencidos':clientes_vencidos,
        'vencidos':vencidos,
        'proximos':proximos,
    }