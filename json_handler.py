#!/usr/bin/env python3
import json

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
        updated_data = existing_data + new_data
        with open(self.file_path, 'w', encoding='utf-8') as json_file:
            json.dump(updated_data, json_file, indent = 2)
