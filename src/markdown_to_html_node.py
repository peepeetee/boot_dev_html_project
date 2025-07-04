from markdown_blocks import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import *

from textnode import *

from inline_markdown import text_to_textnodes


def text_to_htmlnodes(text):
    text_nodes = text_to_textnodes(text)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return html_nodes

def block_to_html_node(block):
    block_type = block_to_block_type(block)
    
    if block_type == BlockType.QUOTE:
        children = []
        lines = block.split("\n")
        new_block = ""
        for line in lines:
            new_block = new_block + line[2:] + " "
            # children.append(text_to_htmlnodes(line))
        return_node = ParentNode("blockquote", text_to_htmlnodes(new_block[:-1]))
    elif block_type == BlockType.ULIST:
        children = []
        lines = block.split("\n")
        for line in lines:
            line = line[2:]
            children.append(ParentNode("li",text_to_htmlnodes(line)))
        return_node = ParentNode("ul", children)
            
            
    elif block_type == BlockType.OLIST:
        children = []
        i = 1
        lines = block.split("\n")
        for line in lines:
            line = line[len(str(i))+2:]
            children.append(ParentNode("li",text_to_htmlnodes(line)))
            i += 1
        return_node = ParentNode("ol", children)
        
        
    elif block_type == BlockType.CODE:
        
        lines = block.split("\n")
        
        processed_lines = lines[1:-1]
        # "\n".join(processed_lines)
        
        inside_node = LeafNode("code",value = "\n".join(processed_lines) + "\n")
        inside_node_list = [inside_node]
        return_node = ParentNode("pre", inside_node_list)
        
    elif block_type == BlockType.HEADING:
        
        
        if block.startswith(("###### ")):
            heading_level = 6
        elif block.startswith(("##### ")):
            heading_level = 5
        elif block.startswith(("#### ")):
            heading_level = 4
        elif block.startswith(("### ")):
            heading_level = 3
        elif block.startswith(("## ")):
            heading_level = 2
        elif block.startswith(("# ")):
            heading_level = 1
        else: raise Exception("Error in block_to_html_node at heading")
        
        new_block = block[heading_level+1:]
        new_block = new_block.replace("\n", "")
        
        return_node = ParentNode(f"h{heading_level}", text_to_htmlnodes(new_block))
        

    elif block_type == BlockType.PARAGRAPH:
        block = block.replace("\n", " ")
        children = text_to_htmlnodes(block)
        return_node = ParentNode("p", children)
    else: raise Exception("Unknown Type in block_to_html_node")
    
    return return_node
    



def markdown_to_html_node(markdown):
    # split the markdown into blocks
    
    blocks = markdown_to_blocks(markdown)
    
    # loop over each block
    children = []
    
    for block in blocks:
        
        
        children.append(block_to_html_node(block))
    
    return_node = ParentNode("div", children)
    
    return return_node


