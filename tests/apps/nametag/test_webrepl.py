def test_config():
    import apps.nametag.webrepl_cfg as c
    assert c.PASS == 'WEBREPL_PASSWORD'
