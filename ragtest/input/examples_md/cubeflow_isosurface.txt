# cubeflow_isosurface

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 8
- **连接数**: 7
- **源节点**: `vtkOpenFOAMReader`
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

### vtkClipDataSet
- **bl_idname**: `VTKClipDataSetType`
- **properties**: `m_GenerateClipScalars`, `m_GenerateClippedOutput`, `m_InsideOut`, `m_MergeTolerance`, `m_UseValueAsOffset`, `m_Value`
- **extra**: `custom_code`

### vtkDataSetRegionSurfaceFilter
- **bl_idname**: `VTKDataSetRegionSurfaceFilterType`
- **properties**: `m_InterfaceIDsName`, `m_MaterialIDsName`, `m_MaterialPIDsName`, `m_MaterialPropertiesName`, `m_NonlinearSubdivisionLevel`, `m_OriginalCellIdsName`, `m_OriginalPointIdsName`, `m_PassThroughCellIds`, `m_PassThroughPointIds`, `m_PieceInvariant`, `m_RegionArrayName`, `m_SingleSided`, `m_UseStrips`
- **extra**: `custom_code`

### vtkPolyDataNormals
- **bl_idname**: `VTKPolyDataNormalsType`
- **properties**: `m_AutoOrientNormals`, `m_ComputeCellNormals`, `m_ComputePointNormals`, `m_Consistency`, `m_FeatureAngle`, `m_FlipNormals`, `m_NonManifoldTraversal`, `m_Splitting`
- **extra**: `custom_code`

## 连接
1. `vtkOpenFOAMReader`:`output` → `Time Selector`:`input`
2. `Time Selector`:`output` → `Multi Block Leaf`:`input`
3. `Multi Block Leaf`:`output` → `vtkAssignAttribute`:`input`
4. `vtkAssignAttribute`:`output` → `vtkClipDataSet`:`input`
5. `vtkClipDataSet`:`output 0` → `vtkDataSetRegionSurfaceFilter`:`input`
6. `vtkDataSetRegionSurfaceFilter`:`output` → `vtkPolyDataNormals`:`input`
7. `vtkPolyDataNormals`:`output` → `VTK To Blender Mesh`:`input`

## 拓扑（简）
- `Multi Block Leaf` → `vtkAssignAttribute`
- `Time Selector` → `Multi Block Leaf`
- `vtkAssignAttribute` → `vtkClipDataSet`
- `vtkClipDataSet` → `vtkDataSetRegionSurfaceFilter`
- `vtkDataSetRegionSurfaceFilter` → `vtkPolyDataNormals`
- `vtkOpenFOAMReader` → `Time Selector`
- `vtkPolyDataNormals` → `VTK To Blender Mesh`

