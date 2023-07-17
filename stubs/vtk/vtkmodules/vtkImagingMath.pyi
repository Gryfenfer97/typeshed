from collections.abc import Callable, Sequence
from typing import Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

VTK_ABS: int
VTK_ADD: int
VTK_ADDC: int
VTK_AND: int
VTK_ATAN: int
VTK_ATAN2: int
VTK_COMPLEX_MULTIPLY: int
VTK_CONJUGATE: int
VTK_COS: int
VTK_DIVIDE: int
VTK_EXP: int
VTK_INVERT: int
VTK_LOG: int
VTK_MAX: int
VTK_MIN: int
VTK_MULTIPLY: int
VTK_MULTIPLYBYK: int
VTK_NAND: int
VTK_NOP: int
VTK_NOR: int
VTK_NOT: int
VTK_OR: int
VTK_REPLACECBYK: int
VTK_SIN: int
VTK_SQR: int
VTK_SQRT: int
VTK_SUBTRACT: int
VTK_XOR: int

class vtkImageDivergence(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageDivergence: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageDivergence: ...

class vtkImageDotProduct(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageDotProduct: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageDotProduct: ...
    def SetInput1Data(self, in_: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetInput2Data(self, in_: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...

class vtkImageLogarithmicScale(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetConstant(self) -> float: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageLogarithmicScale: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageLogarithmicScale: ...
    def SetConstant(self, _arg: float) -> None: ...

class vtkImageLogic(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOperation(self) -> int: ...
    def GetOutputTrueValue(self) -> float: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageLogic: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageLogic: ...
    def SetInput1Data(self, input: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetInput2Data(self, input: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetOperation(self, _arg: int) -> None: ...
    def SetOperationToAnd(self) -> None: ...
    def SetOperationToNand(self) -> None: ...
    def SetOperationToNor(self) -> None: ...
    def SetOperationToNot(self) -> None: ...
    def SetOperationToOr(self) -> None: ...
    def SetOperationToXor(self) -> None: ...
    def SetOutputTrueValue(self, _arg: float) -> None: ...

class vtkImageMagnitude(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageMagnitude: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageMagnitude: ...

class vtkImageMaskBits(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def GetMasks(self) -> Tuple[int, int, int, int]: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOperation(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageMaskBits: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageMaskBits: ...
    def SetMask(self, mask: int) -> None: ...
    @overload
    def SetMasks(self, _arg1: int, _arg2: int, _arg3: int, _arg4: int) -> None: ...
    @overload
    def SetMasks(self, _arg: Sequence[int]) -> None: ...
    @overload
    def SetMasks(self, mask1: int, mask2: int) -> None: ...
    @overload
    def SetMasks(self, mask1: int, mask2: int, mask3: int) -> None: ...
    def SetOperation(self, _arg: int) -> None: ...
    def SetOperationToAnd(self) -> None: ...
    def SetOperationToNand(self) -> None: ...
    def SetOperationToNor(self) -> None: ...
    def SetOperationToOr(self) -> None: ...
    def SetOperationToXor(self) -> None: ...

class vtkImageMathematics(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def DivideByZeroToCOff(self) -> None: ...
    def DivideByZeroToCOn(self) -> None: ...
    def GetConstantC(self) -> float: ...
    def GetConstantK(self) -> float: ...
    def GetDivideByZeroToC(self) -> int: ...
    @overload
    def GetInput(self, idx: int) -> vtkmodules.vtkCommonDataModel.vtkDataObject: ...
    @overload
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkDataObject: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfInputs(self) -> int: ...
    def GetOperation(self) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageMathematics: ...
    def ReplaceNthInputConnection(self, idx: int, input: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageMathematics: ...
    def SetConstantC(self, _arg: float) -> None: ...
    def SetConstantK(self, _arg: float) -> None: ...
    def SetDivideByZeroToC(self, _arg: int) -> None: ...
    def SetInput1Data(self, in_: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetInput2Data(self, in_: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    @overload
    def SetInputConnection(self, idx: int, input: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    @overload
    def SetInputConnection(self, input: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    @overload
    def SetInputData(self, idx: int, input: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    @overload
    def SetInputData(self, input: vtkmodules.vtkCommonDataModel.vtkDataObject) -> None: ...
    def SetOperation(self, _arg: int) -> None: ...
    def SetOperationToATAN(self) -> None: ...
    def SetOperationToATAN2(self) -> None: ...
    def SetOperationToAbsoluteValue(self) -> None: ...
    def SetOperationToAdd(self) -> None: ...
    def SetOperationToAddConstant(self) -> None: ...
    def SetOperationToComplexMultiply(self) -> None: ...
    def SetOperationToConjugate(self) -> None: ...
    def SetOperationToCos(self) -> None: ...
    def SetOperationToDivide(self) -> None: ...
    def SetOperationToExp(self) -> None: ...
    def SetOperationToInvert(self) -> None: ...
    def SetOperationToLog(self) -> None: ...
    def SetOperationToMax(self) -> None: ...
    def SetOperationToMin(self) -> None: ...
    def SetOperationToMultiply(self) -> None: ...
    def SetOperationToMultiplyByK(self) -> None: ...
    def SetOperationToReplaceCByK(self) -> None: ...
    def SetOperationToSin(self) -> None: ...
    def SetOperationToSquare(self) -> None: ...
    def SetOperationToSquareRoot(self) -> None: ...
    def SetOperationToSubtract(self) -> None: ...

class vtkImageWeightedSum(vtkmodules.vtkCommonExecutionModel.vtkThreadedImageAlgorithm):
    def CalculateTotalWeight(self) -> float: ...
    def GetNormalizeByWeight(self) -> int: ...
    def GetNormalizeByWeightMaxValue(self) -> int: ...
    def GetNormalizeByWeightMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetWeights(self) -> vtkmodules.vtkCommonCore.vtkDoubleArray: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkImageWeightedSum: ...
    def NormalizeByWeightOff(self) -> None: ...
    def NormalizeByWeightOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkImageWeightedSum: ...
    def SetNormalizeByWeight(self, _arg: int) -> None: ...
    def SetWeight(self, id: int, weight: float) -> None: ...
    def SetWeights(self, __a: vtkmodules.vtkCommonCore.vtkDoubleArray) -> None: ...
