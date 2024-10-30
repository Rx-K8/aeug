from aeug.utils.typing import MetaData


class TestMetaData:
    def test_metadata(self):
        metadata = MetaData(url="https://www.google.com", pubmed_id="123456")
        assert metadata.url == "https://www.google.com"
        assert metadata.pubmed_id == "123456"
