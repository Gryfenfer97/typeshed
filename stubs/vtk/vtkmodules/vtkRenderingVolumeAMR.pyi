from collections.abc import Callable, MutableSequence, Sequence
from typing import Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkRenderingCore
import vtkmodules.vtkRenderingVolume

Callback = Union[Callable[..., None], None]
Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkAMRVolumeMapper(vtkmodules.vtkRenderingVolume.vtkVolumeMapper):
    DefaultRenderMode: int
    GPURenderMode: int
    InvalidRenderMode: int
    RayCastAndTextureRenderMode: int
    RayCastRenderMode: int
    TextureRenderMode: int
    UndefinedRenderMode: int

    @staticmethod
    def ComputeResamplerBoundsFrustumMethod(
        camera: vtkmodules.vtkRenderingCore.vtkCamera,
        renderer: vtkmodules.vtkRenderingCore.vtkRenderer,
        data_bounds: Sequence[float],
        out_bounds: MutableSequence[float],
    ) -> bool: ...
    def GetArrayAccessMode(self) -> int: ...
    def GetArrayId(self) -> int: ...
    def GetArrayName(self) -> str: ...
    def GetBlendMode(self) -> int: ...
    @overload
    def GetBounds(self) -> Tuple[float, float, float, float, float, float]: ...
    @overload
    def GetBounds(self, bounds: MutableSequence[float]) -> None: ...
    def GetCropping(self) -> int: ...
    def GetCroppingRegionFlags(self) -> int: ...
    @overload
    def GetCroppingRegionPlanes(self, planes: MutableSequence[float]) -> None: ...
    @overload
    def GetCroppingRegionPlanes(self) -> Tuple[float, float, float, float, float, float]: ...
    def GetFreezeFocalPoint(self) -> bool: ...
    def GetInterpolationMode(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfSamples(self) -> Tuple[int, int, int]: ...
    def GetRequestedRenderMode(self) -> int: ...
    def GetRequestedResamplingMode(self) -> int: ...
    def GetResamplerUpdateTolerance(self) -> float: ...
    def GetScalarModeAsString(self) -> str: ...
    def GetUseDefaultThreading(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkAMRVolumeMapper: ...
    def ReleaseGraphicsResources(self, __a: vtkmodules.vtkCommonCore.vtkWindow) -> None: ...
    def Render(self, ren: vtkmodules.vtkRenderingCore.vtkRenderer, vol: vtkmodules.vtkRenderingCore.vtkVolume) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkAMRVolumeMapper: ...
    @overload
    def SelectScalarArray(self, arrayNum: int) -> None: ...
    @overload
    def SelectScalarArray(self, arrayName: str) -> None: ...
    def SetBlendMode(self, mode: int) -> None: ...
    def SetCropping(self, __a: int) -> None: ...
    def SetCroppingRegionFlags(self, mode: int) -> None: ...
    @overload
    def SetCroppingRegionPlanes(self, arg1: float, arg2: float, arg3: float, arg4: float, arg5: float, arg6: float) -> None: ...
    @overload
    def SetCroppingRegionPlanes(self, planes: Sequence[float]) -> None: ...
    def SetFreezeFocalPoint(self, _arg: bool) -> None: ...
    @overload
    def SetInputConnection(self, port: int, input: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    @overload
    def SetInputConnection(self, input: vtkmodules.vtkCommonExecutionModel.vtkAlgorithmOutput) -> None: ...
    @overload
    def SetInputData(self, __a: vtkmodules.vtkCommonDataModel.vtkImageData) -> None: ...
    @overload
    def SetInputData(self, __a: vtkmodules.vtkCommonDataModel.vtkDataSet) -> None: ...
    @overload
    def SetInputData(self, __a: vtkmodules.vtkCommonDataModel.vtkRectilinearGrid) -> None: ...
    @overload
    def SetInputData(self, __a: vtkmodules.vtkCommonDataModel.vtkOverlappingAMR) -> None: ...
    def SetInterpolationMode(self, mode: int) -> None: ...
    def SetInterpolationModeToCubic(self) -> None: ...
    def SetInterpolationModeToLinear(self) -> None: ...
    def SetInterpolationModeToNearestNeighbor(self) -> None: ...
    @overload
    def SetNumberOfSamples(self, _arg1: int, _arg2: int, _arg3: int) -> None: ...
    @overload
    def SetNumberOfSamples(self, _arg: Sequence[int]) -> None: ...
    def SetRequestedRenderMode(self, mode: int) -> None: ...
    def SetRequestedRenderModeToDefault(self) -> None: ...
    def SetRequestedRenderModeToGPU(self) -> None: ...
    def SetRequestedRenderModeToRayCast(self) -> None: ...
    def SetRequestedRenderModeToRayCastAndTexture(self) -> None: ...
    def SetRequestedRenderModeToTexture(self) -> None: ...
    def SetRequestedResamplingMode(self, _arg: int) -> None: ...
    def SetResamplerUpdateTolerance(self, _arg: float) -> None: ...
    def SetScalarMode(self, mode: int) -> None: ...
    def SetUseDefaultThreading(self, _arg: bool) -> None: ...
    def UpdateResampler(
        self, ren: vtkmodules.vtkRenderingCore.vtkRenderer, amr: vtkmodules.vtkCommonDataModel.vtkOverlappingAMR
    ) -> None: ...
    def UpdateResamplerFrustrumMethod(
        self, ren: vtkmodules.vtkRenderingCore.vtkRenderer, amr: vtkmodules.vtkCommonDataModel.vtkOverlappingAMR
    ) -> None: ...
