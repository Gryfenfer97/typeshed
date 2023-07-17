from collections.abc import Callable
from typing import TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkRenderingCore
import vtkmodules.vtkRenderingOpenGL2
import vtkmodules.vtkRenderingSceneGraph

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkVtkJSSceneGraphSerializer(vtkmodules.vtkCommonCore.vtkObject):
    @overload
    def Add(self, __a: vtkmodules.vtkRenderingSceneGraph.vtkViewNode, __b: vtkmodules.vtkRenderingCore.vtkActor) -> None: ...
    @overload
    def Add(
        self, __a: vtkmodules.vtkRenderingSceneGraph.vtkViewNode, __b: vtkmodules.vtkRenderingCore.vtkCompositePolyDataMapper
    ) -> None: ...
    @overload
    def Add(
        self, __a: vtkmodules.vtkRenderingSceneGraph.vtkViewNode, __b: vtkmodules.vtkRenderingOpenGL2.vtkCompositePolyDataMapper2
    ) -> None: ...
    @overload
    def Add(
        self, __a: vtkmodules.vtkRenderingSceneGraph.vtkViewNode, __b: vtkmodules.vtkRenderingCore.vtkGlyph3DMapper
    ) -> None: ...
    @overload
    def Add(self, __a: vtkmodules.vtkRenderingSceneGraph.vtkViewNode, __b: vtkmodules.vtkRenderingCore.vtkMapper) -> None: ...
    @overload
    def Add(self, __a: vtkmodules.vtkRenderingSceneGraph.vtkViewNode, __b: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...
    @overload
    def Add(
        self, __a: vtkmodules.vtkRenderingSceneGraph.vtkViewNode, __b: vtkmodules.vtkRenderingCore.vtkRenderWindow
    ) -> None: ...
    def GetDataArray(self, __a: int) -> vtkmodules.vtkCommonCore.vtkDataArray: ...
    def GetDataArrayId(self, __a: int) -> str: ...
    def GetDataObject(self, __a: int) -> vtkmodules.vtkCommonDataModel.vtkDataObject: ...
    def GetNumberOfDataArrays(self) -> int: ...
    def GetNumberOfDataObjects(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkVtkJSSceneGraphSerializer: ...
    def Reset(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkVtkJSSceneGraphSerializer: ...

class vtkVtkJSViewNodeFactory(vtkmodules.vtkRenderingSceneGraph.vtkViewNodeFactory):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetSerializer(self) -> vtkVtkJSSceneGraphSerializer: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkVtkJSViewNodeFactory: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkVtkJSViewNodeFactory: ...
    def SetSerializer(self, __a: vtkVtkJSSceneGraphSerializer) -> None: ...
