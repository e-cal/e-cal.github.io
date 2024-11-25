# Website

This is my fourth iteration of my website. 

- All content is in markdown, site is vanilla html and css
- All html apart from the template is completely generated (via pandoc)
- Python script to render X posts as html
- Hosted on github pages
  - jekyll automatically handles all the routing for me

build script:

```sh
#!/usr/bin/env bash

# Find all markdown files in md/ and translate to html with a mirrored path
find md/ -name "*.md" | while read -r md_file; do
    out=$(echo "$md_file" | sed -e 's/md\///' -e 's/\.md/\.html/')
    output_dir=$(dirname "$out")
    mkdir -p "$output_dir"
    css=$(find styles/ -name "*.css" -exec echo --css=/{} \;)
    python process.py "$md_file" | pandoc -f gfm --mathjax $css --template=template.html --standalone -t html -o "$out" 2>/dev/null
    echo "Processed: $md_file -> $out"
done
```

## New Site


The only fancy bit is the python script that parses out x posts and renders them
as html (instead of using embeds or just linking).

## Previous versions

### Customized Gatsby tech portfolio template

<span style="display: flex; justify-content: space-between; width: 100%">
<img src="/assets/site1-home.png" style="width: 49%">
<img src="/assets/site1-projects.png" style="width: 49%">
</span>


Thought this one was uninspired. 

Using a template is fine, I don't judge others for it, but personally I always felt a little ashamed that I didn't _really_ build my website myself.

### Single page pure html/css/js with client-rendered interactive background

<span style="display: flex; justify-content: space-between; width: 100%">
<img src="/assets/site2-home.png" style="width: 49%">
<img src="/assets/site2-projects.png" style="width: 49%">
</span>

Very proud of the look and feel of this one. However, the complexity had lots of
little visual bugs that got increasingly annoying to fix, and the interactive
background could be slow or buggy on certain devices. Client side rendering a
bunch of particles and interactions is just a bit gimmicky and unnecessary for a
personal website. Still super cool and fun to build though.

### Fully custom htmx / python / jinja2 / html & css server side rendered site

<span style="display: flex; justify-content: space-between; width: 100%">
<img src="/assets/site3-home.png" style="width: 49%">
<img src="/assets/site3-projects.png" style="width: 49%">
</span>

I'm a big fan of htmx, but shoehorning it into a static personal website just
doesn't make any sense. Also a looping mp4 background made the initial load time
really slow, and the design was unique but I got tired of it after awhile.


