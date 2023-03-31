import logging
logger = logging.getLogger()

# easikit imports
from easiutils import service as sv, exceptions as er

# project specific imports
from handler.model import entity


# the service file acts as go-between for the handler (user interaction) and the
# model (backend interaction), it takes data from the incoming request or event
# and converts it into basic dictionaries for the model to process onward
# it does not know anything about how the backend works and does not know how
# the incoming events are recieved, but it does know what they contain and
# what data the backend needs

# replace get_<entity> with the name of actual resource
def get_entity(req=None):
    '''handles the GET method on <entity>, extracting data from
    the easikit request object and passing it to the model to
    mediate with the backend, then marshalling the response from
    the model into something the front end format
    '''

    # using sv.handle_request handles all errors raised in standard way
    with sv.handle_request() as h:
        # extract the full path from request, pass it to the <entity>
        # class and pass the data retrieved back to the handler
        # (also pass the full req, for demo purposes)
        uri = req["full_path"]
        data = entity.retrieve(uri, req)
        h.resp = { "body": data, "status": 200 }

    return h.resp


def post_entity(payload):
    '''handles the POST method on <entity>, extracting data from
    the incoming body payload, passing it to the model to
    mediate with the backend, then marshalling the response from
    the model into something the front end format
    '''

    # using sv.handle_request handles all errors raised in standard way
    with sv.handle_request() as h:
        data = entity.create(payload)
        h.resp = {
            "body": None,
            "status": "201",
            "content": "text/plain"
        }

    return h.resp