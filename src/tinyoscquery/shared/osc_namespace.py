import logging
from functools import lru_cache

from .osc_path_node import OSCPathNode

logger = logging.getLogger(__name__)


class OSCNamespace:
    def __init__(self):
        self._root = OSCPathNode("/", description="root node")

    @property
    def root_node(self) -> OSCPathNode:
        return self._root

    @property
    @lru_cache()
    def number_of_nodes(self) -> int:
        number_of_nodes = 0
        for _ in self._root:
            number_of_nodes += 1
        return number_of_nodes

    def add_node(self, node: OSCPathNode):
        if self.find_node(node.full_path) is not None:
            logger.warning(
                "Node (%s) already exists, not added again to namespace", node.full_path
            )
            return

        path = node.full_path.split("/")

        child_path = ""
        current_node = self._root

        for path_segment in path:
            if path_segment == "":
                continue
            child_path += "/" + path_segment

            if child_path == node.full_path:
                # All nodes up to the destination have been created, the last node is the actual node that is to be added
                child = node
            else:
                child = self.find_node(child_path)
            if not child:
                child = OSCPathNode(child_path)
            current_node.contents.append(child)
            current_node = child

        self.__class__.number_of_nodes.fget.cache_clear()

    def find_node(self, address: str) -> OSCPathNode:
        return self.root_node.find_subnode(address)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.number_of_nodes} nodes)"
