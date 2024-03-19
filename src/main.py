
import re
import os 
import shutil
from textnode import TextNode
from htmlnode import LeafNode, HTMLNode
from split_nodes import *
from pages import generate_page

def main():
    copy_static()
    generate_page("./content/index.md", "./template.html", "./public/index.html")


def copy_static():
    if os.path.exists("./public/"):
        shutil.rmtree("./public/")
    os.mkdir("./public/")
    r_copy_static("./static", "./public")


def r_copy_static(p, destination):
    static_files = os.listdir(p)
    for file in static_files:
        print(f'Moving "{file}"...')
        if "." in file:
            shutil.copy(f"{p}/{file}", destination)
            
        else:
            os.mkdir(f"{destination}/{file}/")
            r_copy_static(f"{p}/{file}/", f"{destination}/{file}/")



main()