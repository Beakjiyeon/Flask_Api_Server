from flask import has_request_context, request
import logging
class RequestFormatter(logging.Formatter):
    def format(self, record):
        if has_request_context():
            from ..service.validation import validate_request_service
            if validate_request_service(request.url):
                record.url = f"{request.url.split('/')[3]}/{request.url.split('/')[4]}"
            else:
                record.url = 'ILLEGAL-SERVICE'
            record.remote_addr = request.remote_addr
        else:
            record.url = None
            record.remote_addr = None
        return super().format(record)