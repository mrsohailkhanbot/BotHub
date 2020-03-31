"""Use cmd .bothub , .armor , .love , .hero and check what happens"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "bothub":

        await event.edit(input_str)

        animation_chars = [

            "M_",

            "MD_",
 
            "S_",

            "SO_",

            "SOH_",

            "SOHA__",
            
            "SOHAI_",
            
            "SOHAIL_",

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])


@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "armor":

        await event.edit(input_str)

        animation_chars = [

            "A_",

            "AR_",

            "ARM_",

            "ARMO_",
            
            "ARMOR_",
            
            "ARMOR🛡_",
            
            ".🛡🛡🛡🛡🛡🛡🛡.",

        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])



"""Emoji

Available Commands:

.emoji shrug

.emoji apple

.emoji :/

.emoji -_-"""

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "love":

        await event.edit(input_str)

        animation_chars = [

            "SO_",

            "SOHAI_",

            "SOHAIL_",

            "SOHAIL LOVE_",
            
            "SOHAIL LOVE YOU❤️",
            
            "❤️❤️❤️❤️",
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])

@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    input_str = event.pattern_match.group(1)

    if input_str == "hero":

        await event.edit(input_str)

        animation_chars = [

            "SOH_",

            "SOHAIL_",

            "SOHAIL IS_",

            "SOHAIL IS HE_",
            
            "SOHAIL IS HERO💪🏻💪",
            
            "💪🏻SOHAIL KHAN💪🏻",
            
        ]

        for i in animation_ttl:

            await asyncio.sleep(animation_interval)

            await event.edit(animation_chars[i % 10])
