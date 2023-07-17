from collections.abc import Callable, Sequence
from typing import Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkImagingCore

Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkImageButterworthHighPass(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetCutOff(self) -> Tuple[float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOrder(self) -> int: ...
    def GetXCutOff(self) -> float: ...
    def GetYCutOff(self) -> float: ...
    def GetZCutOff(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageButterworthHighPass: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageButterworthHighPass: ...
    @overload
    def SetCutOff(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetCutOff(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetCutOff(self, v: float) -> None: ...
    def SetOrder(self, _arg: int) -> None: ...
    def SetXCutOff(self, cutOff: float) -> None: ...
    def SetYCutOff(self, cutOff: float) -> None: ...
    def SetZCutOff(self, cutOff: float) -> None: ...

class vtkImageButterworthLowPass(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetCutOff(self) -> Tuple[float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOrder(self) -> int: ...
    def GetXCutOff(self) -> float: ...
    def GetYCutOff(self) -> float: ...
    def GetZCutOff(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageButterworthLowPass: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageButterworthLowPass: ...
    @overload
    def SetCutOff(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetCutOff(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetCutOff(self, v: float) -> None: ...
    def SetOrder(self, _arg: int) -> None: ...
    def SetXCutOff(self, cutOff: float) -> None: ...
    def SetYCutOff(self, cutOff: float) -> None: ...
    def SetZCutOff(self, cutOff: float) -> None: ...

class vtkImageComplex_t:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, __a: vtkImageComplex_t) -> None: ...

class vtkImageFourierFilter(vtkmodules.vtkImagingCore.vtkImageDecomposeFilter):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageFourierFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageFourierFilter: ...

class vtkImageFFT(vtkImageFourierFilter):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageFFT: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageFFT: ...

class vtkImageFourierCenter(vtkmodules.vtkImagingCore.vtkImageDecomposeFilter):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageFourierCenter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageFourierCenter: ...

class vtkImageIdealHighPass(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetCutOff(self) -> Tuple[float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetXCutOff(self) -> float: ...
    def GetYCutOff(self) -> float: ...
    def GetZCutOff(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageIdealHighPass: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageIdealHighPass: ...
    @overload
    def SetCutOff(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetCutOff(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetCutOff(self, v: float) -> None: ...
    def SetXCutOff(self, cutOff: float) -> None: ...
    def SetYCutOff(self, cutOff: float) -> None: ...
    def SetZCutOff(self, cutOff: float) -> None: ...

class vtkImageIdealLowPass(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetCutOff(self) -> Tuple[float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetXCutOff(self) -> float: ...
    def GetYCutOff(self) -> float: ...
    def GetZCutOff(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageIdealLowPass: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageIdealLowPass: ...
    @overload
    def SetCutOff(self, _arg1: float, _arg2: float, _arg3: float) -> None: ...
    @overload
    def SetCutOff(self, _arg: Sequence[float]) -> None: ...
    @overload
    def SetCutOff(self, v: float) -> None: ...
    def SetXCutOff(self, cutOff: float) -> None: ...
    def SetYCutOff(self, cutOff: float) -> None: ...
    def SetZCutOff(self, cutOff: float) -> None: ...

class vtkImageRFFT(vtkImageFourierFilter):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageRFFT: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageRFFT: ...
