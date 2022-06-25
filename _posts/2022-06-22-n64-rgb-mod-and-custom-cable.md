---
layout: post
title: "N64 RGB Mod and Custom Cable"
tags: [electronics, mod]
comments: true
---
In this post, I'll go over how I RGB-modded my N64, and how I built a custom cable to connect it to my [gbs-control]({% post_url 2022-04-01-gbs-control %}).

## RGB Mod

For the RGB mod, following [this excellent guide on retrorgb.com](https://www.retrorgb.com/n64rgbcompatible.html), I confirmed that my N64 was an earlier revision with a VDC-NUS video chip, which meant that I could install a "basic" RGB mod.

Initially, I tried to buy [Voultar's kit](https://voultar.com/index.php?route=product/product&product_id=50&tracking=5824d766cf098), but shipping outside the US was not available. So I decided to order it from AliExpress. Search for "N64 RGB Mod", and you should get a few hits. The one I ordered is based off the [bitfunx.com version](https://www.bitfunx.com/2022/04/02/n64rgb-installation-guide/). I received it a few weeks later:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5746.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5747.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5748.jpg)

I opened up my N64 and got the PCB out:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5751.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5757.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5761.jpg)

There are a good number of different sized screws, so I highly recommend keeping track of each set on a drawing so that it's easy to put back together. Also note that you don't need to remove the heat shield for this mod.

With the PCB out, I could now install the mod board over the multiout pins beneath the board (top-left):

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5762.jpg)

As per the instructions, I added some wire tape to cover up a portion of the bottom, to ensure no shorts:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5764.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5765.jpg)

Then I placed it over the multiout pins and soldered it in place, making sure to use flux to ensure a solid connection:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5766.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5769.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5770.jpg)

This is what it looked like after cleaning up with some IPA:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5772.jpg)

Next up was to solder the three wires to the red, green, and blue sources on the N64 PCB at the vias labelled R8, R9, and R10 respectively. The kit comes with the three wires, conveniently colored red, green, and blue. It's really important not to insert the wires too far into the vias, otherwise they will make contact with one of the legs of the IC on the other side, and the mod will not work. I cut the ends of the wire very short:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5774.jpg)

I used a fiberglass pen to remove any solder mask and residue off the three vias, added flux, and soldered the three wires in place:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5777.jpg)

Next, I added a wire for clean CSYNC to the via labelled R16:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5780.jpg)

Note that my revision of the N64 motherboard did not have CSYNC connected to the multiout's pin 3, so I did not have to do any more than this. I knew this because C22, R1, and R14 were all unpopulated:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5766-2.jpg)

If the cap and two resistors are there, you can simply remove them.

Finally, I cut the 4 wires to length and soldered them to their respective pads on the mod board:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5786.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5788.jpg)

Although this came later while testing, I'll mention it here: the mod board uses a [THS7374 IC](https://www.ti.com/lit/ds/symlink/ths7374.pdf?ts=1656112700901&ref_url=https%253A%252F%252Fwww.google.com%252F#:~:text=THS7374%20is%20a%20low%2Dpower,MHz%20(%E2%80%933%20dB)%20Butterworth) as a video amplifier, and has an option to bypass this IC's built-in filtering by soldering two pads together. After testing both, I decided that I preferred the look without the filtering, and soldered the two pads under the BYPASS label:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5819.jpg)

With the mod in place, it was time to close up the console. The only thing is that the metal shielding now comes into contact with the new mod board, making it difficult to close, and possibly resulting in shorts:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5884.jpg)

So I used some pliers to fold in this flap in:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5885.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5886.jpg)

Now I could finally close up the console:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5887.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5889.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5891.jpg)

## Custom RGB to 15 Khz "VGA" cable

