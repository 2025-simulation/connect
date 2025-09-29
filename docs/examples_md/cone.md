# cone

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 5
- **连接数**: 4
- **源节点**: `vtkConeSource`, `Color Ramp`
- **汇节点**: `VTK To Blender Mesh`

## 节点
### vtkConeSource
- **bl_idname**: `VTKConeSourceType`
- **properties**: `m_Angle`, `m_Capping`, `m_Center`, `m_Direction`, `m_Height`, `m_Radius`, `m_Resolution`
- **extra**: `custom_code`

### vtkElevationFilter
- **bl_idname**: `VTKElevationFilterType`
- **properties**: `m_HighPoint`, `m_LowPoint`, `m_ScalarRange`
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
1. `vtkConeSource`:`output` → `vtkElevationFilter`:`input`
2. `vtkElevationFilter`:`output` → `Color Mapper`:`input`
3. `Color Ramp`:`lookupTable` → `Color Mapper`:`lookuptable`
4. `Color Mapper`:`output` → `VTK To Blender Mesh`:`input`

## 拓扑（简）
- `Color Mapper` → `VTK To Blender Mesh`
- `Color Ramp` → `Color Mapper`
- `vtkConeSource` → `vtkElevationFilter`
- `vtkElevationFilter` → `Color Mapper`

