from collections.abc import MutableSequence
from typing import TypeVar, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkImagingColor
import vtkmodules.vtkInteractionStyle
import vtkmodules.vtkInteractionWidgets
import vtkmodules.vtkRenderingCore

_Pointer = TypeVar("_Pointer")

class vtkImageViewer(vtkmodules.vtkCommonCore.vtkObject):
    def GetActor2D(self) -> vtkmodules.vtkRenderingCore.vtkActor2D: ...
    def GetColorLevel(self) -> float: ...
    def GetColorWindow(self) -> float: ...
    def GetImageMapper(self) -> vtkmodules.vtkRenderingCore.vtkImageMapper: ...
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOffScreenRendering(self) -> int: ...
    def GetPosition(self) -> tuple[int, int]: ...
    def GetRenderWindow(self) -> vtkmodules.vtkRenderingCore.vtkRenderWindow: ...
    def GetRenderer(self) -> vtkmodules.vtkRenderingCore.vtkRenderer: ...
    def GetSize(self) -> tuple[int, int]: ...
    def GetWholeZMax(self) -> int: ...
    def GetWholeZMin(self) -> int: ...
    def GetWindowName(self) -> str: ...
    def GetZSlice(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageViewer: ...
    def OffScreenRenderingOff(self) -> None: ...
    def OffScreenRenderingOn(self) -> None: ...
    def Render(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageViewer: ...
    def SetColorLevel(self, s: float) -> None: ...
    def SetColorWindow(self, s: float) -> None: ...
    def SetDisplayId(self, a: _Pointer) -> None: ...
    def SetInputConnection(self, input: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetInputData(self, in_: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    def SetOffScreenRendering(self, __a: int) -> None: ...
    def SetParentId(self, a: _Pointer) -> None: ...
    @overload
    def SetPosition(self, x: int, y: int) -> None: ...
    @overload
    def SetPosition(self, a: MutableSequence[int]) -> None: ...
    def SetRenderWindow(self, renWin: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> None: ...
    @overload
    def SetSize(self, width: int, height: int) -> None: ...
    @overload
    def SetSize(self, a: MutableSequence[int]) -> None: ...
    def SetWindowId(self, a: _Pointer) -> None: ...
    def SetZSlice(self, s: int) -> None: ...
    def SetupInteractor(self, __a: vtkmodules.vtkRenderingCore.vtkRenderWindowInteractor) -> None: ...

class vtkImageViewer2(vtkmodules.vtkCommonCore.vtkObject):
    SLICE_ORIENTATION_XY: int
    SLICE_ORIENTATION_XZ: int
    SLICE_ORIENTATION_YZ: int
    def GetColorLevel(self) -> float: ...
    def GetColorWindow(self) -> float: ...
    def GetImageActor(self) -> vtkmodules.vtkRenderingCore.vtkImageActor: ...
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetInteractorStyle(self) -> vtkmodules.vtkInteractionStyle.vtkInteractorStyleImage: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOffScreenRendering(self) -> int: ...
    def GetPosition(self) -> tuple[int, int]: ...
    def GetRenderWindow(self) -> vtkmodules.vtkRenderingCore.vtkRenderWindow: ...
    def GetRenderer(self) -> vtkmodules.vtkRenderingCore.vtkRenderer: ...
    def GetSize(self) -> tuple[int, int]: ...
    def GetSlice(self) -> int: ...
    def GetSliceMax(self) -> int: ...
    def GetSliceMin(self) -> int: ...
    def GetSliceOrientation(self) -> int: ...
    @overload
    def GetSliceRange(self, range: MutableSequence[int]) -> None: ...
    @overload
    def GetSliceRange(self, min: int, max: int) -> None: ...
    @overload
    def GetSliceRange(self) -> Pointer: ...
    def GetWindowLevel(self) -> vtkmodules.vtkImagingColor.vtkImageMapToWindowLevelColors: ...
    def GetWindowName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageViewer2: ...
    def OffScreenRenderingOff(self) -> None: ...
    def OffScreenRenderingOn(self) -> None: ...
    def Render(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageViewer2: ...
    def SetColorLevel(self, s: float) -> None: ...
    def SetColorWindow(self, s: float) -> None: ...
    def SetDisplayId(self, a: _Pointer) -> None: ...
    def SetInputConnection(self, input: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetInputData(self, in_: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    def SetOffScreenRendering(self, __a: int) -> None: ...
    def SetParentId(self, a: _Pointer) -> None: ...
    @overload
    def SetPosition(self, x: int, y: int) -> None: ...
    @overload
    def SetPosition(self, a: MutableSequence[int]) -> None: ...
    def SetRenderWindow(self, arg: vtkmodules.vtkRenderingCore.vtkRenderWindow) -> None: ...
    def SetRenderer(self, arg: vtkmodules.vtkRenderingCore.vtkRenderer) -> None: ...
    @overload
    def SetSize(self, width: int, height: int) -> None: ...
    @overload
    def SetSize(self, a: MutableSequence[int]) -> None: ...
    def SetSlice(self, s: int) -> None: ...
    def SetSliceOrientation(self, orientation: int) -> None: ...
    def SetSliceOrientationToXY(self) -> None: ...
    def SetSliceOrientationToXZ(self) -> None: ...
    def SetSliceOrientationToYZ(self) -> None: ...
    def SetWindowId(self, a: _Pointer) -> None: ...
    def SetupInteractor(self, __a: vtkmodules.vtkRenderingCore.vtkRenderWindowInteractor) -> None: ...
    def UpdateDisplayExtent(self) -> None: ...

class vtkResliceImageViewer(vtkImageViewer2):
    RESLICE_AXIS_ALIGNED: int
    RESLICE_OBLIQUE: int
    SliceChangedEvent: int

    def GetInteractor(self) -> vtkmodules.vtkRenderingCore.vtkRenderWindowInteractor: ...
    def GetLookupTable(self) -> vtkmodules.vtkCommonCore.vtkScalarsToColors: ...
    def GetMeasurements(self) -> vtkResliceImageViewerMeasurements: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPointPlacer(self) -> vtkmodules.vtkInteractionWidgets.vtkBoundedPlanePointPlacer: ...
    def GetResliceCursor(self) -> vtkmodules.vtkInteractionWidgets.vtkResliceCursor: ...
    def GetResliceCursorWidget(self) -> vtkmodules.vtkInteractionWidgets.vtkResliceCursorWidget: ...
    def GetResliceMode(self) -> int: ...
    def GetSliceScrollFactor(self) -> float: ...
    def GetSliceScrollOnMouseWheel(self) -> int: ...
    def GetThickMode(self) -> int: ...
    def IncrementSlice(self, inc: int) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkResliceImageViewer: ...
    def Render(self) -> None: ...
    def Reset(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkResliceImageViewer: ...
    def SetColorLevel(self, s: float) -> None: ...
    def SetColorWindow(self, s: float) -> None: ...
    def SetInputConnection(self, input: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetInputData(self, in_: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    def SetLookupTable(self, __a: vtkmodules.vtkCommonCore.vtkScalarsToColors) -> None: ...
    def SetResliceCursor(self, rc: vtkmodules.vtkInteractionWidgets.vtkResliceCursor) -> None: ...
    def SetResliceMode(self, resliceMode: int) -> None: ...
    def SetResliceModeToAxisAligned(self) -> None: ...
    def SetResliceModeToOblique(self) -> None: ...
    def SetSliceScrollFactor(self, _arg: float) -> None: ...
    def SetSliceScrollOnMouseWheel(self, _arg: int) -> None: ...
    def SetThickMode(self, __a: int) -> None: ...
    def SliceScrollOnMouseWheelOff(self) -> None: ...
    def SliceScrollOnMouseWheelOn(self) -> None: ...

class vtkResliceImageViewerMeasurements(vtkmodules.vtkCommonCore.vtkObject):
    def AddItem(self, __a: vtkmodules.vtkInteractionWidgets.vtkAbstractWidget) -> None: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetProcessEvents(self) -> int: ...
    def GetProcessEventsMaxValue(self) -> int: ...
    def GetProcessEventsMinValue(self) -> int: ...
    def GetResliceImageViewer(self) -> vtkResliceImageViewer: ...
    def GetTolerance(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkResliceImageViewerMeasurements: ...
    def ProcessEventsOff(self) -> None: ...
    def ProcessEventsOn(self) -> None: ...
    def RemoveAllItems(self) -> None: ...
    def RemoveItem(self, __a: vtkmodules.vtkInteractionWidgets.vtkAbstractWidget) -> None: ...
    def Render(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkResliceImageViewerMeasurements: ...
    def SetProcessEvents(self, _arg: int) -> None: ...
    def SetResliceImageViewer(self, __a: vtkResliceImageViewer) -> None: ...
    def SetTolerance(self, _arg: float) -> None: ...
    def Update(self) -> None: ...
