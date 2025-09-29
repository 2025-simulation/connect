# cubeflow_vector_glyphs

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 10
- **连接数**: 9
- **源节点**: `vtkArrowSource`, `vtkOpenFOAMReader`, `Color Ramp`
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

### vtkCellCenters
- **bl_idname**: `VTKCellCentersType`
- **properties**: `m_CopyArrays`, `m_VertexCells`
- **extra**: `custom_code`

### vtkMaskPoints
- **bl_idname**: `VTKMaskPointsType`
- **properties**: `m_GenerateVertices`, `m_MaximumNumberOfPoints`, `m_Offset`, `m_OnRatio`, `m_ProportionalMaximumNumberOfPoints`, `m_RandomMode`, `m_RandomModeType`, `m_SingleVertexPerCell`
- **extra**: `custom_code`

### vtkArrowSource
- **bl_idname**: `VTKArrowSourceType`
- **properties**: `m_Invert`, `m_ShaftRadius`, `m_ShaftResolution`, `m_TipLength`, `m_TipRadius`, `m_TipResolution`
- **extra**: `custom_code`

### vtkGlyph3D
- **bl_idname**: `VTKGlyph3DType`
- **properties**: `m_Clamping`, `m_FillCellData`, `m_GeneratePointIds`, `m_Orient`, `m_PointIdsName`, `m_Range`, `m_ScaleFactor`, `m_Scaling`
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
3. `Multi Block Leaf`:`output` → `vtkCellCenters`:`input`
4. `vtkCellCenters`:`output` → `vtkMaskPoints`:`input`
5. `vtkMaskPoints`:`output` → `vtkGlyph3D`:`input 0`
6. `vtkArrowSource`:`output` → `vtkGlyph3D`:`input 1`
7. `vtkGlyph3D`:`output` → `Color Mapper`:`input`
8. `Color Ramp`:`lookupTable` → `Color Mapper`:`lookuptable`
9. `Color Mapper`:`output` → `VTK To Blender Mesh`:`input`

## 拓扑（简）
- `Color Mapper` → `VTK To Blender Mesh`
- `Color Ramp` → `Color Mapper`
- `Multi Block Leaf` → `vtkCellCenters`
- `Time Selector` → `Multi Block Leaf`
- `vtkArrowSource` → `vtkGlyph3D`
- `vtkCellCenters` → `vtkMaskPoints`
- `vtkGlyph3D` → `Color Mapper`
- `vtkMaskPoints` → `vtkGlyph3D`
- `vtkOpenFOAMReader` → `Time Selector`

