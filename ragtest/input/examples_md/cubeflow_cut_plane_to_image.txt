# cubeflow_cut_plane_to_image

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 11
- **连接数**: 10
- **源节点**: `vtkPlane`, `vtkOpenFOAMReader`, `Color Ramp`
- **汇节点**: `VTK To Blender Mesh`, `VTK To Blender Image`

## 节点
### vtkOpenFOAMReader
- **bl_idname**: `VTKOpenFOAMReaderType`
- **properties**: `m_AddDimensionsToArrayNames`, `m_CacheMesh`, `m_CopyDataToCellZones`, `m_CreateCellToPoint`, `m_DecomposePolyhedra`, `m_FileName`, `m_ListTimeStepsByControlDict`, `m_PositionsIsIn13Format`, `m_ReadZones`, `m_SkipZeroTime`, `m_TimeValue`, `m_Use64BitFloats`, `m_Use64BitLabels`
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
- **extra**: `custom_code`, `color_by`, `texture_name`

### VTK To Blender Mesh
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
- **extra**: `custom_code`

### VTK To Blender Image
- **bl_idname**: `BVTK_Node_VTKToBlenderImageType`
- **properties**: `m_Name`
- **extra**: `custom_code`

### vtkResampleToImage
- **bl_idname**: `VTKResampleToImageType`
- **properties**: `m_SamplingDimensions`, `m_UseInputBounds`
- **extra**: `custom_code`

### vtkArrayCalculator
- **bl_idname**: `VTKArrayCalculatorType`
- **properties**: `m_CoordinateResults`, `m_Function`, `m_IgnoreMissingArrays`, `m_ReplaceInvalidValues`, `m_ReplacementValue`, `m_ResultArrayName`, `m_ResultArrayType`, `m_ResultNormals`, `m_ResultTCoords`
- **extra**: `custom_code`

## 连接
1. `vtkOpenFOAMReader`:`output` → `Time Selector`:`input`
2. `Time Selector`:`output` → `Multi Block Leaf`:`input`
3. `Multi Block Leaf`:`output` → `vtkArrayCalculator`:`input`
4. `vtkPlane`:`output` → `vtkCutter`:`CutFunction`
5. `vtkCutter`:`output` → `Color Mapper`:`input`
6. `vtkCutter`:`output` → `vtkResampleToImage`:`input`
7. `Color Ramp`:`lookupTable` → `Color Mapper`:`lookuptable`
8. `Color Mapper`:`output` → `VTK To Blender Mesh`:`input`
9. `vtkResampleToImage`:`output` → `VTK To Blender Image`:`input`
10. `vtkArrayCalculator`:`output` → `vtkCutter`:`input`

## 拓扑（简）
- `Color Mapper` → `VTK To Blender Mesh`
- `Color Ramp` → `Color Mapper`
- `Multi Block Leaf` → `vtkArrayCalculator`
- `Time Selector` → `Multi Block Leaf`
- `vtkArrayCalculator` → `vtkCutter`
- `vtkCutter` → `Color Mapper`
- `vtkCutter` → `vtkResampleToImage`
- `vtkOpenFOAMReader` → `Time Selector`
- `vtkPlane` → `vtkCutter`
- `vtkResampleToImage` → `VTK To Blender Image`

