import pytest

from tinyoscquery.shared.osc_namespace import OSCNamespace
from tinyoscquery.shared.osc_path_node import OSCPathNode


def path():
    return "/test"


@pytest.fixture
def namespace():
    return OSCNamespace()


class TestOSCNamespace:
    def test_empty_namespace_contains_root_node(self):
        # Arrange
        ns = OSCNamespace()
        # Act
        # Assert
        assert ns.root_node is not None
        assert ns.root_node.full_path == "/"
        assert ns.number_of_nodes == 1

    def test_namespace_with_one_toplevel_node_contains_two_nodes(self):
        # Arrange
        ns = OSCNamespace()
        # Act
        ns.add_node(OSCPathNode("/test"))
        # Assert
        assert ns.number_of_nodes == 2

    def test_namespace_repr(self):
        # Arrange
        ns = OSCNamespace()
        # Act
        # Assert
        assert ns.__class__.__name__ in repr(ns)
        assert str(ns.number_of_nodes) in repr(ns)

    def test_namespace_finds_added_node(self):
        # Arrange
        ns = OSCNamespace()
        node = OSCPathNode("/test/for/bar/baz")

        # Act
        ns.add_node(node)

        # Assert
        assert ns.find_node(node.full_path) is node

    def test_namespace_does_not_find_none_existing_node(self):
        # Arrange
        ns = OSCNamespace()
        node = OSCPathNode("/test/for/bar/baz")

        # Act
        ns.add_node(node)

        # Assert
        assert ns.find_node("/some/other/address") is None

    def test_namespace_adding_creates_missing_path_nodes(self):
        # Arrange
        ns = OSCNamespace()
        # Act
        ns.add_node(OSCPathNode("/test/foo/bar/baz"))
        # Assert
        assert ns.number_of_nodes == 5
        assert ns.find_node("/test") is not None
        assert ns.find_node("/test/foo") is not None
        assert ns.find_node("/test/foo/bar") is not None
        assert ns.find_node("/test/foo/bar/baz") is not None

    @pytest.mark.parametrize(
        "path",
        [
            "/",
            "/testing",
            "/testing/foo",
            "/testing/foo/bar",
        ],
        indirect=False,
    )
    def test_namespace_adding_child_with_same_path_does_nothing(self, path, namespace):
        # Arrange
        node = OSCPathNode(path)
        namespace.add_node(node)
        number_of_children_before_adding = namespace.number_of_nodes
        # Act
        namespace.add_node(OSCPathNode(path))
        # Assert
        assert namespace.number_of_nodes == number_of_children_before_adding
