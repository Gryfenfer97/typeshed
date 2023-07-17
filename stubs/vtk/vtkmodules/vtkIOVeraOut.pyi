import vtkmodules.vtkCommonCore
import vtkmodules.vtkCommonExecutionModel

class vtkVeraOutReader(vtkmodules.vtkCommonExecutionModel.vtkRectilinearGridAlgorithm):
    def GetCellDataArraySelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetFieldDataArraySelection(self) -> vtkmodules.vtkCommonCore.vtkDataArraySelection: ...
    def GetFileName(self) -> str: ...
    def GetMTime(self) -> int: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkVeraOutReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkVeraOutReader: ...
    def SetFileName(self, _arg: str) -> None: ...
