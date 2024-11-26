---
title: projects/website
---

# Website

This is my fourth iteration of my website.

<div class="bullets-no-spacing">

- All content is in markdown, site is vanilla html and css
- Hosted on github pages ([here](https://github.com/e-cal/e-cal.github.io))
- <details><summary>All html apart from the template is completely generated (via pandoc)</summary>

  ```sh
  # from build script
  CSS_FILES=$(find styles/ -name "*.css" -exec echo --css=/{} \;)
  python process.py "$md_file" | \
      pandoc \
          $CSS_FILES \
          -f gfm \
          --mathjax \
          -t html \
          --template=template.html \
          --metadata title="$title" \
          --standalone \
          -o "$out"
  ```
  </details>
- <details><summary>Python script to render X posts as html</summary>

  ```python
  def tweet_to_html(url, tweet):
      html = f"""<blockquote>
  <div class="tweet">
  <div class="tweet-header">
  <a href="{url}"><img class="tweet-profile-pic" src="{tweet.user.profile_image_url}" /><span class="tweet-header-text">{tweet.user.name}<span class="tweet-screen-name">@{tweet.user.screen_name}</span></span></a>
  </div>
  <div class="tweet-body">
  {tweet.text}
  """
      if tweet.media:
          for m in tweet.media:
              html = html.replace(m["url"], "")
              html += f'\n<img class="tweet-image" src="{m["media_url_https"]}" />\n'
      html += "</div>\n</div>\n</blockquote>"
      return html
  ```
  </details>
- <details> <summary>Inject code syntax highlighting via shiki</summary>

  ```html
  <script type="module">
    import { codeToHtml } from "https://esm.sh/shiki@1.0.0";

    async function highlightCode() {
      const preBlocks = document.querySelectorAll("pre");
      for (const block of preBlocks) {
        var code = block.textContent;
        const lang = block.className.replace("sourceCode ", "");

        block.innerHTML = await codeToHtml(code, {
          lang: lang,
          theme: "catppuccin-mocha",
        });
      }
    }

    highlightCode();
  </script>
  ```

  </details>

</div>


## Previous versions

### 3. Fully custom htmx / python / jinja2 / html & css server side rendered site

<span style="display: flex; justify-content: space-between; width: 100%">
<img src="/assets/site3-home.png" style="width: 49%">
<img src="/assets/site3-projects.png" style="width: 49%">
</span>

I'm a big fan of htmx, but shoehorning it into a static personal website just
doesn't make any sense. Also a looping mp4 background made the initial load time
really slow, and the design was unique but I got tired of it after awhile.

### 2. Single page pure html/css/js with client-rendered interactive background

<span style="display: flex; justify-content: space-between; width: 100%">
<img src="/assets/site2-home.png" style="width: 49%">
<img src="/assets/site2-projects.png" style="width: 49%">
</span>

Very proud of the look and feel of this one. However, the complexity had lots of
little visual bugs that got increasingly annoying to fix, and the interactive
background could be slow or buggy on certain devices. Client side rendering a
bunch of particles and interactions is just a bit gimmicky and unnecessary for a
personal website. Still super cool and fun to build though.

### 1. Customized Gatsby tech portfolio template

<span style="display: flex; justify-content: space-between; width: 100%">
<img src="/assets/site1-home.png" style="width: 49%">
<img src="/assets/site1-projects.png" style="width: 49%">
</span>

My first website, I hosted this one on a raspberry pi in my room!

The design was super uninspired. Using a template is fine, but after a while I really wanted to build something myself.
