
import re
import os 
import shutil
from pages import generate_page, generate_pages_recursive

def main():
    copy_static()
    generate_pages_recursive("./content", "./template.html", "./public")


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

main()