With the RGB mod complete, I now needed a way to connect my N64 to my TV to actually play in RGB mode. The most common way people do this is by purchasing an [HD Retrovision SNES YPbPr cable](https://www.hdretrovision.com/snes). This cable will work with the N64 mod, but it's quite expensive and usually on backorder, taking months to arrive.

Since I knew I had a gbs-control, I decided to make my own cable, [like I did for my PS1]({% post_url 2022-04-02-ps1-vga-mod %}). One of the challenges would be to output not only video, but also audio. Further, I had read that the RGB signals would need 220uF capacitors on each line to properly attenuate the signals. In searching for cable options, I stumbled upon [this one by retro-access.com](https://retro-access.com/collections/rgbs-dsub-cables/products/fortraflex-super-nintendo-ntsc-individually-shielded-rgbs-dsub-cable) and used it as inspiration.

### Design

Here's a table of the final design for how I wired everything up (see pinouts for each below):

| SNES Signal | SNES Pin | VGA Pin | VGA Signal | RCA Audio | Cable Color |
|-------------|----------|---------|------------|-----------|-------------|
| Red         | 1        | 1       | Red        |           | Red         |
| Green       | 2        | 2       | Green      |           | Green       |
| Blue        | 4        | 3       | Blue       |           | Blue        |
| GND         | 5        | 10      | GND        |           | Black       |
| SVID-Y      | 7        | 13      | HSYNC      |           | Yellow      |
| Right Audio | 11       |         |            | Red       | Orange      |
| Left Audio  | 12       |         |            | White     | White       |
| GND         | 6        |         |            | GND       | Brown       |

The Cable Color column is not really relevant to how to wire this up - I just assigned colors based on the cable I ordered from AliExpress. I left it here, though, as it will help to understand the pictures below.

One thing to note: in creating my cable, I went through a few different iterations of determining how to best connect sync from the SNES multiout to my GBS-control via VGA pin 13. I had three options: CSYNC (pin 3), composite video (pin 9), or S-video Y (pin 7). CSYNC is the pure sync signal from the N64 that I connected to the multiout as part of the RGB mod install. This is a TTL-level signal, which means that a 480 ohm resistor in series is required to attenuate the signal down to expected levels for most TVs and the gbs-control. The other two are video signals that also carry sync in them. After testing out each option, I found that using S-video Y worked best with my gbs-control, resulting in no sync loss, and no audio interference. I mention this, though, as it may not be the best solution for everyone.

Here's the pinout for the N64 (and SNES) multiout connector for North American revisions from [pinoutguide.com](https://pinoutguide.com/Game/n64video_pinout.shtml):

![](/assets/images/n64-rgb-mod-and-custom-cable/n64_snes_pinout.jpg)

NOTE: CSYNC (pin 3) is replaced by +12V on PAL SNES and PAL Gamecube consoles (but not PAL N64), so it's really important not to use this cable on those models.

Here's the pinout for a standard DE-15 VGA style connector from [Wikipedia](https://en.wikipedia.org/wiki/VGA_connector):

![](/assets/images/n64-rgb-mod-and-custom-cable/vga_pinout.jpg)

For the audio output, I decided to use a regular white + red RCA cable, as gbs-control uses this for audio input.

### Creating the cable

From AliExpress, I ordered the parts I would need:

* SNES male connector, $5.31 for 2
* DE-15 male VGA style connector, $3.70 for 2
* D-size 10V 220uF tantalum capacitors, $4.61 for 10
* 5 meters 8 core 28 AWG sheathed wire, $10.21

I received everything after a few weeks:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5789.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5995.jpg)

#### VGA + Audio End

I stripped one end of my (way too long) cable, stripped each wire, and tinned them:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5795.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5797.jpg)

I soldered each wire for the video signal to the VGA connector, leaving the audio connectors aside:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5802.jpg)

Using an old RCA audio cable, I cut it down to length, combined the grounding wires wrapped around each of red and white, and tinned all three:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5837.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5839.jpg)

I soldered them to their respective wires on the cable, and covered up the exposed wires with heat shrink tubing:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5856.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5860.jpg)

Finally, I put everything together into the VGA connector shell, clamping both the main cable along with the RCA cable together with the strain relief:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5861.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5862.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5863.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5864.jpg)

I must say that I'm quite happy with how this side ended up. Here's what it looks like connected to the gbs-control:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5866.jpg)

#### Multiout End Attempt #1

For the SNES multiout end, initially, to test things out, I actually soldered Dupont cables so that I could test things with a breadboard, like capacitor values and resistors. Also, the tantalum caps took a little longer to receive than the rest of the parts, so this way I could at least use through-hole caps:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5832.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5831.jpg)

