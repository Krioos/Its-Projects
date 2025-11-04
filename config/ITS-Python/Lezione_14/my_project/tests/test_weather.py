from my_project.weather import check_weather
import pytest

@pytest.mark.parametrize("temperature, expected", [
    (21.00, "hot"),
    (13.00, "average"),
    (0.00, "cold"),
    (15.00, "cold")
])
def test_check_weather(temperature, expected):
    ae: str = ""
    if temperature > 20:
        ae = "temperatures over 20 degrees must be considered as hot"
    elif 10 < temperature <= 20:
        ae = "temperatures between 10 and 20 degrees must be considered as average"
    else:
        ae = "temperatures below 10 must be considered as cold"
    assert check_weather(temperature) == expected, ae