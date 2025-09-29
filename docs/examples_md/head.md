# head

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 6
- **连接数**: 5
- **源节点**: `vtkXMLImageDataReader`
- **汇节点**: `VTK To Blender Mesh.001`, `VTK To Blender Mesh`

## 节点
### vtkXMLImageDataReader
- **bl_idname**: `VTKXMLImageDataReaderType`
- **properties**: `m_FileName`, `m_ReadFromInputString`, `m_TimeStep`, `m_TimeStepRange`, `m_WholeSlices`
- **extra**: `custom_code`

### vtkImageGaussianSmooth
- **bl_idname**: `VTKImageGaussianSmoothType`
- **properties**: `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_MinimumPieceSize`, `m_NumberOfThreads`, `m_RadiusFactors`, `m_StandardDeviations`
- **extra**: `custom_code`

### vtkContourFilter
- **bl_idname**: `VTKContourFilterType`
- **properties**: `m_ArrayComponent`, `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_GenerateTriangles`, `m_NumberOfContours`
- **extra**: `custom_code`

### VTK To Blender Mesh
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
- **extra**: `custom_code`

### vtkContourFilter.001
- **bl_idname**: `VTKContourFilterType`
- **properties**: `m_ArrayComponent`, `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_GenerateTriangles`, `m_NumberOfContours`
- **extra**: `custom_code`

### VTK To Blender Mesh.001
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
- **extra**: `custom_code`

## 连接
1. `vtkXMLImageDataReader`:`output` → `vtkImageGaussianSmooth`:`input`
2. `vtkImageGaussianSmooth`:`output` → `vtkContourFilter`:`input`
3. `vtkImageGaussianSmooth`:`output` → `vtkContourFilter.001`:`input`
4. `vtkContourFilter`:`output` → `VTK To Blender Mesh`:`input`
5. `vtkContourFilter.001`:`output` → `VTK To Blender Mesh.001`:`input`

## 拓扑（简）
- `vtkContourFilter` → `VTK To Blender Mesh`
- `vtkContourFilter.001` → `VTK To Blender Mesh.001`
- `vtkImageGaussianSmooth` → `vtkContourFilter`
- `vtkImageGaussianSmooth` → `vtkContourFilter.001`
- `vtkXMLImageDataReader` → `vtkImageGaussianSmooth`

