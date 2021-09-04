def check_ansible_play(host):
    """
    Verify that a package is installed using Ansible
    package module
    """
    assert not host.ansible("package", "name=httpd state=present")["changed"]