It may not be clear in the image above, but I actually had three pairs of 100uF capacitors in parallel to get close to the 220uF required for each color signal. With this in place, I was able to test the cable, and amazingly it worked first try!

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_5810.jpg)

Once the tantalum caps came in, it was time to properly wire the multiout end. This part was much harder, and quite fiddly. The multiout shells available on AliExpress (and other sources as far as I can tell) are smaller than the original. For comparison, here's the one I got from AliExpress (top) compared to the original N64 multiout cable (bottom):

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6066.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6067.jpg)

The real challenge was fitting the tantalum capacitors along with the rest of the wires in this small shell:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6005.jpg)

I tried many things, but I'll only share a couple here. First, I shortened and soldered the RGB lines to the caps:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6007.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6008.jpg)

I soldered the rest of the wires to their respective pins on the multiout connector:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6013.jpg)

The red heat shrink tubing is something I initially put around the 3 tantalum caps, but eventually removed because I found it too difficult to manage. Instead, I wrapped the three caps in some wire tape to keep them together:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6030.jpg)

The multiout shell did not come with any kind of strain relief, so I made my own using two tie wraps threaded into each other:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6033.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6034.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6035.jpg)

Finally, I squeezed everything into the shell, which required folding up the caps vertically:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6036.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6037.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6038.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6039.jpg)

I must say, I was quite pleased at this point; however, after a bit of use, the colors started messing up, and wiggling the wire would sometimes restore it. So I took it apart, and tried something else.

#### Multiout End Attempt #2

I figured that the reason the cables came undone might be because the caps were not really held well together (I was probably wrong about this, more on that later). So I used my least favorite tool, my glue gun, and ended up with this mess:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6100.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6101.jpg)

One good thing about the glue, I told myself, was that at least the exposed pads and wires could not be shorted against.

I also decided to forgo the clever dual tie-wrap strain relief, figuring it was just too tight in the shell, and that might have also contributed to the flakiness. Instead, I wrapped up the cable in loads of wire tape, until it fit very snugly into the shell:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6103.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6105.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6106.jpg)

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6108.jpg)

This is how my cable ended up. However, I will say that I really don't like having this wire tape sticking out, and it doesn't feel like a permanent solution, knowing that wire tape eventually softens and often comes unstuck after a while.

I think the real reason my first attempt failed was because I cut the RGB wires coming out of the cable too short - especially the red one. They were not long enough to allow for any movement of the cable. If I were to redo this, I'd go with my first attempt, make the RGB wires longer, and maybe put hot glue around twist-tie end to make it thicker so that it doesn't move as much inside the shell.

### Results

With the cable working, here are comparison shots of Mario 64 using the N64's official composite cable going straight to my TV (left) vs the custom cable I made going to the TV via the gbs-control (right):

![](/assets/images/n64-rgb-mod-and-custom-cable/rgb_cable_n64_compare.jpg)

Keep in mind that the images above were taken with my phone camera of my TV screen, and then compressed, so it doesn't really do it justice. However, you should notice how the typical composite signal artifacts are gone. In person, especially on my 70" TV, the quality difference is astounding.

Since I can use this same cable with an SNES, here are more comparison shots of Super Mario World:

![](/assets/images/n64-rgb-mod-and-custom-cable/rgb_cable_snes_compare.jpg)

With a 2D game, the differences are even more obvious.

### Thoughts

I've been playing a bunch of N64 games since I made this mod, and I must say that I'm quite pleased with the results. The total cost for me was quite low, given that I could use a simple RGB board, and because I made my own cable.

The N64 RGB mod itself was very easy to do; however, making the cable was more challenging than expected because of the small multiout shell. One thought I had was sacrificing an original SNES/N64 composite multiout cable to be able to use the larger shell, but I'm not a fan of destroying original cables.

One other thing I would change is the length of the cable as it's way too long. Instead of 5 meters, I would have been fine with 5 feet. I'll probably cut it down to size someday, but so far it hasn't been a real problem.

Anyway, to wrap this up, if you find yourself in a similar situation, I would definitely recommend this mod!
