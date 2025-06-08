import unittest

from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_noneprint(self):
        node = HTMLNode()
        print("\n")
        print(node)
    def test_print(self):
        child_node1 = HTMLNode("tag1", "This is a child node", None, None)
        child_node2 = HTMLNode("tag2", "This is a child node", None, {"href": "https://www.google.com","target": "_blank",})
        parent_node = HTMLNode("tag3", "This is a parent node", [child_node1, child_node2], None)
        print("\n")
        print(child_node1)
        print(child_node2)
        print(parent_node)
    def test_print_props(self):
        child_node2 = HTMLNode("tag", "This is a child node", None, {"href": "https://www.google.com","target": "_blank",})
        print("\n")
        print(child_node2.props_to_html())
        
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    # def test_repr(self):
    #     node = HTMLNode(
    #         "p",
    #         "What a strange world",
    #         None,
    #         {"class": "primary"},
    #     )
    #     self.assertEqual(
    #         node.__repr__(),
    #         "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
    #     )
    
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_with_props(self):
        node = LeafNode("p", "Hello, world!", {"href": "https://www.google.com","target": "_blank",})
        self.assertEqual(node.to_html(), "<p href=\"https://www.google.com\" target=\"_blank\">Hello, world!</p>")   

    def test_leaf_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(
            node.to_html(),
            '<a href="https://www.google.com">Click me!</a>',
        )

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")


    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )


if __name__ == "__main__":
    unittest.main()