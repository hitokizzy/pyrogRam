from time import sleep
from userbot.events import register


@register(outgoing=True, pattern='^.r(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("`Hai Perkenalkan namaku coco`")
    sleep(3)
    await typew.edit("`umurku 18 tahu `")
    sleep(1)
    await typew.edit("`Tinggal Di petukangan, Saalam kenal yah semuanya:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Pertama aku kenalan`")
    sleep(3)
    await typew.edit("`kedua ku jadi suka`")
    sleep(1)
    await typew.edit("`ketiga kita friendzone`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Happy Kiyowo`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur tentang apa yang telah di berikan oleh sang pencipta`")
# Create by myself @localheart
