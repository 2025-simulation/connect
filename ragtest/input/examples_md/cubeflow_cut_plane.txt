# cubeflow_cut_plane

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 8
- **连接数**: 7
- **源节点**: `vtkPlane`, `vtkOpenFOAMReader`, `Color Ramp`
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

### vtkPlane
- **bl_idname**: `VTKPlaneType`
- **properties**: `m_Normal`, `m_Origin`
- **extra**: `custom_code`

### vtkCutter
- **bl_idname**: `VTKCutterType`
- **properties**: `m_GenerateCutScalars`, `m_GenerateTriangles`, `m_NumberOfContours`
- **extra**: `custom_code`

### Color Ramp
- **bl_idname**: `BVTK_Node_ColorRampType`
- **extra**: `custom_code`, `texture_name`

### Color Mapper
- **bl_idname**: `BVTK_Node_ColorMapperType`
- **extra**: `custom_code`, `color_by`

### VTK To Blender Mesh
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
- **extra**: `custom_code`

## 连接
1. `vtkOpenFOAMReader`:`output` → `Time Selector`:`input`
2. `Time Selector`:`output` → `Multi Block Leaf`:`input`
3. `Multi Block Leaf`:`output` → `vtkCutter`:`input`
4. `vtkPlane`:`output` → `vtkCutter`:`CutFunction`
5. `vtkCutter`:`output` → `Color Mapper`:`input`
6. `Color Ramp`:`lookupTable` → `Color Mapper`:`lookuptable`
7. `Color Mapper`:`output` → `VTK To Blender Mesh`:`input`

## 拓扑（简）
- `Color Mapper` → `VTK To Blender Mesh`
- `Color Ramp` → `Color Mapper`
- `Multi Block Leaf` → `vtkCutter`
- `Time Selector` → `Multi Block Leaf`
- `vtkCutter` → `Color Mapper`
- `vtkOpenFOAMReader` → `Time Selector`
- `vtkPlane` → `vtkCutter`

