from collections.abc import Callable, Sequence
from typing import Tuple, TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkParallelCore

Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkIOSSReader(vtkmodules.vtkCommonExecutionModel.vtkReaderAlgorithm):
    class EntityType(int): ...
    BLOCK_END: EntityType
    BLOCK_START: EntityType
    EDGEBLOCK: EntityType
    EDGESET: EntityType
    ELEMENTBLOCK: EntityType
    ELEMENTSET: EntityType
    ENTITY_END: EntityType
    ENTITY_START: EntityType
    FACEBLOCK: EntityType
    FACESET: EntityType
    NODEBLOCK: EntityType
    NODESET: EntityType
    NUMBER_OF_ENTITY_TYPES: EntityType
    SET_END: EntityType
    SET_START: EntityType
    SIDESET: EntityType
    STRUCTUREDBLOCK: EntityType
    def AddFileName(self, fname: str) -> None: ...
    @overload
    def AddProperty(self, name: str, value: int) -> None: ...
    @overload
    def AddProperty(self, name: str, value: float) -> None: ...
    @overload
    def AddProperty(self, name: str, value: Pointer) -> None: ...
    @overload
    def AddProperty(self, name: str, value: str) -> None: ...
    def AddSelector(self, selector: str) -> bool: ...
    def ApplyDisplacementsOff(self) -> None: ...
    def ApplyDisplacementsOn(self) -> None: ...
    def ClearFileNames(self) -> None: ...
    def ClearProperties(self) -> None: ...
    def ClearSelectors(self) -> None: ...
    @staticmethod
    def DoTestFilePatternMatching() -> bool: ...
    def GenerateFileIdOff(self) -> None: ...
    def GenerateFileIdOn(self) -> None: ...
    def GetApplyDisplacements(self) -> bool: ...
    def GetAssembly(self) -> vtkmodules.vtkCommonDataModel.vtkDataAssembly: ...
    def GetAssemblyTag(self) -> int: ...
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    @staticmethod
    def GetDataAssemblyNodeNameForEntityType(type: int) -> str: ...
    def GetDatabaseTypeOverride(self) -> str: ...
    def GetDisplacementMagnitude(self) -> float: ...
    def GetEdgeBlockFieldSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetEdgeBlockIdMapAsString(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetEdgeBlockSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetEdgeSetFieldSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetEdgeSetIdMapAsString(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetEdgeSetSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetElementBlockFieldSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetElementBlockIdMapAsString(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetElementBlockSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetElementSetFieldSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetElementSetIdMapAsString(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetElementSetSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetEntityIdMapAsString(self, type: int) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetEntitySelection(self, type: int) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    @staticmethod
    def GetEntityTypeIsBlock(type: int) -> bool: ...
    @staticmethod
    def GetEntityTypeIsSet(type: int) -> bool: ...
    def GetFaceBlockFieldSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetFaceBlockIdMapAsString(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetFaceBlockSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetFaceSetFieldSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetFaceSetIdMapAsString(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetFaceSetSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetFieldSelection(self, type: int) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetFileName(self, index: int) -> str: ...
    def GetFileRange(self) -> Tuple[int, int]: ...
    def GetFileStride(self) -> int: ...
    def GetFileStrideMaxValue(self) -> int: ...
    def GetFileStrideMinValue(self) -> int: ...
    def GetGenerateFileId(self) -> bool: ...
    def GetMTime(self) -> int: ...
    def GetNodeBlockFieldSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetNodeBlockIdMapAsString(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetNodeBlockSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetNodeSetFieldSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetNodeSetIdMapAsString(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetNodeSetSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetNumberOfFileNames(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetNumberOfSelectors(self) -> int: ...
    def GetReadGlobalFields(self) -> bool: ...
    def GetReadIds(self) -> bool: ...
    def GetReadQAAndInformationRecords(self) -> bool: ...
    def GetRemoveUnusedPoints(self) -> bool: ...
    def GetScanForRelatedFiles(self) -> bool: ...
    def GetSelector(self, index: int) -> str: ...
    def GetSideSetFieldSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetSideSetIdMapAsString(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetSideSetSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetStructuredBlockFieldSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetStructuredBlockIdMapAsString(self) -> vtkmodules.vtkCommonCore.vtkStringArray: ...
    def GetStructuredBlockSelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkIOSSReader: ...
    def ReadArrays(self, __a: int, __b: int, __c: int, __d: int, __e: vtkmodules.vtkCommonDataModel.vtkDataObject) -> int: ...
    def ReadGlobalFieldsOff(self) -> None: ...
    def ReadGlobalFieldsOn(self) -> None: ...
    def ReadIdsOff(self) -> None: ...
    def ReadIdsOn(self) -> None: ...
    def ReadMesh(
        self, piece: int, npieces: int, nghosts: int, timestep: int, output: vtkmodules.vtkCommonDataModel.vtkDataObject
    ) -> int: ...
    def ReadMetaData(self, metadata: vtkmodules.vtkCommonCore.vtkInformation) -> int: ...
    def ReadPoints(self, __a: int, __b: int, __c: int, __d: int, __e: vtkmodules.vtkCommonDataModel.vtkDataObject) -> int: ...
    def ReadQAAndInformationRecordsOff(self) -> None: ...
    def ReadQAAndInformationRecordsOn(self) -> None: ...
    def RemoveAllEntitySelections(self) -> None: ...
    def RemoveAllFieldSelections(self) -> None: ...
    def RemoveAllSelections(self) -> None: ...
    def RemoveProperty(self, name: str) -> None: ...
    def RemoveUnusedPointsOff(self) -> None: ...
    def RemoveUnusedPointsOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkIOSSReader: ...
    def ScanForRelatedFilesOff(self) -> None: ...
    def ScanForRelatedFilesOn(self) -> None: ...
    def SetApplyDisplacements(self, _arg: bool) -> None: ...
    def SetController(self, controller: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def SetDatabaseTypeOverride(self, _arg: str) -> None: ...
    def SetDisplacementMagnitude(self, magnitude: float) -> None: ...
    def SetFileName(self, fname: str) -> None: ...
    @overload
    def SetFileRange(self, _arg1: int, _arg2: int) -> None: ...
    @overload
    def SetFileRange(self, _arg: Sequence[int]) -> None: ...
    def SetFileStride(self, _arg: int) -> None: ...
    def SetGenerateFileId(self, _arg: bool) -> None: ...
    def SetReadGlobalFields(self, _arg: bool) -> None: ...
    def SetReadIds(self, _arg: bool) -> None: ...
    def SetReadQAAndInformationRecords(self, _arg: bool) -> None: ...
    def SetRemoveUnusedPoints(self, __a: bool) -> None: ...
    def SetScanForRelatedFiles(self, value: bool) -> None: ...
    def SetSelector(self, selector: str) -> None: ...

class vtkIOSSWriter(vtkmodules.vtkCommonExecutionModel.vtkDataObjectAlgorithm):
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetDisplacementMagnitude(self) -> float: ...
    def GetDisplacementMagnitudeMaxValue(self) -> float: ...
    def GetDisplacementMagnitudeMinValue(self) -> float: ...
    def GetFileName(self) -> str: ...
    def GetMaximumTimeStepsPerFile(self) -> int: ...
    def GetMaximumTimeStepsPerFileMaxValue(self) -> int: ...
    def GetMaximumTimeStepsPerFileMinValue(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOffsetGlobalIds(self) -> bool: ...
    def GetPreserveInputEntityGroups(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkIOSSWriter: ...
    def OffsetGlobalIdsOff(self) -> None: ...
    def OffsetGlobalIdsOn(self) -> None: ...
    def PreserveInputEntityGroupsOff(self) -> None: ...
    def PreserveInputEntityGroupsOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkIOSSWriter: ...
    def SetController(self, controller: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
    def SetDisplacementMagnitude(self, _arg: float) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetMaximumTimeStepsPerFile(self, _arg: int) -> None: ...
    def SetOffsetGlobalIds(self, _arg: bool) -> None: ...
    def SetPreserveInputEntityGroups(self, _arg: bool) -> None: ...
    def Write(self) -> bool: ...
