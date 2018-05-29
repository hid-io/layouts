# Base Layout Configuration

This directory contains the base layout configurations, assuming no locale adjustment done by the OS.
It is laid out in the same way that the USB HID spec defines it.

Remember, all names are **case insensitive** to more easily translate names where only one case is standard (e.g. C-style defines).


## [base.json](base.json)

Master configuration file, contains the mapping from names to numeric codes.
Numeric codes have a single mapping to a name.
However, there may be multiple aliases for a numeric code.

```
0x2C -> Space
```

```
Space    -> 0x2C
Spacebar -> 0x2C
```

This JSON file is not useful by itself as it only has direct mappings.
`default.json` is required to handle composition rules (e.g. Shifted keys such as `!` on US ANSI; `Shift+1 -> !`).


## [default.json](default.json)

This is the default layout configuration defined by the USB HID spec for US ANSI.
Since all of the mappings are taken directly from `base.json` the `to_hid` and `from_hid` sections are not necessary.

The `composition` section is used to handle string translation (i.e. ASCII to USB HID codes).
Composition is defined as a string input (should be a single character if possible) and an output defined as a sequence of combinations.

```
a ->                A (0x04)
A -> Shift (0xE1) + A (0x04)
```

For US ANSI sequences are not necessary; however, in some languages, dead keys are necessary.
These dead keys must be inputted as a sequence and key combinations are not sufficient.

