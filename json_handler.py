#!/usr/bin/env python3
import json
from datetime import datetime

class JsonHandler:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        try:
            with open(self.file_path, 'r') as json_file:
                existing_data = json.load(json_file)
            return existing_data
        except (FileNotFoundError, json.JSONDecodeError) as e:
            return []

    def update_existing_data(self, new_data):
        existing_data = self.load_data()

        # Use a set to keep track of unique links
        unique_links = {item.get('link') for item in existing_data}

        # Identify new items and add a timestamp
        new_items = []
        for item in new_data:
            link = item.get('link')
            if link is not None and link not in unique_links:
                item['timestamp'] = datetime.now().isoformat()
                new_items.append(item)
                unique_links.add(link)

        updated_data = existing_data + new_items

        with open(self.file_path, 'w', encoding='utf-8') as json_file:
            json.dump(updated_data, json_file, indent=2)
