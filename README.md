# Keyboard Layout / Locale Mappings

This repository contains a list of mappings between various keyboard layouts.
As you may, or may not know, USB HID defines the default mapping of a key per a US layout.
Any other language is a remapping to the USB HID mapping which is done by the OS and not the keyboard.

This definitely complicates configuring a programmable as the keyboard must be programmed with a US layout, even if you are using a Spanish keyboard to assign the keys.

To solve all this in a convenient way, this repo provides a JSON file per keyboard layout which defines the mappings required by KLL (and the configurator).
That means if your keyboard layout isn't available, all you have to do is submit a Pull Request and it will be added to the configurator!

[![Travis Status](https://travis-ci.org/hid-io/layouts.svg?branch=master)](https://travis-ci.org/hid-io/layouts)

[![Visit our IRC channel](https://kiwiirc.com/buttons/irc.freenode.net/hid-io.png)](https://kiwiirc.com/client/irc.freenode.net/#hid-io)


## Layouts

Default configurators (per the USB HID spec) are organized within [base](base).
This is assumed to be based around US ANSI configurations (again, this is the assumption of the USB HID spec).

Any deviation or adjustment from the default are found within [keyboards](keyboards).
If you are wondering where to add your own layout, this is where it should go.

* [base](base)
* [keyboards](keyboards)


## References

* [USB HID Spec v1.11](http://www.usb.org/developers/hidpage/HID1_11.pdf)
* [USB HID Usage Tables v1.12](http://www.usb.org/developers/hidpage/Hut1_12v2.pdf)
* [USB HID Information](http://www.usb.org/developers/hidpage/)

