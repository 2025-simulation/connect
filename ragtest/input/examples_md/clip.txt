# clip

生成说明
- 本文件由脚本自动生成，来源于相同文件名的 .json
- 结构：节点列表、连接关系、简要拓扑

## 总览
- **节点数**: 5
- **连接数**: 4
- **源节点**: `vtkPlane`, `vtkSphereSource`
- **汇节点**: `VTK To Blender Mesh.001`, `VTK To Blender Mesh`

## 节点
### vtkSphereSource
- **bl_idname**: `VTKSphereSourceType`
- **properties**: `m_Center`, `m_EndPhi`, `m_EndTheta`, `m_LatLongTessellation`, `m_PhiResolution`, `m_Radius`, `m_StartPhi`, `m_StartTheta`, `m_ThetaResolution`
- **extra**: `custom_code`

### vtkPlane
- **bl_idname**: `VTKPlaneType`
- **properties**: `m_Normal`, `m_Origin`
- **extra**: `custom_code`

### vtkClipPolyData
- **bl_idname**: `VTKClipPolyDataType`
- **properties**: `m_GenerateClipScalars`, `m_GenerateClippedOutput`, `m_InsideOut`, `m_Value`
- **extra**: `custom_code`

### VTK To Blender Mesh
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
- **extra**: `custom_code`

### VTK To Blender Mesh.001
- **bl_idname**: `BVTK_Node_VTKToBlenderMeshType`
- **properties**: `m_Name`
- **extra**: `custom_code`

## 连接
1. `vtkSphereSource`:`output` → `vtkClipPolyData`:`input`
2. `vtkPlane`:`output` → `vtkClipPolyData`:`ClipFunction`
3. `vtkClipPolyData`:`output 0` → `VTK To Blender Mesh`:`input`
4. `vtkClipPolyData`:`output 1` → `VTK To Blender Mesh.001`:`input`

## 拓扑（简）
- `vtkClipPolyData` → `VTK To Blender Mesh`
- `vtkClipPolyData` → `VTK To Blender Mesh.001`
- `vtkPlane` → `vtkClipPolyData`
- `vtkSphereSource` → `vtkClipPolyData`

