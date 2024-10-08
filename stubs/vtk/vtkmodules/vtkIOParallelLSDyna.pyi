import vtkmodules.vtkCommonCore
import vtkmodules.vtkIOLSDyna
import vtkmodules.vtkParallelCore

class vtkPLSDynaReader(vtkmodules.vtkIOLSDyna.vtkLSDynaReader):
    def CanReadFile(self, fname: str) -> int: ...
    def GetController(self) -> vtkmodules.vtkParallelCore.vtkMultiProcessController: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPLSDynaReader: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPLSDynaReader: ...
    def SetController(self, c: vtkmodules.vtkParallelCore.vtkMultiProcessController) -> None: ...
