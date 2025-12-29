from pythonoscquery.shared.osc_host_info import OSCHostInfo


class TestOscHostInfo:
    def test_hostinfo_created(self):
        # Arrange
        hs = OSCHostInfo(
            "Hostname",
            {
                "ACCESS": True,
                "CLIPMODE": False,
                "RANGE": False,
                "TYPE": True,
                "VALUE": True,
            },
            "127.0.0.2",
            "1234",
            "UDP",
            "127.0.0.1",
            "5678",
        )
        # Act
        json = hs.to_json()
        # Assert
        assert (
            json == ""
            '{"NAME": "Hostname", "OSC_IP": "127.0.0.2", "OSC_PORT": "1234", "OSC_TRANSPORT": "UDP", "WS_IP": "127.0.0.1", "WS_PORT": "5678", "EXTENSIONS": {"ACCESS": true, "CLIPMODE": false, "RANGE": false, "TYPE": true, "VALUE": true}}'
        )
        assert OSCHostInfo.__name__ in repr(hs)

    def test_hostinfo_created_some_items_missing(self):
        # Arrange
        hs = OSCHostInfo(
            "Hostname",
            {
                "ACCESS": True,
                "CLIPMODE": False,
                "RANGE": False,
                "TYPE": True,
                "VALUE": True,
            },
            "127.0.0.2",
            "1234",
            "UDP",
        )
        # Act
        json = hs.to_json()
        # Assert
        assert (
            json == ""
            '{"NAME": "Hostname", "OSC_IP": "127.0.0.2", "OSC_PORT": "1234", "OSC_TRANSPORT": "UDP", "EXTENSIONS": {"ACCESS": true, "CLIPMODE": false, "RANGE": false, "TYPE": true, "VALUE": true}}'
        )
