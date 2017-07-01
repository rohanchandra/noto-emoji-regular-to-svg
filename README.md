# Noto Emoji Regular to SVG

![SVG preview](https://user-images.githubusercontent.com/816965/27758160-8a788232-5e51-11e7-9d6e-ca8995e11587.png)

A small set of scripts to convert the black-and-white [Noto Emoji](https://www.google.com/get/noto/#emoji-zsye) (`NotoEmoji-Regular.ttf`) file into SVG.

Note: Noto Emoji Color SVG can be found in the [noto-emoji](https://github.com/googlei18n/noto-emoji/tree/master/svg) repo.

## Usage

Emoji glyphs from this SVG font are converted to separate SVG paths in `/svg`.

A mapping of emoji filenames to categories based on data from the [emoji-data](https://github.com/iamcal/emoji-data) project is available in `/json`.

These files can be downloaded from the [releases page](https://github.com/rohanchandra/noto-emoji-regular-to-svg/releases).

## Build

To recreate the SVG font and glyph paths, the following dependencies are required:
* [FontForge](https://fontforge.github.io/en-US/)
* [svg-caster](https://github.com/icons8/svg-caster)
* [Python 3.6.x](https://www.python.org/)

Run the `build.sh` script to convert the `ttf` to `svg` and generate the category mapping `json` file:

```
$ git clone git@github.com:RohanChandra/noto-emoji-regular-to-svg.git
$ cd noto-emoji-regular-to-svg/
$ sh ./build.sh
```

## License

The Noto Emoji font is licensed under the SIL Open Font License, version 1.1. The Noto Emoji font is the [work of Google Inc](https://github.com/googlei18n/noto-emoji/blob/master/AUTHORS).

Code is licensed under Apache license, version 2.0 and modified code under the Apache license is used. Emoji categorization is performed based on data available under the MIT license.
