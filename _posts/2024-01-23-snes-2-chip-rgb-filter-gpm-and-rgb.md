---
layout: post
title: "SNES 2-Chip RGB Filter Mod: SNS-CPU-GPM and SNS-CPU-RGB"
tags: [Electronics, SNES]
comments: true
toc: true
draft: true
---

A while back, I posted about how I [modded my 2-chip SNES]({% post_url 2022-10-14-snes-2-chip-rgb-filter-mod %}), model `SHVC-CPU-01`, to improve the video output quality using [Buttersoft's filter board](https://www.aussiearcade.com/topic/90003-snes-sfc-shvc-cpu-001-2-chip-rgb-filter-mod-video-fix/), then later posted how user [*axmcxx* performed a similar mod]({% post_url 2023-03-07-snes-2-chip-rgb-filter-rgb-02 %}) on his `SNS-CPU-RGB-02`. Well, another user on the [ConsoleMods](https://consolemods.org/wiki/Main_Page) Discord named *Toxic_Tripod0* reached out after modding various `SNS-CPU-GPM-01/02` models, and graciously shared his pics and steps with me so that I can share it with the community on my blog. He also performed this mod on `SNS-CPU-RGB-01/02` models, and we'll go over some of the improvements he made for these.

## SNS-CPU-GPM-01/02

### Parts

The list of parts is about the same as for the [`SHVC-CPU-01`]({% post_url 2022-10-14-snes-2-chip-rgb-filter-mod %}#parts), with these differences/extras:

* Cap Kit - $4.95 on [Console5](https://console5.com/store/snes-cap-kit-non-shvc-models.html)
* 35V In 5V Out 2A linear voltage regulator - ~$1.10 each from Mouser
* 470uF 6.3V electrolytic capacitor - $1.21 for 10 on AliExpress
* 1x 22uF X5R 0805 ceramic caps - $2.90 for 100 on AliExpress
* 11x 10uf X7R 0805 ceramic caps (instead of 8x) - $1.80 for 100 on AliExpress

Note that the voltage regulator is difficult to find as they are no longer in production. Look on Mouser, Digikey, eBay, or AliExpress, and make sure it's rated for 2A - most are 0.5A or 1A, and also rated for 35V input - most are 6.5V. The higher voltage rating means it runs cooler.


### The Build

Toxic_Tripod0 took apart his SNES, and then recapped it using a capacitor kit from Console5. He recommends this, especially after seeing that upon removal, most caps had leaked underneath. Leaking capacitors indicates that they are no longer working optimally, which not only affect their performance, but can erode and cause damage to the main board. Unfortunately, I don't have any pics of the recap, but Console5 provides excellent documentation and images to follow.

Next, he followed the [steps on my first post](({% post_url 2022-10-14-snes-2-chip-rgb-filter-mod %}#the-build)) on how to populate the filter board PCB. As with the `SHVC-CPU-01`, he removed and transferred the 3 transistors - this time at locations Q3, Q4, and Q5 - to the PCB, and wired them up:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/gpm_mainboard_rgb_wiring.jpg)

Next, he stacked the eleven 10uF ceramic caps on top of the existing ones at these locations (he actually recommends replacing them entirely rather than stacking):

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/gpm_mainboard_filter_caps.jpg)

In the picture above, we can also see that the 5V supply for the PCB is connected to the right-hand side of C83, while the board's ground is connected to the top of C91.

Here is where we diverge from the previous posts. To address the thick single white line that can sometimes be seen on the SNES, Toxic_Tripod0 first replaced the original voltage regulator with a new one:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/voltage_reg.jpg)

Then, on the underside of the board, where the three pins of the voltage regulator are soldered, he added a 470uF electrolytic capacitor on the 5V and GND pins of the regulator, and also replaced the 0.1uF ceramic cap at C81 with a 22uF X5R:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/gpm_mainboard_voltage_reg_filter.jpg)

Note that even if the SNES does not display the thick white line, Toxic_Tripod0 found that doing this mod helped to dim the faint vertical lines ("jailbars") that he was seeing.

Finally, he lifted pin 27 on PPU2, as this has the greatest impact on reducing jailbars:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/gpm_ppu2.jpg)

Note that Toxic_Tripod0 did not lift pin 3 on PPU2 because he did not notice any diagonal lines, as is common on `SNS-CPU-RGB` models. Lifting pin 3 results in the composite and s-video signals losing their color signal, so it's better if it can be avoided.

Here's a complete picture of all the mods made to the underside of the main board:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/gpm_mainboard_full.jpg)


## SNS-CPU-RGB-01/02

As I've already covered [*axmcxx*'s mod of a `SNS-CPU-RGB-02`](({% post_url 2023-03-07-snes-2-chip-rgb-filter-rgb-02 %})) before, we'll focus on the differences here.

