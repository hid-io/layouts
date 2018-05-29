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
	"to_hid": {
	},
	"from_hid": {
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

