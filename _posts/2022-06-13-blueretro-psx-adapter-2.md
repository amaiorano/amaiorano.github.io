---
layout: post
title: "Another BlueRetro PSX/PS2 Adapter"
tags: [Electronics, BlueRetro, PS2]
comments: true
---
After [building a BlueRetro adapter for my PS1]({% post_url 2022-04-23-blueretro-and-psx-adapter %}), I decided to build a second one for my PS2 so that I wouldn't have to disconnect and reconnect the adapter between the two consoles. Normally I wouldn't bother writing about this, as it should have been the same process as the first, but I ran into a surprising snag that I thought worth sharing. I also improved on the wiring by connecting pins that I had ignored in my first build.

## The Build

As with the first build, I ordered a DB25 male connector, shell, and two PSX/PS2 extension cables from AliExpress:

![](/assets/images/blueretro-psx-adapter-2/IMG_5944.jpg)

Before I did anything, I tested the extension cables, and this is when I hit the snag I mentioned earlier. One of the cables wouldn't fit properly into my PSX nor PS2. It was extremely tight going in, and after a while of pushing, I stopped and had a difficult time pulling it out. I was quite surprised as I had ordered these from the same seller as last time, and the other cable I had received was just fine. It took me a while to understand what was going on: the problem was that the two plastic separators in the cable were too thick:

![](/assets/images/blueretro-psx-adapter-2/IMG_5952.jpg)

In the picture above, I had already removed the pins (see below), but you can sort of see how in the top one, the plastic "walls" that separate the pins into triplets are slightly thicker than in the bottom one. Rather than return these, and wait the many weeks before getting a new one from AliExpress, I decided to fix it myself.

Using a utility knife, I carefully separated the plastic shell from the connector:

![](/assets/images/blueretro-psx-adapter-2/IMG_5946.jpg)

Then I used my tweezers to extract each pin from its slot:

![](/assets/images/blueretro-psx-adapter-2/IMG_5948.jpg)

![](/assets/images/blueretro-psx-adapter-2/IMG_5949.jpg)

Now I needed to figure out how to make those separators thinner. I didn't have a thin filing tool on hand, so I built one using some sandpaper, a thin screwdriver, and some tape:

![](/assets/images/blueretro-psx-adapter-2/IMG_5954.jpg)

I tried to keep the sandpaper exposed only on one side. Then I inserted the tool into the connector and filed down the separators:

![](/assets/images/blueretro-psx-adapter-2/IMG_5957.jpg)

I had to change the sandpaper once. But after lots of sanding, I managed to make the separators thin enough that I could insert it into my PS2 without issue:

![](/assets/images/blueretro-psx-adapter-2/IMG_5958.jpg)

![](/assets/images/blueretro-psx-adapter-2/IMG_5959.jpg)

![](/assets/images/blueretro-psx-adapter-2/IMG_5960.jpg)

I put it all back together and tested it:

![](/assets/images/blueretro-psx-adapter-2/IMG_5962.jpg)

![](/assets/images/blueretro-psx-adapter-2/IMG_5963.jpg)

After that, it was pretty much the same as with the first adapter. The only difference is that this time, I realized that I had not connected a bunch of pins on the DB25 connector to ground, as specified in the [connection diagram](https://github.com/darthcloud/BlueRetroHW/blob/master/DIY/BlueRetroDIY.pdf). To do this, I cut of bunch of wires and soldered the ends together:

![](/assets/images/blueretro-psx-adapter-2/IMG_5970.jpg)

![](/assets/images/blueretro-psx-adapter-2/IMG_5971.jpg)

Then soldered these to the pins that needed to be grounded:

![](/assets/images/blueretro-psx-adapter-2/IMG_5972.jpg)

After connecting the rest of the wires, I soldered the two black ground wires from the PSX extension cables to the ground wires from the cable:

![](/assets/images/blueretro-psx-adapter-2/IMG_5976.jpg)

I wrapped up the ground wires with some heat shrink:

![](/assets/images/blueretro-psx-adapter-2/IMG_5981.jpg)

![](/assets/images/blueretro-psx-adapter-2/IMG_5982.jpg)

Finally, I put it all together in the shell:

![](/assets/images/blueretro-psx-adapter-2/IMG_5984.jpg)

![](/assets/images/blueretro-psx-adapter-2/IMG_5986.jpg)

![](/assets/images/blueretro-psx-adapter-2/IMG_5987.jpg)

![](/assets/images/blueretro-psx-adapter-2/IMG_5990.jpg)


## Thoughts

As with the first one, this adapter works great. I didn't expect to have to spend time taking apart one of the extension cables to sand down the plastic separators, but I suppose that's the risk of buying these cheaper knock-off items from AliExpress. As for properly grounding the pins, I didn't do this in my first adapter, and haven't had any issues so far; however, leaving pins floating isn't a great idea, and could cause problems in the future, so I'll probably fix my first adapter in a similar way to what I did here.
