---
layout: post
title: "N64/SNES Custom Cable - Take 2"
tags: [Electronics, SNES, N64]
comments: true
---

A few months ago, I [wrote about]({% post_url 2022-06-22-n64-rgb-mod-and-custom-cable %}#custom-rgb-to-15-khz-vga-cable) how I made a custom cable to hook up my N64 to my gbs-control. Although the VGA + Audio end worked out fine, I wasn't super happy with the multiout end. I had made a bunch of mistakes:

Mistake #1: I had cut the RGB wires too short because I knew I'd need to solder the 220uF caps in between them and the multiout pins. As a result, these pins got disconnected too easily once some strain was put on the cable:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6007.jpg)

Mistake #2: I had removed my clever dual tie-wrap strain relief because I thought it might have contributed to the color issues I was having with it (it hand't), and because it took up precious space in the shell:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6037.jpg)

Instead, I replaced it with wire tape (yuck!), and sure it enough, after some use, the whole thing slipped back out of the shell:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6106.jpg)

Mistake #3: I had covered the caps in hot glue to avoid the wires getting detached. Although this worked, it was awkward and made the whole thing bulkier:

![](/assets/images/n64-rgb-mod-and-custom-cable/IMG_6100.jpg)


Having recently restored my childhood SNES, I needed a second custom cable, so now was my chance to learn from my mistakes and make an even better one!

I got all the parts I needed:

![](/assets/images/multiout-custom-cable-take-2/IMG_8098.jpg)

As before, I followed the [same design]({% post_url 2022-06-22-n64-rgb-mod-and-custom-cable %}#design) for how to wire up everything.


## VGA + Audio End

I stripped one end of the cable to expose the wires, stripped and tinned each wire, and then soldered all but the three audio wires to the DB15 connector:

![](/assets/images/multiout-custom-cable-take-2/IMG_8101.jpg)

I cut and prepared my audio RCA cable, exposing the leads and twisting the ground sheath together:

![](/assets/images/multiout-custom-cable-take-2/IMG_8102.jpg)

![](/assets/images/multiout-custom-cable-take-2/IMG_8103.jpg)

Using my new and awesome [Omnifixo](https://omnifixo.com/) helping hands, I soldered the RCA wires to the three audio wires from the cable, and used heat shrink to wrap them up:

![](/assets/images/multiout-custom-cable-take-2/IMG_8104.jpg)

![](/assets/images/multiout-custom-cable-take-2/IMG_8107.jpg)

I used the strain relief to hold both the cable and the RCA wires together, and put everything into the DB15 shell:

![](/assets/images/multiout-custom-cable-take-2/IMG_8109.jpg)

![](/assets/images/multiout-custom-cable-take-2/IMG_8112.jpg)

![](/assets/images/multiout-custom-cable-take-2/IMG_8114.jpg)


## Multiout End

Now it was time to make the Multiout end. This is where all the improvements kick in.

First, I lined up the three caps, and used a strip of Kapton tape underneath to hold them together:

![](/assets/images/multiout-custom-cable-take-2/IMG_8115.jpg)

![](/assets/images/multiout-custom-cable-take-2/IMG_8116.jpg)

I soldered the three RGB wires to teh caps, keeping them at full length:

![](/assets/images/multiout-custom-cable-take-2/IMG_8117.jpg)

I then soldered three 30 AWG wires to the other end of the caps:

![](/assets/images/multiout-custom-cable-take-2/IMG_8119.jpg)

Instead of hot glue, I wrapped up the caps with more Kapton tape. Not only is this so much easier, but it holds well, avoids shorts, and lets us see what's underneath:

![](/assets/images/multiout-custom-cable-take-2/IMG_8121.jpg)

![](/assets/images/multiout-custom-cable-take-2/IMG_8122.jpg)

Next, I soldered all the wires to the multiout:

![](/assets/images/multiout-custom-cable-take-2/IMG_8128.jpg)

![](/assets/images/multiout-custom-cable-take-2/IMG_8130.jpg)

Now for the strain relief. Again, I decided to use tie wraps, but very small ones:

![](/assets/images/multiout-custom-cable-take-2/IMG_8135.jpg)

I slid each end into the other to form a rectangle:

![](/assets/images/multiout-custom-cable-take-2/IMG_8137.jpg)

I slipped it around the cable, then closed it up and made it very tight around the edge of the cable:

![](/assets/images/multiout-custom-cable-take-2/IMG_8138.jpg)

![](/assets/images/multiout-custom-cable-take-2/IMG_8139.jpg)

I cut the ends off:

![](/assets/images/multiout-custom-cable-take-2/IMG_8140.jpg)

I tried packing it into the shell, but my tie wrap strain relief was a little big, so I used my flush cutters to snip some plastic off the top and bottom:

![](/assets/images/multiout-custom-cable-take-2/IMG_8142.jpg)

With a little patience, I was able to fit it all into the shell:

![](/assets/images/multiout-custom-cable-take-2/IMG_8141.jpg)

![](/assets/images/multiout-custom-cable-take-2/IMG_8144.jpg)

The strain relief works surprisingly well, keeping everything in place, and not ripping anything if the wire is pulled instead of the shell:

![](/assets/images/multiout-custom-cable-take-2/IMG_8146.jpg)

And with that, the cable's done!

![](/assets/images/multiout-custom-cable-take-2/IMG_8150.jpg)

A quick test shows that everything works perfectly:

![](/assets/images/multiout-custom-cable-take-2/IMG_8133.jpg)


## Thoughts

This attempt at making the cable was definitely much better than the first. In fact, right after making this one, I took the first one I had made and redid the multiout end on it. A few things that really helped this time around was having some helping hands, as well as Kapton tape.
