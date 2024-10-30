import json

import pytest

from aeug.io.json import JsonWriter
from aeug.utils.typing import Results


class TestJsonWriter:
    @pytest.fixture
    def temp_file(self, tmpdir):
        self.tmpfile = tmpdir.join("test.json")
        yield
        tmpdir.remove()

    def test_write(self, temp_file):
        data: Results = [
            {"query_id": "11", "query": "test", "rank": 1, "score": 0.1},
            {"query_id": "12", "query": "test", "rank": 2, "score": 0.2},
        ]
        JsonWriter(self.tmpfile, data).write()

        read_data = None
        with open(self.tmpfile, "r", encoding="utf-8") as file:
            read_data = json.load(file)

        assert read_data == data
