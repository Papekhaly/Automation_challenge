import pytest, webtest


def test_elastic_running_and_enabled(host):
    elastic = host.docker("elasticsearch01")
    assert elastic.is_running

#def test_elastic_is_listening(host):
#    assert host.socket('tcp://127.0.0.1:9200').is_listening
