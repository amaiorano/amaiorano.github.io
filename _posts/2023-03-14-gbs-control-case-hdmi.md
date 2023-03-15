---
layout: post
title: "gbs-control Case for HDMI Out"
tags: [Electronics, 3D-printing, gbs-control]
comments: true
---

A little while ago, I [built a gbs-control]({%post_url 2022-04-01-gbs-control %}) to up-scale up video signals from my old consoles to my LCD TV. I eventually built a second one to use as a down-scaler/transcoder to my CRT, and [made a custom cable for it]({%post_url 2022-12-30-gbs-control-db15-to-ypbpr-cable %}). The final missing touch for both these projects was a nice case. In this first post, I'll go over how I designed, printed, and assembled a case for the HDMI out gbs-control. My next post will cover the second case.

## Design

My first gbs-control is the one I use to up-scale RGB and YPbPr input signals to HDMI out:

![](/assets/images/gbs-control-case-hdmi/IMG_8632.jpg)

As you can see, the PCB is screwed into a piece of wood I cut, and there's a VGA-to-HDMI adapter hanging off the back, along with female RCA cables for stereo audio input that connect to the same adapter.

My goals for this case were:

* Get rid of the ugly adapter hanging out the back. Inspired by [this case design](https://www.thingiverse.com/thing:4946190), I'd incorporate the adapter inside the case, and expose only the HDMI port out the back.

* Add a reset button to the front. Sometimes the gbs-control gets in a weird state when disconnecting and connecting devices, and I've found it useful to be able to press the reset button on the NodeMCU board. Since this will be tucked in the case, I decided to expose it at the front of the case.

* Display a status LED on the front. The gbs-control source code turns the NodeMCU on-board LED on to indicate when a proper signal has been detected, and off otherwise. I've found this useful as well, and similar to the reset button, decided to expose it on the front of the case since the NodeMCU would no longer be visible.

### Case

After spending many hours (mostly learning) Fusion 360, here's what I came up with for the case itself:

![](/assets/images/gbs-control-case-hdmi/HDMI_Case_Front.jpg)

![](/assets/images/gbs-control-case-hdmi/HDMI_Case_Back.jpg)

You can see that the front panel has holes for the gbs board's inputs, along with a top row of holes for audio inputs, reset button, and the status LED. On the side is the HDMI "cradle", used to hold the VGA-to-HDMI PCB in place against the back panel.

Note how the back panel is a separate piece. I decided to do this because I knew I'd want a different back panel for my second gbs-control. As it turned out, it also made it much easier to slide in the gbs board into the case.

### Reset and Status LED

To be able to reset the gbs-control from the front panel, I bought a momentary switch:

![](/assets/images/gbs-control-case-hdmi/ResetButton.jpg)

Resetting the NodeMCU is done very simply by connecting the RST pin to ground:

![](/assets/images/gbs-control-case-hdmi/NodeMCUReset.jpg)

For the status LED, it's slightly more complicated. The NodeMCU's LED state is connected to D0 (GPIO16), but it's an "active low" signal, meaning that when the LED is on, D0 is low (GND), and when the LED is off, D1 is high (Vin). This is the opposite of what we need for our external LED. One solution would be to build an inverter circuit, or to use an inverter IC.

Instead, I decided to fix it in software by modifying the gbs-control code to output the non-inverted status on an unused pin, like D7, which is exactly what I did (you can see [my changes here](https://github.com/ramapcsx2/gbs-control/compare/master...amaiorano:gbs-control:amaiorano-changes)). The crux of the change was to modify the `LEDON` AND `LEDOFF` macros to also write the opposite level to D7:

```cpp
#define LEDON                         \
    pinMode(LED_BUILTIN, OUTPUT);     \
    digitalWrite(LED_BUILTIN, LOW);   \
    pinMode(D7, OUTPUT);    /* NEW */ \
    digitalWrite(D7, HIGH); /* NEW */
#define LEDOFF                        \
    digitalWrite(LED_BUILTIN, HIGH);  \
    pinMode(LED_BUILTIN, INPUT);      \
    digitalWrite(D7, LOW); /* NEW */  \
    pinMode(D7, INPUT)     /* NEW */
```

So now, I could simply wire up a LED with one end connected to D7 (with a resistor in series), and the other to ground:

![](/assets/images/gbs-control-case-hdmi/NodeMCUStatusLED.jpg)

## The Build

As a novice to 3D printing and designing, I spent a fair bit of time iterating and printing tests to make sure everything fit:

![](/assets/images/gbs-control-case-hdmi/IMG_9366.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9371.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9376.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9377.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9389.jpg)

Finally, with everything ironed out, I printed out the pieces for the case:

![](/assets/images/gbs-control-case-hdmi/IMG_9402.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9456.jpg)

With the case printed, it was time to prep the gbs board. First I desoldered the VGA output connector off the back of the board:

![](/assets/images/gbs-control-case-hdmi/IMG_9419.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9422.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9423.jpg)

Next up was getting the VGA-to-HDMI adapter PCB out of its case, and removing a few components off of it:

![](/assets/images/gbs-control-case-hdmi/IMG_9581.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9582.jpg)

Using a hot air rework station, I carefully removed the audio input jack:

![](/assets/images/gbs-control-case-hdmi/IMG_9583.jpg)

As well as the micro-usb power connector:

![](/assets/images/gbs-control-case-hdmi/IMG_9584.jpg)

And finally, the VGA input connector:

![](/assets/images/gbs-control-case-hdmi/IMG_9585.jpg)

With all that done, it was time to solder the adapter to the gbs board. Using ribbon cable, I soldered the R, G, and B pads, as well as ground:

![](/assets/images/gbs-control-case-hdmi/IMG_9590.jpg)

And on the other side, the H-sync and V-sync pads:

![](/assets/images/gbs-control-case-hdmi/IMG_9592.jpg)

The other end of the ribbon cable was soldered to the pins that sat behind the VGA output connector I removed:

![](/assets/images/gbs-control-case-hdmi/IMG_9457.jpg)

Note that ground wire isn't connected above. You'll see it connected in later pics.

I soldered a red and white wire - for right and left audio, respectively - to the adapter where the audio input jack used to be:

![](/assets/images/gbs-control-case-hdmi/IMG_9587.jpg)

On the other end, I soldered two ground wires for the audio signals:

![](/assets/images/gbs-control-case-hdmi/IMG_9589.jpg)

You'll see these four wires getting hooked up to the RCA input jacks at the front of the case later below.

To power the adapter, I soldered a yellow wire for 5V and black for ground to this component:

![](/assets/images/gbs-control-case-hdmi/IMG_9593.jpg)

Then soldered the other ends to the gbs board:

![](/assets/images/gbs-control-case-hdmi/IMG_9476.jpg)

I placed the gbs board into the case, and screwed in the four corners:

![](/assets/images/gbs-control-case-hdmi/IMG_9488.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9487.jpg)

Next up were the status LED and reset button:

![](/assets/images/gbs-control-case-hdmi/IMG_9481.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9491.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9493.jpg)

The other ends are connected to the NodeMCU board as shown below. The purple reset wire is tied to the RST pin (obscured in the pic), with the black ground wire next to it. For the LED, the green wire is tied to pin D7, and the brown to ground:

![](/assets/images/gbs-control-case-hdmi/IMG_9504.jpg)

With the LED and reset buttons done, I screwed in the RCA audio input jacks:

![](/assets/images/gbs-control-case-hdmi/IMG_9495.jpg)

Next, I placed the HDMI adapter into its cradle, and screwed it to the back panel:

![](/assets/images/gbs-control-case-hdmi/IMG_9497.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9499.jpg)

I then screwed the back panel to the case:

![](/assets/images/gbs-control-case-hdmi/IMG_9500.jpg)

Finally, I soldered the audio wires coming from the HDMI adapter to the RCA jacks:

![](/assets/images/gbs-control-case-hdmi/IMG_9503.jpg)

And with that, I was done!

![](/assets/images/gbs-control-case-hdmi/IMG_9595.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9597.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9512.jpg)

![](/assets/images/gbs-control-case-hdmi/IMG_9514.jpg)

Here it is, with my N64 hooked up to it:

![](/assets/images/gbs-control-case-hdmi/IMG_9524.jpg)

## Thoughts

I have to say that I'm really happy with the way this case turned out! This was practically my first time designing something more complicated for 3D printing, and although it took quite some time, I learned a great deal and had fun doing it.

The case isn't perfect. For instance, the walls are a bit thin at 2mm, and I can feel them bending a little when I push in cables into it, especially on the back. I'd definitely try making it a little thicker. But apart from minor things like that, overall, I'm quite happy with the result.

In the [next post]({%post_url 2023-03-15-gbs-control-case-ypbpr %}), I'll go over how I made a similar case for my second gbs-control that I use for down-scaling/transcoding.
