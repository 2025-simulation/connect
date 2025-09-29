# kitchen

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 10
- **连接数**: 8
- **源节点**: `vtkPlaneSource`, `vtkPolyDataReader`, `Color Ramp`, `vtkStructuredGridReader`
- **汇节点**: `VTK To Blender Mesh.001`, `VTK To Blender Mesh`

## 节点
### vtkPolyDataReader
- **bl_idname**: `VTKPolyDataReaderType`
- **properties**: `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **extra**: `custom_code`

### VTK To Blender Mesh
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
- **extra**: `custom_code`

### vtkStructuredGridReader
- **bl_idname**: `VTKStructuredGridReaderType`
- **properties**: `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **extra**: `custom_code`

### vtkPlaneSource
- **bl_idname**: `VTKPlaneSourceType`
- **properties**: `m_Center`, `m_Normal`, `m_Origin`, `m_Point1`, `m_Point2`, `m_XResolution`, `m_YResolution`
- **extra**: `custom_code`

### vtkStreamTracer
- **bl_idname**: `VTKStreamTracerType`
- **properties**: `m_ComputeVorticity`, `m_InitialIntegrationStep`, `m_IntegrationStepUnit`, `m_MaximumError`, `m_MaximumIntegrationStep`, `m_MaximumNumberOfSteps`, `m_MaximumPropagation`, `m_MinimumIntegrationStep`, `m_RotationScale`, `m_StartPosition`, `m_SurfaceStreamlines`, `m_TerminalSpeed`
- **extra**: `custom_code`

### vtkTubeFilter
- **bl_idname**: `VTKTubeFilterType`
- **properties**: `m_Capping`, `m_DefaultNormal`, `m_NumberOfSides`, `m_Offset`, `m_OnRatio`, `m_Radius`, `m_RadiusFactor`, `m_SidesShareVertices`, `m_TextureLength`, `m_UseDefaultNormal`
- **extra**: `custom_code`

### vtkPolyDataNormals
- **bl_idname**: `VTKPolyDataNormalsType`
- **properties**: `m_AutoOrientNormals`, `m_ComputeCellNormals`, `m_ComputePointNormals`, `m_Consistency`, `m_FeatureAngle`, `m_FlipNormals`, `m_NonManifoldTraversal`, `m_Splitting`
- **extra**: `custom_code`

### Color Ramp
- **bl_idname**: `BVTK_Node_ColorRampType`
- **extra**: `custom_code`, `texture_name`

### Color Mapper
- **bl_idname**: `BVTK_Node_ColorMapperType`
- **extra**: `custom_code`, `color_by`

### VTK To Blender Mesh.001
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
- **extra**: `custom_code`

## 连接
1. `vtkPolyDataReader`:`output` → `VTK To Blender Mesh`:`input`
2. `vtkStructuredGridReader`:`output` → `vtkStreamTracer`:`input 0`
3. `vtkPlaneSource`:`output` → `vtkStreamTracer`:`input 1`
4. `vtkStreamTracer`:`output` → `vtkTubeFilter`:`input`
5. `vtkTubeFilter`:`output` → `vtkPolyDataNormals`:`input`
6. `vtkPolyDataNormals`:`output` → `Color Mapper`:`input`
7. `Color Ramp`:`lookupTable` → `Color Mapper`:`lookuptable`
8. `Color Mapper`:`output` → `VTK To Blender Mesh.001`:`input`

## 拓扑（简）
- `Color Mapper` → `VTK To Blender Mesh.001`
- `Color Ramp` → `Color Mapper`
- `vtkPlaneSource` → `vtkStreamTracer`
- `vtkPolyDataNormals` → `Color Mapper`
- `vtkPolyDataReader` → `VTK To Blender Mesh`
- `vtkStreamTracer` → `vtkTubeFilter`
- `vtkStructuredGridReader` → `vtkStreamTracer`
- `vtkTubeFilter` → `vtkPolyDataNormals`

