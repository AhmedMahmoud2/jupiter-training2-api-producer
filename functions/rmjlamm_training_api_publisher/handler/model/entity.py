import logging
logger = logging.getLogger()

# easikit imports
from easiutils import exceptions as er

# project specific imports
from handler.utils import utils


# the model package should be a set of files, each of which is responsible
# for managing a different entity
# for small interfaces one file might manage multiple entities but generally
# the files would be split up
# if there is common code amongst entities, a model_utils type file would
# be created and imported by each individual entity

def retrieve(uri=None, req=None):
    '''gets values from the the API call via the service
    and converts them into the format needed by the backend,
    passes the converted values to the backend and converts the
    response into the something the service can use to pass back
    to the user
    '''
    mssg = utils.getmessage()
    rslt = compose_entity(mssg, uri, req)

    return rslt

def compose_entity(mssg, uri, req):
    '''units of functionality - such as translating data - are often split out
    into their own functions to allow easier testing
    '''
    entity = {
        "message": mssg,
        "incoming_uri": uri,
        "easikit_request": req
    }
    return entity


def create(payload):
    '''takes the incoming body, converts it and sends it back
    under other circumstances would do the same as above but for 
    '''
    try:
        rslt = dict(payload)

    except Exception as ex:
        # exceptions outside the service layer should be raised, not handled
        # this allows the service layer to decide how to handle them
        # (though that will invariably be by passing them straight back
        # to the user)
        # all raised errors should be of er.UclError type or subtype
        raise er.UclError(ex)

    return rslt