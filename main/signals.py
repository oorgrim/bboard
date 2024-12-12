<<<<<<< Updated upstream
from django.dispatch import Signal, receiver

=======
from django.dispatch import Signal  
>>>>>>> Stashed changes
from main.utilities import send_activation_notification

post_register = Signal()

@receiver(post_register)
<<<<<<< Updated upstream
def post_register_dispatcher(sender, **kwargs):
=======
def post_register_dispatcher(sender,  **kwargs): # имя неважно
>>>>>>> Stashed changes
    send_activation_notification(kwargs['instance'])
