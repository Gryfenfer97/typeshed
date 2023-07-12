from typing import Callable, MutableSequence, TypeVar, Union

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkRenderingCore

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkFreeTypeStringToImage(vtkmodules.vtkRenderingCore.vtkStringToImage):
    def DeepCopy(self, utility: vtkFreeTypeStringToImage) -> None: ...
    def GetBounds(
        self, property: vtkmodules.vtkRenderingCore.vtkTextProperty, string: str, dpi: int
    ) -> vtkmodules.vtkCommonDataModel.vtkVector2i: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkFreeTypeStringToImage: ...
    def RenderString(
        self,
        property: vtkmodules.vtkRenderingCore.vtkTextProperty,
        string: str,
        dpi: int,
        data: vtkmodules.vtkCommonDataModel.vtkImageData,
        textDims: MutableSequence[int] = ...,
    ) -> int: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkFreeTypeStringToImage: ...
    def SetScaleToPowerOfTwo(self, scale: bool) -> None: ...

class vtkFreeTypeTools(vtkmodules.vtkCommonCore.vtkObject):
    def DebugTexturesOff(self) -> None: ...
    def DebugTexturesOn(self) -> None: ...
    def ForceCompiledFontsOff(self) -> None: ...
    def ForceCompiledFontsOn(self) -> None: ...
    def GetBoundingBox(
        self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, str: str, dpi: int, bbox: MutableSequence[int]
    ) -> bool: ...
    def GetConstrainedFontSize(
        self, str: str, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, dpi: int, targetWidth: int, targetHeight: int
    ) -> int: ...
    def GetDebugTextures(self) -> bool: ...
    def GetForceCompiledFonts(self) -> bool: ...
    @staticmethod
    def GetInstance() -> vtkFreeTypeTools: ...
    def GetMaximumNumberOfBytes(self) -> int: ...
    def GetMaximumNumberOfBytesMaxValue(self) -> int: ...
    def GetMaximumNumberOfBytesMinValue(self) -> int: ...
    def GetMaximumNumberOfFaces(self) -> int: ...
    def GetMaximumNumberOfFacesMaxValue(self) -> int: ...
    def GetMaximumNumberOfFacesMinValue(self) -> int: ...
    def GetMaximumNumberOfSizes(self) -> int: ...
    def GetMaximumNumberOfSizesMaxValue(self) -> int: ...
    def GetMaximumNumberOfSizesMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetScaleToPowerTwo(self) -> bool: ...
    @staticmethod
    def HashBuffer(buffer: Pointer, n: int, hash: int = 0) -> int: ...
    @staticmethod
    def HashString(str: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MapIdToTextProperty(self, tprop_cache_id: int, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty) -> None: ...
    def MapTextPropertyToId(
        self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, tprop_cache_id: MutableSequence[int]
    ) -> None: ...
    def NewInstance(self) -> vtkFreeTypeTools: ...
    def RenderString(
        self,
        tprop: vtkmodules.vtkRenderingCore.vtkTextProperty,
        str: str,
        dpi: int,
        data: vtkmodules.vtkCommonDataModel.vtkImageData,
        textDims: MutableSequence[int] = ...,
    ) -> bool: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkFreeTypeTools: ...
    def ScaleToPowerTwoOff(self) -> None: ...
    def ScaleToPowerTwoOn(self) -> None: ...
    def SetDebugTextures(self, _arg: bool) -> None: ...
    def SetForceCompiledFonts(self, _arg: bool) -> None: ...
    @staticmethod
    def SetInstance(instance: vtkFreeTypeTools) -> None: ...
    def SetMaximumNumberOfBytes(self, _arg: int) -> None: ...
    def SetMaximumNumberOfFaces(self, _arg: int) -> None: ...
    def SetMaximumNumberOfSizes(self, _arg: int) -> None: ...
    def SetScaleToPowerTwo(self, _arg: bool) -> None: ...
    def StringToPath(
        self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, str: str, dpi: int, path: vtkmodules.vtkCommonDataModel.vtkPath
    ) -> bool: ...

class vtkFreeTypeToolsCleanup:
    def __init__(self) -> None: ...

class vtkMathTextFreeTypeTextRenderer(vtkmodules.vtkRenderingCore.vtkTextRenderer):
    def FreeTypeIsSupported(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MathTextIsSupported(self) -> bool: ...
    def NewInstance(self) -> vtkMathTextFreeTypeTextRenderer: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMathTextFreeTypeTextRenderer: ...

class vtkMathTextUtilities(vtkmodules.vtkCommonCore.vtkObject):
    def GetBoundingBox(
        self, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, str: str, dpi: int, bbox: MutableSequence[int]
    ) -> bool: ...
    def GetConstrainedFontSize(
        self, str: str, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, targetWidth: int, targetHeight: int, dpi: int
    ) -> int: ...
    @staticmethod
    def GetInstance() -> vtkMathTextUtilities: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetScaleToPowerOfTwo(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    def IsAvailable(self) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMathTextUtilities: ...
    def RenderString(
        self,
        str: str,
        data: vtkmodules.vtkCommonDataModel.vtkImageData,
        tprop: vtkmodules.vtkRenderingCore.vtkTextProperty,
        dpi: int,
        textDims: MutableSequence[int] = ...,
    ) -> bool: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMathTextUtilities: ...
    @staticmethod
    def SetInstance(instance: vtkMathTextUtilities) -> None: ...
    def SetScaleToPowerOfTwo(self, scale: bool) -> None: ...
    def StringToPath(
        self, str: str, path: vtkmodules.vtkCommonDataModel.vtkPath, tprop: vtkmodules.vtkRenderingCore.vtkTextProperty, dpi: int
    ) -> bool: ...

class vtkMathTextUtilitiesCleanup:
    def __init__(self) -> None: ...

class vtkScaledTextActor(vtkmodules.vtkRenderingCore.vtkTextActor):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkScaledTextActor: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkScaledTextActor: ...

class vtkTextRendererStringToImage(vtkmodules.vtkRenderingCore.vtkStringToImage):
    def DeepCopy(self, utility: vtkTextRendererStringToImage) -> None: ...
    def GetBounds(
        self, property: vtkmodules.vtkRenderingCore.vtkTextProperty, string: str, dpi: int
    ) -> vtkmodules.vtkCommonDataModel.vtkVector2i: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTextRendererStringToImage: ...
    def RenderString(
        self,
        property: vtkmodules.vtkRenderingCore.vtkTextProperty,
        string: str,
        dpi: int,
        data: vtkmodules.vtkCommonDataModel.vtkImageData,
        textDims: MutableSequence[int] = ...,
    ) -> int: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTextRendererStringToImage: ...
    def SetScaleToPowerOfTwo(self, scale: bool) -> None: ...

class vtkVectorText(vtkmodules.vtkCommonExecutionModel.vtkPolyDataAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetText(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkVectorText: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkVectorText: ...
    def SetText(self, _arg: str) -> None: ...
