from collections.abc import Callable, Sequence
from typing import Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkSILBuilder(vtkmodules.vtkCommonCore.vtkObject):
    def AddChildEdge(self, parent: int, child: int) -> int: ...
    def AddCrossEdge(self, src: int, dst: int) -> int: ...
    def AddVertex(self, name: str) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRootVertex(self) -> int: ...
    def GetSIL(self) -> vtkmodules.vtkCommonDataModel.vtkMutableDirectedGraph: ...
    def Initialize(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkSILBuilder: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkSILBuilder: ...
    def SetSIL(self, __a: vtkmodules.vtkCommonDataModel.vtkMutableDirectedGraph) -> None: ...

class vtkXdmfDataArray(vtkmodules.vtkCommonCore.vtkObject):
    def FromArray(self) -> vtkmodules.vtkCommonCore.vtkDataArray: ...
    def FromXdmfArray(
        self, ArrayName: str = ..., CopyShape: int = 1, rank: int = 1, Components: int = 1, MakeCopy: int = 1
    ) -> vtkmodules.vtkCommonCore.vtkDataArray: ...
    def GetArray(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetVtkArray(self) -> vtkmodules.vtkCommonCore.vtkDataArray: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkXdmfDataArray: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkXdmfDataArray: ...
    def SetArray(self, TagName: str) -> None: ...
    def SetVtkArray(self, array: vtkmodules.vtkCommonCore.vtkDataArray) -> None: ...
    def ToArray(self) -> str: ...
    def ToXdmfArray(self, DataArray: vtkmodules.vtkCommonCore.vtkDataArray = ..., CopyShape: int = 1) -> str: ...

class vtkXdmfReader(vtkmodules.vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    def CanReadFile(self, filename: str) -> int: ...
    def GetCellArrayName(self, index: int) -> str: ...
    def GetCellArrayStatus(self, name: str) -> int: ...
    def GetDomainName(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetGridArrayName(self, index: int) -> str: ...
    def GetGridArrayStatus(self, name: str) -> int: ...
    def GetGridName(self, index: int) -> str: ...
    def GetGridStatus(self, gridname: str) -> int: ...
    def GetInputArray(self) -> vtkmodules.vtkCommonCore.vtkCharArray: ...
    def GetInputString(self) -> str: ...
    def GetInputStringLength(self) -> int: ...
    def GetNumberOfCellArrays(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfGridArrays(self) -> int: ...
    def GetNumberOfGrids(self) -> int: ...
    def GetNumberOfPointArrays(self) -> int: ...
    def GetNumberOfSetArrays(self) -> int: ...
    def GetNumberOfSets(self) -> int: ...
    def GetPointArrayName(self, index: int) -> str: ...
    def GetPointArrayStatus(self, name: str) -> int: ...
    def GetReadFromInputString(self) -> bool: ...
    def GetSIL(self) -> vtkmodules.vtkCommonDataModel.vtkGraph: ...
    def GetSILUpdateStamp(self) -> int: ...
    def GetSetArrayName(self, index: int) -> str: ...
    def GetSetArrayStatus(self, name: str) -> int: ...
    def GetSetName(self, index: int) -> str: ...
    def GetSetStatus(self, gridname: str) -> int: ...
    def GetStride(self) -> Tuple[int, int, int]: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkXdmfReader: ...
    def ReadFromInputStringOff(self) -> None: ...
    def ReadFromInputStringOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkXdmfReader: ...
    def SetBinaryInputString(self, __a: str, len: int) -> None: ...
    def SetCellArrayStatus(self, name: str, status: int) -> None: ...
    def SetDomainName(self, _arg: str) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetGridStatus(self, gridname: str, status: int) -> None: ...
    def SetInputArray(self, __a: vtkmodules.vtkCommonCore.vtkCharArray) -> None: ...
    @overload
    def SetInputString(self, in_: str, len: int) -> None: ...
    @overload
    def SetInputString(self, input: str) -> None: ...
    def SetPointArrayStatus(self, name: str, status: int) -> None: ...
    def SetReadFromInputString(self, _arg: bool) -> None: ...
    def SetSetStatus(self, gridname: str, status: int) -> None: ...
    @overload
    def SetStride(self, _arg1: int, _arg2: int, _arg3: int) -> None: ...
    @overload
    def SetStride(self, _arg: Sequence[int]) -> None: ...

class vtkXdmfWriter(vtkmodules.vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    def GetFileName(self) -> str: ...
    def GetHeavyDataFileName(self) -> str: ...
    def GetHeavyDataGroupName(self) -> str: ...
    def GetLightDataLimit(self) -> int: ...
    def GetMeshStaticOverTime(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetWriteAllTimeSteps(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MeshStaticOverTimeOff(self) -> None: ...
    def MeshStaticOverTimeOn(self) -> None: ...
    def NewInstance(self) -> vtkXdmfWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkXdmfWriter: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetHeavyDataFileName(self, _arg: str) -> None: ...
    def SetHeavyDataGroupName(self, _arg: str) -> None: ...
    def SetInputData(self, dobj: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetLightDataLimit(self, _arg: int) -> None: ...
    def SetMeshStaticOverTime(self, _arg: bool) -> None: ...
    def SetNumberOfPieces(self, _arg: int) -> None: ...
    def SetPiece(self, _arg: int) -> None: ...
    def SetWriteAllTimeSteps(self, _arg: int) -> None: ...
    def Write(self) -> int: ...
    def WriteAllTimeStepsOff(self) -> None: ...
    def WriteAllTimeStepsOn(self) -> None: ...
