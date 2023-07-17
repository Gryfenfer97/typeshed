from typing import overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel

class vtkH5RageReader(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def DisableAllPointArrays(self) -> None: ...
    def EnableAllPointArrays(self) -> None: ...
    def GetCurrentTimeStep(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfPointArrays(self) -> int: ...
    @overload
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    @overload
    def GetOutput(self, index: int) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetPointArrayName(self, index: int) -> str: ...
    def GetPointArrayStatus(self, name: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkH5RageReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkH5RageReader: ...
    def SetCurrentTimeStep(self, _arg: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetPointArrayStatus(self, name: str, status: int) -> None: ...
