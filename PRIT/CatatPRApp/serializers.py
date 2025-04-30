from CatatPRApp.models import PR
from rest_framework import serializers

class PRSerializer(serializers.ModelSerializer):
    class Meta:
        model = PR
        fields = ['tgl_pr', 'partnumber', 'partname', 'qty', 'deskripsi', 'status', 'tgl_sent_to_purchase', 'tgl_terima']
        