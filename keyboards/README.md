# Keyboard Layouts

This directory contains all of the various keyboard layouts that exist.
It's not complete, but someday it (with your help!) it might be!

Locale base layouts (e.g. AZERTY, QWERTZ-DE, etc.) usually belong here, unless you can make a case that many layouts derive from it.
In which case, it can live under [base](../base).
Alternative layout configurations such as Dvorak, Colemak definitely belong here.

The main ask is that the layout filename is a descriptive as possible and that there are no alias name conflicts with other layouts.

Please run the `layouts-validator` program as it will check to make sure there are no conflicts.
If there are conflicts, it may not be your layout that is at fault; please suggest the correct change and explain why you think it is better.

Layouts will be accepted in PR as long as the following rules are followed.

1. `layouts-validator` passes
1. Not duplicate of another layout (a single change is considered a different layout)
1. Descriptive filename that is not ambiguous with other layouts
1. Include a URL in the notes section of the JSON file with a reference to the layout (or a description of where it comes from)

If you're adding a standard keyboard layout for a specific locale, it's recommended you use the [glibc code](https://lh.2xlibre.net/locales/) for the locale.
Any alternate names should be specified within the JSON file **name** field.


## Layout Format

Here is an example layout of Colemak (without the international symbols, so the example is smaller).
Only deviations from [default.json](../base/default.json), the parent, have to be defined.
If you need to "unset" a composition, set it to `null`.

```json
{
	"name": ["Colemak-Simplified"],
	"authors": ["Jacob Alexander <haata@kiibohd.com>"],
	"locale": ["None", "US"],
	"hid_locale": "0",
	"parent": "base/default.json",
	"notes": ["https://colemak.com/"],
	"to_hid_keyboard": {
		"0x04": "A",
		"0x05": "B",
		"0x06": "C",
		"0x07": "S",
		"0x08": "F",
		"0x09": "T",
		"0x0A": "D",
		"0x0B": "H",
		"0x0C": "U",
		"0x0D": "N",
		"0x0E": "E",
		"0x0F": "I",
		"0x10": "M",
		"0x11": "K",
		"0x12": "Y",
		"0x13": "Semicolon",
		"0x14": "Q",
		"0x15": "P",
		"0x16": "R",
		"0x17": "G",
		"0x18": "L",
		"0x19": "V",
		"0x1A": "W",
		"0x1B": "X",
		"0x1C": "J",
		"0x1D": "Z",

		"0x33": "O",

		"0x64": "Minus",
	},
	"from_hid_keyboard": {
		"A": "0x04",
		"B": "0x05",
		"C": "0x06",
		"S": "0x07",
		"F": "0x08",
		"T": "0x09",
		"D": "0x0A",
		"H": "0x0B",
		"U": "0x0C",
		"N": "0x0D",
		"E": "0x0E",
		"I": "0x0F",
		"M": "0x10",
		"K": "0x11",
		"Y": "0x12",
		"Semicolon": "0x13",
		";": "0x13",
		"Q": "0x14",
		"P": "0x15",
		"R": "0x16",
		"G": "0x17",
		"L": "0x18",
		"V": "0x19",
		"W": "0x1A",
		"X": "0x1B",
		"J": "0x1C",
		"Z": "0x1D",

		"O": "0x33"
	},
	"composition": {
		"f": [["E"]],
		"p": [["R"]],
		"g": [["T"]],
		"j": [["Y"]],
		"l": [["U"]],
		"u": [["I"]],
		"y": [["O"]],
		";": [["P"]],

		"r": [["S"]],
		"s": [["D"]],
		"t": [["F"]],
		"d": [["G"]],
		"n": [["J"]],
		"e": [["K"]],
		"i": [["L"]],
		"o": [[";"]],

		"k": [["N"]],

		"F": [["Shift", "E"]],
		"P": [["Shift", "R"]],
		"G": [["Shift", "T"]],
		"J": [["Shift", "Y"]],
		"L": [["Shift", "U"]],
		"U": [["Shift", "I"]],
		"Y": [["Shift", "O"]],
		":": [["Shift", "P"]],

		"R": [["Shift", "S"]],
		"S": [["Shift", "D"]],
		"T": [["Shift", "F"]],
		"D": [["Shift", "G"]],
		"N": [["Shift", "J"]],
		"E": [["Shift", "K"]],
		"I": [["Shift", "L"]],
		"O": [["Shift", ";"]],

		"K": [["Shift", "N"]],
	}
}
```

