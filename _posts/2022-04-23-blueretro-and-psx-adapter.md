---
layout: post
title: "BlueRetro Receiver and PSX/PS2 Adapter"
tags: [electronics, mod]
comments: true
---
After [modding my PS1]({% post_url 2022-03-31-psnee-mod %}) and [improving its output]({% post_url 2022-04-02-ps1-vga-mod %}), the last thing I wanted to fix was having to deal with the annoying controller cables. As much as I love old consoles, I do not love having to sit close, or untangle a bunch of cables. I considered buying an 8bitdo wireless controller, but then I heard about a really cool project named [BlueRetro](https://github.com/darthcloud/BlueRetro) by [darthcloud64](https://twitter.com/darthcloud64).

The BlueRetro project allows you to build a single Bluetooth receiver using just an ESP32 and some cabling, along with multiple controller adapters for many different consoles, so that you can easily use nearly any Bluetooth controller to play on all the different consoles. It's cheap, easy to build, and best of all, is open-source!

So I decided to go ahead and build a BlueRetro receiver, along with a cable adapter for my PSX (and PS2, since they are compatible).

## Building the BlueRetro Receiver

As per the [build instructions](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-DIY-Build-Instructions), I ordered an ESP32-DECKITX-32E with ESP-WROOM-32, a couple of DB-25 male and female connectors with shells, and two PSX controller extension cables, all from AliExpress:

![](/assets/images/blueretro-and-psx-adapter/IMG_5322.jpg)

Unfortunately, I had forgotten to specify *not* to solder on the headers onto the ESP32 board, so the first order of business was to remove them. The method I find easiest is to separate each header from each other with my flush cutters. This allows me to simply heat the solder joint on top and remove each header pin one at a time with pliers:

![](/assets/images/blueretro-and-psx-adapter/IMG_5324.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5326.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5327.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5329.jpg)

I printed out the [connection diagram](https://github.com/darthcloud/BlueRetroHW/blob/master/DIY/BlueRetroDIY.pdf) to wire up the ESP32 module to the DB-25 female connector:

![](/assets/images/blueretro-and-psx-adapter/IMG_5332.jpg)

Since I needed to connect 25 wires, I decided to make use of an old 40-pin IDE cable I had lying around. I removed the excess 15 wires, split out the ends and stripped each one. To help identify the wires, I used markers to color every fifth wire a different color:

![](/assets/images/blueretro-and-psx-adapter/IMG_5333.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5334.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5335.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5336.jpg)

I added wire number and color information to the connection diagram to help me out:

![](/assets/images/blueretro-and-psx-adapter/IMG_5339.jpg)

Then I tinned each wire:

![](/assets/images/blueretro-and-psx-adapter/IMG_5343.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5344.jpg)

And got to soldering. I first soldered every even numbered wire to the top row, then the odd numbered wires to the bottom:

![](/assets/images/blueretro-and-psx-adapter/IMG_5357.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5358.jpg)

Oops, you can see where I accidentally touched the plastic with my soldering iron:

![](/assets/images/blueretro-and-psx-adapter/IMG_5359.jpg)

One side complete:

![](/assets/images/blueretro-and-psx-adapter/IMG_5360.jpg)

Before I soldered the other end to the ESP32 module, I [flashed the latest BlueRetro firmware](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-DIY-Build-Instructions#build-instructions) to it:

![](/assets/images/blueretro-and-psx-adapter/IMG_5362.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5361.jpg)

I initially needed to [install a driver](https://www.silabs.com/developers/usb-to-uart-bridge-vcp-drivers) on my Windows 10 machine for it to recognize the device. Then, when flashing, I needed to press a button on the module so that the tool could connect and upload the firmware to it:

![](/assets/images/blueretro-and-psx-adapter/IMG_5364.jpg)

Once complete, I used [Bluefy](https://apps.apple.com/us/app/bluefy-web-ble-browser/id1492822055), an iOS browser that supports Bluetooth browsing, to connect to the ESP32 running the new firmware:

![](/assets/images/blueretro-and-psx-adapter/IMG_5366.jpg)

This web interface is really cool, allowing you to configure how BlueRetro works. Note that apparently on Android, Chrome supports Bluetooth web browsing, so there's no need to install a separate browser.

Alright, now with the firmware installed, it was time to wire the cable to the ESP32 module:

![](/assets/images/blueretro-and-psx-adapter/IMG_5367.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5369.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5370.jpg)

Three of the wires needed to connect to the Ground pin. I decided to tie all three together and solder them to a single piece of wire to make it easier to pass the wire through the small via:

![](/assets/images/blueretro-and-psx-adapter/IMG_5371.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5372.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5373.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5374.jpg)

This is how it looked in the end:

![](/assets/images/blueretro-and-psx-adapter/IMG_5376.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5377.jpg)

At this point, I still needed to clip the exposed wires under the board, and put the shell on the DB-25 connector. But I left this until the end, once I was sure everything worked.


## Building the PSX Adapter

To build the PSX adapter, I first cut the PSX extension cables, exposed the wires, stripped and tinned them:

![](/assets/images/blueretro-and-psx-adapter/IMG_5380.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5381.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5382.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5385.jpg)

I used my multimeter in continuity mode to identify which pin each colored wire corresponded to, and wrote it down on the [wiring diagram](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-Cables-Build-Instructions#psx--ps2-adapter-cable) I printed out:

![](/assets/images/blueretro-and-psx-adapter/IMG_5383.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5384.jpg)

Note that not all cables are made the same, so it's important to determine these connections on your own.

Following the diagram, I soldered both sets of wires to the DB-25 male connector:

![](/assets/images/blueretro-and-psx-adapter/IMG_5387.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5389.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5390.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5391.jpg)

Now it was time for a quick test. In my case, I decided to use PS3 Sixaxis controllers. I didn't take pictures of it, but in order to pair them with the BlueRetro, I followed [the guide](https://github.com/darthcloud/BlueRetro/wiki/Controller-pairing-guide#ps3), which involved getting the ESP32's MAC address, and using the [Sixaxis Pair Tool](https://sixaxispairtool.en.lo4d.com/windows) to configure each controller to pair with that MAC address.

I hooked up the BlueRetro receiver to the PSX adapter, and plugged it into the PSX, and gave it a spin:

![](/assets/images/blueretro-and-psx-adapter/IMG_5392.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5393.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5395.jpg)

It worked... well almost! The first player controller worked, but not the second. I went over my wiring, and realized I had accidentally swapped two wires on the ESP32 side coming from the second controller. I quickly fixed that, and everything worked beautifully!


## Final Touches

Now that everything was working, it was time to close up the cables, starting with the PSX adapter:

![](/assets/images/blueretro-and-psx-adapter/IMG_5397.jpg)

I attached the included strain relief, popped it into the shell, and buttoned it up:

![](/assets/images/blueretro-and-psx-adapter/IMG_5398.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5399.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5401.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5402.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5403.jpg)

For the BlueRetro receiver, I twisted the IDE cable so that it would fit through the hole in the shell:

![](/assets/images/blueretro-and-psx-adapter/IMG_5404.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5405.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5406.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5407.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5408.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5409.jpg)

I clipped the exposed wires underneath the ESP32 module:

![](/assets/images/blueretro-and-psx-adapter/IMG_5410.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5411.jpg)

Finally, I printed out some labels to identify the player 1 and 2 connectors on the adapter:

![](/assets/images/blueretro-and-psx-adapter/IMG_5416.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5417.jpg)

The final product:

![](/assets/images/blueretro-and-psx-adapter/IMG_5419.jpg)

![](/assets/images/blueretro-and-psx-adapter/IMG_5421.jpg)

The last thing I still need to do is make some kind of shell for the ESP32 module itself. It's fairly sturdy, but it would be safer if it was enclosed in something. If I had to redo it, I'd make the cable shorter, and maybe I wouldn't use a flat IDE cable, but a proper 25 sheathed wire cable. Still, for the price, I'm quite happy with how it turned out!


## Thoughts

Since I built this project, I've been having a blast playing both PSX and PS2 games from the comfort of my couch, without having to worry about long cables, or having to pull the console forward. It works really well! I love it so much that I've already ordered what I need to make an N64 adapter cable!

I definitely recommend this project for anyone looking for an affordable solution to using Bluetooth controllers on their old consoles. If you're decent with a soldering iron, it's not very difficult. If you do decide to make one, consider [sponsoring](https://www.patreon.com/darthcloud) Darthcloud, or [buying him a coffee](https://ko-fi.com/darthcloud).
