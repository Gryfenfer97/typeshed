from collections.abc import MutableSequence, Sequence
from typing import TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonMath
import vtkmodules.vtkFiltersCore
import vtkmodules.vtkIOExport
import vtkmodules.vtkRenderingCore

_Pointer = TypeVar("_Pointer")

class WebGLObjectTypes(int): ...

VTK_ONLYCAMERA: int
VTK_ONLYWIDGET: int
VTK_PARSEALL: int
wLINES: WebGLObjectTypes
wPOINTS: WebGLObjectTypes
wTRIANGLES: WebGLObjectTypes

class vtkPVWebGLExporter(vtkmodules.vtkIOExport.vtkExporter):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPVWebGLExporter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPVWebGLExporter: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkWebGLDataSet(vtkmodules.vtkCommonCore.vtkObject):
    def GenerateBinaryData(self) -> None: ...
    def GetBinaryData(self) -> _Pointer: ...
    def GetBinarySize(self) -> int: ...
    def GetMD5(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def HasChanged(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWebGLDataSet: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWebGLDataSet: ...
    def SetColors(self, c: MutableSequence[int]) -> None: ...
    def SetIndexes(self, i: MutableSequence[int], size: int) -> None: ...
    def SetMatrix(self, m: MutableSequence[float]) -> None: ...
    def SetNormals(self, n: MutableSequence[float]) -> None: ...
    def SetPoints(self, p: MutableSequence[float], size: int) -> None: ...
    def SetTCoords(self, t: MutableSequence[float]) -> None: ...
    def SetType(self, t: WebGLObjectTypes) -> None: ...
    def SetVertices(self, v: MutableSequence[float], size: int) -> None: ...

class vtkWebGLExporter(vtkmodules.vtkCommonCore.vtkObject):
    @staticmethod
    def ComputeMD5(content: Sequence[int], size: int, hash: str) -> None: ...
    def GenerateMetadata(self) -> str: ...
    def GetId(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfObjects(self) -> int: ...
    def GetWebGLObject(self, index: int) -> vtkWebGLObject: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWebGLExporter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWebGLExporter: ...
    def SetCenterOfRotation(self, a1: float, a2: float, a3: float) -> None: ...
    @overload
    def SetMaxAllowedSize(self, mesh: int, lines: int) -> None: ...
    @overload
    def SetMaxAllowedSize(self, size: int) -> None: ...
    def exportStaticScene(
        self, renderers: vtkmodules.vtkRenderingCore.vtkRendererCollection, width: int, height: int, path: str
    ) -> None: ...
    def hasChanged(self) -> bool: ...
    def parseScene(self, renderers: vtkmodules.vtkRenderingCore.vtkRendererCollection, viewId: str, parseType: int) -> None: ...

class vtkWebGLObject(vtkmodules.vtkCommonCore.vtkObject):
    def GenerateBinaryData(self) -> None: ...
    @overload
    def GetBinaryData(self, part: int) -> _Pointer: ...
    @overload
    def GetBinaryData(self, part: int, buffer: vtkmodules.vtkCommonCore.vtkUnsignedCharArray) -> None: ...
    def GetBinarySize(self, part: int) -> int: ...
    def GetId(self) -> str: ...
    def GetLayer(self) -> int: ...
    def GetMD5(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfParts(self) -> int: ...
    def GetRendererId(self) -> int: ...
    def HasChanged(self) -> bool: ...
    def HasTransparency(self) -> bool: ...
    def InteractAtServer(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWebGLObject: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWebGLObject: ...
    def SetHasTransparency(self, t: bool) -> None: ...
    def SetId(self, i: str) -> None: ...
    def SetInteractAtServer(self, i: bool) -> None: ...
    def SetIsWidget(self, w: bool) -> None: ...
    def SetLayer(self, l: int) -> None: ...
    def SetRendererId(self, i: int) -> None: ...
    def SetTransformationMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...
    def SetType(self, t: WebGLObjectTypes) -> None: ...
    def SetVisibility(self, vis: bool) -> None: ...
    def SetWireframeMode(self, wireframe: bool) -> None: ...
    def isVisible(self) -> bool: ...
    def isWidget(self) -> bool: ...
    def isWireframeMode(self) -> bool: ...

class vtkWebGLPolyData(vtkWebGLObject):
    def GenerateBinaryData(self) -> None: ...
    def GetBinaryData(self, part: int) -> _Pointer: ...
    def GetBinarySize(self, part: int) -> int: ...
    def GetColorsFromPointData(
        self,
        color: MutableSequence[int],
        pointdata: vtkmodules.vtkCommonDataModel.vtkPointData,
        polydata: vtkmodules.vtkCommonDataModel.vtkPolyData,
        actor: vtkmodules.vtkRenderingCore.vtkActor,
    ) -> None: ...
    def GetColorsFromPolyData(
        self,
        color: MutableSequence[int],
        polydata: vtkmodules.vtkCommonDataModel.vtkPolyData,
        actor: vtkmodules.vtkRenderingCore.vtkActor,
    ) -> None: ...
    def GetLines(
        self, polydata: vtkmodules.vtkFiltersCore.vtkTriangleFilter, actor: vtkmodules.vtkRenderingCore.vtkActor, lineMaxSize: int
    ) -> None: ...
    def GetLinesFromPolygon(
        self,
        mapper: vtkmodules.vtkRenderingCore.vtkMapper,
        actor: vtkmodules.vtkRenderingCore.vtkActor,
        lineMaxSize: int,
        edgeColor: MutableSequence[float],
    ) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfParts(self) -> int: ...
    def GetPoints(
        self, polydata: vtkmodules.vtkFiltersCore.vtkTriangleFilter, actor: vtkmodules.vtkRenderingCore.vtkActor, maxSize: int
    ) -> None: ...
    def GetPolygonsFromCellData(
        self, polydata: vtkmodules.vtkFiltersCore.vtkTriangleFilter, actor: vtkmodules.vtkRenderingCore.vtkActor, maxSize: int
    ) -> None: ...
    def GetPolygonsFromPointData(
        self, polydata: vtkmodules.vtkFiltersCore.vtkTriangleFilter, actor: vtkmodules.vtkRenderingCore.vtkActor, maxSize: int
    ) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWebGLPolyData: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWebGLPolyData: ...
    def SetLine(
        self,
        _points: MutableSequence[float],
        _numberOfPoints: int,
        _index: MutableSequence[int],
        _numberOfIndex: int,
        _colors: MutableSequence[int],
        maxSize: int,
    ) -> None: ...
    def SetMesh(
        self,
        _vertices: MutableSequence[float],
        _numberOfVertices: int,
        _index: MutableSequence[int],
        _numberOfIndexes: int,
        _normals: MutableSequence[float],
        _colors: MutableSequence[int],
        _tcoords: MutableSequence[float],
        maxSize: int,
    ) -> None: ...
    def SetPoints(
        self, points: MutableSequence[float], numberOfPoints: int, colors: MutableSequence[int], maxSize: int
    ) -> None: ...
    def SetTransformationMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...

class vtkWebGLWidget(vtkWebGLObject):
    def GenerateBinaryData(self) -> None: ...
    def GetBinaryData(self, part: int) -> _Pointer: ...
    def GetBinarySize(self, part: int) -> int: ...
    def GetDataFromColorMap(self, actor: vtkmodules.vtkRenderingCore.vtkActor2D) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfParts(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkWebGLWidget: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkWebGLWidget: ...
