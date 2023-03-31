import unittest, logging, os
import json, jsonschema

from testutils import test_setup
logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG")))

# test specific imports
from handler.model import heartbeat

logging.disable(logging.CRITICAL)

class HeartbeatTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_model_heartbeat(self):
        # model tests are often skipped as they connect to a backend
        # inaccessible to GitHub, when tests are run by the GitHub Action
        if "SKIP_INTEGRATION_TESTS" in os.environ: print("skipped ..."); return

        # no input needed for heartbeat response
        r = heartbeat.heartbeat()

        self.assertIn("status", r, "Retrieve should include message field")
        self.assertEqual(r["status"], "EASIKIT_API_TEMPLATE", "Should return status")
