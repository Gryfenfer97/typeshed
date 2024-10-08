from collections.abc import Callable
from typing import TypeAlias

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel

Callback: TypeAlias = Callable[..., None] | None

VTK_COLOR_BY_INPUT: int
VTK_COLOR_BY_SOURCE: int

class vtkProgrammableAttributeDataFilter(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def AddInput(self, in_: vtkmodules.vtkCommonDataModel.vtkDataSet) -> None: ...
    def GetInputList(self) -> vtkmodules.vtkCommonDataModel.vtkDataSetCollection: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkProgrammableAttributeDataFilter: ...
    def RemoveInput(self, in_: vtkmodules.vtkCommonDataModel.vtkDataSet) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkProgrammableAttributeDataFilter: ...
    def SetExecuteMethod(self, f: Callback) -> None: ...

class vtkProgrammableFilter(vtkmodules.vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    def CopyArraysOff(self) -> None: ...
    def CopyArraysOn(self) -> None: ...
    def GetCopyArrays(self) -> bool: ...
    def GetGraphInput(self) -> vtkmodules.vtkCommonDataModel.vtkGraph: ...
    def GetHyperTreeGridInput(self) -> vtkmodules.vtkCommonDataModel.vtkHyperTreeGrid: ...
    def GetMoleculeInput(self) -> vtkmodules.vtkCommonDataModel.vtkMolecule: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPolyDataInput(self) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    def GetRectilinearGridInput(self) -> vtkmodules.vtkCommonDataModel.vtkRectilinearGrid: ...
    def GetStructuredGridInput(self) -> vtkmodules.vtkCommonDataModel.vtkStructuredGrid: ...
    def GetStructuredPointsInput(self) -> vtkmodules.vtkCommonDataModel.vtkStructuredPoints: ...
    def GetTableInput(self) -> vtkmodules.vtkCommonDataModel.vtkTable: ...
    def GetUnstructuredGridInput(self) -> vtkmodules.vtkCommonDataModel.vtkUnstructuredGrid: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkProgrammableFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkProgrammableFilter: ...
    def SetCopyArrays(self, _arg: bool) -> None: ...
    def SetExecuteMethod(self, f: Callback) -> None: ...

class vtkProgrammableGlyphFilter(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetColorMode(self) -> int: ...
    def GetColorModeAsString(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPoint(self) -> tuple[float, float, float]: ...
    def GetPointData(self) -> vtkmodules.vtkCommonDataModel.vtkPointData: ...
    def GetPointId(self) -> int: ...
    def GetSource(self) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkProgrammableGlyphFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkProgrammableGlyphFilter: ...
    def SetColorMode(self, _arg: int) -> None: ...
    def SetColorModeToColorByInput(self) -> None: ...
    def SetColorModeToColorBySource(self) -> None: ...
    def SetGlyphMethod(self, f: Callback) -> None: ...
    def SetSourceConnection(self, output: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetSourceData(self, source: vtkmodules.vtkCommonDataModel.vtkPolyData) -> None: ...
