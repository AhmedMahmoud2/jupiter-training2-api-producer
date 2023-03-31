import logging, os
logger = logging.getLogger()

# easikit imports
from easiutils import exceptions as er


# utils files are intended as functions that can be used by multiple
# files within that folder, not as a way to make a single file shorter
# if a function can only be used by one process, create a specific file for it

def getmessage(message=None):
    if message == None:
      message = "Hello! Your world executed successfully from: " + os.getcwd()

    return message


def getstatus():
    return "EASIKIT_API_TEMPLATE"