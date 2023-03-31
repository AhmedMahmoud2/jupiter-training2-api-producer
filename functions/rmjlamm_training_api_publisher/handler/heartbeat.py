import logging
logger = logging.getLogger()

# easikit imports
from easiutils import service as sv, exceptions as er, easiutils as eu

# project specific imports
from handler.model import heartbeat


# the heartbeat module is intended to give a single endpoint healthcheck for the function
# ideally this means an end-to-end check of all the components - ensuring it can connect
# to the backend, checking networking, username/password and any other useful dependencies
# in a single api call
# if this isn't possible, delete this module and the basic easikit docker module will
# return a standard heartbeat response (i.e. timestamp, function name and version)

def get_heartbeat():
    '''a bespoke way to handle the /heartbeat route
    checks with backend via model, then combines that to returns a message,
    a timestamp and the contents of feature.properties
    (i.e. the function name and version)
    '''

    # using sv.handle_request handles all errors raised in standard way
    with sv.handle_request() as h:
        # get any heartbeat status info from backend via model
        # get a timestamp, extract the function properties and 
        # pass the package back to the handler
        data = heartbeat.heartbeat()

        h.resp = {
            "body": {
                "heartbeat": {
                    "timestamp": eu.timestamp(),
                    **eu.get_config(),
                    **data
                }
            },
            "status": 200
        }

    return h.resp