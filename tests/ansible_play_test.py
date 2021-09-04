assert not host.ansible("package", "name=python3.9 state=present")["changed"]
