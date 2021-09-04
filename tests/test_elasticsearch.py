def test_elastic_running_and_enabled(host):
    elastic = host.docker("elasticsearch01")
    assert elastic.is_running
   

