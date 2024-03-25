import re 
import os
import shutil
from blocks import markdown_to_html_node, markdown_to_blocks, block_to_block_type

def copy_static():
    if os.path.exists("./public/"):
        shutil.rmtree("./public/")
    os.mkdir("./public/")
    copy_static_recursive("./static", "./public")


def copy_static_recursive(p, destination):
    static_files = os.listdir(p)
    for file in static_files:
        print(f'Moving "{file}"...')
        if "." in file:
            shutil.copy(f"{p}/{file}", destination)
            
        else:
            os.mkdir(f"{destination}/{file}/")
            copy_static_recursive(f"{p}/{file}/", f"{destination}/{file}/")


def extract_title(markdown):
    try:
        return re.match(r"[#]{1}[ ](.*)", markdown)[0][2:]
    except:
        raise Exception("No title in markdown file!")

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
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    files = os.listdir(dir_path_content)
    for i in files:
        if os.path.isfile(f"{dir_path_content}/{i}"):
            print(f"Generating {i}")
            # replace with regex
            file_name = i.split('.')[0]+'.html'
            generate_page(f"{dir_path_content}/{i}", template_path, f"{dest_dir_path}/{file_name}")

        else:
            os.mkdir(f"{dest_dir_path}/{i}")
            generate_pages_recursive(f"{dir_path_content}/{i}", template_path, f"{dest_dir_path}/{i}")


def generate_site(dir_path_content, template_path, dest_dir_path):
    copy_static()
    generate_pages_recursive(dir_path_content, template_path, dest_dir_path)