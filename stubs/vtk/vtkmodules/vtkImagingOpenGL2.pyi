from collections.abc import Callable
from typing import TypeVar, Union

import vtkmodules.vtkCommonCore
import vtkmodules.vtkImagingGeneral
import vtkmodules.vtkRenderingCore

Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkOpenGLImageGradient(vtkmodules.vtkImagingGeneral.vtkImageGradient):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOpenGLImageGradient: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenGLImageGradient: ...
    def SetRenderWindow(self, __a: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> None: ...
