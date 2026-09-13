

# Leaflet cluster map of talk locations.
#
# The previous AcademicPages helper depended on unmaintained getorg/geopy APIs
# and no longer runs in the local environment. This drop-in generator retains
# the existing Leaflet map and org-locations.js output, using only Python's
# standard library and Nominatim's public geocoding endpoint.

from __future__ import annotations

import json
import re
import time
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parent
TALKS_DIRECTORY = ROOT / "_talks"
OUTPUT = ROOT / "talkmap" / "org-locations.js"
LOCATION_PATTERN = re.compile(r'^location:\s*["\']?(.+?)["\']?\s*$', re.MULTILINE)


def talk_locations() -> list[str]:
    locations = []
    for talk_file in sorted(TALKS_DIRECTORY.glob("*.md")):
        match = LOCATION_PATTERN.search(talk_file.read_text(encoding="utf-8"))
        if not match:
            raise ValueError(f"Missing location in {talk_file.relative_to(ROOT)}")
        location = match.group(1).strip()
        if "," not in location:
            raise ValueError(f"Location needs city and country: {talk_file.relative_to(ROOT)}")
        if location not in locations:
            locations.append(location)
    return locations


def geocode(location: str) -> tuple[float, float]:
    query = urlencode({"format": "jsonv2", "limit": 1, "q": location})
    request = Request(
        f"https://nominatim.openstreetmap.org/search?{query}",
        headers={"User-Agent": "thyuen.github.io-talk-map/1.0"},
    )
    with urlopen(request, timeout=30) as response:
        result = json.load(response)
    if not result:
        raise ValueError(f"Could not geocode {location!r}")
    return float(result[0]["lat"]), float(result[0]["lon"])


def main() -> None:
    points = []
    for index, location in enumerate(talk_locations()):
        if index:
            time.sleep(1)  # Respect Nominatim's public API usage policy.
        latitude, longitude = geocode(location)
        print(f"{location}: {latitude}, {longitude}")
        points.append([location, latitude, longitude])
    OUTPUT.write_text("var addressPoints = " + json.dumps(points, indent=2) + ";\n", encoding="utf-8")


if __name__ == "__main__":
    main()



