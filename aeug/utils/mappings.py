from types import MappingProxyType

BM25FLAT_INDEX = MappingProxyType(
    {
        # BEIR(Benchmarking IR)
        "beir_trec_covid": "beir-v1.0.0-trec-covid.flat",
        "beir_bioasq": "beir-v1.0.0-bioasq.flat",
        "beir_nfcorpus": "beir-v1.0.0-nfcorpus.flat",
        "beir_nq": "beir-v1.0.0-nq.flat",
        "beir_hotpotqa": "beir-v1.0.0-hotpotqa.flat",
        "beir_fiqa": "beir-v1.0.0-fiqa.flat",
        "beir_signal1m": "beir-v1.0.0-signal1m.flat",
        "beir_trec_news": "beir-v1.0.0-trec-news.flat",
        "beir_robust04": "beir-v1.0.0-robust04.flat",
        "beir_arguana": "beir-v1.0.0-arguana.flat",
        "beir_webis_touche2020": "beir-v1.0.0-webis-touche2020.flat",
        "beir_quora": "beir-v1.0.0-quora.flat",
        "beir_dbpedia_entity": "beir-v1.0.0-dbpedia-entity.flat",
        "beir_scidocs": "beir-v1.0.0-scidocs.flat",
        "beir_fever": "beir-v1.0.0-fever.flat",
        "beir_climate_fever": "beir-v1.0.0-climate-fever.flat",
        "beir_scifact": "beir-v1.0.0-scifact.flat",
        ## CQADupStack is one of the benchmarks included in BEIR. CQADupStack contains 12 different datasets.
        "beir_cqadupstack_android": "beir-v1.0.0-cqadupstack-android.flat",
        "beir_cqadupstack_english": "beir-v1.0.0-cqadupstack-english.flat",
        "beir_cqadupstack_gaming": "beir-v1.0.0-cqadupstack-gaming.flat",
        "beir_cqadupstack_gis": "beir-v1.0.0-cqadupstack-gis.flat",
        "beir_cqadupstack_mathematica": "beir-v1.0.0-cqadupstack-mathematica.flat",
        "beir_cqadupstack_physics": "beir-v1.0.0-cqadupstack-physics.flat",
        "beir_cqadupstack_programmers": "beir-v1.0.0-cqadupstack-programmers.flat",
        "beir_cqadupstack_stats": "beir-v1.0.0-cqadupstack-stats.flat",
        "beir_cqadupstack_tex": "beir-v1.0.0-cqadupstack-tex.flat",
        "beir_cqadupstack_unix": "beir-v1.0.0-cqadupstack-unix.flat",
        "beir_cqadupstack_webmasters": "beir-v1.0.0-cqadupstack-webmasters.flat",
        "beir_cqadupstack_wordpress": "beir-v1.0.0-cqadupstack-wordpress.flat",
        # TREC
        "trec2019": "msmarco-v1-passage",
        "trec2020": "msmarco-v1-passage",
    }
)


TOPICS = MappingProxyType(
    {
        # BEIR(Benchmarking IR)
        "beir_trec_covid": "beir-v1.0.0-trec-covid-test",
        # TREC
        "trec2019": "dl19-passage",
        "trec2020": "dl20-passage",
    }
)
