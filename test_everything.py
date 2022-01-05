from engine import Engine
from gasoline import Gasoline, GasPortion
from gas_pump import GasPump
from pedal import Pedal

class TestEverythingTogether:
    
    def test_everything_ok(self) -> None:
        
        class Benzine(Gasoline):
            pass
        
        bezine95 = Benzine(octane=95)
        bezine98 = Benzine(octane=98)
        
        gas_tank = GasPortion(
            gasoline=bezine95,
            volume_liters=20
        )
        
        gas_tank += GasPortion(
            gasoline=bezine98,
            volume_liters=20
        )
        
        assert gas_tank.volume_liters == 40
        assert gas_tank.gasoline.octane == 96.5
        
        engine = Engine(gasoline=bezine98)
        
        gas_pump = GasPump(
            connected_engine=engine,
            connected_gas_tank=gas_tank,
            max_flow_lps=0.2
        )
        
        pedal = Pedal(connected_gas_pump=gas_pump)
        pedal.press(how_hard=0.8, seconds=5)
        assert engine.rotations == 328.23
        
        pedal.press(how_hard=0.8, seconds=5)
        assert engine.rotations == 328.23*2