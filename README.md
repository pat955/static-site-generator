# Static Site Generator
Converts markdown files to html and pushes it to your localhost. Customize the appearance via. css

## How to use
### Clone project
In your terminal using git:
```bash
git clone https://github.com/pat955/static-site-generator/
```
### Run Example Site
Then, move into the content folder and start creating your markdown files. Before doing that, run this (while in folder) to see an example:
```bash
cd static-site-generator
./main.sh
```
Now visit [localhost:8888](http://localhost:8888/)
Feel free to delete everything inside the static/images folder and everything inside content, **however** remember to have keep index.md inside content. This acts as your frontpage. 

To exit press: **Ctrl + C** or **Cmd + .**

> **Not yet tested on Mac**

### Adding more pages
To add another page, simply add a folder to /content, and create a markdown file named **"index.md"** 

In your main index file you can do something like this to "link" it:
```
Hello! Read my [first post here](/example)
```
Or if you want to go backwards (added the | because of a bug, fixing it soon):
```
|[Back Home](/)|
```
This can also be chained: (/example/more_info/something_else)
To go back one "chain": (..)
If you're not familiar with markdown, take a look at this site for the basics: [markdownguide.org](https://www.markdownguide.org/getting-started/) **OBS:** Not everything may be supported

## Customize apperance
Right now the static site generator will only create dark pages, to change the colors, fonts and sizes, find **index.css** at the root of the project. 
```
body {
    background-color: #0d1117; 
    color: #c9d1d9;
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
    line-height: 1.5;
    margin: 0;
    padding: 20px;
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}
```
Mess around with the colors and rerun the program to see how your new pages look!

# Contributing
Python version: 3.12
### Clone project
```bash
git clone https://github.com/pat955/static-site-generator
```
### Download dependencies
Install pip and python if you haven't already

### Run Script
Run the script instead of main.py, the script also starts localhos
```bash
./scripts/main.sh
```

### Run the tests

```bash
./scripts/tests.sh
```

### Submit a pull request

If you'd like to contribute, please fork the repository and open a pull request to the `main` branch.

# Roadmap
- [ ] Clean up code, issues, better documentation
- [ ] Folder structure
- [ ] Templates
- [ ] Easier way to customize look
