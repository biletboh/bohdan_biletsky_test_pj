import json
import re

from django.conf import settings
from django.utils import timezone
import six

from notes.models import HttpRequest
from notes.signals import post_save_message_request, post_save_message_response


class HttpRequestMiddleware(object):

    def process_request(self, request):
        """
        Process incoming requests. If we're tracking this request, we'll store
        a created `HttpRequest` object in `request.request_message`.
        """

        request.request_message = None

        req_started_at = timezone.now()

        req_content_type = None
        req_headers = []

        for (key, value) in six.iteritems(request.META):
            if key.startswith('HTTP_'):
                key = key[5:].title()
                req_headers.append((key, value))
                if key == 'Content-Type':
                    req_content_type = value
        request.request_message = HttpRequest.objects.create(
            time=timezone.now(),
            remote_addr=request.META['REMOTE_ADDR'],
            req_method=request.method,
            req_path=request.path,
            req_protocol=request.META['SERVER_PROTOCOL'],
            req_headers_json=json.dumps(req_headers),
        )

        post_save_message_request.send(
            sender=self.__class__,
            request=request,
            message=request.request_message
        )

