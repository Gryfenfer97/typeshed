from collections.abc import Callable, Sequence
from typing import Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkImagingCore

Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkImageHSIToRGB(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetMaximum(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageHSIToRGB: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageHSIToRGB: ...
    def SetMaximum(self, _arg: float) -> None: ...

class vtkImageHSVToRGB(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetMaximum(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageHSVToRGB: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageHSVToRGB: ...
    def SetMaximum(self, _arg: float) -> None: ...

class vtkImageLuminance(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageLuminance: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageLuminance: ...

class vtkImageMapToRGBA(vtkmodules.vtkImagingCore.vtkImageMapToColors):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageMapToRGBA: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageMapToRGBA: ...

class vtkImageMapToWindowLevelColors(vtkmodules.vtkImagingCore.vtkImageMapToColors):
    def GetLevel(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetWindow(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageMapToWindowLevelColors: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageMapToWindowLevelColors: ...
    def SetLevel(self, _arg: float) -> None: ...
    def SetWindow(self, _arg: float) -> None: ...

class vtkImageQuantizeRGBToIndex(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetBuildTreeExecuteTime(self) -> float: ...
    def GetInitializeExecuteTime(self) -> float: ...
    def GetInputType(self) -> int: ...
    def GetLookupIndexExecuteTime(self) -> float: ...
    def GetLookupTable(self) -> vtkmodules.vtkCommonCore.vtkLookupTable: ...
    def GetNumberOfColors(self) -> int: ...
    def GetNumberOfColorsMaxValue(self) -> int: ...
    def GetNumberOfColorsMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSamplingRate(self) -> Tuple[int, int, int]: ...
    def GetSortIndexByLuminance(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageQuantizeRGBToIndex: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageQuantizeRGBToIndex: ...
    def SetBuildTreeExecuteTime(self, _arg: float) -> None: ...
    def SetInitializeExecuteTime(self, _arg: float) -> None: ...
    def SetLookupIndexExecuteTime(self, _arg: float) -> None: ...
    def SetNumberOfColors(self, _arg: int) -> None: ...
    @overload
    def SetSamplingRate(self, _arg1: int, _arg2: int, _arg3: int) -> None: ...
    @overload
    def SetSamplingRate(self, _arg: Sequence[int]) -> None: ...
    def SetSortIndexByLuminance(self, _arg: bool) -> None: ...
    def SortIndexByLuminanceOff(self) -> None: ...
    def SortIndexByLuminanceOn(self) -> None: ...

class vtkImageRGBToHSI(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetMaximum(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageRGBToHSI: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageRGBToHSI: ...
    def SetMaximum(self, _arg: float) -> None: ...

class vtkImageRGBToHSV(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetMaximum(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageRGBToHSV: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageRGBToHSV: ...
    def SetMaximum(self, _arg: float) -> None: ...

class vtkImageRGBToYIQ(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetMaximum(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageRGBToYIQ: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageRGBToYIQ: ...
    def SetMaximum(self, _arg: float) -> None: ...

class vtkImageYIQToRGB(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetMaximum(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageYIQToRGB: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageYIQToRGB: ...
    def SetMaximum(self, _arg: float) -> None: ...
