---
layout: post
title: "NES Restoration"
tags: [Electronics, NES]
comments: true
---

I bought a NES for $20 on Marketplace. The seller said it wasn't working well. I tested it, and sure enough I got the blinking screen most of the time. But with some fiddling, I managed to get a game working, so I knew it just needed a good cleaning and restoration. In this post, I go over the process of restoring this NES.

## Cleaning

The NES was a little dirty and yellowed:

![](/assets/images/nes-restoration/IMG_7518.jpg)

![](/assets/images/nes-restoration/IMG_7519.jpg)

![](/assets/images/nes-restoration/IMG_7523.jpg)

Inside was also pretty dirty:

![](/assets/images/nes-restoration/IMG_7526.jpg)

![](/assets/images/nes-restoration/IMG_7530.jpg)

The power/RF module was quite rusty:

![](/assets/images/nes-restoration/IMG_7528.jpg)

So I took everything apart:

![](/assets/images/nes-restoration/IMG_7533.jpg)

![](/assets/images/nes-restoration/IMG_7536.jpg)

![](/assets/images/nes-restoration/IMG_7537.jpg)

![](/assets/images/nes-restoration/IMG_7543.jpg)

I gave all the plastic parts a good clean:

![](/assets/images/nes-restoration/IMG_7547.jpg)

![](/assets/images/nes-restoration/IMG_7548.jpg)

I noticed some markings on the top shell:

![](/assets/images/nes-restoration/IMG_7549.jpg)

![](/assets/images/nes-restoration/IMG_7550.jpg)

To get rid of it, I used a vinegar and baking soda mixture, and some elbow grease:

![](/assets/images/nes-restoration/IMG_7552.jpg)

Much better:

![](/assets/images/nes-restoration/IMG_7553.jpg)

![](/assets/images/nes-restoration/IMG_7554.jpg)

## Retrobriting

Next step was retrobriting. For this, I used 6% hydrogen peroxide cream (aka 20 volume developer) diluted in water. I poured this into a bin that is surrounded by led strip lights, and I placed a more powerful UV lamp on top:

![](/assets/images/nes-restoration/IMG_7555.jpg)

![](/assets/images/nes-restoration/IMG_7556.jpg)

![](/assets/images/nes-restoration/IMG_7557.jpg)

![](/assets/images/nes-restoration/IMG_7558.jpg)

Retrobriting can take some time, depending on the concentration of the solution, and how yellowed the plastics are. In my case, I believe I left it in for about two days.

# Boiling the cartridge connector

While retrobriting, I took care of the cartridge connector. To improve cartridge connectivity, I boiled the connector for about 30 minutes, which helps to bring back the pins to their original positions:

![](/assets/images/nes-restoration/IMG_7615.jpg)

![](/assets/images/nes-restoration/IMG_7616.jpg)

![](/assets/images/nes-restoration/IMG_7621.jpg)

Although the boiling method helped, I did end up using a needle to push some of the more bent pins up into position. I don't love doing this, as it results in a tighter grip on the cartridge, but it's better than dealing with the blinking light issue.

## Rust removal

Next, I took care of the power module, removing the rust with some sandpaper:

![](/assets/images/nes-restoration/IMG_7612.jpg)

![](/assets/images/nes-restoration/IMG_7613.jpg)

![](/assets/images/nes-restoration/IMG_7614.jpg)

Not shown here, but I also used sandpaper to remove some rust off the RF shielding.

## Recapping

Next up was recapping. As most of the capacitors to change are in the power module, I needed to remove it from the main board. This is never an easy process, but with the right tools, and some patience, it's very doable.

First, I removed the metal cap on the power module to expose the 5 pins I needed to desolder:

![](/assets/images/nes-restoration/IMG_7622.jpg)

I added some fresh solder to each pin, then used my desoldering gun with a 1.5mm nozzle to remove the solder:

![](/assets/images/nes-restoration/IMG_7624.jpg)

![](/assets/images/nes-restoration/IMG_7623.jpg)

Next, I flipped the board over, and used a combination of my desoldering gun and some wick to remove the solder around the four legs that attach the power module to the main board:

![](/assets/images/nes-restoration/IMG_7625.jpg)

![](/assets/images/nes-restoration/IMG_7626.jpg)

![](/assets/images/nes-restoration/IMG_7628.jpg)

Once all the solder was removed, I grabbed the module, and slowly rocked it back and forth until it came off:

![](/assets/images/nes-restoration/IMG_7627.jpg)

![](/assets/images/nes-restoration/IMG_7629.jpg)

I was now able to remove the cover on the opposite side, revealing the capacitors that need replacing:

![](/assets/images/nes-restoration/IMG_7630.jpg)

![](/assets/images/nes-restoration/IMG_7631.jpg)

I wrote down the values and position of each cap:

![](/assets/images/nes-restoration/IMG_7633.jpg)

Then using a [cap kit I bought from Console5](https://console5.com/store/nintendo-nes-frontloader-cap-kit-nes-001.html), I matched up the caps to replace, keeping in mind that the capacitance (in farads) must match, but voltage can be greater or equal in value:

![](/assets/images/nes-restoration/IMG_7636.jpg)

![](/assets/images/nes-restoration/IMG_7637.jpg)

![](/assets/images/nes-restoration/IMG_7638.jpg)

![](/assets/images/nes-restoration/IMG_7639.jpg)

One problem I ran into was that the large 2200uF cap didn't fit through the hole on the metal cover. It was slightly too large. I ended up using a file to make the hole large enough:

![](/assets/images/nes-restoration/IMG_7640.jpg)

With that done, I soldered the power module back onto the board:

![](/assets/images/nes-restoration/IMG_7643.jpg)

![](/assets/images/nes-restoration/IMG_7644.jpg)

Finally, I removed the three caps on the main board, and replaced them:

![](/assets/images/nes-restoration/IMG_7645.jpg)

![](/assets/images/nes-restoration/IMG_7646.jpg)

This specific cap is next to the PPU. I purposely layed this one flat in case I ever decide to install an [NESRGB mod](https://etim.net.au/nesrgb/), as it would sit right on top of this area:

![](/assets/images/nes-restoration/IMG_7648.jpg)

## Reassembly

After a couple of days, the retrobriting was done. I removed and washed each piece:

![](/assets/images/nes-restoration/IMG_7659.jpg)

![](/assets/images/nes-restoration/IMG_7661.jpg)

Once everything was dry, it was time to reassemble:

![](/assets/images/nes-restoration/IMG_7683.jpg)

![](/assets/images/nes-restoration/IMG_7684.jpg)

![](/assets/images/nes-restoration/IMG_7687.jpg)

![](/assets/images/nes-restoration/IMG_7688.jpg)

![](/assets/images/nes-restoration/IMG_7689.jpg)

![](/assets/images/nes-restoration/IMG_7691.jpg)

![](/assets/images/nes-restoration/IMG_7694.jpg)

Done!

![](/assets/images/nes-restoration/IMG_7695.jpg)

![](/assets/images/nes-restoration/IMG_7697.jpg)

And working well:

![](/assets/images/nes-restoration/IMG_7701.jpg)

Here's a before and after shot to show how the retrobriting helped to de-yellow the console:

![](/assets/images/nes-restoration/before_after.jpg)

## Thoughts

I believe this is the fifth NES I restore. With experience, things are definitely a lot smoother now. The NES is my favorite console, so it it makes me especially happy to breath new life into them.
