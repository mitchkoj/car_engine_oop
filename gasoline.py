import dataclasses
from abc import ABC
from dataclasses import dataclass

@dataclass
class Gasoline(ABC):
    """
    class representing gasoline type

    Args:
        ABC (abc.ABCMeta): Abstract Base Class to create the meta class Gasoline.
    """
    octane: float
    
    
class UnwantedGasolineMix(ValueError):
    pass


@dataclass
class GasPortion:
    """
    class representing a specific portion of a Gasoline object.

    Raises:
        UnwantedGasolineMix: error raised when wrong gasoline is provided.

    Returns:
        Gasoline
    """
    gasoline: Gasoline
    volume_liters: float
    
    def __add__(self, other: "GasPortion") -> "GasPortion":
        """
        sums up two objects of type GasPortion.
        checks if the types of gasoline are the same.
        calculates the the octane number based on the volume in liters

        Raises:
            UnwantedGasolineMix: error output if gasoline types are different.

        Returns:
            GasPortion 
        """
        
        if type(self.gasoline).__name__ != type(other.gasoline).__name__:
            raise UnwantedGasolineMix
        
        volume_liters = self.volume_liters + other.volume_liters
        octane = self.gasoline.octane * (self.volume_liters / volume_liters)
        octane += other.gasoline.octane * (other.volume_liters / volume_liters)
        octane = round(octane, ndigits=2)
        
        return GasPortion(
            gasoline=dataclasses.replace(self.gasoline, octane=octane),
            volume_liters=volume_liters,
        )

