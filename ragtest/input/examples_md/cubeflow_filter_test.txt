# cubeflow_filter_test

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 12
- **连接数**: 12
- **源节点**: `vtkOpenFOAMReader`, `VTKImageData Object Source`
- **汇节点**: `VTK To Blender Mesh`

## 节点
### vtkOpenFOAMReader
- **bl_idname**: `VTKOpenFOAMReaderType`
- **properties**: `m_AddDimensionsToArrayNames`, `m_CacheMesh`, `m_CopyDataToCellZones`, `m_CreateCellToPoint`, `m_DecomposePolyhedra`, `m_FileName`, `m_ListTimeStepsByControlDict`, `m_ObjectName`, `m_PositionsIsIn13Format`, `m_ReadZones`, `m_SkipZeroTime`, `m_TimeValue`, `m_Use64BitFloats`, `m_Use64BitLabels`
- **extra**: `custom_code`

### Time Selector
- **bl_idname**: `BVTK_Node_TimeSelectorType`
- **extra**: `custom_code`, `time_index`

### Custom Filter
- **bl_idname**: `BVTK_Node_CustomFilterType`
- **extra**: `custom_code`

### vtkAssignAttribute
- **bl_idname**: `VTKAssignAttributeType`
- **properties**: `m_ObjectName`
- **extra**: `custom_code`

### vtkMarchingCubes
- **bl_idname**: `VTKMarchingCubesType`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_NumberOfContours`
- **extra**: `custom_code`

### VTKImageData Object Source
- **bl_idname**: `BVTK_Node_ImageDataObjectSourceType`
- **extra**: `custom_code`

### vtkProbeFilter
- **bl_idname**: `VTKProbeFilterType`
- **properties**: `m_CategoricalData`, `m_ComputeTolerance`, `m_ObjectName`, `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPointArrays`, `m_SpatialMatch`, `m_Tolerance`, `m_ValidPointMaskArrayName`
- **extra**: `custom_code`

### vtkThreshold
- **bl_idname**: `VTKThresholdType`
- **properties**: `m_AttrName`, `m_Value1`, `m_Value2`
- **extra**: `custom_code`

### vtkTransformFilter
- **bl_idname**: `VTKTransformFilterType`
- **properties**: `m_Rotation`, `m_Scale`, `m_Translation`
- **extra**: `custom_code`

### vtkAppendFilter
- **bl_idname**: `VTKAppendFilterType`
- **properties**: `m_MergePoints`, `m_Tolerance`, `m_ToleranceIsAbsolute`
- **extra**: `custom_code`

### VTK To Blender Mesh
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
- **extra**: `custom_code`

### vtkBoxClipDataSet
- **bl_idname**: `VTKBoxClipDataSetType`
- **properties**: `m_BoxClip`, `m_GenerateClipScalars`, `m_GenerateClippedOutput`, `m_Orientation`
- **extra**: `custom_code`

## 连接
1. `vtkOpenFOAMReader`:`output` → `Time Selector`:`input`
2. `Time Selector`:`output` → `Custom Filter`:`aux_in1`
3. `Custom Filter`:`output` → `vtkAssignAttribute`:`input`
4. `Custom Filter`:`output` → `vtkThreshold`:`input`
5. `vtkAssignAttribute`:`output` → `vtkProbeFilter`:`input 1`
6. `vtkMarchingCubes`:`output` → `vtkAppendFilter`:`input1`
7. `VTKImageData Object Source`:`output` → `vtkProbeFilter`:`input 0`
8. `vtkProbeFilter`:`output` → `vtkMarchingCubes`:`input`
9. `vtkThreshold`:`output` → `vtkBoxClipDataSet`:`input`
10. `vtkTransformFilter`:`output` → `vtkAppendFilter`:`input2`
11. `vtkAppendFilter`:`output` → `VTK To Blender Mesh`:`input`
12. `vtkBoxClipDataSet`:`output 0` → `vtkTransformFilter`:`input`

## 拓扑（简）
- `Custom Filter` → `vtkAssignAttribute`
- `Custom Filter` → `vtkThreshold`
- `Time Selector` → `Custom Filter`
- `VTKImageData Object Source` → `vtkProbeFilter`
- `vtkAppendFilter` → `VTK To Blender Mesh`
- `vtkAssignAttribute` → `vtkProbeFilter`
- `vtkBoxClipDataSet` → `vtkTransformFilter`
- `vtkMarchingCubes` → `vtkAppendFilter`
- `vtkOpenFOAMReader` → `Time Selector`
- `vtkProbeFilter` → `vtkMarchingCubes`
- `vtkThreshold` → `vtkBoxClipDataSet`
- `vtkTransformFilter` → `vtkAppendFilter`

