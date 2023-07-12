from typing import Callable, MutableSequence, TypeVar, Union

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkRenderingCore
import vtkmodules.vtkRenderingFreeType

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkMatplotlibMathTextUtilities(vtkmodules.vtkRenderingFreeType.vtkMathTextUtilities):
    def GetBoundingBox(
        self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, str: str, dpi: int, bbox: MutableSequence[int]
    ) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetScaleToPowerOfTwo(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    def IsAvailable(self) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMatplotlibMathTextUtilities: ...
    def RenderString(
        self,
        str: str,
        image: vtkmodules.vtkCommonDataModel.vtkImageData,
        tprop: vtkmodules.vtkRenderingCore.vtkTextProperty,
        dpi: int,
        textDims: MutableSequence[int] = ...,
    ) -> bool: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMatplotlibMathTextUtilities: ...
    def SetScaleToPowerOfTwo(self, val: bool) -> None: ...
    def StringToPath(
        self, str: str, path: vtkmodules.vtkCommonDataModel.vtkPath, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, dpi: int
    ) -> bool: ...
