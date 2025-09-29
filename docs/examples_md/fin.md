# fin

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 16
- **连接数**: 15
- **源节点**: `vtkPlane`, `vtkArrowSource`, `Color Ramp`, `vtkStructuredGridReader`, `Color Ramp.001`
- **汇节点**: `VTK To Blender Mesh`, `VTK To Blender Mesh.001`, `VTK To Blender Mesh.002`

## 节点
### vtkStructuredGridReader
- **bl_idname**: `VTKStructuredGridReaderType`
- **properties**: `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **extra**: `custom_code`

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

### vtkStructuredGridOutlineFilter
- **bl_idname**: `VTKStructuredGridOutlineFilterType`
- **extra**: `custom_code`

### vtkTubeFilter
- **bl_idname**: `VTKTubeFilterType`
- **properties**: `m_Capping`, `m_DefaultNormal`, `m_NumberOfSides`, `m_Offset`, `m_OnRatio`, `m_Radius`, `m_RadiusFactor`, `m_SidesShareVertices`, `m_TextureLength`, `m_UseDefaultNormal`
- **extra**: `custom_code`

### vtkPolyDataNormals
- **bl_idname**: `VTKPolyDataNormalsType`
- **properties**: `m_AutoOrientNormals`, `m_ComputeCellNormals`, `m_ComputePointNormals`, `m_Consistency`, `m_FeatureAngle`, `m_FlipNormals`, `m_NonManifoldTraversal`, `m_Splitting`
- **extra**: `custom_code`

### VTK To Blender Mesh.001
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
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

### Color Ramp.001
- **bl_idname**: `BVTK_Node_ColorRampType`
- **extra**: `custom_code`, `texture_name`

### Color Mapper.001
- **bl_idname**: `BVTK_Node_ColorMapperType`
- **extra**: `custom_code`, `color_by`

### VTK To Blender Mesh.002
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
- **extra**: `custom_code`

## 连接
1. `vtkStructuredGridReader`:`output` → `vtkCutter`:`input`
2. `vtkStructuredGridReader`:`output` → `vtkStructuredGridOutlineFilter`:`input`
3. `vtkStructuredGridReader`:`output` → `vtkMaskPoints`:`input`
4. `vtkPlane`:`output` → `vtkCutter`:`CutFunction`
5. `vtkCutter`:`output` → `Color Mapper`:`input`
6. `Color Ramp`:`lookupTable` → `Color Mapper`:`lookuptable`
7. `Color Mapper`:`output` → `VTK To Blender Mesh`:`input`
8. `vtkStructuredGridOutlineFilter`:`output` → `vtkTubeFilter`:`input`
9. `vtkTubeFilter`:`output` → `vtkPolyDataNormals`:`input`
10. `vtkPolyDataNormals`:`output` → `VTK To Blender Mesh.001`:`input`
11. `vtkMaskPoints`:`output` → `vtkGlyph3D`:`input 0`
12. `vtkArrowSource`:`output` → `vtkGlyph3D`:`input 1`
13. `vtkGlyph3D`:`output` → `Color Mapper.001`:`input`
14. `Color Ramp.001`:`lookupTable` → `Color Mapper.001`:`lookuptable`
15. `Color Mapper.001`:`output` → `VTK To Blender Mesh.002`:`input`

## 拓扑（简）
- `Color Mapper` → `VTK To Blender Mesh`
- `Color Mapper.001` → `VTK To Blender Mesh.002`
- `Color Ramp` → `Color Mapper`
- `Color Ramp.001` → `Color Mapper.001`
- `vtkArrowSource` → `vtkGlyph3D`
- `vtkCutter` → `Color Mapper`
- `vtkGlyph3D` → `Color Mapper.001`
- `vtkMaskPoints` → `vtkGlyph3D`
- `vtkPlane` → `vtkCutter`
- `vtkPolyDataNormals` → `VTK To Blender Mesh.001`
- `vtkStructuredGridOutlineFilter` → `vtkTubeFilter`
- `vtkStructuredGridReader` → `vtkCutter`
- `vtkStructuredGridReader` → `vtkMaskPoints`
- `vtkStructuredGridReader` → `vtkStructuredGridOutlineFilter`
- `vtkTubeFilter` → `vtkPolyDataNormals`

