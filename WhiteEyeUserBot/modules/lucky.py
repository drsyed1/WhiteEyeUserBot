# plugin by lejend @ravana69
"""Emoji

Available Commands:

.lucky"""


import asyncio

from uniborg.util import WhiteEye_on_cmd


@WhiteEye.on(WhiteEye_on_cmd(pattern="lucky"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 17)

    # input_str = event.pattern_match.group(1)

    # if input_str == "lucky":

    await event.edit("Lucky..")

    animation_chars = [
        "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜",
        "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜",
        "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜",
        "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜",
        "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜",
        "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜",
        "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜",
        "⬛⬛⬛⬛⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜\n⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬛⬜\n⬜⬜⬜👇⬜\n⬜⬜⬜[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬛⬛⬛⬜⬜\n⬜⬜👇⬜⬜\n⬜⬜[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬛⬛⬜⬜⬜\n⬜👇⬜⬜⬜\n⬜[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬛⬜⬜⬜⬜\n👇⬜⬜⬜⬜\n[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜",
        "⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜\n⬜⬜⬜⬜",
        "⬜⬜⬜\n⬜⬜⬜\n⬜⬜⬜",
        "⬜⬜\n⬜⬜",
        "[🎁](https://github.com/mrdayamzaidi-bit/WhiteEyeUserBot/)",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 17])
