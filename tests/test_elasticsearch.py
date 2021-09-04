def test_nginx_is_installed(host):
    elastic = host.package("{{ elasticsearch_hostname }}")
    assert elastic.is_installed
    assert elastic.version.startswith("7.4.0")


def test_elastic_running_and_enabled(host):
    elastic = host.service("{{ elasticsearch_hostname }}")
    assert elastic.is_running
    assert elastic.is_enabled

