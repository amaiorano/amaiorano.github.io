---
layout: post
title: "Making a gbs-control video scaler"
tags: [Electronics, Mods, gbs-control]
comments: true
---

I've been playing most of my retro consoles on my 20" CRT, which has been great, but there are times - like when playing four-player [Micro Mages](http://morphcat.de/micromages/) on the NES - when you really want to play on a big screen. Unfortunately, older consoles like the NES output a 240p image, and newer TVs like my 70" 4K don't accept this low resolution signal. The fix is to use a scaler, like the [RetroTINK](https://www.retrotink.com/) or [OSSC](https://videogameperfection.com/products/open-source-scan-converter/) to scale up the resolution to at least 480p, but these always seemed a bit expensive. Then I watched [this video](https://youtu.be/1AVXhiTlmgo) from Voultar where he shows how to build a scaler for about $35 USD.

The project is called [gbs-control](https://github.com/ramapcsx2/gbs-control), and it's basically a mod of the GBS8200, a cheap scaler that was apparently developed for arcade owners to convert their cabinets from using CRTs to LCD panels. The scaler itself is apparently not very good on its own, but [Robert Neumann](https://github.com/ramapcsx2) developed an open-source firmware that you can flash on the popular (and cheap) ESP8266 microcontroller, and wire up to a GBS8200 to take control of it and make it a much better scaler. Check out the [README](https://github.com/ramapcsx2/gbs-control#readme) for more details.

## The Build

I ordered the parts I needed:

* GBS800 board (eBay $22 USD)
* ESP8266 board (AliExpress $4 USD)
* Si5351A Clock Breakout Board (AliExpress $4 USD)
* 0805 SMD 10uF caps (AliExpress $2 USD for 100 pcs)
* VGA male to HDMI female converter (AliExpress $4.30 USD)

Mostly following [Voultar's video](https://youtu.be/1AVXhiTlmgo), along with reading the official instructions on how to [build the hardware](https://github.com/ramapcsx2/gbs-control/wiki/Build-the-Hardware), it wasn't very hard to put this project together.

First order of business, load up the firmware onto the ESP8266:

![](/assets/images/gbs-control/IMG_4314.jpg)

Then I removed the socket on the side of the GBS8200 board:

![](/assets/images/gbs-control/IMG_4320.jpg)

![](/assets/images/gbs-control/IMG_4321.jpg)

Next I bridged P8 to enabled debug mode, which allows the ESP board to take control (see the next photo for where it's actually bridged):

![](/assets/images/gbs-control/IMG_4327.jpg)

Following Voultar's method, I soldered the ESP board sideways onto the GBS board:

![](/assets/images/gbs-control/IMG_4328.jpg)

Soldered the necessary connections:

![](/assets/images/gbs-control/IMG_4331.jpg)

![](/assets/images/gbs-control/IMG_4337.jpg)

I connected the 5V DC input barrel jack to the ESP board:

![](/assets/images/gbs-control/IMG_4338.jpg)

![](/assets/images/gbs-control/IMG_4340.jpg)

The VGA to HDMI converter needs 5V as well. Using the USB plug that came with the converter, and the pig tail that came with the board, I spliced them together:

![](/assets/images/gbs-control/IMG_4343.jpg)

![](/assets/images/gbs-control/IMG_4344.jpg)

![](/assets/images/gbs-control/IMG_4345.jpg)

![](/assets/images/gbs-control/IMG_4347.jpg)

![](/assets/images/gbs-control/IMG_4349.jpg)

Now we can easily power the converter:

![](/assets/images/gbs-control/IMG_4351.jpg)

Time to put everything together and perform a quick test:

![](/assets/images/gbs-control/IMG_4352.jpg)

![](/assets/images/gbs-control/IMG_4353.jpg)

Success! This is a PS2 connected via component into the GBS, and the GBS outputting 1080p over HDMI.

Next up was removing some caps and stacking some to improve the GBS performance and filtering:

![](/assets/images/gbs-control/IMG_4356.jpg)

![](/assets/images/gbs-control/IMG_4358.jpg)

![](/assets/images/gbs-control/IMG_4361.jpg)

![](/assets/images/gbs-control/IMG_4363.jpg)

Next I installed the [clock generator board](https://github.com/ramapcsx2/gbs-control/wiki/Si5351-Clock-Generator-install-notes) which apparently fixes horizontal tearing at high resolutions:

![](/assets/images/gbs-control/IMG_4365.jpg)

![](/assets/images/gbs-control/IMG_4366.jpg)

![](/assets/images/gbs-control/IMG_4367.jpg)

![](/assets/images/gbs-control/IMG_4369.jpg)

![](/assets/images/gbs-control/IMG_4370.jpg)

![](/assets/images/gbs-control/IMG_4378.jpg)

![](/assets/images/gbs-control/IMG_4381.jpg)

Finally, with everything wired up, I decided to mount it on a piece of wood I cut and sanded:

![](/assets/images/gbs-control/IMG_4542.jpg)

![](/assets/images/gbs-control/IMG_4543.jpg)

![](/assets/images/gbs-control/IMG_4541.jpg)

Note that although it's not shown in the pics, I also attached a dual RCA female to phono male cable to the VGA to HDMI converter to be able to mix in stero audio into the HDMI signal.

## Thoughts

This was a super fun build to make. There are a lot of steps, but it's not too difficult. The scaler itself works amazingly well! You can connect to the ESP board over WiFi to configure options like resolution, scanlines, and much more. When connecting my NESRGB-modded NES to to via component, the image quality on my 70" TV is crisp and clear. I definitely recommend building one of these!
