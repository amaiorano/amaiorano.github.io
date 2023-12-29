---
layout: post
title: "gbs-control Case for YPbPr Out"
tags: [Electronics, 3D-printing, gbs-control]
comments: true
toc: true
---

In [my last post]({% post_url 2023-03-14-gbs-control-case-hdmi %}), I went over how I designed and built a case for my gbs-control used for up-scaling with HDMI output. This post will be about my second case, designed for the gbs-control I use for down-scaling/transcoding with RGB/YPbPr out.

## Design

My second gbs-control is used for transcoding and down-scaling input signals, usually from RGB to YPbPr, using a [custom DB-15 to RCA cable]({%post_url 2022-12-30-gbs-control-db15-to-ypbpr-cable %}) to feed the YPbPr signal to my CRT, along with a stereo RCA extension for audio:

![](/assets/images/gbs-control-case-ypbpr/IMG_8660.jpg)

Here were my design goals for this second case:

* Keep the VGA out connector, but also add 5 RCA output jacks to the back panel to carry YPbPr (or RGB) along with left/right audio. This would allow me to hook up this gbs-control directly to my CRT using regular RCA cables, rather than my custom one.

* As with the HDMI case, I wanted the same reset button and status LED on the front panel.

Having made the back panel a separate piece in my original design, all I had to do was design a new one:

![](/assets/images/gbs-control-case-ypbpr/YPbPr_Case_Back.jpg)

I decided to label each of the RCA output holes because finding RCA jacks of the right color isn't easy.

## The Build

This process went smoother than the for the HDMI case. The one hitch was that I had two versions of the gbs board, a V4 and a V5, and I didn't realize that they weren't exactly the same size. I had to make the case a little smaller for the V4 used in this build. But apart from that, it was pretty smooth sailing.

I printed all the parts again:

![](/assets/images/gbs-control-case-ypbpr/IMG_9842.jpg)

This is the V4 board destined for this case:

![](/assets/images/gbs-control-case-ypbpr/IMG_9850.jpg)

I desoldered this header that shares the connections from the VGA output connector next to it:

![](/assets/images/gbs-control-case-ypbpr/IMG_9851.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9853.jpg)

I soldered a ribbon cable to the exposed pads. This time, I only needed the red, green, blue, along with three ground connections:

![](/assets/images/gbs-control-case-ypbpr/IMG_9854.jpg)

As before, I soldered a resistor to one of the legs of a LED:

![](/assets/images/gbs-control-case-ypbpr/IMG_9856.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9860.jpg)

One leg (green wire) is connected to D7, and the other (pink) is connected to ground:

![](/assets/images/gbs-control-case-ypbpr/IMG_9864.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9863.jpg)

For the reset button, I soldered two wires to the RST and ground pins:

![](/assets/images/gbs-control-case-ypbpr/IMG_9865.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9866.jpg)

The board was now ready to be put into the case:

![](/assets/images/gbs-control-case-ypbpr/IMG_9867.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9869.jpg)

Here's the new back panel:

![](/assets/images/gbs-control-case-ypbpr/IMG_9870.jpg)

I bought a set of 20 RCA connectors off Amazon for the back panel for $14 ($0.70 each), which was a lot cheaper than the ones I had bought for the front ($2 each):

![](/assets/images/gbs-control-case-ypbpr/IMG_9871.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9872.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9873.jpg)

I screwed them into the back panel:

![](/assets/images/gbs-control-case-ypbpr/IMG_9874.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9875.jpg)

I oriented the ground tabs away from the power and VGA output connectors:

![](/assets/images/gbs-control-case-ypbpr/IMG_9877.jpg)

I soldered up the red, green, and blue connections. For the gbs-control, when YPbPr mode is enabled, red maps to Pr, green to Y, and blue to Pb:

![](/assets/images/gbs-control-case-ypbpr/IMG_9881.jpg)

For audio, I used another ribbon cable:

![](/assets/images/gbs-control-case-ypbpr/IMG_9882.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9883.jpg)

Next I installed the reset button and audio input jacks:

![](/assets/images/gbs-control-case-ypbpr/IMG_9885.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9887.jpg)

I slid the board into the case and screwed it into place in the four corners:

![](/assets/images/gbs-control-case-ypbpr/IMG_9890.jpg)

I soldered up the reset button:

![](/assets/images/gbs-control-case-ypbpr/IMG_9891.jpg)

Then screwed in the back panel:

![](/assets/images/gbs-control-case-ypbpr/IMG_9893.jpg)

And finally soldered the other end of the audio ribbon cable to the RCA input jacks, being careful to swap the ends so that left and right are correctly oriented:

![](/assets/images/gbs-control-case-ypbpr/IMG_9894.jpg)

All done, and looking mighty clean:

![](/assets/images/gbs-control-case-ypbpr/IMG_9896.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9898.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9899.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9900.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9901.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9902.jpg)

Here it is hooked up with regular RCA cables for YPbPr and audio going straight to my CRT:

![](/assets/images/gbs-control-case-ypbpr/IMG_9905.jpg)

![](/assets/images/gbs-control-case-ypbpr/IMG_9906.jpg)

Success!

![](/assets/images/gbs-control-case-ypbpr/IMG_9908.jpg)


## Thoughts

Building this second case went a lot smoother than the first one, both because it was my second go-around, and also because I didn't have to mess around with the VGA-to-HDMI adapter.

As with the first one, I would definitely make the case walls thicker so that they don't bend when pushing in cables to connect them. Another thing I would consider doing is adding some artificial weight to the cases so that they don't move around so easily.

Having said all that, I'm super happy with the final result for both cases. They look great in my setup -- definitely a lot better than the exposed PCBs screwed into blocks of wood!
