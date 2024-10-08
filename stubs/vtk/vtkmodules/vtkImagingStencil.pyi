from collections.abc import Sequence
from typing import overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkImagingCore

class vtkImageStencil(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetBackgroundColor(self) -> tuple[float, float, float, float]: ...
    def GetBackgroundInput(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetBackgroundValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetReverseStencil(self) -> int: ...
    def GetStencil(self) -> vtkmodules.vtkImagingCore.vtkImageStencilData: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageStencil: ...
    def ReverseStencilOff(self) -> None: ...
    def ReverseStencilOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageStencil: ...
    @overload
    def SetBackgroundColor(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float) -> None: ...
    @overload
    def SetBackgroundColor(self, _arg: Sequence[float]) -> None: ...
    def SetBackgroundInputData(self, input: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    def SetBackgroundValue(self, val: float) -> None: ...
    def SetReverseStencil(self, _arg: int) -> None: ...
    def SetStencilConnection(self, outputPort: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    def SetStencilData(self, stencil: vtkmodules.vtkImagingCore.vtkImageStencilData) -> None: ...

class vtkImageStencilToImage(vtkmodules.vtkCommonExecutionModel.vtkImageAlgorithm):
    def GetInsideValue(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputScalarType(self) -> int: ...
    def GetOutsideValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageStencilToImage: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageStencilToImage: ...
    def SetInsideValue(self, _arg: float) -> None: ...
    def SetOutputScalarType(self, _arg: int) -> None: ...
    def SetOutputScalarTypeToChar(self) -> None: ...
    def SetOutputScalarTypeToDouble(self) -> None: ...
    def SetOutputScalarTypeToFloat(self) -> None: ...
    def SetOutputScalarTypeToInt(self) -> None: ...
    def SetOutputScalarTypeToLong(self) -> None: ...
    def SetOutputScalarTypeToShort(self) -> None: ...
    def SetOutputScalarTypeToUnsignedChar(self) -> None: ...
    def SetOutputScalarTypeToUnsignedInt(self) -> None: ...
    def SetOutputScalarTypeToUnsignedLong(self) -> None: ...
    def SetOutputScalarTypeToUnsignedShort(self) -> None: ...
    def SetOutsideValue(self, _arg: float) -> None: ...

class vtkImageToImageStencil(vtkmodules.vtkImagingCore.vtkImageStencilAlgorithm):
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkImageData: ...
    def GetLowerThreshold(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUpperThreshold(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageToImageStencil: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageToImageStencil: ...
    def SetInputData(self, input: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    def SetLowerThreshold(self, _arg: float) -> None: ...
    def SetUpperThreshold(self, _arg: float) -> None: ...
    def ThresholdBetween(self, lower: float, upper: float) -> None: ...
    def ThresholdByLower(self, thresh: float) -> None: ...
    def ThresholdByUpper(self, thresh: float) -> None: ...

class vtkImplicitFunctionToImageStencil(vtkmodules.vtkImagingCore.vtkImageStencilSource):
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkImplicitFunction: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetThreshold(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImplicitFunctionToImageStencil: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImplicitFunctionToImageStencil: ...
    def SetInput(self, __a: vtkmodules.vtkCommonDataModel.vtkImplicitFunction) -> None: ...
    def SetThreshold(self, _arg: float) -> None: ...

class vtkLassoStencilSource(vtkmodules.vtkImagingCore.vtkImageStencilSource):
    POLYGON: int
    SPLINE: int
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPoints(self) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def GetShape(self) -> int: ...
    def GetShapeAsString(self) -> str: ...
    def GetShapeMaxValue(self) -> int: ...
    def GetShapeMinValue(self) -> int: ...
    def GetSliceOrientation(self) -> int: ...
    def GetSliceOrientationMaxValue(self) -> int: ...
    def GetSliceOrientationMinValue(self) -> int: ...
    def GetSlicePoints(self, i: int) -> vtkmodules.vtkCommonCore.vtkPoints: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkLassoStencilSource: ...
    def RemoveAllSlicePoints(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkLassoStencilSource: ...
    def SetPoints(self, points: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...
    def SetShape(self, _arg: int) -> None: ...
    def SetShapeToPolygon(self) -> None: ...
    def SetShapeToSpline(self) -> None: ...
    def SetSliceOrientation(self, _arg: int) -> None: ...
    def SetSlicePoints(self, i: int, points: vtkmodules.vtkCommonCore.vtkPoints) -> None: ...

class vtkPolyDataToImageStencil(vtkmodules.vtkImagingCore.vtkImageStencilSource):
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkPolyData: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetTolerance(self) -> float: ...
    def GetToleranceMaxValue(self) -> float: ...
    def GetToleranceMinValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPolyDataToImageStencil: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPolyDataToImageStencil: ...
    def SetInputData(self, __a: vtkmodules.vtkCommonDataModel.vtkPolyData) -> None: ...
    def SetTolerance(self, _arg: float) -> None: ...

class vtkROIStencilSource(vtkmodules.vtkImagingCore.vtkImageStencilSource):
    BOX: int
    CYLINDERX: int
    CYLINDERY: int
    CYLINDERZ: int
    ELLIPSOID: int
    def GetBounds(self) -> tuple[float, float, float, float, float, float]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetShape(self) -> int: ...
    def GetShapeAsString(self) -> str: ...
    def GetShapeMaxValue(self) -> int: ...
    def GetShapeMinValue(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkROIStencilSource: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkROIStencilSource: ...
    @overload
    def SetBounds(self, _arg1: float, _arg2: float, _arg3: float, _arg4: float, _arg5: float, _arg6: float) -> None: ...
    @overload
    def SetBounds(self, _arg: Sequence[float]) -> None: ...
    def SetShape(self, _arg: int) -> None: ...
    def SetShapeToBox(self) -> None: ...
    def SetShapeToCylinderX(self) -> None: ...
    def SetShapeToCylinderY(self) -> None: ...
    def SetShapeToCylinderZ(self) -> None: ...
    def SetShapeToEllipsoid(self) -> None: ...
