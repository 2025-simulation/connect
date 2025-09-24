# cubeflow_openvdb_export

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 9
- **连接数**: 8
- **源节点**: `vtkOpenFOAMReader`, `VTKImageData Object Source`
- **汇节点**: `VTK To OpenVDB Exporter`, `VTK To Blender Volume`

## 节点
### VTKImageData Object Source
- **bl_idname**: `BVTK_Node_ImageDataObjectSourceType`
- **extra**: `custom_code`

### VTK To OpenVDB Exporter
- **bl_idname**: `BVTK_Node_VTKToOpenVDBExporterType`
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

### vtkArrayCalculator
- **bl_idname**: `VTKArrayCalculatorType`
- **properties**: `m_CoordinateResults`, `m_Function`, `m_IgnoreMissingArrays`, `m_ObjectName`, `m_ReplaceInvalidValues`, `m_ReplacementValue`, `m_ResultArrayName`, `m_ResultArrayType`, `m_ResultNormals`, `m_ResultTCoords`
- **extra**: `custom_code`

### vtkArrayCalculator.001
- **bl_idname**: `VTKArrayCalculatorType`
- **properties**: `m_CoordinateResults`, `m_Function`, `m_IgnoreMissingArrays`, `m_ObjectName`, `m_ReplaceInvalidValues`, `m_ReplacementValue`, `m_ResultArrayName`, `m_ResultArrayType`, `m_ResultNormals`, `m_ResultTCoords`
- **extra**: `custom_code`

### vtkProbeFilter
- **bl_idname**: `VTKProbeFilterType`
- **properties**: `m_CategoricalData`, `m_ComputeTolerance`, `m_ObjectName`, `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPointArrays`, `m_SpatialMatch`, `m_Tolerance`, `m_ValidPointMaskArrayName`
- **extra**: `custom_code`

### VTK To Blender Volume
- **bl_idname**: `BVTK_Node_VTKToBlenderVolumeType`
- **extra**: `custom_code`

## 连接
1. `VTKImageData Object Source`:`output` → `vtkProbeFilter`:`input 0`
2. `vtkOpenFOAMReader`:`output` → `Time Selector`:`input`
3. `Time Selector`:`output` → `Multi Block Leaf`:`input`
4. `Multi Block Leaf`:`output` → `vtkArrayCalculator`:`input`
5. `vtkArrayCalculator`:`output` → `vtkArrayCalculator.001`:`input`
6. `vtkArrayCalculator.001`:`output` → `vtkProbeFilter`:`input 1`
7. `vtkProbeFilter`:`output` → `VTK To OpenVDB Exporter`:`input`
8. `vtkProbeFilter`:`output` → `VTK To Blender Volume`:`input`

## 拓扑（简）
- `Multi Block Leaf` → `vtkArrayCalculator`
- `Time Selector` → `Multi Block Leaf`
- `VTKImageData Object Source` → `vtkProbeFilter`
- `vtkArrayCalculator` → `vtkArrayCalculator.001`
- `vtkArrayCalculator.001` → `vtkProbeFilter`
- `vtkOpenFOAMReader` → `Time Selector`
- `vtkProbeFilter` → `VTK To Blender Volume`
- `vtkProbeFilter` → `VTK To OpenVDB Exporter`