### Parts

As usual, get the parts listed for the [`SHVC-CPU-01`]({% post_url 2022-10-14-snes-2-chip-rgb-filter-mod %}#parts), with these differences/extras:
* Cap Kit - $4.95 on [Console5](https://console5.com/store/snes-cap-kit-non-shvc-models.html)
* 3x extra transistors (2SA1037AKT146Q) - $0.30 each from [Digikey](https://www.digikey.com/en/products/detail/rohm-semiconductor/2SA1037AKT146Q/650439)
* 5V 2A linear voltage regulator - ~$1.10 each from Mouser
* 470uF 6.3V electrolytic capacitor - $1.21 for 10 on AliExpress
* 1x 22uF X5R 0805 ceramic caps - $2.90 for 100 on AliExpress
* 12x 10uf X7R 0805 ceramic caps (instead of 8x) - $1.80 for 100 on AliExpress

Unlike the `SHVC-CPU` and `SNS-CPU-GPM` models, we need to leave the 3 transistors on the main board, which is why 3 more need to be bought.

### The Build

Toxic_Tripod0 took apart his SNES and recapped it using the kit from Console5. Next, he followed the [steps on my first post](({% post_url 2022-10-14-snes-2-chip-rgb-filter-mod %}#the-build)) to populate the filter board PCB, this time installing the three new transistors on the PCB.

On the main board, he lifted the 'base' leg of each of the three transistors at Q1, Q2, and Q3, and then wired up to the mod board as follows:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/rgb_mainboard_rgb_wiring.jpg)

Here's a pic from *axmccx*'s install that shows more clearly how to lift the transistor legs, using some kapton tape to ensure it doesn't short with the pad on the main board:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/transistor_leg_lift.jpg)

Next, he replaced the twelve 10uF ceramic caps at the following locations:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/rgb_mainboard_filter_caps.jpg)

Above, we can also see that the 5V supply for the PCB is connected to the right of C63, while ground is connected to the left of C64. Also, the 10uF cap that between R9 and C10 is actually floating - there are no pads to solder to:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/rgb_floating_cap.jpg)

Toxic_Tripod0 used a wire to bridge the gap between the two locations, as the cap is too small. If you have a 1206 10uF capacitor, it might fit better. The reason for this capacitor is that on the schematics for the `SHVC-CPU` model, there is a filter cap between the green line at that point and ground, but this cap is missing from the `SNS-CPU-RGB` models entirely.

As with the `SNS-CPU-GPM`, he then replaced the voltage regulator:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/voltage_reg.jpg)

On the underside of the board, where the three pins of the voltage regulator are soldered, he added a 470uF electrolytic capacitor on the 5V and GND pins of the regulator, and also replaced the 0.1uF ceramic cap at C81 with a 22uF X5R:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/rgb_mainboard_voltage_reg_filter.jpg)

Finally, he lifted pins 3 and 27 on PPU2, to fix diagonal lines and jailbars respectively:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/rgb_ppu2.jpg)

Here's a complete picture of all the mods made to the underside of the main board:

![](/assets/images/snes-2-chip-rgb-filter-gpm-and-rgb/rgb_mainboard_full.jpg)


## Thoughts

Unfortunately, Toxic_Tripod0 did not take before/after pics, as he felt that it was difficult to see the differences this way. However, we can expect that the differences should be at least as good as what I've shown in the previous two posts, if not better considering the extra mods that were made. Toxic_Tripod0 told me that in person, the video output from his modded `SNS-CPU-GPM` looks identical to the 1-chip or the Jr.

Anyway, our hope is that this post is useful to those looking to perform a similar mod. Huge thanks to Toxic_Tripod0 for sharing his pics and experience!
