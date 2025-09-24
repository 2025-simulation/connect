# cubeflow_particle_instancing

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 9
- **连接数**: 7
- **源节点**: `vtkArrowSource`, `vtkOpenFOAMReader`
- **汇节点**: `VTK To Blender Mesh`, `VTK To Blender Particles`

## 节点
### vtkArrowSource
- **bl_idname**: `VTKArrowSourceType`
- **properties**: `m_Invert`, `m_ObjectName`, `m_ShaftRadius`, `m_ShaftResolution`, `m_TipLength`, `m_TipRadius`, `m_TipResolution`
- **extra**: `custom_code`

### VTK To Blender Mesh
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
- **extra**: `custom_code`

### vtkOpenFOAMReader
- **bl_idname**: `VTKOpenFOAMReaderType`
- **properties**: `m_AddDimensionsToArrayNames`, `m_CacheMesh`, `m_CopyDataToCellZones`, `m_CreateCellToPoint`, `m_DecomposePolyhedra`, `m_FileName`, `m_ListTimeStepsByControlDict`, `m_ObjectName`, `m_PositionsIsIn13Format`, `m_ReadZones`, `m_SkipZeroTime`, `m_TimeValue`, `m_Use64BitFloats`, `m_Use64BitLabels`
- **extra**: `custom_code`

### Time Selector
- **bl_idname**: `BVTK_Node_TimeSelectorType`
- **extra**: `custom_code`, `time_index`

### Multi Block Leaf
- **bl_idname**: `BVTK_Node_MultiBlockLeafType`
- **extra**: `custom_code`, `block`

### vtkCellCenters
- **bl_idname**: `VTKCellCentersType`
- **properties**: `m_CopyArrays`, `m_ObjectName`, `m_VertexCells`
- **extra**: `custom_code`

### vtkMaskPoints
- **bl_idname**: `VTKMaskPointsType`
- **properties**: `m_GenerateVertices`, `m_MaximumNumberOfPoints`, `m_ObjectName`, `m_Offset`, `m_OnRatio`, `m_ProportionalMaximumNumberOfPoints`, `m_RandomMode`, `m_RandomModeType`, `m_RandomSeed`, `m_SingleVertexPerCell`
- **extra**: `custom_code`

### VTK To Blender Particles
- **bl_idname**: `BVTK_Node_VTKToBlenderParticlesType`
- **extra**: `custom_code`

### vtkArrayCalculator
- **bl_idname**: `VTKArrayCalculatorType`
- **properties**: `m_CoordinateResults`, `m_Function`, `m_IgnoreMissingArrays`, `m_ObjectName`, `m_ReplaceInvalidValues`, `m_ReplacementValue`, `m_ResultArrayName`, `m_ResultArrayType`, `m_ResultNormals`, `m_ResultTCoords`
- **extra**: `custom_code`

## 连接
1. `vtkArrowSource`:`output` → `VTK To Blender Mesh`:`input`
2. `vtkOpenFOAMReader`:`output` → `Time Selector`:`input`
3. `Time Selector`:`output` → `Multi Block Leaf`:`input`
4. `Multi Block Leaf`:`output` → `vtkCellCenters`:`input`
5. `vtkCellCenters`:`output` → `vtkMaskPoints`:`input`
6. `vtkMaskPoints`:`output` → `vtkArrayCalculator`:`input`
7. `vtkArrayCalculator`:`output` → `VTK To Blender Particles`:`input`

## 拓扑（简）
- `Multi Block Leaf` → `vtkCellCenters`
- `Time Selector` → `Multi Block Leaf`
- `vtkArrayCalculator` → `VTK To Blender Particles`
- `vtkArrowSource` → `VTK To Blender Mesh`
- `vtkCellCenters` → `vtkMaskPoints`
- `vtkMaskPoints` → `vtkArrayCalculator`
- `vtkOpenFOAMReader` → `Time Selector`

