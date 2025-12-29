import json
from json import JSONEncoder


class OSCHostInfoEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, OSCHostInfo):
            obj_dict = {}
            for k, v in vars(o).items():
                if v is None:
                    continue
                obj_dict[k.upper()] = v
            return obj_dict

        return json.JSONEncoder.default(self, o)  # pragma: no cover


class OSCHostInfo:
    def __init__(
        self,
        name: str,
        extensions,
        osc_ip: str | None = None,
        osc_port=None,
        osc_transport=None,
        ws_ip=None,
        ws_port=None,
    ) -> None:
        self.name = name
        self.osc_ip = osc_ip
        self.osc_port = osc_port
        self.osc_transport = osc_transport
        self.ws_ip = ws_ip
        self.ws_port = ws_port
        self.extensions = extensions

    def to_json(self) -> str:
        return json.dumps(self, cls=OSCHostInfoEncoder)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.name}, {self.osc_ip}, {self.osc_port}, {self.osc_transport}, {self.ws_ip}, {self.ws_port}, {self.extensions})"
