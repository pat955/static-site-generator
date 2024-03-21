import re 
import os
from blocks import markdown_to_html_node, markdown_to_blocks, block_to_block_type

def extract_title(markdown):
    #raise error if no title is present 
    return re.match(r"[#]{1}[ ](.*)", markdown)[0][2:]

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page...")
    
    with open(from_path, "r") as f:
        from_markdown = f.read()

    with open(template_path, "r") as f:
        temp_markdown = f.read()

    html = markdown_to_html_node(from_markdown).to_html()
    title = extract_title(from_markdown)

    temp_markdown = temp_markdown.replace("{{ Title }}", title)
    temp_markdown = temp_markdown.replace("{{ Content }}", html)
    with open(dest_path, "a") as f:
        f.write(temp_markdown)
    
def r_generate_pages(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for i in files:
        if os.path.isfile(f"{dir_path_content}/{i}"):
            print(f"Generating {i}")
            generate_page(f"{dir_path_content}/{i}", template_path, f"{dest_dir_path}/{i}.html")

        else:
            os.mkdir(f"{dest_dir_path}/{i}")
            r_generate_pages(f"{dir_path_content}/{i}", template_path, f"{dest_dir_path}/{i}")
