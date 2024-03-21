
import re
import os 
import shutil
from textnode import TextNode
from htmlnode import LeafNode, HTMLNode
from split_nodes import *
from pages import generate_page, r_generate_pages

def main():
    copy_static()
    r_generate_pages("./content", "./template.html", "./public")


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