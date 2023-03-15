---
layout: post
title: "Custom Cases for my gbs-controls"
tags: [Electronics, 3D-printing, gbs-control]
comments: true
---

A little while ago, I [built a gbs-control]({% post_url 2022-04-01-gbs-control %}) to up-scale up video signals from my old consoles to my LCD TV. I eventually built a second one to use as a down-scaler/transcoder to my CRT, and [made a custom cable for it]({%post_url 2022-12-30-gbs-control-db15-to-ypbpr-cable %}). The final missing touch for both these projects was a nice case. In this post, I go over how I designed and 3D-printed two different cases, one for each gbs-control, and how I put everything together.

## Case #1 for HDMI out

### Design

My first gbs-control is the one I use to up-scale RGB and YPbPr input signals to HDMI out:

![](/assets/images/gbs-control-case/IMG_8632.jpg)

As you can see, the PCB is screwed into a piece of wood I cut, and there's a VGA-to-HDMI adapter hanging off the back, along with female RCA cables for stereo audio input that connect to the same adapter.

My goals for this case were:

* Get rid of the ugly adapter hanging out the back. Inspired by [this case design](https://www.thingiverse.com/thing:4946190), I'd incorporate the adapter inside the case, and expose only the HDMI port out the back.

* Add a reset button to the front. Sometimes the gbs-control gets in a weird state when disconnecting and connecting devices, and I've found it useful to be able to press the reset button on the ESP8266 board. Since this will be tucked in the case, I decided to expose it at the front of the case.

* Display a status LED on the front. The gbs-control source code turns the ESP8266 on-board LED on to indicate when a proper signal has been detected, and off otherwise. I've found this useful as well, and similar to the reset button, decided to expose it on the front of the case since the ESP8266 would no longer be visible.

After spending many hours (mostly learning) Fusion 360, here's what I came up with:

![](/assets/images/gbs-control-case/HDMI_Case_Front.jpg)

![](/assets/images/gbs-control-case/HDMI_Case_Back.jpg)

You can see that the front panel has holes for the gbs board's inputs, along with a top row of holes for audio inputs, reset button, and the status LED. On the side is the HDMI "cradle", used to hold the VGA-to-HDMI PCB in place against the back panel.

Note how the back panel is a separate piece. I decided to do this because I knew I'd want a different back panel for my second gbs-control case. As it turned out, it also made it much easier to slide in the gbs board into the case.

### The Build

As a novice to 3D printing and designing, I spent a fair bit of time iterating and printing tests to make sure everything fit:

![](/assets/images/gbs-control-case/IMG_9366.jpg)

![](/assets/images/gbs-control-case/IMG_9371.jpg)

![](/assets/images/gbs-control-case/IMG_9376.jpg)

![](/assets/images/gbs-control-case/IMG_9377.jpg)

![](/assets/images/gbs-control-case/IMG_9389.jpg)

Finally, with everything ironed out, I printed out the pieces for the case:

![](/assets/images/gbs-control-case/IMG_9402.jpg)

![](/assets/images/gbs-control-case/IMG_9456.jpg)

With the case printed, it was time to prep the gbs board. First I desoldered the VGA output connector off the back of the board:

![](/assets/images/gbs-control-case/IMG_9419.jpg)

![](/assets/images/gbs-control-case/IMG_9422.jpg)

![](/assets/images/gbs-control-case/IMG_9423.jpg)

Next up was getting the VGA-to-HDMI adapter PCB out of its case, and removing a few components off of it:

![](/assets/images/gbs-control-case/IMG_9581.jpg)

![](/assets/images/gbs-control-case/IMG_9582.jpg)

Using a hot air rework station, I carefully removed the audio input jack:

![](/assets/images/gbs-control-case/IMG_9583.jpg)

As well as the micro-usb power connector:

![](/assets/images/gbs-control-case/IMG_9584.jpg)

And finally, the VGA input connector:

![](/assets/images/gbs-control-case/IMG_9585.jpg)

With all that done, it was time to solder the adapter to the gbs board. Using ribbon cable, I soldered the R, G, and B pads, as well as ground:

![](/assets/images/gbs-control-case/IMG_9590.jpg)

And on the other side, the H-sync and V-sync pads:

![](/assets/images/gbs-control-case/IMG_9592.jpg)

The other end of the ribbon cable was soldered to the pins that sat behind the VGA output connector I removed:

![](/assets/images/gbs-control-case/IMG_9457.jpg)

Note that ground wire isn't connected above. You'll see it connected in later pics.

I soldered a red and white wire - for right and left audio, respectively - to the adapter where the audio input jack used to be:

![](/assets/images/gbs-control-case/IMG_9587.jpg)

On the other end, I soldered two ground wires for the audio signals:

![](/assets/images/gbs-control-case/IMG_9589.jpg)

You'll see these four wires getting hooked up to the RCA input jacks at the front of the case later below.

To power the adapter, I soldered a yellow wire for 5V and black for ground to this component:

![](/assets/images/gbs-control-case/IMG_9593.jpg)

Then soldered the other ends to the gbs board:

![](/assets/images/gbs-control-case/IMG_9476.jpg)

With the HDMI adapter mostly done, I moved on to the status LED and reset button:

![](/assets/images/gbs-control-case/IMG_9481.jpg)

![](/assets/images/gbs-control-case/IMG_9491.jpg)

![](/assets/images/gbs-control-case/IMG_9493.jpg)

The other ends are connected to the NodeMCU board as shown below. The purple reset wire is tied to the RST pin (obscured in the pic), with the black ground wire next to it. For the LED, the green wire is tied to pin D7, and the brown to ground:

![](/assets/images/gbs-control-case/IMG_9504.jpg)

I should point out that the NodeMCU's LED state isn't actually output to D7, but rather to D0 (pin 16). Unfortunately, the signal to D0 is inverted, meaning it's low when the LED is on, and high when the LED is off. So for my front-panel LED to emit the same thing, I would have had to build an inverter circuit, or use an inverter IC. Instead, I decided to fix it in software by modifying the gbs-control code to output the non-inverted status on an unused pin, like D7, which is exactly what I did (you can see [my changes here](https://github.com/ramapcsx2/gbs-control/compare/master...amaiorano:gbs-control:amaiorano-changes)).

With the LED and reset buttons done, I screwed in the RCA audio input jacks:

![](/assets/images/gbs-control-case/IMG_9495.jpg)

Next, I placed the HDMI adapter into its cradle, and screwed it to the back panel:

![](/assets/images/gbs-control-case/IMG_9497.jpg)

![](/assets/images/gbs-control-case/IMG_9499.jpg)

I then screwed the back panel to the case:

![](/assets/images/gbs-control-case/IMG_9500.jpg)

Finally, I soldered the audio wires coming from the HDMI adapter to the RCA jacks:

![](/assets/images/gbs-control-case/IMG_9503.jpg)

And with that, I was done!

![](/assets/images/gbs-control-case/IMG_9595.jpg)

![](/assets/images/gbs-control-case/IMG_9597.jpg)

![](/assets/images/gbs-control-case/IMG_9512.jpg)

![](/assets/images/gbs-control-case/IMG_9514.jpg)

Here it is, with my N64 hooked up to it:

![](/assets/images/gbs-control-case/IMG_9524.jpg)


## Case #2 for RGB/YPbPr out

### Design

My second gbs-control is used for transcoding and down-scaling input signals, usually from RGB to YPbPr, using a [custom DB-15 to RCA cable](({%post_url 2022-12-30-gbs-control-db15-to-ypbpr-cable %})) to feed the YPbPr signal to my CRT, along with a stereo RCA extension for audio:

![](/assets/images/gbs-control-case/IMG_8660.jpg)

Here were my design goals for this second case:

* Keep the VGA out connector, but also add 5 RCA output jacks to the back panel to carry YPbPr (or RGB) along with left/right audio. This would allow me to hook up this gbs-control directly to my CRT using regular RCA cables, rather than my custom one.

* As with the HDMI case, I wanted the same reset button and status LED on the front panel.

Having made the back panel a separate pice in my original design, all I had to do was design a new back panel:

![](/assets/images/gbs-control-case/YPbPr_Case_Back.jpg)

I decided to label each of the RCA output holes because finding RCA jacks of the right color isn't easy.

### The Build

This process went smoother than the for the HDMI case. The one hitch was that I had two versions of the gbs board, a V4 and a V5, and I didn't realize that they weren't exactly the same size. I had to make the case a little smaller for the V4 used in this build. But apart from that, it was pretty smooth sailing.

I printed all the parts again:

![](/assets/images/gbs-control-case/IMG_9842.jpg)

This is the V4 board destined for this case:

![](/assets/images/gbs-control-case/IMG_9850.jpg)

I desoldered this header that shares the connections from the VGA output connector next to it:

![](/assets/images/gbs-control-case/IMG_9851.jpg)

![](/assets/images/gbs-control-case/IMG_9853.jpg)

I soldered a ribbon cable to the exposed pads. This time, I only needed the red, green, blue, along with three ground connections:

![](/assets/images/gbs-control-case/IMG_9854.jpg)

As before, I soldered a resistor to one of the legs of a LED:

![](/assets/images/gbs-control-case/IMG_9856.jpg)

6
![](/assets/images/gbs-control-case/IMG_9860.jpg)

One leg (green wire) is connected to D7, and the other (pink) is connected to ground:

![](/assets/images/gbs-control-case/IMG_9864.jpg)

![](/assets/images/gbs-control-case/IMG_9863.jpg)

For the reset button, I soldered two wires to the RST and ground pins:

![](/assets/images/gbs-control-case/IMG_9865.jpg)

![](/assets/images/gbs-control-case/IMG_9866.jpg)

The board was now ready to be put into the case:

![](/assets/images/gbs-control-case/IMG_9867.jpg)

![](/assets/images/gbs-control-case/IMG_9869.jpg)

Here's the new back panel:

![](/assets/images/gbs-control-case/IMG_9870.jpg)

I bought a set of 20 RCA connectors off Amazon for the back panel for $14 ($0.70 each), which was a lot cheaper than the ones I had bought for the front ($2 each):

![](/assets/images/gbs-control-case/IMG_9871.jpg)

![](/assets/images/gbs-control-case/IMG_9872.jpg)

![](/assets/images/gbs-control-case/IMG_9873.jpg)

I screwed them into the back panel:

![](/assets/images/gbs-control-case/IMG_9874.jpg)

![](/assets/images/gbs-control-case/IMG_9875.jpg)

I oriented the ground tabs away from the power and VGA output connectors:

![](/assets/images/gbs-control-case/IMG_9877.jpg)

I soldered up the red, green, and blue connections. For the gbs-control, when YPbPr mode is enabled, red maps to Pr, green to Y, and blue to Pb:

![](/assets/images/gbs-control-case/IMG_9881.jpg)

For audio, I used another ribbon cable:

![](/assets/images/gbs-control-case/IMG_9882.jpg)

![](/assets/images/gbs-control-case/IMG_9883.jpg)

Next I installed the reset button and audio input jacks:

![](/assets/images/gbs-control-case/IMG_9885.jpg)

![](/assets/images/gbs-control-case/IMG_9887.jpg)

I slid the board into the case:

![](/assets/images/gbs-control-case/IMG_9890.jpg)

And soldered up the reset button:

![](/assets/images/gbs-control-case/IMG_9891.jpg)

I screwed in the back panel:

![](/assets/images/gbs-control-case/IMG_9893.jpg)

And finally soldered the other end of the audio ribbon cable to the RCA input jacks, being careful to swap the ends so that left and right are correctly oriented:

![](/assets/images/gbs-control-case/IMG_9894.jpg)

All done, and looking mighty clean:

![](/assets/images/gbs-control-case/IMG_9896.jpg)

![](/assets/images/gbs-control-case/IMG_9898.jpg)

![](/assets/images/gbs-control-case/IMG_9899.jpg)

![](/assets/images/gbs-control-case/IMG_9900.jpg)

![](/assets/images/gbs-control-case/IMG_9901.jpg)

![](/assets/images/gbs-control-case/IMG_9902.jpg)

Here it is hooked up with regular RCA cables for YPbPr and audio going straight to my CRT:

![](/assets/images/gbs-control-case/IMG_9905.jpg)

![](/assets/images/gbs-control-case/IMG_9906.jpg)

Success!

![](/assets/images/gbs-control-case/IMG_9908.jpg)


## Thoughts

I have to say that I'm really happy with the way these two cases turned out! This was practically my first time designing something more complicated for 3D printing, and although it took quite some time, I learned a great deal and had fun doing it.

The case isn't perfect. For instance, the walls are a bit thin at 2mm, and I can feel them bending a little when I push in RCA connectors into it. I'd definitely try making it a little thicker. But apart from minor things like that, overall, I think it looks great in my setup -- definitely a lot better than the exposed PCBs screwed into blocks of wood!
