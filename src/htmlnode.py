

class HTMLNode:
    def __init__(self,tag = None, value = None, children = None, props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Not implemented")
    
    def props_to_html(self):
        return_string = ""
        if self.props is None:
            return return_string
        for prop in self.props:
            return_string += f" {prop}=\"{self.props[prop]}\""
        return return_string

    def __repr__(self):
        return f"tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props_to_html()}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        
    def to_html(self):
        if self.value == None:
            raise ValueError("Leaf node has no value")
        if self.tag == None:
            return self.value
        else:
            props_string = ""
            if self.props != None:
                props_string = self.props_to_html()
            return f"<{self.tag}{props_string}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("Parent node has no tag")
        elif self.children == None:
            raise ValueError("Parent node has no children")
        else:
            props_string = ""
            if self.props != None:
                props_string = self.props_to_html()
            return_string = f"<{self.tag}{props_string}>"
            
            for child in self.children:
                return_string += child.to_html()
                
            return_string += f"</{self.tag}>"
            
            return return_string
            
  