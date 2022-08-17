---
layout: post
title: "BlueRetro N64 Adapter"
tags: [electronics, mod]
comments: true
---

This is [yet]({% post_url 2022-04-23-blueretro-and-psx-adapter %}) [another]({% post_url 2022-06-13-blueretro-psx-adapter-2 %}) [post]({% post_url 2022-07-26-blueretro-nes-adapter %}) on a BlueRetro adapter I made, this time for the N64. This adapter is almost certainly the easiest one to make, as there are only three wires per controller, and the voltage matches that of the ESP32 (3V3).

## The Build

When making an adapter for the N64, you can choose to support one to four controllers. In my case, I decided to only support two controllers as I don't expect to play local multiplayer games very often; however, should that change in the future, it should be easy enough to add the missing ones.

As per the [bill of materials](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-Cables-Build-Instructions#bill-of-materials-28), I ordered two N64 controller extensions, and a DB25 male connector along with a shell:

![](/assets/images/blueretro-n64-adapter/IMG_5895.jpg)

I printed out the [DIY cable-building instructions](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-Cables-Build-Instructions#diy-through-hole-15) along with the [schematics](https://github.com/darthcloud/BlueRetroHW/blob/master/DIY/N64.pdf):

![](/assets/images/blueretro-n64-adapter/IMG_5894.jpg)

I cut the extension cables, stripped them back to expose the three wires in each, and stripped each of them:

![](/assets/images/blueretro-n64-adapter/IMG_5897.jpg)

With my multimeter in continuity mode, I identified what pins each of the three wires mapped to:

![](/assets/images/blueretro-n64-adapter/IMG_5898.jpg)

I marked the wire colors on my printout:

![](/assets/images/blueretro-n64-adapter/IMG_5913.jpg)

I made sure to tin my wires:

![](/assets/images/blueretro-n64-adapter/IMG_5899.jpg)

Then following the schematics, I proceeded to solder the wires to the DB25 connector:

![](/assets/images/blueretro-n64-adapter/IMG_5903.jpg)

The first thing I did was solder together black wires for all the GND connections, and red wires for all the 3V3 connections:

![](/assets/images/blueretro-n64-adapter/IMG_5905.jpg)

Note that I would not do it this way again, particularly for the GND connections as there are so many of them. I've found that a better way is to connect each pin to the metal housing of the DB25 connector, and only have a single GND wire from one of the pins or the housing connected to the GNDs from the extension cables. For an example of this, see how I made my [NES BlueRetro adapter]({% post_url 2022-07-26-blueretro-nes-adapter %}).

Anyway, after that, I connected the rest of the wires up:

![](/assets/images/blueretro-n64-adapter/IMG_5907.jpg)

With the soldering done, it was time to put the connector into its shell:

![](/assets/images/blueretro-n64-adapter/IMG_5914.jpg)

But first, I wrapped up the exposed 3V3 and GND wires with heat shrink tubing:

![](/assets/images/blueretro-n64-adapter/IMG_5917.jpg)

![](/assets/images/blueretro-n64-adapter/IMG_5918.jpg)

I put on the strain relief:

![](/assets/images/blueretro-n64-adapter/IMG_5919.jpg)

And tucked it all into the shell:

![](/assets/images/blueretro-n64-adapter/IMG_5920.jpg)

![](/assets/images/blueretro-n64-adapter/IMG_5922.jpg)

![](/assets/images/blueretro-n64-adapter/IMG_5923.jpg)

It's important to know which wire goes into which port on the N64, so I printed up some labels:

![](/assets/images/blueretro-n64-adapter/IMG_5924.jpg)

![](/assets/images/blueretro-n64-adapter/IMG_5927.jpg)

All done:

![](/assets/images/blueretro-n64-adapter/IMG_5928.jpg)

I attached the BlueRetro Receiver to test it, and it worked perfectly (note that this pic was taken before I put on the shell):

![](/assets/images/blueretro-n64-adapter/IMG_5910.jpg)


## Thoughts

It should come as no surprise by now that I love my BlueRetro setup. Playing N64 with a wireless controller is great. Personally, I use a PS3 controller, and I find that it works just fine, but for a more authentic experience, you can also use one of those [official Bluetooth N64 controllers](https://www.nintendo.com/en-ca/store/products/nintendo-64-controller/) that Nintendo released to play N64 games on the Switch. The only problem is that it seems it's always sold out.

As I already mentioned, this is probably the easiest BlueRetro adapter to make, so I definitely recommend it as a good first project.
