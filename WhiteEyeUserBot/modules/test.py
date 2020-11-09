from uniborg.util import WhiteEye_on_cmd


@WhiteEye.on(WhiteEye_on_cmd(pattern=r"test"))
async def test(event):
    if event.fwd_from:
        return
    await event.edit("Test Successfull. Boss !")
