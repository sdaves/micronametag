def test_config():
    import examples.nametag.webrepl_cfg as sut
    assert sut.PASS == 'WEBREPL_PASSWORD'
