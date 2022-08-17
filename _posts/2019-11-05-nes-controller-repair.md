---
layout: post
title: NES Controller Repair
tags: [Electronics, Repair]
comments: true
---

One of the NES controllers I received in an eBay lot was defective. It seemed none of the buttons worked, except for the "A" button, which behaved like "Start". At first, I thought maybe the contacts were dirty, as I had read online that this could happen sometimes. But after attempting to clean, and even sand the contacts on the board, I realized this wasn't the issue. With a little more searching online, I learned that sometimes the shift register chip becomes faulty, and needs replacing.

So first thing I did was open up the controller, and desolder the shift register chip off the controller board:

![](/assets/images/nes-controller-repair/IMG_7526.jpg)

![](/assets/images/nes-controller-repair/IMG_7529.jpg)

In the picture above, you can see where I had attempted to sand the contacts. I regret having done that, as I ended up removing the protective coating on them. It still worked in the end, but I may have reduced its lifetime.

Here's the chip I removed and needed to replace:

![](/assets/images/nes-controller-repair/IMG_7530.jpg)

![](/assets/images/nes-controller-repair/IMG_7532.jpg)

I ordered a pair of new ones off eBay for about $1.30 CAD (about $1 USD). I searched for "4021B shift register 16 pin", and ended up buying this:

![](/assets/images/nes-controller-repair/ebay_shift_register.jpg)

It took a good couple of months, but I finally received them:

![](/assets/images/nes-controller-repair/IMG_7635.jpg)

I popped it onto the board, and soldered it in place:

![](/assets/images/nes-controller-repair/IMG_7636.jpg)

![](/assets/images/nes-controller-repair/IMG_7637.jpg)

![](/assets/images/nes-controller-repair/IMG_7638.jpg)

![](/assets/images/nes-controller-repair/IMG_7639.jpg)

Then I put the controller back together, after giving everything a good cleaning:

![](/assets/images/nes-controller-repair/IMG_7640.jpg)

I made sure to thread the cable back into the strain relief:

![](/assets/images/nes-controller-repair/IMG_7642.jpg)

And closed it all up:

![](/assets/images/nes-controller-repair/IMG_7643.jpg)

Gave it a test, and it worked perfectly:

![](/assets/images/nes-controller-repair/IMG_7644.jpg)

This was an easy fix, and very cheap. If you've got a controller that isn't working, I'd definitely recommend trying to replace the shift register before chucking it in the garbage.

