from django.dispatch import Signal
from django.dispatch import receiver
from django.db.models.signals import pre_delete, post_delete
from notes.models import Notes


post_save_message_request = Signal(
    providing_args=['request', 'message']
)


post_save_message_response = Signal(
    providing_args=['request', 'response', 'message']
)


@receiver(pre_delete, sender=Notes)
def delete_empty_books(sender, instance, **kwargs):
    """Singal that deletes books without notes."""

    for book in instance.books_set.all():
        if book.notes.count() == 1:
            book.delete()

