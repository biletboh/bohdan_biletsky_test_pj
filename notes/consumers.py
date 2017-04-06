from channels import Group
from channels.sessions import channel_session
from notes.models import HttpRequestStorage


@channel_session
def ws_connect(message):
    request_list = HttpRequestStorage.objects.all()[0:10]
    Group('request_list').add(message.reply_channel)
    message.channel_session['request_list'] = 'requests'

@channel_session
def ws_receive(message):
#    prefix, label = message['path'].strip('/').split('/')
#    request_list = HttpRequestStorage.objects.all()[0:10]
#    Group('request_list').add(message.reply_channel)
    message.reply_channel.send({
        "text": message.content['text'],
    })

    #message.reply_channel.send({'request_list'] = 
