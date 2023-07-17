from collections.abc import Callable, MutableSequence
from typing import TypeVar, Union

import vtkmodules.vtkCommonCore
import vtkmodules.vtkRenderingContext2D
import vtkmodules.vtkRenderingCore
import vtkmodules.vtkViewsCore

Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkContextInteractorStyle(vtkmodules.vtkRenderingCore.vtkInteractorStyle):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetScene(self) -> vtkmodules.vtkRenderingContext2D.vtkContextScene: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkContextInteractorStyle: ...
    def OnChar(self) -> None: ...
    def OnKeyPress(self) -> None: ...
    def OnKeyRelease(self) -> None: ...
    def OnLeftButtonDoubleClick(self) -> None: ...
    def OnLeftButtonDown(self) -> None: ...
    def OnLeftButtonUp(self) -> None: ...
    def OnMiddleButtonDoubleClick(self) -> None: ...
    def OnMiddleButtonDown(self) -> None: ...
    def OnMiddleButtonUp(self) -> None: ...
    def OnMouseMove(self) -> None: ...
    def OnMouseWheelBackward(self) -> None: ...
    def OnMouseWheelForward(self) -> None: ...
    def OnRightButtonDoubleClick(self) -> None: ...
    def OnRightButtonDown(self) -> None: ...
    def OnRightButtonUp(self) -> None: ...
    def OnSceneModified(self) -> None: ...
    def OnSelection(self, rect: MutableSequence[int]) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkContextInteractorStyle: ...
    def SetScene(self, scene: vtkmodules.vtkRenderingContext2D.vtkContextScene) -> None: ...

class vtkContextView(vtkmodules.vtkViewsCore.vtkRenderViewBase):
    def GetContext(self) -> vtkmodules.vtkRenderingContext2D.vtkContext2D: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetScene(self) -> vtkmodules.vtkRenderingContext2D.vtkContextScene: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkContextView: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkContextView: ...
    def SetContext(self, context: vtkmodules.vtkRenderingContext2D.vtkContext2D) -> None: ...
    def SetScene(self, scene: vtkmodules.vtkRenderingContext2D.vtkContextScene) -> None: ...
