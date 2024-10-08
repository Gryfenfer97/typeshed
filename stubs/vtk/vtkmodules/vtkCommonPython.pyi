import vtkmodules.vtkCommonCore

class vtkPythonArchiver(vtkmodules.vtkCommonCore.vtkArchiver):
    def CloseArchive(self) -> None: ...
    def Contains(self, relativePath: str) -> bool: ...
    def GetNumberOfGenerationsFromBase(self, type: str) -> int: ...
    @staticmethod
    def GetNumberOfGenerationsFromBaseType(type: str) -> int: ...
    def InsertIntoArchive(self, relativePath: str, data: str, size: int) -> None: ...
    def IsA(self, type: str) -> int: ...
    @staticmethod
    def IsTypeOf(type: str) -> int: ...
    def NewInstance(self) -> vtkPythonArchiver: ...
    def OpenArchive(self) -> None: ...
    @staticmethod
    def SafeDownCast(o: vtkmodules.vtkCommonCore.vtkObjectBase) -> vtkPythonArchiver: ...
    def SetPythonObject(self, obj: PyObject) -> None: ...
