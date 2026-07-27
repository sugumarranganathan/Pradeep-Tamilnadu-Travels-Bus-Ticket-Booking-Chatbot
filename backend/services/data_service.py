"""
Data Service
Loads routes, buses, timings and fares from JSON files.
"""

import json
from pathlib import Path


class DataService:

    def __init__(self):

        self.data_folder = (
            Path(__file__).resolve().parent.parent / "data"
        )

    def _load_json(self, filename):

        file_path = self.data_folder / filename

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)

    # -------------------------
    # Routes
    # -------------------------

    def get_routes(self):

        return self._load_json("routes.json")

    # -------------------------
    # Buses
    # -------------------------

    def get_buses(self):

        return self._load_json("buses.json")

    # -------------------------
    # Timings
    # -------------------------

    def get_timings(self):

        return self._load_json("timings.json")

    # -------------------------
    # Fares
    # -------------------------

    def get_fares(self):

        return self._load_json("fares.json")
