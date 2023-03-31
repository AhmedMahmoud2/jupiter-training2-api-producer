import unittest, logging, os
import json

from testutils import test_setup
logger = logging.getLogger()
logger.setLevel(logging.getLevelName(os.environ.get("LOG_LEVEL", "DEBUG")))

# test specific imports
from handler import handler

logging.disable(logging.CRITICAL)

class FullHandlerTestCase(unittest.TestCase):

    def setUp(self):
        pass

    def test_full_handler(self):
        #if "SKIP_INTEGRATION_TESTS" in os.environ: print("skipped ..."); return

        event = test_setup.event("api-gateway-event-sample")

        r = handler.handler(event)
        #print(json.loads(r["body"]))
        
        self.assertEqual(r['statusCode'], 200, "Status code should be 200.")

        body = json.loads(r["body"])
        self.assertIn("message", body, "Body should contain 'message'")


    def test_full_handler_req_invalid(self):
        #if "SKIP_INTEGRATION_TESTS" in os.environ: print("skipped ..."); return

        event = test_setup.event("api-gateway-404-event-sample")

        r = handler.handler(event)

        self.assertEqual(r['statusCode'], 404, "Status code should be 404.")

        body = json.loads(r["body"])
        self.assertIn("code", body, "Error body should contain 'code'")
        self.assertIn("request", body, "Error body should contain 'request'")
        self.assertEqual(body["code"], "REQ_UNHANDLED_ROUTE", "Code should be UNHANDLED")


    def test_full_handler_heartbeat(self):
        #if "SKIP_INTEGRATION_TESTS" in os.environ: print("skipped ..."); return

        event = test_setup.event("api-gateway-heartbeat-event-sample")

        r = handler.handler(event)

        self.assertEqual(r['statusCode'], 200, "Status code should be 200.")

        body = json.loads(r["body"])
        self.assertIn("heartbeat", body, "Response should heartbeat property")

        h = body["heartbeat"]
        self.assertIn("timestamp", h, "Heartbeat should include timestamp")
        self.assertIn("name", h, "Heartbeat should include func name")
        self.assertIn("version", h, "Heartbeat should include func version")
        self.assertIn("status", h, "Heartbeat should include status")