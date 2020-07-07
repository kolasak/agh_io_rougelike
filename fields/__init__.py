from .EndStageField import EndStageField
from .Field import Field
from .GateField import GateField
from .MountainField import MountainField
from .RoadField import RoadField
from .TownField import TownField
from .WallField import WallField
from .WaterField import WaterField
from .ForestField import ForestField

CHARACTER_TO_FIELD = {
    'E': EndStageField,
    'G': GateField,
    'M': MountainField,
    'R': RoadField,
    'T': TownField,
    'V': WallField,
    'W': WaterField,
    'F': ForestField
}