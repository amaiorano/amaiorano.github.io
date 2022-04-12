---
layout: post
title: "Genesis Vectrex Controller - Take 2"
tags: [electronics, mod, Vectrex]
comments: true
---

Back in January 2020, I made my [first Genesis Vectrex controller mod]({% post_url 2020-01-02-genesis-vectrex-controller %}). As it was my first, and my electronics skills were still in development, it wasn't the cleanest job. In September 2021, I decided to make a second one. This one went much better.

## The Build

As with the previous mod, I opened the controller and cleaned everthing:

![](/assets/images/genesis-vectrex-controller-2/IMG_3463.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3464.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3466.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3467.jpg)

I removed all unnecessary components (resistors and IC) from the PCB:

![](/assets/images/genesis-vectrex-controller-2/IMG_3420.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3421.jpg)

This PCB layout is different from the first one I modded. Using a photo editing tool, I marked up the solder points and where to cut traces:

![](/assets/images/genesis-vectrex-controller-2/genesis_vectrex_plan.jpg)

In the photo above, you can see three red lines (top-left, middle-left, and bottom-right) where I need to cut the traces. These are important because unlike the Genesis, the Vectrex has an analog stick, so it uses +5V and -5V as a reference rather than ground to get the stick's relative position. Also, with this layout, there wasn't a convenient pad available for the "Right Up +5V", so you can see in yellow how I planned to scrape solder mask off the narrow trace near the right button pad, and bridge it to via on the right, where +5V would be connected.

With this plan in place, I proceeded to solder two sets of 2x10K and 2x3.3K resistors together. I found twisting the legs together, and soldering the twisted part to be the easiest way:

![](/assets/images/genesis-vectrex-controller-2/IMG_3424.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3425.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3426.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3427.jpg)

I soldered the resistors to the x-direction (green) and y-direction (blue) wires coming from the controller cable (note that the colors may not match in all controllers):

![](/assets/images/genesis-vectrex-controller-2/IMG_3438.jpg)

I soldered the other wires onto the ends of the resistors, using my multimeter to identify the correct ones ([this is still a good reference](https://www.playvectrex.com/vectech/controller.txt)):

![](/assets/images/genesis-vectrex-controller-2/IMG_3439.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3440.jpg)

Note that I'm using heat shrink now to avoid having to use wire tape as I did in my first build.

Next, I cut the three traces on the PCB:

![](/assets/images/genesis-vectrex-controller-2/IMG_3428.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3429.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3430.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3431.jpg)

And started wiring everything to the PCB as per my plan:

![](/assets/images/genesis-vectrex-controller-2/IMG_3444.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3445.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3447.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3448.jpg)

This is what it looked like when I was done:

![](/assets/images/genesis-vectrex-controller-2/IMG_3457.jpg)

Definitely much better than my first mod. The wires are cut to length, there's no need to use wire tape, and the whole thing takes less room than in my first mod. This means it will be that much easier to close up the controller, and less chance of accidental shorts.

On the other side of the PCB, I still needed to scrape the solder mask off that narrow trace and bridge it to where I would connect +5V. I used a cut off resistor leg to bridge it:

![](/assets/images/genesis-vectrex-controller-2/IMG_3453.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3454.jpg)

Finally, I put everything together into the controller case, making sure to carefully position the wires so that they didn't get in the way of the plastic from the top part:

![](/assets/images/genesis-vectrex-controller-2/IMG_3478.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3479.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3480.jpg)

I cut off the two corners of the connector side that goes into the Vectrex, using the actual Vectrex controller as a reference:

![](/assets/images/genesis-vectrex-controller-2/IMG_3459.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3460.jpg)

![](/assets/images/genesis-vectrex-controller-2/IMG_3461.jpg)

Done! I tested the controller, and it works perfectly.


## Thoughts

Being my second time doing this mod, and with more experience under my belt, I felt this mod went very smoothly. Now I have two Genesis controllers for my Vectrex, which makes it a lot more fun to play games like [Rip Off](https://vectrex.fandom.com/wiki/Rip_Off) with my kids. I definitely recommend it!
