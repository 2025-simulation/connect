# cubeflow_stream_tracers

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 11
- **连接数**: 10
- **源节点**: `vtkOpenFOAMReader`, `vtkPlaneSource`, `Color Ramp`
- **汇节点**: `VTK To Blender Mesh`

## 节点
### vtkOpenFOAMReader
- **bl_idname**: `VTKOpenFOAMReaderType`
- **properties**: `m_AddDimensionsToArrayNames`, `m_CacheMesh`, `m_CopyDataToCellZones`, `m_CreateCellToPoint`, `m_DecomposePolyhedra`, `m_FileName`, `m_ListTimeStepsByControlDict`, `m_PositionsIsIn13Format`, `m_ReadZones`, `m_SkipZeroTime`, `m_Use64BitFloats`, `m_Use64BitLabels`
- **extra**: `custom_code`

### Time Selector
- **bl_idname**: `BVTK_Node_TimeSelectorType`
- **extra**: `custom_code`, `time_index`

### Multi Block Leaf
- **bl_idname**: `BVTK_Node_MultiBlockLeafType`
- **extra**: `custom_code`, `block`

### vtkAssignAttribute
- **bl_idname**: `VTKAssignAttributeType`
- **extra**: `custom_code`

### VTK To Blender Mesh
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
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

## 连接
1. `vtkOpenFOAMReader`:`output` → `Time Selector`:`input`
2. `Time Selector`:`output` → `Multi Block Leaf`:`input`
3. `Multi Block Leaf`:`output` → `vtkAssignAttribute`:`input`
4. `vtkAssignAttribute`:`output` → `vtkStreamTracer`:`input 0`
5. `vtkPlaneSource`:`output` → `vtkStreamTracer`:`input 1`
6. `vtkStreamTracer`:`output` → `vtkTubeFilter`:`input`
7. `vtkTubeFilter`:`output` → `vtkPolyDataNormals`:`input`
8. `vtkPolyDataNormals`:`output` → `Color Mapper`:`input`
9. `Color Ramp`:`lookupTable` → `Color Mapper`:`lookuptable`
10. `Color Mapper`:`output` → `VTK To Blender Mesh`:`input`

## 拓扑（简）
- `Color Mapper` → `VTK To Blender Mesh`
- `Color Ramp` → `Color Mapper`
- `Multi Block Leaf` → `vtkAssignAttribute`
- `Time Selector` → `Multi Block Leaf`
- `vtkAssignAttribute` → `vtkStreamTracer`
- `vtkOpenFOAMReader` → `Time Selector`
- `vtkPlaneSource` → `vtkStreamTracer`
- `vtkPolyDataNormals` → `Color Mapper`
- `vtkStreamTracer` → `vtkTubeFilter`
- `vtkTubeFilter` → `vtkPolyDataNormals`

