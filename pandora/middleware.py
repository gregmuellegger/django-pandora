from pandora import box


class RequestMiddleware(object):
    def process_request(self, request):
        box['request'] = request


class UserMiddleware(object):
    def process_request(self, request):
        box['user'] = request.user
