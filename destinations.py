"""Sumburgh Airport (LSI) destinations — April 2026."""

DESTINATIONS = {
    "LSI": {
        "name": "Sumburgh (Shetland)",
        "routes": {
            "ABZ": "Aberdeen",
            "DND": "Dundee",
            "EDI": "Edinburgh",
            "GLA": "Glasgow",
            "INV": "Inverness",
            "KOI": "Kirkwall",
        },
    },
}


def get_destinations(airport: str) -> dict:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("routes", {})


def get_airport_name(airport: str) -> str:
    entry = DESTINATIONS.get(airport, {})
    return entry.get("name", airport)
