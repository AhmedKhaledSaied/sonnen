import pytest

from dut import DUT


@pytest.fixture
def setup_dut():
    dut = DUT()
    yield dut
    dut.reset()


def test_energy_algorithm(setup_dut):
    dut = setup_dut
    dut.set("PV_power", 1000)  # let PV power to be 1000 W
    dut.set("house_consumption", 500)  # let house consumption to be 500 W
    dut.set("storage system", "charging")
    power = dut.get("power")
    assert power > 0, "storage system is charging"  # first case

    grid_power = dut.get("grid power")
    assert grid_power > 0, "surplus power is fed to the grid"  # second case

    dut.set("PV_power", 500)  # let PV power to be 500 W
    dut.set("house_consumption", 1000)  # let house consumption to be 1000 W
    dut.set("storage system", "discharging")
    power = dut.get("power")
    assert power < 0, "storage system is discharging"  # third case

    grid_power = dut.get("grid_power")
    assert grid_power > 0, "grid is supplying the power"  # forth case

@pytest.mark.parametrize("setup", [
    {"inverters": 1, "battery_modules": 2, "controllers": 1},  # Basic
    {"inverters": 1, "battery_modules": 3, "controllers": 1},  # Standard
    {"inverters": 1, "battery_modules": 5, "controllers": 1}  # Pro
 ])
def test_different_setups(setup_dut, setup):
    dut = setup_dut
    dut.set("system_setup", setup)
    assert dut.get("system_setup") == setup

