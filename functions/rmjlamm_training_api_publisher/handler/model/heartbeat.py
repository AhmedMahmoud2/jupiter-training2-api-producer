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

def heartbeat():
    '''this function, for best reporting would connect to any dependencies,
    such as databases or similar API backend status endpoints with username and password,
    to ensure a basic monitor would know if this API was misbehaving
    for this template, it just returns the basic config
    '''
    rslt = { "status": utils.getstatus() }

    return rslt