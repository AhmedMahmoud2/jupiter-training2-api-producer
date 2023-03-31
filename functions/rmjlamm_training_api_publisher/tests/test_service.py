import unittest, logging, os
from unittest.mock import patch
import json, jsonschema

from testutils import test_setup
logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG")))

# easiutils imports
from easiutils import exceptions as er

# test specific imports
from handler import service

logging.disable(logging.CRITICAL)

class ServiceTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_service_get_entity(self):
        # if "SKIP_INTEGRATION_TESTS" in os.environ: print("skipped ..."); return

        # unit test only needs enough data required to prove functionality
        uri = "https://aais.integration-dev.ucl.ac.uk/easiutils/test"
        req = { "full_path": uri, "method": "GET" }
        r = service.get_entity(req)

        self.assertIn("body", r, "Response should have body field")
        self.assertIn("status", r, "Response should have status field")
        self.assertIn("message", r["body"], "Body should have message field")
        self.assertEqual(r["status"], 200, "Status should be 200")


    @patch("handler.model.entity")
    def test_service_get_entity_error(self, mockery):
        # mock the actual model/backend to ensure you get the response you
        # are testing your service layer's ability to handle; the model/entity
        # unit tests should test how the model works, the service can thus
        # assume it works correctly and just deal with waht it returns

        # mock model.entity generating an exception
        # to test that service.get_entity handles it as expected
        mockery.return_value = er.UclError()

        # the service methods using the "with sv.handle_request()" context
        # manager should handle exceptions, so nothing need be caught here
        uri = "https://aais.integration-dev.ucl.ac.uk/easiutils/test"
        req = { "path": uri, "method": "GET" }
        r = service.get_entity(req)

        # test it raises the right exception
        self.assertIsInstance(r, er.UclError, "Should generate UclError")
        self.assertEqual(r.type, er.GENERIC, "Should return generic error")


    def test_service_post_entity(self):
        # test each major block of code individually in the appropriate test file
        pass