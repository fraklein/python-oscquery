import logging

logging.basicConfig(level=logging.DEBUG)
from tinyoscquery.osc_handler_wrapper import OSCHandlerWrapper
from tinyoscquery.shared.osc_path_node import OSCPathNode


class TestHandlerWrapper:
    def test_main(self):
        w = OSCHandlerWrapper(OSCPathNode("/test"))

        w()

