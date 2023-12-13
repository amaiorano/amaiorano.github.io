---
layout: post
title: "BlueRetro AIO"
tags: [Electronics, BlueRetro, 3D-printing, NES, SNES, N64, GameCube, PS1, PS2]
comments: true
---

I love the [BlueRetro](https://github.com/darthcloud/BlueRetro) project, and on this blog, I've shown how I've made multiple [DIY HW1](https://github.com/darthcloud/BlueRetro/wiki#1---building-hardware-hw1) adapters for [different consoles](/tags/#BlueRetro) by soldering wires to DB25 connectors, and wrapping them up in DB25 shells. In this blog post, I'm going to cover a different way to make these adapters using PCBs and 3D-printed shells designed by [pmgducati](https://github.com/pmgducati) known as [BlueRetro AIO Units](https://github.com/pmgducati/Blue-Retro-AIO-Units).

As this post is quite long, here are links to the different sections below:

* [My Setup](#my-setup)
* [Making BlueRetro AIO Units](#making-blueretro-aio-units)
* [The Builds](#the-builds)
  * [Receiver](#receiver)
  * [N64](#n64)
  * [GameCube](#gamecube)
  * [PSX/PS2](#psxps2)
  * [SNES - 2 Player](#snes---2-player)
  * [SNES - Multitap](#snes---multitap)
  * [NES](#nes)
* [Thoughts](#thoughts)

## My Setup

Before getting into how I made these AIO units, I thought I'd share what my final setup looks like with them, so that you know where we're headed. I currently have 6 BlueRetro AIO adapters, and one receiver (connected to the NES adapter in these pics):

![](/assets/images/blueretro-aio/setup/IMG_3661.jpg)

![](/assets/images/blueretro-aio/setup/IMG_3666.jpg)

I also have an array of Bluetooth controllers as well:

![](/assets/images/blueretro-aio/setup/IMG_3662.jpg)

When I want to play a different system, I simply disconnect and reconnect the receiver to that system's adapter. It's quick, and since I have only one receiver, I only have one device to configure and update.

Alright, let's get into the how I made these.


## Making BlueRetro AIO Units

Making BlueRetro AIO units requires a few parts:

**PCB**

For the PCBs, I personally use [JLCPCB](https://jlcpcb.com/) because it's cheaper for me than most other options. Simply download the [Gerber files](https://github.com/pmgducati/Blue-Retro-AIO-Units/tree/main/Gerbers) for the system you need, and uploaded them to JLCPCB, sticking to default options (except board color). Note that the BlueRetro "receiver" - the part that holds the ESP32 devkit board - is called "Main_`<date>`.zip". The file names for each console-specific PCB has the name of the console in it (e.g. "SNES_`<date>`.zip").

**3D-printed shell**

For the 3D-printed shells, the STL files can be [downloaded from here](https://github.com/pmgducati/Blue-Retro-AIO-Units/tree/main/STL). The way it works is that there are two parts, the top and the bottom. For the receiver, you'll want to print [this top](https://github.com/pmgducati/Blue-Retro-AIO-Units/blob/main/STL/Blue%20Retro%20Main%20Housing%20Top.STL) and [this bottom](https://github.com/pmgducati/Blue-Retro-AIO-Units/blob/main/STL/Blue%20Retro%20Main%20Housing%20Bottom.STL).

For each console adapter, select the top that's specific to the console. The only difference here is that each one has a nice logo embedded into it (see the [SNES one](https://github.com/pmgducati/Blue-Retro-AIO-Units/blob/main/STL/Aux%20Top%20-%20Nintendo%20SNES.STL), for example). For the bottom part, you'll need to choose from one of the "Aux Bottom - `<N>` Player.STL" files, where `<N>` is the number of controllers you intend to connect. This basically translates into how many holes the bottom case will have for the controller cables to pass through. You don't have to match the number of ports on the target console; for instance, the N64 supports up to four controllers, but I decided to only connect two, as I don't expect to play four player games. See this [BOM](https://github.com/pmgducati/Blue-Retro-AIO-Units/blob/main/BOM%20-%203D%20Printed%20Parts.pdf) for what you'd typically want to print for each console.

**Controller cables and other components**

Finally, you'll also need controller cables, and depending on the console, potentially some other components, such as through-hole level-shifter ICs. For controller cables, I normally buy extension cables from AliExpress that I can cut, keeping the console plug side intact. See this [very detailed BOM](https://github.com/pmgducati/Blue-Retro-AIO-Units/blob/main/BOM%20-%20Purchased%20Parts.pdf) for the parts you'll need per console.


## The Builds

### Receiver

Let's start with the receiver, which is the part that connects to each adapter.

Parts:
- 3D printed shell
- PCB
- ESP32-DEVKITC-32E (aka ESP32-WROOM-32E)
- DB25 connector (female, 90 degrees)
- 2x 19 position pin sockets
- Optional:
  - Blue LED (470nm 3.3V 1206)
  - 84.5 ohm resistor (SMD 1206)

Here are the main parts:

![](/assets/images/blueretro-aio/receiver/IMG_9214.jpg)

Along with the 3D-printed shell:

![](/assets/images/blueretro-aio/receiver/IMG_9063.jpg)

And the optional LED and resistor:

![](/assets/images/blueretro-aio/receiver/IMG_13348.jpg)

To save money, instead of buying two 19-pin sockets, I bought a bunch of 4-pin ones from AliExpress. Unfortunately, when inserting them into the PCB, I realized that they didn't quite fit well together:

![](/assets/images/blueretro-aio/receiver/IMG_9215.jpg)

So I ended up filing the edges of each one with some sandpaper until they fit well enough:

![](/assets/images/blueretro-aio/receiver/IMG_9217.jpg)

![](/assets/images/blueretro-aio/receiver/IMG_9218.jpg)

![](/assets/images/blueretro-aio/receiver/IMG_9220.jpg)

After inserting 4 of them on one side, the last one needed to be 3 pins wide, so I cut off the extra one with flush cutters:

![](/assets/images/blueretro-aio/receiver/IMG_9221.jpg)

![](/assets/images/blueretro-aio/receiver/IMG_9222.jpg)

I did the same for the other side, and to hold everything in place, I inserted the ESP32 board into them:

![](/assets/images/blueretro-aio/receiver/IMG_9224.jpg)

![](/assets/images/blueretro-aio/receiver/IMG_9223.jpg)
(Note that the ESP32 board is actually inserted the wrong way in the pic above, as this was only temporary to solder in the sockets).

I soldered the pins to the underside:

![](/assets/images/blueretro-aio/receiver/IMG_9234.jpg)

![](/assets/images/blueretro-aio/receiver/IMG_9235.jpg)

This worked out okay, but I would recommend just getting the 19-pin sockets instead.

Next, I soldered the female DB25 connector to the PCB. Note that the AIO BOM suggests using a male connector for the receiver, and female ones for each console adapter. I went the opposite way, which is totally fine:

![](/assets/images/blueretro-aio/receiver/IMG_9236.jpg)

![](/assets/images/blueretro-aio/receiver/IMG_9237.jpg)

![](/assets/images/blueretro-aio/receiver/IMG_9238.jpg)

![](/assets/images/blueretro-aio/receiver/IMG_9239.jpg)

I removed the two screw posts from the DB25 connector. The 3D printed shells are made such that these posts should be removed, though the metal plate that is held by the screw posts is kept:

![](/assets/images/blueretro-aio/receiver/IMG_9241.jpg)

Finally, I placed the board into the shell, and closed it up:

![](/assets/images/blueretro-aio/receiver/IMG_9243.jpg)

![](/assets/images/blueretro-aio/receiver/IMG_9244.jpg)

![](/assets/images/blueretro-aio/receiver/IMG_9245.jpg)

At this point, we can stop. However, I got the optional LED and resistor, which are useful for showing the status of the BlueRetro receiver (e.g. it flashes in pairing mode). I soldered on the LED and the resistor to the underside of the PCB:

![](/assets/images/blueretro-aio/receiver/IMG_13350.jpg)

![](/assets/images/blueretro-aio/receiver/IMG_13363.jpg)

The LED shows through the hole in the 3D-printed cover:

![](/assets/images/blueretro-aio/receiver/IMG_13359.jpg)

Here it is in action:

![](/assets/images/blueretro-aio/receiver/IMG_13364.jpg)


### N64

The N64 is probably the easiest adapter to build, so let's start with that one.

Parts:
- PCB
- 3D-printed shell
- DB25 connector (male, 90 degrees)
- N64 extension cables (1, 2, or 4)

![](/assets/images/blueretro-aio/n64/IMG_3324.jpg)

The N64 supports up to 4 controllers, but as I don't expect to play 4 player games very often, I decided to only build a 2-player adapter.

First, I undid my existing DIY adapter. If starting from scratch, you'd want to cut and strip the ends of the extension cables, and tin each end:

![](/assets/images/blueretro-aio/n64/IMG_3326.jpg)

![](/assets/images/blueretro-aio/n64/IMG_3328.jpg)

I inserted the two cables into the 2-player bottom shell:

![](/assets/images/blueretro-aio/n64/IMG_3329.jpg)

I then soldered the DB25 connector to the PCB:

![](/assets/images/blueretro-aio/n64/IMG_3330.jpg)

![](/assets/images/blueretro-aio/n64/IMG_3331.jpg)

Next up was wiring the cables to the PCB. I referred to the [schematic](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-Cables-Build-Instructions#cable-schematic-15) I had printed before where I had identified which color wire each of the three pins mapped to:

![](/assets/images/blueretro-aio/n64/IMG_3327.jpg)

In my case, white is data, red is 3V3, and black in ground. So I soldered the three wires from the first controller to P1DATA, P13V3, and P1GND respectively. I then did the same for the second controller:

![](/assets/images/blueretro-aio/n64/IMG_3334.jpg)

Since I decided not to connect player 3 and player 4 cables, as per the [assembly instructions](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-Cables-Build-Instructions#assembly-instructions-26), I needed to connect P3DATA and P4DATA to 3V3. This is how the BlueRetro knows that these are not connected. I did this by soldering a short (pink) wire to P23V3 on one end, and the other end to both P3DATA and P4DATA:

![](/assets/images/blueretro-aio/n64/IMG_3335.jpg)

With the wiring done, it was time to put it all together:

![](/assets/images/blueretro-aio/n64/IMG_3336.jpg)

To avoid the wires being ripped off the PCB, I used a couple of small zip ties that I tied very tightly to the ends of the cables:

![](/assets/images/blueretro-aio/n64/IMG_3337.jpg)

I then threaded the cables out, positioned the PCB in the shell, and closed it all up:

![](/assets/images/blueretro-aio/n64/IMG_3338.jpg)

![](/assets/images/blueretro-aio/n64/IMG_3339.jpg)

![](/assets/images/blueretro-aio/n64/IMG_3340.jpg)

Done!

![](/assets/images/blueretro-aio/n64/IMG_3343.jpg)


### GameCube

The GameCube adapter is about as easy as the N64 one, only with a few more wires to solder.

Parts:
- PCB
- 3D-printed shell
- DB25 connector (male, 90 degrees)
- GameCube extension cables (1, 2, or 4)

![](/assets/images/blueretro-aio/gamecube/IMG_3631.jpg)

First, I undid my existing adapter. If starting from scratch, you'd want to cut and strip the ends of the extension cables, and tin each end:

![](/assets/images/blueretro-aio/gamecube/IMG_3634.jpg)

I inserted the two cables into the 2-player bottom shell:

![](/assets/images/blueretro-aio/gamecube/IMG_3643.jpg)

Next, I soldered the DB25 connector to the PCB:

![](/assets/images/blueretro-aio/gamecube/IMG_3636.jpg)

![](/assets/images/blueretro-aio/gamecube/IMG_3639.jpg)

![](/assets/images/blueretro-aio/gamecube/IMG_3642.jpg)

Now for wiring the cables to the PCB. I referred to the [schematic](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-Cables-Build-Instructions#cable-schematic-17) I had printed before where I had identified which color wire each of the three pins mapped to:

![](/assets/images/blueretro-aio/gamecube/IMG_3644.jpg)

In my case, red is DATA, white is 5V, black and blue are GND, and green is 3V3, which is not used in this adapter.

I started off by soldering the black and blue GND wires for player 1 and 2 to their respective pads, P1GND and P2GND:

![](/assets/images/blueretro-aio/gamecube/IMG_3646.jpg)

I then soldered the rest of the wires, player 1 red and white to P1DATA and P15V, and player 2 red and white to P2DATA and P25V:

![](/assets/images/blueretro-aio/gamecube/IMG_3649.jpg)

Similar to the N64 adapter, because I wasn't connecting player 3 and 4 cables, I needed to connect P3DATA and P4DATA high, so I used a short piece of orange wire to connect these two pads to P25V. Note that the [assembly instructions](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-Cables-Build-Instructions#assembly-instructions-30) actually say to connect these to 3V3, which I could have done by hooking up the 2 green wires to these two pads; but the ESP32 module should be able to handle the 5V on these two pins.

With the wiring done, I used zip ties to create strain reliefs:

![](/assets/images/blueretro-aio/gamecube/IMG_3650.jpg)

![](/assets/images/blueretro-aio/gamecube/IMG_3651.jpg)

![](/assets/images/blueretro-aio/gamecube/IMG_3652.jpg)

Once again, the screw posts on the DB25 connector need to be removed, though the metal face plate remains:

![](/assets/images/blueretro-aio/gamecube/IMG_3653.jpg)

![](/assets/images/blueretro-aio/gamecube/IMG_3654.jpg)

![](/assets/images/blueretro-aio/gamecube/IMG_3655.jpg)

Done!

![](/assets/images/blueretro-aio/gamecube/IMG_3656.jpg)

Here it is, hooked up to the receiver:

![](/assets/images/blueretro-aio/gamecube/IMG_3657.jpg)


### PSX/PS2

The PSX/PS2 adapter is also straightforward to build.

Parts:
- PCB
- 3D-printed shell
- DB25 connector (male, 90 degrees)
- PSX/PS2 extension cables (1 or 2)

First, I undid my existing adapter. If starting from scratch, you'd want to cut and strip the ends of the extension cables, and tin each end:

![](/assets/images/blueretro-aio/psx-ps2/IMG_3106.jpg)

![](/assets/images/blueretro-aio/psx-ps2/IMG_3107.jpg)

Next, I soldered the DB25 connector to the PCB:

![](/assets/images/blueretro-aio/psx-ps2/IMG_3108.jpg)

![](/assets/images/blueretro-aio/psx-ps2/IMG_3111.jpg)

I threaded the cables through the bottom shell:

![](/assets/images/blueretro-aio/psx-ps2/IMG_3121.jpg)

Now it was time to wire the cables to the PCB. I referred to the [schematic](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-Cables-Build-Instructions#cable-schematic-10) I had printed before, where I had identified which color wire maps to which of the controller 9 pins:

![](/assets/images/blueretro-aio/psx-ps2/IMG_3115.jpg)

The PCB has all the player 1 pads on one side, and player 2 pads on the other side. I soldered the player 1 wires to each pad:

![](/assets/images/blueretro-aio/psx-ps2/IMG_3117.jpg)

Then flipped the PCB and soldered the player 2 wires:

![](/assets/images/blueretro-aio/psx-ps2/IMG_3119.jpg)

Note that on both sides, I did not solder anything to pads P1-3 and P2-3. This is because Pin 3 is 8V and Pin 5 is 3V3, and you should only solder one of these, not both for BlueRetro to work properly. I chose to solder to pin 5, and left the white wire (pin 3) disconnected.

With wiring done, it was time to close things up:

![](/assets/images/blueretro-aio/psx-ps2/IMG_3123.jpg)

I removed the screw posts. Note that the metal face plate should be kept on the DB25 connector, unlike in this pic:

![](/assets/images/blueretro-aio/psx-ps2/IMG_3124.jpg)

I used zip ties to create strain reliefs:

![](/assets/images/blueretro-aio/psx-ps2/IMG_3125.jpg)

![](/assets/images/blueretro-aio/psx-ps2/IMG_3127.jpg)

Then closed everything up:

![](/assets/images/blueretro-aio/psx-ps2/IMG_3128.jpg)

![](/assets/images/blueretro-aio/psx-ps2/IMG_3130.jpg)

![](/assets/images/blueretro-aio/psx-ps2/IMG_3131.jpg)

Done!

![](/assets/images/blueretro-aio/psx-ps2/IMG_3132.jpg)


### SNES - 2 Player

The first time I made the SNES adapter, it only supported 2 players. I also didn't have my 3D printer yet, so this build was a little bare-boned.

Parts:
- PCB
- DB25 connector (male, 90 degrees)
- SNES extension cables (x2)
- 74AHCT125N quad level-shifters (x2 for 2-player)

![](/assets/images/blueretro-aio/snes-2p/IMG_8331.jpg)

Looking at the [schematic](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-Cables-Build-Instructions#cable-schematic-6), it initially looks like we need to wire up 7 wires for the first controller, and 6 for the second, because the LATCH (pin 3) is not required for player 2:

![](/assets/images/blueretro-aio/snes-2p/schematic_left.jpg)

However, the rest of the schematic outlines connections in blue that only need to be made if you want multitap support:

![](/assets/images/blueretro-aio/snes-2p/schematic_right.jpg)

In this build, we're only interested in supporting 2 players, so we don't need to connect P1-SEL, P2-SEL, P1-D1, and P2-D1. We also don't need a third level-shifter. So that means we only need 5 wires for the first controller, and 4 for the second. In fact, it turns out that SNES controllers (and extension cables) only have 5 wires in them. The other pins are left unpopulated, and were there for third-party adapters, such as the light gun and the multitap.

Alright, on with the build!

First, I cut, stripped, and tinned the extension cables:

![](/assets/images/blueretro-aio/snes-2p/IMG_8334.jpg)

![](/assets/images/blueretro-aio/snes-2p/IMG_8342.jpg)

Using my multimeter, I identified the mapping of each pin to each wire color. You can see how there are only 5 wires:

![](/assets/images/blueretro-aio/snes-2p/IMG_8343.jpg)

Next, I soldered in the 2 level-shifters to the PCB:

![](/assets/images/blueretro-aio/snes-2p/IMG_8344.jpg)

![](/assets/images/blueretro-aio/snes-2p/IMG_8346.jpg)

Then I soldered the DB25 connector:

![](/assets/images/blueretro-aio/snes-2p/IMG_8347.jpg)

![](/assets/images/blueretro-aio/snes-2p/IMG_8352.jpg)

If I had the 3D-printed shells, I would normally have inserted the controller cables into them here. But I didn't, so I proceeded to solder each one to the PCB:

![](/assets/images/blueretro-aio/snes-2p/IMG_8353.jpg)

Player 1 side:

![](/assets/images/blueretro-aio/snes-2p/IMG_8354.jpg)

Player 2 side:

![](/assets/images/blueretro-aio/snes-2p/IMG_8357.jpg)

Note that the player 2's latch wire (white) is not soldered to the board:

![](/assets/images/blueretro-aio/snes-2p/IMG_8358.jpg)

In retrospect, I realize that one thing I forgot to do is to "connect IO21 & IO25 to GND", as per the [assembly instructions](https://github.com/darthcloud/BlueRetro/wiki/BlueRetro-Cables-Build-Instructions#assembly-instructions-11), since we're not enabling multitap support. Concretely, this means I should have soldered the P1-D1 and P2-D1 pads to one of the GND pads.

As I didn't have my 3D printer yet, I used a couple of zip ties to secure the wires:

![](/assets/images/blueretro-aio/snes-2p/IMG_8377.jpg)

And with that, I was done. In the next section, I convert this one to support 4-player multitap mode, and add a proper shell.


### SNES - Multitap

Making a [multitap](https://en.wikipedia.org/wiki/Multitap#Fourth_generation) BlueRetro adapter is a bit more work because SNES controllers/extensions only have 5 wires in them, but we need 7 for the first player, and 6 for the second. This means we need a 7 wire cable for each controller, as well as 3 extra pin ends to insert into the SNES controller ends. All of this will be made clearer below.

Parts:
- PCB
- DB25 connector (male, 90 degrees)
- 7 wire cable (can use a PSX/PS2 controller cable)
- SNES controllers/extensions (3x)
- 74AHCT125N quad level-shifters (x3 for 4-player)

First, I took apart the 2-player version I had made, and soldered in the third level-shifter:

![](/assets/images/blueretro-aio/snes-4p/IMG_0976.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_0978.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_0979.jpg)

I had bought a lot of Super Famicom controllers on eBay with the intention of converting four of them into Bluetooth controllers using [8BitDo mod kits](https://www.8bitdo.com/mod-kit-for-snes-controller/). As I didn't need the cables, I decided to use the controller ends from two of them:

![](/assets/images/blueretro-aio/snes-4p/IMG_0982.jpg)

It turns out it's really heard to open up the controller end. I made myself a little tool using one of those paper clips:

![](/assets/images/blueretro-aio/snes-4p/IMG_0983.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_0985.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_0986.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_0987.jpg)

This was still really hard, so I ended up using a blade to cut off the two plastic pegs on the other side. Once cut, and using my tool, I was finally able to pry off the end:

![](/assets/images/blueretro-aio/snes-4p/IMG_1078.jpg)

Lifting up the plastic "door", we can see how SNES controllers only have 5 wires in them, leaving 2 pins empty:

![](/assets/images/blueretro-aio/snes-4p/IMG_1042.jpg)

Our goal is to cut off all those metal pins and resolder them to a 7-cable wire. But for that, I needed 3 more pins, which I got from one of the extension cables:

![](/assets/images/blueretro-aio/snes-4p/IMG_1073.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1075.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1081.jpg)

I cut off all the ends, keeping a little bit of the wire:

![](/assets/images/blueretro-aio/snes-4p/IMG_1085.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1088.jpg)

7 wires for player 1 (top), and 6 for player 2 (bottom):

![](/assets/images/blueretro-aio/snes-4p/IMG_1089.jpg)

I used an 8-wire cable I had lying around. Another alternative is to use a PSX/PS2 controller cable, which has 7 wires in it:

![](/assets/images/blueretro-aio/snes-4p/IMG_1090.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1091.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1092.jpg)

I soldered the controller end pins to each cable:

![](/assets/images/blueretro-aio/snes-4p/IMG_1102.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1103.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1104.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1105.jpg)

I then reinserted the pins back into the controller ends, making sure they matched up with the schematic.

![](/assets/images/blueretro-aio/snes-4p/IMG_1106.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1111.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1112.jpg)

I slid the cap back on, but left it loose until the very end. It was a pain to remove, so I wanted to make sure everything worked first:

![](/assets/images/blueretro-aio/snes-4p/IMG_1116.jpg)

I inserted the player 2 cable wires, which is missing the LATCH wire (third from left):

![](/assets/images/blueretro-aio/snes-4p/IMG_1125.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1129.jpg)

These cables were pretty thick, so to insert them into the bottom shell, I needed to make the hole bigger by manually twisting a drill bit through the holes:

![](/assets/images/blueretro-aio/snes-4p/IMG_1134.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1136.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1137.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1138.jpg)

I soldered the player 1 wires to one side of the PCB:

![](/assets/images/blueretro-aio/snes-4p/IMG_1139.jpg)

Then player 2:

![](/assets/images/blueretro-aio/snes-4p/IMG_1141.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1142.jpg)

To close things up, I needed to add some kind of strain relief to the cable end:

![](/assets/images/blueretro-aio/snes-4p/IMG_1152.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1154.jpg)

This didn't quite fit in the little cavity inside the cable end cover, so I snipped a little off the zip tie, and that worked:

![](/assets/images/blueretro-aio/snes-4p/IMG_1162.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1163.jpg)

I also put the usual strain reliefs on the other end of the cables so that they stay inside the shell:

![](/assets/images/blueretro-aio/snes-4p/IMG_1171.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1172.jpg)

And closed everything up:

![](/assets/images/blueretro-aio/snes-4p/IMG_1174.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1178.jpg)

![](/assets/images/blueretro-aio/snes-4p/IMG_1179.jpg)

Done!

![](/assets/images/blueretro-aio/snes-4p/IMG_1180.jpg)


### NES

The last build I'm covering is the NES one. This one is simpler that the SNES one, but I cover it afterwards because I ended up using a SNES PCB instead of an NES one. The reason for this is that the NES and SNES controllers are very similar, as are the PCBs for both. Since JLPCB requires a minimum order of 5 PCBs, this also allowed me to save money and avoid printing 5 more for the NES. 

Parts:
- PCB
- DB25 connector (male, 90 degrees)
- NES extension cables (x2)
- 74AHCT125N quad level-shifters (x2)

The first thing I did was compare the two PCBs online, and map out the differences:

![](/assets/images/blueretro-aio/nes/IMG_8664.jpg)

Basically, the pads map this way:

| NES    | SNES   |
| ------ | ------ |
| P1-D0  | P1-D0  |
| P1-CUP | P1-CLK |
| OUT0   | LATCH  |
| GND1   | GND1   |
| 5VIN1  | 5VIN1  |
|        |        |
| P2-D0  | P2-D0  |
| P2-CUP | P2-CLK |
| GND2   | GND2   |
| 5VIN2  | 5VIN2  |

The other important part is how the BlueRetro identifies that it's the NES that's connected, and not the SNES. The way it does this is by looking at pin 22 of the DB25 connector: if it's tied to GND, then it's a SNES, if it's tied to 3V3, it's an NES. The SNES PCB is designed to tie pin 22 to GND, so we need to address this.

First, I soldered the two level-shifters to the PCB:

![](/assets/images/blueretro-aio/nes/IMG_8666.jpg)

![](/assets/images/blueretro-aio/nes/IMG_8667.jpg)

![](/assets/images/blueretro-aio/nes/IMG_8668.jpg)

Now here is where we address pin 22 that needs to be tied to 3V3. What I did was bend pin 22 across this way:

![](/assets/images/blueretro-aio/nes/IMG_8669.jpg)

Then I soldered the connector to the PCB. Notice how one of the vias has no pin coming through it:

![](/assets/images/blueretro-aio/nes/IMG_8670.jpg)

That pin 22 I lifted is visible on the other side:

![](/assets/images/blueretro-aio/nes/IMG_8672.jpg)

![](/assets/images/blueretro-aio/nes/IMG_8673.jpg)

Since we need this to be tied to 3V3, I soldered a short wire from that pin to the 3V3 leg of one of the level shifters:

![](/assets/images/blueretro-aio/nes/IMG_8675.jpg)

For the cables, I took apart the DIY adapter I had made before:

![](/assets/images/blueretro-aio/nes/IMG_8676.jpg)

![](/assets/images/blueretro-aio/nes/IMG_8679.jpg)

I stripped and tinned the wires, then passed the cables through the bottom shell:

![](/assets/images/blueretro-aio/nes/IMG_9096.jpg)

I soldered the wires to the PCB, starting with player 1:

![](/assets/images/blueretro-aio/nes/IMG_8682.jpg)

And player 2:

![](/assets/images/blueretro-aio/nes/IMG_8684.jpg)

Finally, I removed the screw posts, added zip tie strain reliefs, and put it all together:

![](/assets/images/blueretro-aio/nes/IMG_9099.jpg)

![](/assets/images/blueretro-aio/nes/IMG_9103.jpg)

![](/assets/images/blueretro-aio/nes/IMG_9105.jpg)

![](/assets/images/blueretro-aio/nes/IMG_9106.jpg)

![](/assets/images/blueretro-aio/nes/IMG_9107.jpg)

All done!

![](/assets/images/blueretro-aio/nes/IMG_9108.jpg)


## Thoughts

I've already mentioned multiple times how much I love the BlueRetro project, so I'll share my thoughts on the difference between these AIO units over the standard DIY through-hole method.

Overall, the main advantages to the AIO units are:

1. They're easier to build, as you get to solder wires to a PCB rather than to pins of a DB25 connector or level shifter.
2. It's easier to get the orientation right when connecting the receiver to the adapter, since the 3D-printed shell has a very clear "top" side that you need to line up.
3. They just look nicer with the 3D-printed shell.

The disadvantages are:
1. They're more expensive to make, as you need to get the PCBs and 3D-printed parts made.
2. The 3D-printed part models don't print as nicely with FDM printers. The general shape and small grooves results in long bridges, which despite my best efforts, never looked as beautiful as I hoped.

Having said all that, I'm actually quite happy with these AIO units, and would definitely recommend them!
