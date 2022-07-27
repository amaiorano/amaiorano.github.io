---
layout: post
title: "BlueRetro NES Adapter"
tags: [electronics, mod]
comments: true
---

As much as I love retro consoles, I am not a fan of wired controllers, and have been gradually updating my retro gaming setup to use only Bluetooth controllers. To that end, a while back I purchased four [8BitDo NES controller Mod Kits](https://www.8bitdo.com/mod-kit-for-nes-controller/) along with four of their [NES Retro Receivers](https://www.8bitdo.com/retro-receiver-nes/) to plug into my [NES Four Score](https://en.wikipedia.org/wiki/NES_Four_Score) for some fun four-player action (translation: to play [Micro Mages](http://morphcat.de/micromages/) with my wife and kids). Sadly, I found out the hard way that four Retro Receivers running at the same time resulted in lots of input lag on some of the controllers. I suspect the problem is that having four Bluetooth receivers in such close proximity causes some kind of interference.

Eventually, when I learned about the [BlueRetro](https://github.com/darthcloud/BlueRetro) project, I wondered if having a single receiver would solve my input lag problems with four controllers connected to it. The neat thing about how BlueRetro works for NES is that you only need to plug it into the two controller ports, and it's able to emulate the Four Score. Well, after building the adapter and receivers for my [PS1]({% post_url 2022-04-23-blueretro-and-psx-adapter %}) and [PS2]({% post_url 2022-06-13-blueretro-psx-adapter-2 %}), it was time to build an adapter for my NES.

## The Build

Although the steps are roughly the same for all adapters, what makes the NES one different is that the NES uses 5V DC to power its components, while the BlueRetro needs 3V3 for its ESP32 module, so the adapter needs to make sure to convert 5V to 3V3 for inputs from the controller ports, and convert 3V3 back to 5V for outputs. It does this using a couple of 74AHCT125N quad level-shifters. I ordered a pack of 10 from AliExpress:

![](/assets/images/blueretro-nes-adapter/IMG_6234.jpg)

I also ordered 2 NES extension cables, a DB25 male connector and shell:

![](/assets/images/blueretro-nes-adapter/IMG_6235.jpg)

![](/assets/images/blueretro-nes-adapter/IMG_6246.jpg)

As usual, I cut up the extension cables, exposed and stripped the wires:

![](/assets/images/blueretro-nes-adapter/IMG_6237.jpg)

![](/assets/images/blueretro-nes-adapter/IMG_6238.jpg)

I used my multimeter to map each wire color to each controller pin:

![](/assets/images/blueretro-nes-adapter/IMG_6239.jpg)

I wrote everything down on my printout of the [BlueRetro instructions](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-Cables-Build-Instructions#fc--nes-adapter-cable):

![](/assets/images/blueretro-nes-adapter/IMG_6242.jpg)

After reading through the [wiring diagram](https://github.com/darthcloud/BlueRetroHW/blob/master/DIY/NES.pdf), I also marked up how I'd connect everything to the two 74AHCT125N quad level-shifters (I personally find the wiring diagram confusing on this aspect):

![](/assets/images/blueretro-nes-adapter/IMG_6244.jpg)

The big challenge here was figuring out how to fit the two level-shifters in the DB25 shell:

![](/assets/images/blueretro-nes-adapter/IMG_6247.jpg)

I decided that I'd wire everything up, and put the two ICs back-to-back. First, I clipped the legs short and bent the pins against the IC:

![](/assets/images/blueretro-nes-adapter/IMG_6248.jpg)

![](/assets/images/blueretro-nes-adapter/IMG_6250.jpg)

As I would need to ground multiple pins on each IC, I soldered together a daisy chain of 30 AWG wire:

![](/assets/images/blueretro-nes-adapter/IMG_6253.jpg)

I soldered these to the IC:

![](/assets/images/blueretro-nes-adapter/IMG_6255.jpg)

Then soldered the rest of the wires from the extension cables:

![](/assets/images/blueretro-nes-adapter/IMG_6258.jpg)

After doing the same with the other IC, I ended up with this:

![](/assets/images/blueretro-nes-adapter/IMG_6264.jpg)

Now it was time to solder up the DB25 connector. Like the ICs above, the connector has a lot of pins that need to be connected to ground. In the past, I'd connect a wire to each and solder them all together with the ground wires from the controller cables. But this usually ended up kind of ugly and would take up room in the shell. This time, I decided to solder each pin to the connector body itself:

![](/assets/images/blueretro-nes-adapter/IMG_6269.jpg)

Then I'd only have one wire from the body to connect to ground from the controller:

![](/assets/images/blueretro-nes-adapter/IMG_6270.jpg)

I then proceeded to wire up the rest of the connections between the controller wires, the ICs, and the DB25 connector:

![](/assets/images/blueretro-nes-adapter/IMG_6275.jpg)

![](/assets/images/blueretro-nes-adapter/IMG_6289.jpg)

A quick test showed that everything was wired up correctly:

![](/assets/images/blueretro-nes-adapter/IMG_6290.jpg)

It was now time to fit everything into the shell. I used some two-sided tape to stick the two ICs together, then wrapped it up in wire tape to avoid shorts:

![](/assets/images/blueretro-nes-adapter/IMG_6293.jpg)

![](/assets/images/blueretro-nes-adapter/IMG_6295.jpg)

With a little wire twisting, I eventually managed to fit everything neatly into the shell, along with the strain relief:

![](/assets/images/blueretro-nes-adapter/IMG_6297.jpg)

![](/assets/images/blueretro-nes-adapter/IMG_6298.jpg)

And here's the final product:

![](/assets/images/blueretro-nes-adapter/IMG_6302.jpg)

![](/assets/images/blueretro-nes-adapter/IMG_6304.jpg)

![](/assets/images/blueretro-nes-adapter/IMG_6305.jpg)

With that, I gave it a final test with my four Bluetooth NES controllers:

![](/assets/images/blueretro-nes-adapter/IMG_6309.jpg)

![](/assets/images/blueretro-nes-adapter/IMG_6314.jpg)


## Thoughts

As usual, I'm super happy with my BlueRetro setup, and this NES one is no different. So what's the verdict on playing four player games with this? As I expected, it works great! The only issue I have is some intermittent pairing issues with the NES Bluetooth controllers, but I'm sure this has more to do with the controllers than the receiver itself, as I never have this problem when pairing my PS3 controllers to it.

Overall, I highly recommend this mod to NES fans out there. If you want to play four player games, this not only works well, but saves you from having to buy a Four Score, which is pretty awesome.
