from markdown_blocks import markdown_to_blocks, block_to_block_type
from htmlnode import *

from textnode import *


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    



def markdown_to_html_node(markdown):
    # split the markdown into blocks
    
    blocks = markdown_to_blocks(markdown)
    
    # loop over each block
    
    for block in blocks:
        
        
        html_node = block_to_html_node(block)
    


