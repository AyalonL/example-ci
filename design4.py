from _pytest.monkeypatch import MonkeyPatch

def check_reactor_temperature(temperature_celsius):
    """
    Checkswheter temperature is above max_temperature
    and returns a status.
    """

#    from reactor import max_temperature
    max_temperature = 100

    if temperature_celsius > max_temperature:
        status = 1
    else:
        status = 0

    return status
    
    
def test_set_temp(monkeypatch):
#    monkeypatch.setattr(reactor, "max_temperature", 100)
    assert check_reactor_temperature(99) == 0
    assert check_reactor_temperature(100) == 0 # boundary cases easily go wrong
    assert check_reactor_temperature(101) == 1
