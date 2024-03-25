from pages import generate_site

def main():
    copy_static()
    generate_pages_recursive("./content", "./template.html", "./public")

main()