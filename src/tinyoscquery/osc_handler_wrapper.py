import logging

from tinyoscquery.shared.osc_path_node import OSCPathNode


logger = logging.getLogger(__name__)

class OSCHandlerWrapper:
    def __init__(self, node:OSCPathNode):
        self.node = node

    def __call__(self, *args, **kwargs):
        logger.debug(f"OSCHandlerWrapper {self.node.full_path} called with args={args} kwargs={kwargs}")
