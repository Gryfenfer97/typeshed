from collections.abc import Callable
from typing import TypeVar, Union, overload

import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonDataModel
import vtkmodules.vtkCommonExecutionModel
import vtkmodules.vtkIOLegacy
import vtkmodules.vtkIOXML

Buffer = TypeVar("Buffer")
Pointer = TypeVar("Pointer")
Template = TypeVar("Template")

class vtkBiomTableReader(vtkmodules.vtkIOLegacy.vtkTableReader):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @overload
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkTable: ...
    @overload
    def GetOutput(self, idx: int) -> vtkmodules.vtkCommonDataModel.vtkTable: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkBiomTableReader: ...
    def ReadMeshSimple(self, fname: str, output: vtkmodules.vtkCommonDataModel.vtkDataObject) -> int: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkBiomTableReader: ...
    def SetOutput(self, output: vtkmodules.vtkCommonDataModel.vtkTable) -> None: ...

class vtkChacoGraphReader(vtkmodules.vtkCommonExecutionModel.vtkUndirectedGraphAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkChacoGraphReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkChacoGraphReader: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkDIMACSGraphReader(vtkmodules.vtkCommonExecutionModel.vtkGraphAlgorithm):
    def GetEdgeAttributeArrayName(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetVertexAttributeArrayName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkDIMACSGraphReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDIMACSGraphReader: ...
    def SetEdgeAttributeArrayName(self, _arg: str) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetVertexAttributeArrayName(self, _arg: str) -> None: ...

class vtkDIMACSGraphWriter(vtkmodules.vtkIOLegacy.vtkDataWriter):
    @overload
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkGraph: ...
    @overload
    def GetInput(self, port: int) -> vtkmodules.vtkCommonDataModel.vtkGraph: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkDIMACSGraphWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDIMACSGraphWriter: ...

class vtkDelimitedTextReader(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    def AddTabFieldDelimiterOff(self) -> None: ...
    def AddTabFieldDelimiterOn(self) -> None: ...
    def DetectNumericColumnsOff(self) -> None: ...
    def DetectNumericColumnsOn(self) -> None: ...
    def ForceDoubleOff(self) -> None: ...
    def ForceDoubleOn(self) -> None: ...
    def GeneratePedigreeIdsOff(self) -> None: ...
    def GeneratePedigreeIdsOn(self) -> None: ...
    def GetAddTabFieldDelimiter(self) -> bool: ...
    def GetDefaultDoubleValue(self) -> float: ...
    def GetDefaultIntegerValue(self) -> int: ...
    def GetDetectNumericColumns(self) -> bool: ...
    def GetFieldDelimiterCharacters(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetForceDouble(self) -> bool: ...
    def GetGeneratePedigreeIds(self) -> bool: ...
    def GetHaveHeaders(self) -> bool: ...
    def GetInputString(self) -> str: ...
    def GetInputStringLength(self) -> int: ...
    def GetLastError(self) -> str: ...
    def GetMaxRecords(self) -> int: ...
    def GetMergeConsecutiveDelimiters(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetOutputPedigreeIds(self) -> bool: ...
    def GetPedigreeIdArrayName(self) -> str: ...
    def GetReadFromInputString(self) -> int: ...
    def GetReplacementCharacter(self) -> int: ...
    def GetStringDelimiter(self) -> str: ...
    def GetTrimWhitespacePriorToNumericConversion(self) -> bool: ...
    def GetUTF8FieldDelimiters(self) -> str: ...
    def GetUTF8RecordDelimiters(self) -> str: ...
    def GetUTF8StringDelimiters(self) -> str: ...
    def GetUnicodeCharacterSet(self) -> str: ...
    def GetUseStringDelimiter(self) -> bool: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MergeConsecutiveDelimitersOff(self) -> None: ...
    def MergeConsecutiveDelimitersOn(self) -> None: ...
    def NewInstance(self) -> vtkDelimitedTextReader: ...
    def OutputPedigreeIdsOff(self) -> None: ...
    def OutputPedigreeIdsOn(self) -> None: ...
    def ReadFromInputStringOff(self) -> None: ...
    def ReadFromInputStringOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkDelimitedTextReader: ...
    def SetAddTabFieldDelimiter(self, _arg: bool) -> None: ...
    def SetDefaultDoubleValue(self, _arg: float) -> None: ...
    def SetDefaultIntegerValue(self, _arg: int) -> None: ...
    def SetDetectNumericColumns(self, _arg: bool) -> None: ...
    def SetFieldDelimiterCharacters(self, _arg: str) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetForceDouble(self, _arg: bool) -> None: ...
    def SetGeneratePedigreeIds(self, _arg: bool) -> None: ...
    def SetHaveHeaders(self, _arg: bool) -> None: ...
    @overload
    def SetInputString(self, in_: str, len: int) -> None: ...
    @overload
    def SetInputString(self, input: str) -> None: ...
    def SetMaxRecords(self, _arg: int) -> None: ...
    def SetMergeConsecutiveDelimiters(self, _arg: bool) -> None: ...
    def SetOutputPedigreeIds(self, _arg: bool) -> None: ...
    def SetPedigreeIdArrayName(self, _arg: str) -> None: ...
    def SetReadFromInputString(self, _arg: int) -> None: ...
    def SetReplacementCharacter(self, _arg: int) -> None: ...
    def SetStringDelimiter(self, _arg: str) -> None: ...
    def SetTrimWhitespacePriorToNumericConversion(self, _arg: bool) -> None: ...
    def SetUTF8FieldDelimiters(self, delimiters: str) -> None: ...
    def SetUTF8RecordDelimiters(self, delimiters: str) -> None: ...
    def SetUTF8StringDelimiters(self, delimiters: str) -> None: ...
    def SetUnicodeCharacterSet(self, _arg: str) -> None: ...
    def SetUseStringDelimiter(self, _arg: bool) -> None: ...
    def TrimWhitespacePriorToNumericConversionOff(self) -> None: ...
    def TrimWhitespacePriorToNumericConversionOn(self) -> None: ...
    def UseStringDelimiterOff(self) -> None: ...
    def UseStringDelimiterOn(self) -> None: ...

class vtkFixedWidthTextReader(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    def GetFieldWidth(self) -> int: ...
    def GetFileName(self) -> str: ...
    def GetHaveHeaders(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetStripWhiteSpace(self) -> bool: ...
    def GetTableErrorObserver(self) -> vtkmodules.vtkCommonCore.vtkCommand: ...
    def HaveHeadersOff(self) -> None: ...
    def HaveHeadersOn(self) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkFixedWidthTextReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkFixedWidthTextReader: ...
    def SetFieldWidth(self, _arg: int) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetHaveHeaders(self, _arg: bool) -> None: ...
    def SetStripWhiteSpace(self, _arg: bool) -> None: ...
    def SetTableErrorObserver(self, __a: vtkmodules.vtkCommonCore.vtkCommand) -> None: ...
    def StripWhiteSpaceOff(self) -> None: ...
    def StripWhiteSpaceOn(self) -> None: ...

class vtkISIReader(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    def GetDelimiter(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetMaxRecords(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkISIReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkISIReader: ...
    def SetDelimiter(self, _arg: str) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetMaxRecords(self, _arg: int) -> None: ...

class vtkMultiNewickTreeReader(vtkmodules.vtkIOLegacy.vtkDataReader):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @overload
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkMultiPieceDataSet: ...
    @overload
    def GetOutput(self, idx: int) -> vtkmodules.vtkCommonDataModel.vtkMultiPieceDataSet: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkMultiNewickTreeReader: ...
    def ReadMeshSimple(self, fname: str, output: vtkmodules.vtkCommonDataModel.vtkDataObject) -> int: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkMultiNewickTreeReader: ...
    def SetOutput(self, output: vtkmodules.vtkCommonDataModel.vtkMultiPieceDataSet) -> None: ...

class vtkNewickTreeReader(vtkmodules.vtkIOLegacy.vtkDataReader):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @overload
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkTree: ...
    @overload
    def GetOutput(self, idx: int) -> vtkmodules.vtkCommonDataModel.vtkTree: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkNewickTreeReader: ...
    def ReadMeshSimple(self, fname: str, output: vtkmodules.vtkCommonDataModel.vtkDataObject) -> int: ...
    def ReadNewickTree(self, buffer: str, tree: vtkmodules.vtkCommonDataModel.vtkTree) -> int: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkNewickTreeReader: ...
    def SetOutput(self, output: vtkmodules.vtkCommonDataModel.vtkTree) -> None: ...

class vtkNewickTreeWriter(vtkmodules.vtkIOLegacy.vtkDataWriter):
    def GetEdgeWeightArrayName(self) -> str: ...
    @overload
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkTree: ...
    @overload
    def GetInput(self, port: int) -> vtkmodules.vtkCommonDataModel.vtkTree: ...
    def GetNodeNameArrayName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkNewickTreeWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkNewickTreeWriter: ...
    def SetEdgeWeightArrayName(self, _arg: str) -> None: ...
    def SetNodeNameArrayName(self, _arg: str) -> None: ...

class vtkPhyloXMLTreeReader(vtkmodules.vtkIOXML.vtkXMLReader):
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    @overload
    def GetOutput(self) -> vtkmodules.vtkCommonDataModel.vtkTree: ...
    @overload
    def GetOutput(self, idx: int) -> vtkmodules.vtkCommonDataModel.vtkTree: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPhyloXMLTreeReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPhyloXMLTreeReader: ...

class vtkPhyloXMLTreeWriter(vtkmodules.vtkIOXML.vtkXMLWriter):
    def GetDefaultFileExtension(self) -> str: ...
    def GetEdgeWeightArrayName(self) -> str: ...
    @overload
    def GetInput(self) -> vtkmodules.vtkCommonDataModel.vtkTree: ...
    @overload
    def GetInput(self, port: int) -> vtkmodules.vtkCommonDataModel.vtkTree: ...
    def GetNodeNameArrayName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IgnoreArray(self, arrayName: str) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPhyloXMLTreeWriter: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPhyloXMLTreeWriter: ...
    def SetEdgeWeightArrayName(self, _arg: str) -> None: ...
    def SetNodeNameArrayName(self, _arg: str) -> None: ...

class vtkRISReader(vtkmodules.vtkCommonExecutionModel.vtkTableAlgorithm):
    def GetDelimiter(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetMaxRecords(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkRISReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkRISReader: ...
    def SetDelimiter(self, _arg: str) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetMaxRecords(self, _arg: int) -> None: ...

class vtkTemporalDelimitedTextReader(vtkDelimitedTextReader):
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetRemoveTimeStepColumn(self) -> bool: ...
    def GetTimeColumnId(self) -> int: ...
    def GetTimeColumnName(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTemporalDelimitedTextReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTemporalDelimitedTextReader: ...
    def SetRemoveTimeStepColumn(self, rts: bool) -> None: ...
    def SetTimeColumnId(self, idx: int) -> None: ...
    def SetTimeColumnName(self, name: str) -> None: ...

class vtkTulipReader(vtkmodules.vtkCommonExecutionModel.vtkUndirectedGraphAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkTulipReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkTulipReader: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkXGMLReader(vtkmodules.vtkCommonExecutionModel.vtkUndirectedGraphAlgorithm):
    def GetFileName(self) -> str: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkXGMLReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkXGMLReader: ...
    def SetFileName(self, _arg: str) -> None: ...

class vtkXMLTreeReader(vtkmodules.vtkCommonExecutionModel.vtkTreeAlgorithm):
    def GenerateEdgePedigreeIdsOff(self) -> None: ...
    def GenerateEdgePedigreeIdsOn(self) -> None: ...
    def GenerateVertexPedigreeIdsOff(self) -> None: ...
    def GenerateVertexPedigreeIdsOn(self) -> None: ...
    def GetEdgePedigreeIdArrayName(self) -> str: ...
    def GetFileName(self) -> str: ...
    def GetGenerateEdgePedigreeIds(self) -> bool: ...
    def GetGenerateVertexPedigreeIds(self) -> bool: ...
    def GetMaskArrays(self) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def GetReadCharData(self) -> bool: ...
    def GetReadTagName(self) -> bool: ...
    def GetVertexPedigreeIdArrayName(self) -> str: ...
    def GetXMLString(self) -> str: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def MaskArraysOff(self) -> None: ...
    def MaskArraysOn(self) -> None: ...
    def NewInstance(self) -> vtkXMLTreeReader: ...
    def ReadCharDataOff(self) -> None: ...
    def ReadCharDataOn(self) -> None: ...
    def ReadTagNameOff(self) -> None: ...
    def ReadTagNameOn(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkXMLTreeReader: ...
    def SetEdgePedigreeIdArrayName(self, _arg: str) -> None: ...
    def SetFileName(self, _arg: str) -> None: ...
    def SetGenerateEdgePedigreeIds(self, _arg: bool) -> None: ...
    def SetGenerateVertexPedigreeIds(self, _arg: bool) -> None: ...
    def SetMaskArrays(self, _arg: bool) -> None: ...
    def SetReadCharData(self, _arg: bool) -> None: ...
    def SetReadTagName(self, _arg: bool) -> None: ...
    def SetVertexPedigreeIdArrayName(self, _arg: str) -> None: ...
    def SetXMLString(self, _arg: str) -> None: ...
