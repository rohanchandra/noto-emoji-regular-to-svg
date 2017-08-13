# Copyright 2017 Rohan Chandra. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Rename generated emoji filenames to an escaped unicode name"""

from xml.dom import minidom
from pathlib import Path
from string_util import get_unicode_escape_string

# Mapping of glyph name to Unicode emoji character
name_map = {}
glyph_elements = minidom.parse('./font/NotoEmoji-Regular.svg').getElementsByTagName('glyph')
for glyph_element in glyph_elements:
    if glyph_element.hasAttribute('unicode') and glyph_element.hasAttribute('glyph-name'):
        glyph_name = glyph_element.attributes['glyph-name'].value
        code = glyph_element.attributes['unicode'].value
        name_map[glyph_name] = code

# Rename output files
root_dir = Path(__file__).parents[1]
svg_path = root_dir.joinpath('svg')  # ../svg

for f in svg_path.iterdir():
    file_name = f.stem
    file_suffix = f.suffix

    if file_suffix == '.svg':
        # Set all filenames to emoji unicode
        if file_name in name_map:
            file_name = name_map[file_name]

        # Escape emoji unicode filenames
        new_path = Path(svg_path, get_unicode_escape_string(file_name) + file_suffix)
        f.rename(new_path)
