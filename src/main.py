from pages import generate_pages_recursive, copy_static

def main():
    copy_static()
    generate_pages_recursive("./content", "./template.html", "./public")

main()