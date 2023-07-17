from collections.abc import Callable
from typing import TypeVar, Union

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkCityGMLReader(vtkmodules.vtkCommonExecutionModel.vtkMultiBlockDataSetAlgorithm):
    def GetBeginBuildingIndex(self) -> int: ...
    def GetEndBuildingIndex(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetLOD(self) -> int: ...
    def GetLODMaxValue(self) -> int: ...
    def GetLODMinValue(self) -> int: ...
    def GetNumberOfBuildings(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUseTransparencyAsOpacity(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCityGMLReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCityGMLReader: ...
    def SetBeginBuildingIndex(self, _arg: int) -> None: ...
    def SetEndBuildingIndex(self, _arg: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetLOD(self, _arg: int) -> None: ...
    def SetNumberOfBuildings(self, _arg: int) -> None: ...
    def SetUseTransparencyAsOpacity(self, _arg: int) -> None: ...
    def UseTransparencyAsOpacityOff(self) -> None: ...
    def UseTransparencyAsOpacityOn(self) -> None: ...
