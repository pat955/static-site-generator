import re 
import os
from blocks import markdown_to_html_node

def extract_title(markdown):
    #raise error if no title is present 
    return re.match(r"[#]{1}[ ](.*)", markdown)[0][2:]

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page ")
    from_markdown = None
    temp_markdown = None
    with open(from_path, "r") as f:
        from_markdown = f.read()

    with open(template_path, "r") as f:
        temp_markdown = f.readlines()

    if not os.path.exists(dest_path):
        os.mkdir(dest_path)

    html = markdown_to_html_node(from_markdown).to_html()
    title = extract_title(from_markdown)
    
