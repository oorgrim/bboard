<<<<<<< Updated upstream
from django.conf import settings
from django.core.signing import Signer
from django.template.loader import render_to_string
=======
# заглушка

from django.core.signing import Signer
>>>>>>> Stashed changes

signer = Signer()

def send_activation_notification(user):
    if settings.ALLOWED_HOSTS:
        host = 'http://' + settings.ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'user': user, 'host': host, 'sign': signer.sign(user.username)}
    subject = render_to_string('email/activation_letter_subject.txt', context)
<<<<<<< Updated upstream
    body_text = render_to_string('email/activation_letter_body.txt', context)
    user.email_user(subject, body_text)
=======
    subject = render_to_string('email/activation_letter_subject.txt', context)
>>>>>>> Stashed changes
