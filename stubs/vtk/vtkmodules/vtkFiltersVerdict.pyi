from typing import overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel

class vtkCellQuality(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetUndefinedQuality(self) -> float: ...
    def GetUnsupportedGeometry(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCellQuality: ...
    def PixelArea(self, __a: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    def PolygonArea(self, __a: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCellQuality: ...
    def SetQualityMeasure(self, measure: int) -> None: ...
    def SetQualityMeasureToArea(self) -> None: ...
    def SetQualityMeasureToAspectFrobenius(self) -> None: ...
    def SetQualityMeasureToAspectGamma(self) -> None: ...
    def SetQualityMeasureToAspectRatio(self) -> None: ...
    def SetQualityMeasureToCollapseRatio(self) -> None: ...
    def SetQualityMeasureToCondition(self) -> None: ...
    def SetQualityMeasureToDiagonal(self) -> None: ...
    def SetQualityMeasureToDimension(self) -> None: ...
    def SetQualityMeasureToDistortion(self) -> None: ...
    def SetQualityMeasureToJacobian(self) -> None: ...
    def SetQualityMeasureToMaxAngle(self) -> None: ...
    def SetQualityMeasureToMaxAspectFrobenius(self) -> None: ...
    def SetQualityMeasureToMaxEdgeRatio(self) -> None: ...
    def SetQualityMeasureToMedAspectFrobenius(self) -> None: ...
    def SetQualityMeasureToMinAngle(self) -> None: ...
    def SetQualityMeasureToOddy(self) -> None: ...
    def SetQualityMeasureToRadiusRatio(self) -> None: ...
    def SetQualityMeasureToRelativeSizeSquared(self) -> None: ...
    def SetQualityMeasureToScaledJacobian(self) -> None: ...
    def SetQualityMeasureToShape(self) -> None: ...
    def SetQualityMeasureToShapeAndSize(self) -> None: ...
    def SetQualityMeasureToShear(self) -> None: ...
    def SetQualityMeasureToShearAndSize(self) -> None: ...
    def SetQualityMeasureToSkew(self) -> None: ...
    def SetQualityMeasureToStretch(self) -> None: ...
    def SetQualityMeasureToTaper(self) -> None: ...
    def SetQualityMeasureToVolume(self) -> None: ...
    def SetQualityMeasureToWarpage(self) -> None: ...
    def SetUndefinedQuality(self, _arg: float) -> None: ...
    def SetUnsupportedGeometry(self, _arg: float) -> None: ...
    def TriangleStripArea(self, __a: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...

class vtkCellSizeFilter(vtkmodules.vtkCommonExecutionModel.vtkPassInputTypeAlgorithm):
    def ComputeAreaOff(self) -> None: ...
    def ComputeAreaOn(self) -> None: ...
    def ComputeLengthOff(self) -> None: ...
    def ComputeLengthOn(self) -> None: ...
    def ComputeSumOff(self) -> None: ...
    def ComputeSumOn(self) -> None: ...
    def ComputeVertexCountOff(self) -> None: ...
    def ComputeVertexCountOn(self) -> None: ...
    def ComputeVolumeOff(self) -> None: ...
    def ComputeVolumeOn(self) -> None: ...
    def GetAreaArrayName(self) -> str: ...
    def GetComputeArea(self) -> bool: ...
    def GetComputeLength(self) -> bool: ...
    def GetComputeSum(self) -> bool: ...
    def GetComputeVertexCount(self) -> bool: ...
    def GetComputeVolume(self) -> bool: ...
    def GetLengthArrayName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetVertexCountArrayName(self) -> str: ...
    def GetVolumeArrayName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkCellSizeFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkCellSizeFilter: ...
    def SetAreaArrayName(self, _arg: str) -> None: ...
    def SetComputeArea(self, _arg: bool) -> None: ...
    def SetComputeLength(self, _arg: bool) -> None: ...
    def SetComputeSum(self, _arg: bool) -> None: ...
    def SetComputeVertexCount(self, _arg: bool) -> None: ...
    def SetComputeVolume(self, _arg: bool) -> None: ...
    def SetLengthArrayName(self, _arg: str) -> None: ...
    def SetVertexCountArrayName(self, _arg: str) -> None: ...
    def SetVolumeArrayName(self, _arg: str) -> None: ...

class vtkMatrixMathFilter(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOperation(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMatrixMathFilter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMatrixMathFilter: ...
    def SetOperation(self, _arg: int) -> None: ...
    def SetOperationToDeterminant(self) -> None: ...
    def SetOperationToEigenvalue(self) -> None: ...
    def SetOperationToEigenvector(self) -> None: ...
    def SetOperationToInverse(self) -> None: ...

class vtkMeshQuality(vtkmodules.vtkCommonExecutionModel.vtkDataSetAlgorithm):
    class QualityMeasureTypes(int):
        AREA: QualityMeasureTypes
        ASPECT_FROBENIUS: QualityMeasureTypes
        ASPECT_GAMMA: QualityMeasureTypes
        ASPECT_RATIO: QualityMeasureTypes
        COLLAPSE_RATIO: QualityMeasureTypes
        CONDITION: QualityMeasureTypes
        DIAGONAL: QualityMeasureTypes
        DIMENSION: QualityMeasureTypes
        DISTORTION: QualityMeasureTypes
        EDGE_RATIO: QualityMeasureTypes
        EQUIANGLE_SKEW: QualityMeasureTypes
        EQUIVOLUME_SKEW: QualityMeasureTypes
        JACOBIAN: QualityMeasureTypes
        MAX_ANGLE: QualityMeasureTypes
        MAX_ASPECT_FROBENIUS: QualityMeasureTypes
        MAX_EDGE_RATIO: QualityMeasureTypes
        MAX_STRETCH: QualityMeasureTypes
        MEAN_ASPECT_FROBENIUS: QualityMeasureTypes
        MEAN_RATIO: QualityMeasureTypes
        MED_ASPECT_FROBENIUS: QualityMeasureTypes
        MIN_ANGLE: QualityMeasureTypes
        NODAL_JACOBIAN_RATIO: QualityMeasureTypes
        NONE: QualityMeasureTypes
        NORMALIZED_INRADIUS: QualityMeasureTypes
        ODDY: QualityMeasureTypes
        RADIUS_RATIO: QualityMeasureTypes
        RELATIVE_SIZE_SQUARED: QualityMeasureTypes
        SCALED_JACOBIAN: QualityMeasureTypes
        SHAPE: QualityMeasureTypes
        SHAPE_AND_SIZE: QualityMeasureTypes
        SHEAR: QualityMeasureTypes
        SHEAR_AND_SIZE: QualityMeasureTypes
        SKEW: QualityMeasureTypes
        SQUISH_INDEX: QualityMeasureTypes
        STRETCH: QualityMeasureTypes
        TAPER: QualityMeasureTypes
        TOTAL_QUALITY_MEASURE_TYPES: QualityMeasureTypes
        VOLUME: QualityMeasureTypes
        WARPAGE: QualityMeasureTypes
    def CompatibilityModeOff(self) -> None: ...
    def CompatibilityModeOn(self) -> None: ...
    def GetCompatibilityMode(self) -> int: ...
    def GetHexQualityMeasure(self) -> QualityMeasureTypes: ...
    def GetLinearApproximation(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetPyramidQualityMeasure(self) -> QualityMeasureTypes: ...
    def GetQuadQualityMeasure(self) -> QualityMeasureTypes: ...
    def GetRatio(self) -> int: ...
    def GetSaveCellQuality(self) -> int: ...
    def GetTetQualityMeasure(self) -> QualityMeasureTypes: ...
    def GetTriangleQualityMeasure(self) -> QualityMeasureTypes: ...
    def GetVolume(self) -> int: ...
    def GetWedgeQualityMeasure(self) -> QualityMeasureTypes: ...
    @staticmethod
    def HexCondition(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexDiagonal(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexDimension(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexDistortion(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexEdgeRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexEquiangleSkew(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexJacobian(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexMaxAspectFrobenius(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexMaxEdgeRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexMedAspectFrobenius(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexNodalJacobianRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexOddy(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexRelativeSizeSquared(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexScaledJacobian(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexShape(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexShapeAndSize(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexShear(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexShearAndSize(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexSkew(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexStretch(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexTaper(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def HexVolume(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def LinearApproximationOff(self) -> None: ...
    def LinearApproximationOn(self) -> None: ...
    def NewInstance(self) -> vtkMeshQuality: ...
    @staticmethod
    def PyramidEquiangleSkew(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def PyramidJacobian(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def PyramidScaledJacobian(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def PyramidShape(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def PyramidVolume(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadArea(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadAspectRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadCondition(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadDistortion(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadEdgeRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadEquiangleSkew(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadJacobian(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadMaxAngle(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadMaxAspectFrobenius(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadMaxEdgeRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadMedAspectFrobenius(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadMinAngle(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadOddy(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadRadiusRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadRelativeSizeSquared(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadScaledJacobian(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadShape(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadShapeAndSize(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadShear(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadShearAndSize(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadSkew(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadStretch(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadTaper(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def QuadWarpage(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    def RatioOff(self) -> None: ...
    def RatioOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMeshQuality: ...
    def SaveCellQualityOff(self) -> None: ...
    def SaveCellQualityOn(self) -> None: ...
    def SetCompatibilityMode(self, cm: int) -> None: ...
    @overload
    def SetHexQualityMeasure(self, _arg: QualityMeasureTypes) -> None: ...
    @overload
    def SetHexQualityMeasure(self, measure: int) -> None: ...
    def SetHexQualityMeasureToCondition(self) -> None: ...
    def SetHexQualityMeasureToDiagonal(self) -> None: ...
    def SetHexQualityMeasureToDimension(self) -> None: ...
    def SetHexQualityMeasureToDistortion(self) -> None: ...
    def SetHexQualityMeasureToEdgeRatio(self) -> None: ...
    def SetHexQualityMeasureToEquiangleSkew(self) -> None: ...
    def SetHexQualityMeasureToJacobian(self) -> None: ...
    def SetHexQualityMeasureToMaxAspectFrobenius(self) -> None: ...
    def SetHexQualityMeasureToMaxEdgeRatio(self) -> None: ...
    def SetHexQualityMeasureToMedAspectFrobenius(self) -> None: ...
    def SetHexQualityMeasureToNodalJacobianRatio(self) -> None: ...
    def SetHexQualityMeasureToOddy(self) -> None: ...
    def SetHexQualityMeasureToRelativeSizeSquared(self) -> None: ...
    def SetHexQualityMeasureToScaledJacobian(self) -> None: ...
    def SetHexQualityMeasureToShape(self) -> None: ...
    def SetHexQualityMeasureToShapeAndSize(self) -> None: ...
    def SetHexQualityMeasureToShear(self) -> None: ...
    def SetHexQualityMeasureToShearAndSize(self) -> None: ...
    def SetHexQualityMeasureToSkew(self) -> None: ...
    def SetHexQualityMeasureToStretch(self) -> None: ...
    def SetHexQualityMeasureToTaper(self) -> None: ...
    def SetHexQualityMeasureToVolume(self) -> None: ...
    def SetLinearApproximation(self, _arg: bool) -> None: ...
    @overload
    def SetPyramidQualityMeasure(self, _arg: QualityMeasureTypes) -> None: ...
    @overload
    def SetPyramidQualityMeasure(self, measure: int) -> None: ...
    def SetPyramidQualityMeasureToEquiangleSkew(self) -> None: ...
    def SetPyramidQualityMeasureToJacobian(self) -> None: ...
    def SetPyramidQualityMeasureToScaledJacobian(self) -> None: ...
    def SetPyramidQualityMeasureToShape(self) -> None: ...
    def SetPyramidQualityMeasureToVolume(self) -> None: ...
    @overload
    def SetQuadQualityMeasure(self, _arg: QualityMeasureTypes) -> None: ...
    @overload
    def SetQuadQualityMeasure(self, measure: int) -> None: ...
    def SetQuadQualityMeasureToArea(self) -> None: ...
    def SetQuadQualityMeasureToAspectRatio(self) -> None: ...
    def SetQuadQualityMeasureToCondition(self) -> None: ...
    def SetQuadQualityMeasureToDistortion(self) -> None: ...
    def SetQuadQualityMeasureToEdgeRatio(self) -> None: ...
    def SetQuadQualityMeasureToEquiangleSkew(self) -> None: ...
    def SetQuadQualityMeasureToJacobian(self) -> None: ...
    def SetQuadQualityMeasureToMaxAngle(self) -> None: ...
    def SetQuadQualityMeasureToMaxAspectFrobenius(self) -> None: ...
    def SetQuadQualityMeasureToMaxEdgeRatio(self) -> None: ...
    def SetQuadQualityMeasureToMedAspectFrobenius(self) -> None: ...
    def SetQuadQualityMeasureToMinAngle(self) -> None: ...
    def SetQuadQualityMeasureToOddy(self) -> None: ...
    def SetQuadQualityMeasureToRadiusRatio(self) -> None: ...
    def SetQuadQualityMeasureToRelativeSizeSquared(self) -> None: ...
    def SetQuadQualityMeasureToScaledJacobian(self) -> None: ...
    def SetQuadQualityMeasureToShape(self) -> None: ...
    def SetQuadQualityMeasureToShapeAndSize(self) -> None: ...
    def SetQuadQualityMeasureToShear(self) -> None: ...
    def SetQuadQualityMeasureToShearAndSize(self) -> None: ...
    def SetQuadQualityMeasureToSkew(self) -> None: ...
    def SetQuadQualityMeasureToStretch(self) -> None: ...
    def SetQuadQualityMeasureToTaper(self) -> None: ...
    def SetQuadQualityMeasureToWarpage(self) -> None: ...
    def SetRatio(self, r: int) -> None: ...
    def SetSaveCellQuality(self, _arg: int) -> None: ...
    @overload
    def SetTetQualityMeasure(self, _arg: QualityMeasureTypes) -> None: ...
    @overload
    def SetTetQualityMeasure(self, measure: int) -> None: ...
    def SetTetQualityMeasureToAspectFrobenius(self) -> None: ...
    def SetTetQualityMeasureToAspectGamma(self) -> None: ...
    def SetTetQualityMeasureToAspectRatio(self) -> None: ...
    def SetTetQualityMeasureToCollapseRatio(self) -> None: ...
    def SetTetQualityMeasureToCondition(self) -> None: ...
    def SetTetQualityMeasureToDistortion(self) -> None: ...
    def SetTetQualityMeasureToEdgeRatio(self) -> None: ...
    def SetTetQualityMeasureToEquiangleSkew(self) -> None: ...
    def SetTetQualityMeasureToEquivolumeSkew(self) -> None: ...
    def SetTetQualityMeasureToJacobian(self) -> None: ...
    def SetTetQualityMeasureToMeanRatio(self) -> None: ...
    def SetTetQualityMeasureToMinAngle(self) -> None: ...
    def SetTetQualityMeasureToNormalizedInradius(self) -> None: ...
    def SetTetQualityMeasureToRadiusRatio(self) -> None: ...
    def SetTetQualityMeasureToRelativeSizeSquared(self) -> None: ...
    def SetTetQualityMeasureToScaledJacobian(self) -> None: ...
    def SetTetQualityMeasureToShape(self) -> None: ...
    def SetTetQualityMeasureToShapeAndSize(self) -> None: ...
    def SetTetQualityMeasureToSquishIndex(self) -> None: ...
    def SetTetQualityMeasureToVolume(self) -> None: ...
    @overload
    def SetTriangleQualityMeasure(self, _arg: QualityMeasureTypes) -> None: ...
    @overload
    def SetTriangleQualityMeasure(self, measure: int) -> None: ...
    def SetTriangleQualityMeasureToArea(self) -> None: ...
    def SetTriangleQualityMeasureToAspectFrobenius(self) -> None: ...
    def SetTriangleQualityMeasureToAspectRatio(self) -> None: ...
    def SetTriangleQualityMeasureToCondition(self) -> None: ...
    def SetTriangleQualityMeasureToDistortion(self) -> None: ...
    def SetTriangleQualityMeasureToEdgeRatio(self) -> None: ...
    def SetTriangleQualityMeasureToEquiangleSkew(self) -> None: ...
    def SetTriangleQualityMeasureToMaxAngle(self) -> None: ...
    def SetTriangleQualityMeasureToMinAngle(self) -> None: ...
    def SetTriangleQualityMeasureToNormalizedInradius(self) -> None: ...
    def SetTriangleQualityMeasureToRadiusRatio(self) -> None: ...
    def SetTriangleQualityMeasureToRelativeSizeSquared(self) -> None: ...
    def SetTriangleQualityMeasureToScaledJacobian(self) -> None: ...
    def SetTriangleQualityMeasureToShape(self) -> None: ...
    def SetTriangleQualityMeasureToShapeAndSize(self) -> None: ...
    def SetVolume(self, cv: int) -> None: ...
    @overload
    def SetWedgeQualityMeasure(self, _arg: QualityMeasureTypes) -> None: ...
    @overload
    def SetWedgeQualityMeasure(self, measure: int) -> None: ...
    def SetWedgeQualityMeasureToCondition(self) -> None: ...
    def SetWedgeQualityMeasureToDistortion(self) -> None: ...
    def SetWedgeQualityMeasureToEdgeRatio(self) -> None: ...
    def SetWedgeQualityMeasureToEquiangleSkew(self) -> None: ...
    def SetWedgeQualityMeasureToJacobian(self) -> None: ...
    def SetWedgeQualityMeasureToMaxAspectFrobenius(self) -> None: ...
    def SetWedgeQualityMeasureToMaxStretch(self) -> None: ...
    def SetWedgeQualityMeasureToMeanAspectFrobenius(self) -> None: ...
    def SetWedgeQualityMeasureToScaledJacobian(self) -> None: ...
    def SetWedgeQualityMeasureToShape(self) -> None: ...
    def SetWedgeQualityMeasureToVolume(self) -> None: ...
    @staticmethod
    def TetAspectFrobenius(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetAspectGamma(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetAspectRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetCollapseRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetCondition(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetDistortion(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetEdgeRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetEquiangleSkew(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetEquivolumeSkew(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetJacobian(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetMeanRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetMinAngle(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetNormalizedInradius(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetRadiusRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetRelativeSizeSquared(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetScaledJacobian(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetShape(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetShapeAndSize(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetSquishIndex(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TetVolume(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleArea(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleAspectFrobenius(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleAspectRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleCondition(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleDistortion(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleEdgeRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleEquiangleSkew(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleMaxAngle(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleMinAngle(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleNormalizedInradius(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleRadiusRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleRelativeSizeSquared(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleScaledJacobian(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleShape(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def TriangleShapeAndSize(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    def VolumeOff(self) -> None: ...
    def VolumeOn(self) -> None: ...
    @staticmethod
    def WedgeCondition(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def WedgeDistortion(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def WedgeEdgeRatio(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def WedgeEquiangleSkew(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def WedgeJacobian(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def WedgeMaxAspectFrobenius(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def WedgeMaxStretch(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def WedgeMeanAspectFrobenius(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def WedgeScaledJacobian(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def WedgeShape(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
    @staticmethod
    def WedgeVolume(cell: vtkmodules.vtkCommonDataModel.vtkCell) -> float: ...
