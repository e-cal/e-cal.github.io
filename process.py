import asyncio
import re
from twikit import Client

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

async def main(filepath):
    client = Client(language='en-US')
    client.load_cookies('cookies.json')

    with open(filepath) as f:
        content = f.read()

    pattern = r'https?://(?:twitter\.com|x\.com)/\S+/(\d+)'
    for match in re.finditer(pattern, content):
        url = match.group(0)
        tweet_id = match.group(1)
        tweet = await client.get_tweet_by_id(tweet_id)
        html = tweet_to_html(url, tweet)
        content = content.replace(url, html)

    print(content)

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("filepath", help="Path to the markdown file")
    args = parser.parse_args()

    asyncio.run(main(args.filepath))
