from gasoline import GasPortion, Gasoline
from gas_pump import GasPump


class Benzine(Gasoline):
    pass 


class TestGasPump:
    def test_gas_pump(self) -> None:
        benzine95 = Benzine(octane=95)
        gas_tank = GasPortion(
            gasoline=benzine95,
            volume_liters=10.0
        )
        
        gas_pump = GasPump(
            connected_gas_tank=gas_tank,
            connected_engine=None,
            max_flow_lps=0.2
        )
        
        output_gas = gas_pump.apply(voltage=6, seconds=5)
        assert output_gas.volume_liters == 0.5 