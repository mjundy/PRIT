from import_export import resources
from .models import PR
from import_export.fields import Field

class PRResource(resources.ModelResource):
    status__status = Field(attribute='status', column_name='status pr')

    class Meta:
        model = PR
        fields = ['tgl_pr',  'tgl_sent_to_purchase', 'partnumber', 'partname', 'qty', 'deskripsi','status__status']
    def get_queryset(self):
        return PR.objects.exclude(status__status="Received")

class ReceivedPRResource(resources.ModelResource):
    status__status = Field(attribute='status', column_name='status pr')

    class Meta:
        model = PR
        fields = ['tgl_pr', 'tgl_sent_to_purchase', 'tgl_terima', 'partnumber', 'partname', 'qty', 'deskripsi','status__status']
    def get_queryset(self):
        return PR.objects.filter(status__status="Received")