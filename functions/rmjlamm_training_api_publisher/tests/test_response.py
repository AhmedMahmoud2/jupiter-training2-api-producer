import unittest, logging, os
import json, jsonschema

from testutils import test_setup
logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG")))

# test specific imports
from handler import handler

logging.disable(logging.CRITICAL)

class ResponseTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_response(self):
        #if "SKIP_INTEGRATION_TESTS" in os.environ: print("skipped ..."); return

        event = test_setup.event("api-gateway-event-sample")
        print ('''

#########################################################################################
#                                                                                       #
#  The test_response.py and test_message.py tests cannot be instantiated until a        #
#  schema has been created. To create a schema using EASIKit run the below to get       #
#  full command details:                                                                #
#                                                                                       #
#  >  e edm -h                                                                          #
#                                                                                       #
#  Once complete, change the entity, mode and resp_type below to validate your body     #
#  against that schema (you'll probably then have to check your handler tests)          #
#                                                                                       #
#########################################################################################
        ''')
        # r = handler.handler(event)
        # entity    = "<entity_name>"
        # mode      = "<event or endpoint>"
        # resp_type = "<collection or individual - endpoints only>"

        # # load the schema from our schemas folder
        # edms = "../../edm-schemas"
        # if mode == "endpoint":
        #   schemafile = edms + f"/{entity}/{entity}-{mode}-{resp_type}-schema.json"
        # else:
        #   schemafile = edms + f"/{entity}/{entity}-{mode}-schema.json"
        # with open(schemafile) as f:
        #     schema = json.load(f)

        # # parse the body string to actual json
        # body = json.loads(r["body"])

        # # compare
        # t = jsonschema.validate(instance=body, schema=schema)

        # self.assertIsNone(t, f"Body should validate against {schemafile}.")
