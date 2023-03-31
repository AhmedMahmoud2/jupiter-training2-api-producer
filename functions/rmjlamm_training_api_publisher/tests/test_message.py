import unittest, logging, os
import json, jsonschema

from testutils import test_setup
logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG")))

# test specific imports
from handler import service

logging.disable(logging.CRITICAL)

class MessageTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_message(self):
        ##if "SKIP_INTEGRATION_TESTS" in os.environ: print("skipped ..."); return

        # # the data in this file should match the data you're expecting
        # # to be sent to the lambda or the data once it's been converted
        # # (assuming that conversion has got separate unit testing)
        # data = test_setup.jsonload("sns-message-entity-sample")

        # entity    = "<entity-name>"
        # mode      = "event"
        # resp_type = None

        # # load the schema from our schemas folder
        # edms = "../../edm-schemas"
        # schemafile = edms + f"/{entity}/{entity}-{mode}-schema.json"
        # with open(schemafile) as f:
        #     schema = json.load(f)

        # # assuming you have a "create_message" wrapper for sns.create_message
        # # in your service module, call that here
        # body = service.create_message(data)

        # # compare
        # t = jsonschema.validate(instance=body, schema=schema)

        # self.assertIsNone(t, f"Message should validate against {schemafile}.")
        pass
