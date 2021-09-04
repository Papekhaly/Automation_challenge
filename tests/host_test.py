import os
import testinfra.utils.ansible_runner
import pytest

from types import GeneratorType


def test_all_the_pings(host):
    host().all.ping()

def test_docker(host):
  daemon = host.service("docker")
  assert daemon.is_running
  assert daemon.is_enabled

def test_release_file(host):
    release_file = host.file("/etc/os-release")
    assert release_file.contains('Debian')
    assert release_file.contains('9 (stretch)')
