from django.db import models
from django.contrib.auth.models import User
from django.db.models import Max

# Create your models here.


class Message(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user')
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='from_user')
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='to_user')
    body = models.TextField(max_length=1000, blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    is_read = models.BooleanField(default=True)

    def senf_message(from_user, to_user, body):
        sender_message = Message(
            user=from_user,
            sender=from_user,
            recipient=to_user,
            body=body,
            is_read=True
        )
        sender_message.save()

        recipient_message = Message(
            user=to_user,
            sender=from_user,
            body=body,
            recipient=from_user
        )
        recipient_message.save()

        return sender_message

    def get_messages(user):
        users = []
        messages = Message.objects.filter(user=user).values(
            'recipient').annotate(Last=Max('date')).order_by('-last')
        for messages in message:
            users.append({
                'user': User.objects.get(pk=message['recipient']),
                'last': message['last'],
                'unread': Message.objects.filter(user=user, recipient__pk=message['recipient'], is_read=False).count()
            })
        return users