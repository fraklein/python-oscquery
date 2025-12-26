from tinyoscquery.shared.osc_namespace import OSCNamespace
from tinyoscquery.shared.osc_path_node import OSCPathNode


class TestOSCNamespace:
    def test_empty_namespace_contains_root_node(self):
        # Arrange
        ns = OSCNamespace()
        # Act
        # Assert
        assert ns.root_node is not None
        assert ns.number_of_nodes == 1

    def test_namespace_with_one_toplevel_node_contains_two_nodes(self):
        # Arrange
        ns = OSCNamespace()
        ns.add_node(OSCPathNode("/test"))
        # Act
        # Assert
        assert ns.number_of_nodes == 2
