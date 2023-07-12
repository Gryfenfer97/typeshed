from typing import Callable, MutableSequence, Sequence, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonMath
import vtkmodules.vtkRenderingContext2D
import vtkmodules.vtkRenderingCore
import vtkmodules.vtkRenderingOpenGL2

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkOpenGLContextActor(vtkmodules.vtkRenderingContext2D.vtkContextActor):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOpenGLContextActor: ...
    def ReleaseGraphicsResources(self, window: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def RenderOverlay(self, viewport: vtkmodules.vtkRenderingCore.vtkViewport) -> int: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenGLContextActor: ...

class vtkOpenGLContextBufferId(vtkmodules.vtkRenderingContext2D.vtkAbstractContextBufferId):
    def Allocate(self) -> None: ...
    def GetContext(self) -> vtkmodules.vtkRenderingCore.vtkRenderWindow: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPickedItem(self, x: int, y: int) -> int: ...
    def IsA(self, type: str) -> int: ...
    def IsAllocated(self) -> bool: ...
    def IsSupported(self) -> bool: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOpenGLContextBufferId: ...
    def ReleaseGraphicsResources(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenGLContextBufferId: ...
    def SetContext(self, context: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> None: ...
    def SetValues(self, srcXmin: int, srcYmin: int) -> None: ...

class vtkOpenGLContextDevice2D(vtkmodules.vtkRenderingContext2D.vtkContextDevice2D):
    def Begin(self, viewport: vtkmodules.vtkRenderingCore.vtkViewport) -> None: ...
    def BufferIdModeBegin(self, bufferId: vtkmodules.vtkRenderingContext2D.vtkAbstractContextBufferId) -> None: ...
    def BufferIdModeEnd(self) -> None: ...
    def ComputeJustifiedStringBounds(self, string: str, bounds: MutableSequence[float]) -> None: ...
    def ComputeStringBounds(self, string: str, bounds: MutableSequence[float]) -> None: ...
    def DrawColoredPolygon(
        self, points: MutableSequence[float], numPoints: int, colors: MutableSequence[int] = ..., nc_comps: int = 0
    ) -> None: ...
    def DrawEllipseWedge(
        self, x: float, y: float, outRx: float, outRy: float, inRx: float, inRy: float, startAngle: float, stopAngle: float
    ) -> None: ...
    def DrawEllipticArc(self, x: float, y: float, rX: float, rY: float, startAngle: float, stopAngle: float) -> None: ...
    @overload
    def DrawImage(self, p: MutableSequence[float], scale: float, image: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    @overload
    def DrawImage(
        self, pos: vtkmodules.vtkCommonDataModel.vtkRectf, image: vtkmodules.vtkCommonDataModel.vtkImageData
    ) -> None: ...
    def DrawLines(self, f: MutableSequence[float], n: int, colors: MutableSequence[int] = ..., nc_comps: int = 0) -> None: ...
    def DrawMarkers(
        self,
        shape: int,
        highlight: bool,
        points: MutableSequence[float],
        n: int,
        colors: MutableSequence[int] = ...,
        nc_comps: int = 0,
    ) -> None: ...
    def DrawMathTextString(self, point: MutableSequence[float], string: str) -> None: ...
    def DrawPointSprites(
        self,
        sprite: vtkmodules.vtkCommonDataModel.vtkImageData,
        points: MutableSequence[float],
        n: int,
        colors: MutableSequence[int] = ...,
        nc_comps: int = 0,
    ) -> None: ...
    def DrawPoints(
        self, points: MutableSequence[float], n: int, colors: MutableSequence[int] = ..., nc_comps: int = 0
    ) -> None: ...
    def DrawPoly(self, f: MutableSequence[float], n: int, colors: MutableSequence[int] = ..., nc_comps: int = 0) -> None: ...
    def DrawPolyData(
        self,
        p: MutableSequence[float],
        scale: float,
        polyData: vtkmodules.vtkCommonDataModel.vtkPolyData,
        colors: vtkmodules.vtkCommonCore.vtkUnsignedCharArray,
        scalarMode: int,
    ) -> None: ...
    def DrawPolygon(self, __a: MutableSequence[float], __b: int) -> None: ...
    def DrawQuad(self, points: MutableSequence[float], n: int) -> None: ...
    def DrawQuadStrip(self, points: MutableSequence[float], n: int) -> None: ...
    def DrawString(self, point: MutableSequence[float], string: str) -> None: ...
    def EnableClipping(self, enable: bool) -> None: ...
    def End(self) -> None: ...
    def GetMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix3x3) -> None: ...
    def GetMaximumMarkerCacheSize(self) -> int: ...
    def GetModelMatrix(self) -> vtkmodules.vtkCommonMath.vtkMatrix4x4: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetProjectionMatrix(self) -> vtkmodules.vtkCommonMath.vtkMatrix4x4: ...
    def GetRenderWindow(self) -> vtkmodules.vtkRenderingOpenGL2.vtkOpenGLRenderWindow: ...
    def HasGLSL(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MultiplyMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix3x3) -> None: ...
    def NewInstance(self) -> vtkOpenGLContextDevice2D: ...
    def PopMatrix(self) -> None: ...
    def PushMatrix(self) -> None: ...
    def ReleaseGraphicsResources(self, window: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenGLContextDevice2D: ...
    def SetClipping(self, x: MutableSequence[int]) -> None: ...
    def SetColor(self, color: MutableSequence[int]) -> None: ...
    def SetColor4(self, color: MutableSequence[int]) -> None: ...
    def SetLineType(self, type: int) -> None: ...
    def SetLineWidth(self, width: float) -> None: ...
    def SetMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix3x3) -> None: ...
    def SetMaximumMarkerCacheSize(self, _arg: int) -> None: ...
    def SetPointSize(self, size: float) -> None: ...
    def SetStringRendererToFreeType(self) -> bool: ...
    def SetStringRendererToQt(self) -> bool: ...
    def SetTexture(self, image: vtkmodules.vtkCommonDataModel.vtkImageData, properties: int = 0) -> None: ...

class vtkOpenGLContextDevice3D(vtkmodules.vtkRenderingContext2D.vtkContextDevice3D):
    def ApplyBrush(self, brush: vtkmodules.vtkRenderingContext2D.vtkBrush) -> None: ...
    def ApplyPen(self, pen: vtkmodules.vtkRenderingContext2D.vtkPen) -> None: ...
    def Begin(self, viewport: vtkmodules.vtkRenderingCore.vtkViewport) -> None: ...
    def DisableClippingPlane(self, i: int) -> None: ...
    def DrawLines(self, verts: Sequence[float], n: int, colors: Sequence[int], nc: int) -> None: ...
    def DrawPoints(self, verts: Sequence[float], n: int, colors: Sequence[int], nc: int) -> None: ...
    def DrawPoly(self, verts: Sequence[float], n: int, colors: Sequence[int], nc: int) -> None: ...
    def DrawTriangleMesh(self, mesh: Sequence[float], n: int, colors: Sequence[int], nc: int) -> None: ...
    def EnableClipping(self, enable: bool) -> None: ...
    def EnableClippingPlane(self, i: int, planeEquation: MutableSequence[float]) -> None: ...
    def GetMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def Initialize(self, __a: vtkmodules.vtkRenderingCore.vtkRenderer, __b: vtkOpenGLContextDevice2D) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MultiplyMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...
    def NewInstance(self) -> vtkOpenGLContextDevice3D: ...
    def PopMatrix(self) -> None: ...
    def PushMatrix(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenGLContextDevice3D: ...
    def SetClipping(self, rect: vtkmodules.vtkCommonDataModel.vtkRecti) -> None: ...
    def SetMatrix(self, m: vtkmodules.vtkCommonMath.vtkMatrix4x4) -> None: ...

class vtkOpenGLPropItem(vtkmodules.vtkRenderingContext2D.vtkPropItem):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkOpenGLPropItem: ...
    def Paint(self, painter: vtkmodules.vtkRenderingContext2D.vtkContext2D) -> bool: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkOpenGLPropItem: ...
