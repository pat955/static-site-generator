# Static Site Generator
Converts markdown files to html and pushes it to your localhost. Customize the appearance via. css

## How to use
In your terminal using git:
```
git clone https://github.com/pat955/static-site-generator/
```

Then, move into the content folder and start creating your markdown files. Before doing that, run this (while in folder) to see an example:
```
./main.sh
```

Now visit [localhost:8888](http://localhost:8888/)
Feel free to delete everything inside the static/images folder and everything inside content, **however** remember to have keep index.md inside content. This acts as your frontpage. 

To exit press: **Ctrl + C** or **Cmd + .**

> **Not yet tested on Mac**


## Changing appearance
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


## Adding more pages
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
