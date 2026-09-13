from scoring_engine.engine.basic_check import BasicCheck


class TCPCheck(BasicCheck):
    required_properties = ["timeout"]
    CMD = "timeout {0} nc -zv {1} {2}"

    def command_format(self, properties):
        return (properties["timeout"], self.host, self.port)
