import unittest, logging, os
import json, jsonschema

from testutils import test_setup
logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG")))

# test specific imports
from handler.model import entity

logging.disable(logging.CRITICAL)

class EntityTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_model_entity_retrieve(self):
        # model tests are often skipped as they connect to a backend
        # inaccessible to GitHub, when tests are run by the GitHub Action
        if "SKIP_INTEGRATION_TESTS" in os.environ: print("skipped ..."); return

        # unit test only needs enough data required to prove functionality
        uri = "https://aais.integration-dev.ucl.ac.uk/easiutils/test"
        req = { "path": uri, "method": "GET" }
        r = entity.retrieve(uri)

        self.assertIn("message", r, "Retrieve should include message field")
        self.assertIn("incoming_uri", r, "Retrieve should include uri field")
        self.assertEqual(r["incoming_uri"], uri, "URI should match input")


    def test_model_compose_entity(self):
        # test that the data format sent from the service
        # is transformed in the data format expected by the backend
        # with whatever conditions you have for including fields
        pass


    def test_model_entity_create(self):
        # test each major block of code individually in the appropriate test file
        pass