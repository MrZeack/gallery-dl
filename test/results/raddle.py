# -*- coding: utf-8 -*-

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as
# published by the Free Software Foundation.

from gallery_dl.extractor import postmill


__tests__ = (
{
    "#url"     : "https://raddle.me/",
    "#category": ("postmill", "raddle.me", "home"),
    "#class"   : postmill.PostmillHomeExtractor,
    "#range"   : "1-25",
    "#count"   : 25,
},

{
    "#url"     : "https://raddle.me/f/traa",
    "#category": ("postmill", "raddle.me", "forum"),
    "#class"   : postmill.PostmillForumExtractor,
    "#count"   : 1,
    "#pattern" : r"^https://raddle\.me/f/traa/156646/click-here-to-go-to-f-traaaaaaannnnnnnnnns$",
},

{
    "#url"     : "https://raddle.me/user/Sam_the_enby/submissions",
    "#category": ("postmill", "raddle.me", "usersubmissions"),
    "#class"   : postmill.PostmillUserSubmissionsExtractor,
    "#range"   : "1-25",
    "#count"   : 25,
},

{
    "#url"     : "https://raddle.me/tag/Trans",
    "#category": ("postmill", "raddle.me", "tag"),
    "#class"   : postmill.PostmillTagExtractor,
},

{
    "#url"     : "https://raddle.me/search?q=tw",
    "#category": ("postmill", "raddle.me", "search"),
    "#class"   : postmill.PostmillSearchExtractor,
    "#range"   : "1-50",
    "#count"   : 50,
},

{
    "#url"     : "https://raddle.me/160845",
    "#category": ("postmill", "raddle.me", "shorturl"),
    "#class"   : postmill.PostmillShortURLExtractor,
    "#pattern" : r"^https://raddle\.me/f/egg_irl/160845/egg_irl$",
},

{
    "#url"     : "https://raddle.me/f/NonBinary/179017/scattered-thoughts-would-appreciate-advice-immensely-tw",
    "#comment" : "Text post",
    "#category": ("postmill", "raddle.me", "post"),
    "#class"   : postmill.PostmillPostExtractor,
    "#sha1_url"    : "99277f815820810d9d7e219d455f818601858378",
    "#sha1_content": "7a1159e1e45f2ce8e2c8b5959f6d66b042776f3b",
    "#count"   : 1,
},

{
    "#url"     : "https://raddle.me/f/egg_irl/160845",
    "#comment" : "Image post",
    "#category": ("postmill", "raddle.me", "post"),
    "#class"   : postmill.PostmillPostExtractor,
    "#sha1_url"    : "48663f767ea258fcd545ab5aa0e734f98f434388",
    "#sha1_content": "431e938082c2b59c44888a83cfc711cd1f0e910a",
    "#count"   : 1,
},

{
    "#url"     : "https://raddle.me/f/trans/177042/tw-vent-nsfw-suicide-i-lost-no-nut-november-tw-trauma",
    "#comment" : "Image + text post (with text enabled)",
    "#category": ("postmill", "raddle.me", "post"),
    "#class"   : postmill.PostmillPostExtractor,
    "#options" : {"save-link-post-body": True},
    "#pattern" : r"^(text:[\s\S]+|https://raddle\.me/submission_images/[0-9a-f]+\.png)$",
    "#count"   : 2,
},

{
    "#url"     : "https://raddle.me/f/videos/179541/raisins-and-sprite",
    "#comment" : "Link post",
    "#category": ("postmill", "raddle.me", "post"),
    "#class"   : postmill.PostmillPostExtractor,
    "#urls"    : "https://m.youtube.com/watch?v=RFJCA5zcZxI",
    "#count"   : 1,
},

{
    "#url"     : "https://raddle.me/f/Anime/150698/neo-tokyo-1987-link-to-the-english-dub-version-last-link",
    "#comment" : "Link + text post (with text disabled)",
    "#category": ("postmill", "raddle.me", "post"),
    "#class"   : postmill.PostmillPostExtractor,
    "#pattern" : r"^https://fantasyanime\.com/anime/neo-tokyo-dub$",
    "#count"   : 1,
},

{
    "#url"     : "https://raddle.me/f/egg_irl/166855/4th-wall-breaking-please-let-this-be-a-flair-egg-irl",
    "#comment" : "Post with multiple flairs",
    "#category": ("postmill", "raddle.me", "post"),
    "#class"   : postmill.PostmillPostExtractor,
    "flair"    : ["Gender non-specific", "4th wall breaking"],
},

)
