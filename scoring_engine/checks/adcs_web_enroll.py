from scoring_engine.engine.basic_check import BasicCheck


class ADCSWebEnrollCheck(BasicCheck):
    """Verify an AD CS Enterprise CA can issue a certificate via web enrollment.

    Requests a certificate for the authenticating account from a *standard*
    template (e.g. User) through the /certsrv Web Enrollment interface, using
    certipy. This exercises the whole legitimate path -- IIS, the CertSrv app,
    AD authentication, and the CA backend actually issuing a cert -- so it only
    fails on a real CA outage, not on hardening the ESC vulnerabilities.

    -no-channel-binding is required because certipy tries to read TLS channel
    binding data even over plain HTTP; -http-scheme http targets the HTTP
    listener. Success prints "Got certificate ...".
    """

    required_properties = ["ca", "template"]
    CMD = (
        "certipy req -u {0} -p {1} -target {2} -target-ip {2} -dc-ip {2} "
        "-ca {3} -template {4} -web -http-scheme http -no-channel-binding "
        "-out /tmp/adcs_{2} 2>&1"
    )

    def command_format(self, properties):
        account = self.get_random_account()
        return (account.username, account.password, self.host, properties["ca"], properties["template"])
