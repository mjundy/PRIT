from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from CatatPRApp.models import PR

@receiver(pre_save, sender=PR)
def update_received_and_sent_dates(sender, instance, **kwargs):
    try:
        # Ambil objek PR sebelumnya dari database
        previous_pr = PR.objects.get(id=instance.id)
    except PR.DoesNotExist:
        # Jika PR baru, tidak ada perubahan status
        return

    # Cek jika status berubah
    if instance.status != previous_pr.status:
        # Jika status baru adalah "Received", simpan tanggal saat ini
        if instance.status.status == "Received":
            instance.received_date = timezone.now().date()

        # Jika status baru adalah "Sent to Purchase", simpan tanggal saat ini
        if instance.status.status == "Sent to Purchase":
            instance.sent_to_purchase = timezone.now().date()
            #instance.save()