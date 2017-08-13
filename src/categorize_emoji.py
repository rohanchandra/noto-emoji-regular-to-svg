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

"""Creates JSON file with metadata given SVG files named using unicode naming convention used by Noto Emoji"""

from collections import defaultdict
from pathlib import Path
import json

ROOT_PATH = Path(__file__).parents[1]
SVG_PATH = ROOT_PATH.joinpath('svg')
EMOJI_JSON_PATH = ROOT_PATH.joinpath('src', 'data', 'emoji.json')
OUTPUT_PATH = ROOT_PATH.joinpath('json', 'categorized_emoji.json')

# Matches filename to the unified / Google name from emoji.json
def get_matching_name(unified_name, google_name, filenames):
    if unified_name in filenames:
        return unified_name
    elif google_name in filenames:
        return google_name
    return None

# Search category lists to find target emoji filename
def is_emoji_categorized(target_emoji_filename, categorized_emoji):
    for _, category_list in categorized_emoji.items():
        for emoji_filename in category_list:
            if emoji_filename == 'u' + target_emoji_filename:
                return True
    return False

# Sort Emoji into category from emoji.json
emoji_filenames = [f.stem[1:] for f in SVG_PATH.iterdir() if f.suffix == '.svg']
categorized_emoji = defaultdict(list)
with open(EMOJI_JSON_PATH) as f:
    for emoji_obj in json.load(f):
        name = get_matching_name(emoji_obj['unified'], emoji_obj['google'], emoji_filenames)
        if name is not None:
            category = emoji_obj['category']
            categorized_emoji[category].append('u' + name)

# Emoji not in the emoji.json data are all in the Symbols category
for file_name in emoji_filenames:
    if not is_emoji_categorized(file_name, categorized_emoji):
        categorized_emoji['Symbols'].append('u' + file_name)

# Export categorized emoji to JSON
with open(OUTPUT_PATH, 'w') as output_json:
    json.dump(categorized_emoji, output_json, ensure_ascii=False)
