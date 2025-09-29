# BVtk Nodes 索引

- 本文档由脚本自动生成
- 来源目录：`BVtkNodes/generated_nodes/`, `BVtkNodes/custom_nodes/`

注：分类取自各文件 `CATEGORIES.append(BVTK_NodeCategory('...'))` 的首个匹配，若缺失则为空。

## Uncategorized

### vtkAppendFilter
- **bl_idname**: `VTKAppendFilterType`
- **module**: `custom_nodes/VTKFilters.py`
- **properties**: `m_MergePoints`, `m_ToleranceIsAbsolute`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBoxClipDataSet
- **bl_idname**: `VTKBoxClipDataSetType`
- **module**: `custom_nodes/VTKFilters.py`
- **properties**: `m_GenerateClipScalars`, `m_GenerateClippedOutput`, `m_Orientation`, `m_BoxClip`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkContourFilter
- **bl_idname**: `VTKContourFilterType`
- **module**: `custom_nodes/VTKFilters.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_GenerateTriangles`, `m_ArrayComponent`, `m_NumberOfContours`, `single_value`, `additional_values`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMarchingCubes
- **bl_idname**: `VTKMarchingCubesType`
- **module**: `custom_nodes/VTKFilters.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_NumberOfContours`, `single_value`, `additional_values`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkThreshold
- **bl_idname**: `VTKThresholdType`
- **module**: `custom_nodes/VTKFilters.py`
- **properties**: `m_Value1`, `m_Value2`, `m_AttrName`, `e_AttrType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransformFilter
- **bl_idname**: `VTKTransformFilterType`
- **module**: `custom_nodes/VTKFilters.py`
- **properties**: `m_Scale`, `m_Rotation`, `m_Translation`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPlane
- **bl_idname**: `VTKPlaneType`
- **module**: `custom_nodes/VTKOthers.py`
- **properties**: `m_Normal`, `m_Origin`, `orientation_object`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSphere
- **bl_idname**: `VTKSphereType`
- **module**: `custom_nodes/VTKOthers.py`
- **properties**: `m_Radius`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

## Filter

### vtkAnnotationLink
- **bl_idname**: `VTKAnnotationLinkType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAutoCorrelativeStatistics
- **bl_idname**: `VTKAutoCorrelativeStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_TestOption`, `m_ObjectName`, `m_NumberOfPrimaryTables`, `m_SliceCardinality`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBandedPolyDataContourFilter
- **bl_idname**: `VTKBandedPolyDataContourFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_Clipping`, `m_GenerateContourEdges`, `m_ObjectName`, `m_Component`, `m_NumberOfContours`, `m_ClipTolerance`, `e_ScalarMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBivariateLinearTableThreshold
- **bl_idname**: `VTKBivariateLinearTableThresholdType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_UseNormalizedDistance`, `m_ObjectName`, `m_Inclusive`, `m_DistanceThreshold`, `e_LinearThresholdType`, `m_ColumnRanges`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBooleanOperationPolyDataFilter
- **bl_idname**: `VTKBooleanOperationPolyDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ReorientDifferenceCells`, `m_ObjectName`, `m_Tolerance`, `e_Operation`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBoxClipDataSet
- **bl_idname**: `VTKBoxClipDataSetType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateClipScalars`, `m_GenerateClippedOutput`, `m_ObjectName`, `m_Orientation`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkClipDataSet
- **bl_idname**: `VTKClipDataSetType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateClipScalars`, `m_GenerateClippedOutput`, `m_InsideOut`, `m_UseValueAsOffset`, `m_ObjectName`, `m_MergeTolerance`, `m_Value`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkClipPolyData
- **bl_idname**: `VTKClipPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateClipScalars`, `m_GenerateClippedOutput`, `m_InsideOut`, `m_ObjectName`, `m_Value`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkClipVolume
- **bl_idname**: `VTKClipVolumeType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateClipScalars`, `m_GenerateClippedOutput`, `m_InsideOut`, `m_Mixed3DCellGeneration`, `m_ObjectName`, `m_MergeTolerance`, `m_Value`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCollisionDetectionFilter
- **bl_idname**: `VTKCollisionDetectionFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateScalars`, `m_ObjectName`, `m_NumberOfCellsPerNode`, `m_BoxTolerance`, `m_CellTolerance`, `m_Opacity`, `e_CollisionMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkComputeHistogram2DOutliers
- **bl_idname**: `VTKComputeHistogram2DOutliersType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ObjectName`, `m_PreferredNumberOfOutliers`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkContingencyStatistics
- **bl_idname**: `VTKContingencyStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_TestOption`, `m_ObjectName`, `m_NumberOfPrimaryTables`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkConvertSelectionDomain
- **bl_idname**: `VTKConvertSelectionDomainType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCorrelativeStatistics
- **bl_idname**: `VTKCorrelativeStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_TestOption`, `m_ObjectName`, `m_NumberOfPrimaryTables`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDescriptiveStatistics
- **bl_idname**: `VTKDescriptiveStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_G1Skewness`, `m_G2Kurtosis`, `m_LearnOption`, `m_SampleEstimate`, `m_SignedDeviations`, `m_TestOption`, `m_UnbiasedVariance`, `m_ObjectName`, `m_GhostsToSkip`, `m_NumberOfPrimaryTables`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDistancePolyDataFilter
- **bl_idname**: `VTKDistancePolyDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ComputeCellCenterDistance`, `m_ComputeSecondDistance`, `m_NegateDistance`, `m_SignedDistance`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEqualizerFilter
- **bl_idname**: `VTKEqualizerFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AllColumns`, `m_Array`, `m_ObjectName`, `m_Points`, `m_SamplingFrequency`, `m_SpectrumGain`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEquirectangularToCubeMapTexture
- **bl_idname**: `VTKEquirectangularToCubeMapTextureType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_CubeMap`, `m_EdgeClamp`, `m_Interpolate`, `m_Mipmap`, `m_PremultipliedAlpha`, `m_Repeat`, `m_RestrictPowerOf2ImageSmaller`, `m_UseSRGBColorSpace`, `m_ObjectName`, `m_BlendingMode`, `m_CubeMapSize`, `m_IsDepthTexture`, `m_TextureType`, `m_Wrap`, `m_MaximumAnisotropicFiltering`, `e_ColorMode`, `e_Quality`, `m_BorderColor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractEnclosedPoints
- **bl_idname**: `VTKExtractEnclosedPointsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_CheckSurface`, `m_GenerateOutliers`, `m_GenerateVertices`, `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractHierarchicalBins
- **bl_idname**: `VTKExtractHierarchicalBinsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateOutliers`, `m_GenerateVertices`, `m_ObjectName`, `m_Bin`, `m_Level`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractHistogram2D
- **bl_idname**: `VTKExtractHistogram2DType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_SwapColumns`, `m_TestOption`, `m_UseCustomHistogramExtents`, `m_ObjectName`, `m_NumberOfPrimaryTables`, `e_ScalarType`, `m_ComponentsToProcess`, `m_NumberOfBins`, `m_CustomHistogramExtents`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractPoints
- **bl_idname**: `VTKExtractPointsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ExtractInside`, `m_GenerateOutliers`, `m_GenerateVertices`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractSelectedRows
- **bl_idname**: `VTKExtractSelectedRowsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AddOriginalRowIdsArray`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractVectorComponents
- **bl_idname**: `VTKExtractVectorComponentsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ExtractToFieldData`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFitImplicitFunction
- **bl_idname**: `VTKFitImplicitFunctionType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateOutliers`, `m_GenerateVertices`, `m_ObjectName`, `m_Threshold`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericClip
- **bl_idname**: `VTKGenericClipType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateClipScalars`, `m_GenerateClippedOutput`, `m_InsideOut`, `m_ObjectName`, `m_MergeTolerance`, `m_Value`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGraphAnnotationLayersFilter
- **bl_idname**: `VTKGraphAnnotationLayersFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGraphToPolyData
- **bl_idname**: `VTKGraphToPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_EdgeGlyphOutput`, `m_ObjectName`, `m_EdgeGlyphPosition`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHausdorffDistancePointSetFilter
- **bl_idname**: `VTKHausdorffDistancePointSetFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ObjectName`, `e_TargetDistanceMethod`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHighestDensityRegionsStatistics
- **bl_idname**: `VTKHighestDensityRegionsStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_TestOption`, `m_ObjectName`, `m_NumberOfPrimaryTables`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageConnectivityFilter
- **bl_idname**: `VTKImageConnectivityFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateRegionExtents`, `m_ObjectName`, `m_ActiveComponent`, `m_LabelConstantValue`, `e_ExtractionMode`, `e_LabelMode`, `e_LabelScalarType`, `m_SizeRange`, `m_ScalarRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImagePermute
- **bl_idname**: `VTKImagePermuteType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AutoCropOutput`, `m_Border`, `m_EnableSMP`, `m_GenerateStencilOutput`, `m_GlobalDefaultEnableSMP`, `m_Interpolate`, `m_Mirror`, `m_Optimization`, `m_SlabTrapezoidIntegration`, `m_TransformInputSampling`, `m_Wrap`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_OutputDimensionality`, `m_OutputScalarType`, `m_SlabNumberOfSlices`, `m_BackgroundLevel`, `m_BorderThickness`, `m_ScalarScale`, `m_ScalarShift`, `m_SlabSliceSpacingFraction`, `e_InterpolationMode`, `e_SlabMode`, `e_SplitMode`, `m_FilteredAxes`, `m_MinimumPieceSize`, `m_OutputExtent`, `m_BackgroundColor`, `m_OutputOrigin`, `m_OutputSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageResample
- **bl_idname**: `VTKImageResampleType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AutoCropOutput`, `m_Border`, `m_EnableSMP`, `m_GenerateStencilOutput`, `m_GlobalDefaultEnableSMP`, `m_Interpolate`, `m_Mirror`, `m_Optimization`, `m_SlabTrapezoidIntegration`, `m_TransformInputSampling`, `m_Wrap`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `m_OutputDimensionality`, `m_OutputScalarType`, `m_SlabNumberOfSlices`, `m_BackgroundLevel`, `m_BorderThickness`, `m_ScalarScale`, `m_ScalarShift`, `m_SlabSliceSpacingFraction`, `e_InterpolationMode`, `e_SlabMode`, `e_SplitMode`, `m_MinimumPieceSize`, `m_OutputExtent`, `m_BackgroundColor`, `m_MagnificationFactors`, `m_OutputOrigin`, `m_OutputSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageReslice
- **bl_idname**: `VTKImageResliceType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AutoCropOutput`, `m_Border`, `m_EnableSMP`, `m_GenerateStencilOutput`, `m_GlobalDefaultEnableSMP`, `m_Interpolate`, `m_Mirror`, `m_Optimization`, `m_SlabTrapezoidIntegration`, `m_TransformInputSampling`, `m_Wrap`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_OutputDimensionality`, `m_OutputScalarType`, `m_SlabNumberOfSlices`, `m_BackgroundLevel`, `m_BorderThickness`, `m_ScalarScale`, `m_ScalarShift`, `m_SlabSliceSpacingFraction`, `e_InterpolationMode`, `e_SlabMode`, `e_SplitMode`, `m_MinimumPieceSize`, `m_OutputExtent`, `m_BackgroundColor`, `m_OutputOrigin`, `m_OutputSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageResliceToColors
- **bl_idname**: `VTKImageResliceToColorsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AutoCropOutput`, `m_Border`, `m_Bypass`, `m_EnableSMP`, `m_GenerateStencilOutput`, `m_GlobalDefaultEnableSMP`, `m_Interpolate`, `m_Mirror`, `m_Optimization`, `m_SlabTrapezoidIntegration`, `m_TransformInputSampling`, `m_Wrap`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_OutputDimensionality`, `m_OutputScalarType`, `m_SlabNumberOfSlices`, `m_BackgroundLevel`, `m_BorderThickness`, `m_ScalarScale`, `m_ScalarShift`, `m_SlabSliceSpacingFraction`, `e_InterpolationMode`, `e_OutputFormat`, `e_SlabMode`, `e_SplitMode`, `m_MinimumPieceSize`, `m_OutputExtent`, `m_BackgroundColor`, `m_OutputOrigin`, `m_OutputSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageStencil
- **bl_idname**: `VTKImageStencilType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ReverseStencil`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_BackgroundValue`, `e_SplitMode`, `m_MinimumPieceSize`, `m_BackgroundColor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImprintFilter
- **bl_idname**: `VTKImprintFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_BoundaryEdgeInsertion`, `m_PassCellData`, `m_PassPointData`, `m_TriangulateOutput`, `m_ObjectName`, `m_DebugCellId`, `m_MergeTolerance`, `m_Tolerance`, `e_DebugOutputType`, `e_MergeToleranceType`, `e_OutputType`, `e_PointInterpolation`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkIntersectionPolyDataFilter
- **bl_idname**: `VTKIntersectionPolyDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_CheckInput`, `m_CheckMesh`, `m_ComputeIntersectionPointArray`, `m_SplitFirstOutput`, `m_SplitSecondOutput`, `m_ObjectName`, `m_RelativeSubtriangleArea`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkKMeansStatistics
- **bl_idname**: `VTKKMeansStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_TestOption`, `m_KValuesArrayName`, `m_ObjectName`, `m_DefaultNumberOfClusters`, `m_GhostsToSkip`, `m_MaxNumIterations`, `m_NumberOfPrimaryTables`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLagrangianParticleTracker
- **bl_idname**: `VTKLagrangianParticleTrackerType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AdaptiveStepReintegration`, `m_GenerateParticlePathsOutput`, `m_GeneratePolyVertexInteractionOutput`, `m_ObjectName`, `m_CellLengthComputationMode`, `m_MaximumNumberOfSteps`, `m_MaximumIntegrationTime`, `m_StepFactor`, `m_StepFactorMax`, `m_StepFactorMin`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLoopBooleanPolyDataFilter
- **bl_idname**: `VTKLoopBooleanPolyDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_NoIntersectionOutput`, `m_ObjectName`, `m_Tolerance`, `e_Operation`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMaskPointsFilter
- **bl_idname**: `VTKMaskPointsFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateOutliers`, `m_GenerateVertices`, `m_ObjectName`, `m_EmptyValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMergeFilter
- **bl_idname**: `VTKMergeFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMultiCorrelativeStatistics
- **bl_idname**: `VTKMultiCorrelativeStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_MedianAbsoluteDeviation`, `m_TestOption`, `m_ObjectName`, `m_GhostsToSkip`, `m_NumberOfPrimaryTables`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOrderStatistics
- **bl_idname**: `VTKOrderStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_Quantize`, `m_TestOption`, `m_ObjectName`, `m_GhostsToSkip`, `m_MaximumHistogramSize`, `m_NumberOfIntervals`, `m_NumberOfPrimaryTables`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPAutoCorrelativeStatistics
- **bl_idname**: `VTKPAutoCorrelativeStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_TestOption`, `m_ObjectName`, `m_NumberOfPrimaryTables`, `m_SliceCardinality`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPBivariateLinearTableThreshold
- **bl_idname**: `VTKPBivariateLinearTableThresholdType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_UseNormalizedDistance`, `m_ObjectName`, `m_Inclusive`, `m_DistanceThreshold`, `e_LinearThresholdType`, `m_ColumnRanges`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPCAStatistics
- **bl_idname**: `VTKPCAStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_MedianAbsoluteDeviation`, `m_TestOption`, `m_ObjectName`, `m_BasisScheme`, `m_FixedBasisSize`, `m_GhostsToSkip`, `m_NormalizationScheme`, `m_NumberOfPrimaryTables`, `m_FixedBasisEnergy`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPComputeHistogram2DOutliers
- **bl_idname**: `VTKPComputeHistogram2DOutliersType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ObjectName`, `m_PreferredNumberOfOutliers`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPContingencyStatistics
- **bl_idname**: `VTKPContingencyStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_TestOption`, `m_ObjectName`, `m_NumberOfPrimaryTables`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPCorrelativeStatistics
- **bl_idname**: `VTKPCorrelativeStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_TestOption`, `m_ObjectName`, `m_NumberOfPrimaryTables`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPDescriptiveStatistics
- **bl_idname**: `VTKPDescriptiveStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_G1Skewness`, `m_G2Kurtosis`, `m_LearnOption`, `m_SampleEstimate`, `m_SignedDeviations`, `m_TestOption`, `m_UnbiasedVariance`, `m_ObjectName`, `m_GhostsToSkip`, `m_NumberOfPrimaryTables`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPExtractHistogram2D
- **bl_idname**: `VTKPExtractHistogram2DType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_SwapColumns`, `m_TestOption`, `m_UseCustomHistogramExtents`, `m_ObjectName`, `m_NumberOfPrimaryTables`, `e_ScalarType`, `m_ComponentsToProcess`, `m_NumberOfBins`, `m_CustomHistogramExtents`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPKMeansStatistics
- **bl_idname**: `VTKPKMeansStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_TestOption`, `m_KValuesArrayName`, `m_ObjectName`, `m_DefaultNumberOfClusters`, `m_GhostsToSkip`, `m_MaxNumIterations`, `m_NumberOfPrimaryTables`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPMultiCorrelativeStatistics
- **bl_idname**: `VTKPMultiCorrelativeStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_MedianAbsoluteDeviation`, `m_TestOption`, `m_ObjectName`, `m_GhostsToSkip`, `m_NumberOfPrimaryTables`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPOrderStatistics
- **bl_idname**: `VTKPOrderStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_Quantize`, `m_TestOption`, `m_ObjectName`, `m_GhostsToSkip`, `m_MaximumHistogramSize`, `m_NumberOfIntervals`, `m_NumberOfPrimaryTables`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPPCAStatistics
- **bl_idname**: `VTKPPCAStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_MedianAbsoluteDeviation`, `m_TestOption`, `m_ObjectName`, `m_BasisScheme`, `m_FixedBasisSize`, `m_GhostsToSkip`, `m_NormalizationScheme`, `m_NumberOfPrimaryTables`, `m_FixedBasisEnergy`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPPairwiseExtractHistogram2D
- **bl_idname**: `VTKPPairwiseExtractHistogram2DType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_TestOption`, `m_ObjectName`, `m_NumberOfPrimaryTables`, `e_ScalarType`, `m_NumberOfBins`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPairwiseExtractHistogram2D
- **bl_idname**: `VTKPairwiseExtractHistogram2DType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_AssessOption`, `m_DeriveOption`, `m_LearnOption`, `m_TestOption`, `m_ObjectName`, `m_NumberOfPrimaryTables`, `e_ScalarType`, `m_NumberOfBins`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataPlaneClipper
- **bl_idname**: `VTKPolyDataPlaneClipperType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_Capping`, `m_ClippingLoops`, `m_PassCapPointData`, `m_ObjectName`, `m_BatchSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProgrammableSource
- **bl_idname**: `VTKProgrammableSourceType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRadiusOutlierRemoval
- **bl_idname**: `VTKRadiusOutlierRemovalType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateOutliers`, `m_GenerateVertices`, `m_ObjectName`, `m_NumberOfNeighbors`, `m_Radius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkResliceCursorPolyDataAlgorithm
- **bl_idname**: `VTKResliceCursorPolyDataAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ObjectName`, `e_ReslicePlaneNormal`, `m_SliceBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkScalarsToTextureFilter
- **bl_idname**: `VTKScalarsToTextureFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_UseTransferFunction`, `m_ObjectName`, `m_TextureDimensions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSelectPolyData
- **bl_idname**: `VTKSelectPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateSelectionScalars`, `m_GenerateUnselectedOutput`, `m_InsideOut`, `m_ObjectName`, `e_EdgeSearchMode`, `e_SelectionMode`, `m_ClosestPoint`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStatisticalOutlierRemoval
- **bl_idname**: `VTKStatisticalOutlierRemovalType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateOutliers`, `m_GenerateVertices`, `m_ObjectName`, `m_SampleSize`, `m_ComputedMean`, `m_ComputedStandardDeviation`, `m_StandardDeviationFactor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStreamingStatistics
- **bl_idname**: `VTKStreamingStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredGridLIC2D
- **bl_idname**: `VTKStructuredGridLIC2DType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ObjectName`, `m_Magnification`, `m_Steps`, `m_StepSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTableBasedClipDataSet
- **bl_idname**: `VTKTableBasedClipDataSetType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateClipScalars`, `m_GenerateClippedOutput`, `m_InsideOut`, `m_UseValueAsOffset`, `m_ObjectName`, `m_MergeTolerance`, `m_Value`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTemporalPathLineFilter
- **bl_idname**: `VTKTemporalPathLineFilterType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_BackwardTime`, `m_KeepDeadTrails`, `m_IdChannelArray`, `m_ObjectName`, `m_MaskPoints`, `m_MaxTrackLength`, `m_MaxStepDistance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVectorFieldTopology
- **bl_idname**: `VTKVectorFieldTopologyType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_ComputeSurfaces`, `m_ExcludeBoundary`, `m_UseBoundarySwitchPoints`, `m_UseIterativeSeeding`, `m_ObjectName`, `m_IntegrationStepUnit`, `m_MaxNumSteps`, `m_EpsilonCriticalPoint`, `m_IntegrationStepSize`, `m_OffsetAwayFromBoundary`, `m_SeparatrixDistance`, `m_VectorAngleThreshold`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVoronoi2D
- **bl_idname**: `VTKVoronoi2DType`
- **module**: `generated_nodes/gen_VTKFilters.py`
- **properties**: `m_GenerateVoronoiFlower`, `m_ObjectName`, `m_MaximumNumberOfTileClips`, `m_PointOfInterest`, `m_Padding`, `e_GenerateScalars`, `e_ProjectionPlaneMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

## Filter1

### vtk3DLinearGridCrinkleExtractor
- **bl_idname**: `VTK3DLinearGridCrinkleExtractorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CopyCellData`, `m_CopyPointData`, `m_RemoveUnusedPoints`, `m_SequentialProcessing`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtk3DLinearGridPlaneCutter
- **bl_idname**: `VTK3DLinearGridPlaneCutterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeNormals`, `m_InterpolateAttributes`, `m_MergePoints`, `m_SequentialProcessing`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAMRCutPlane
- **bl_idname**: `VTKAMRCutPlaneType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseNativeCutter`, `m_ObjectName`, `m_LevelOfResolution`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAMRResampleFilter
- **bl_idname**: `VTKAMRResampleFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseBiasVector`, `m_ObjectName`, `m_DemandDrivenMode`, `m_NumberOfPartitions`, `m_TransferToNodes`, `m_NumberOfSamples`, `m_BiasVector`, `m_Max`, `m_Min`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAMRSliceFilter
- **bl_idname**: `VTKAMRSliceFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_MaxResolution`, `m_Normal`, `m_OffsetFromOrigin`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAMRToMultiBlockFilter
- **bl_idname**: `VTKAMRToMultiBlockFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAdaptiveDataSetSurfaceFilter
- **bl_idname**: `VTKAdaptiveDataSetSurfaceFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_BBSelection`, `m_CellClipping`, `m_CircleSelection`, `m_Delegation`, `m_ExtentClipping`, `m_FastMode`, `m_Merging`, `m_PassThroughCellIds`, `m_PassThroughPointIds`, `m_PointClipping`, `m_RemoveGhostInterfaces`, `m_ViewPointDepend`, `m_ObjectName`, `m_OriginalCellIdsName`, `m_OriginalPointIdsName`, `m_CellMaximum`, `m_CellMinimum`, `m_Degree`, `m_DynamicDecimateLevelMax`, `m_FixedLevelMax`, `m_NonlinearSubdivisionLevel`, `m_PieceInvariant`, `m_PointMaximum`, `m_PointMinimum`, `m_Scale`, `m_Extent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAdaptiveResampleToImage
- **bl_idname**: `VTKAdaptiveResampleToImageType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfImages`, `m_SamplingDimensions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAdaptiveSubdivisionFilter
- **bl_idname**: `VTKAdaptiveSubdivisionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_MaximumNumberOfPasses`, `m_MaximumNumberOfTriangles`, `m_MaximumEdgeLength`, `m_MaximumTriangleArea`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAdaptiveTemporalInterpolator
- **bl_idname**: `VTKAdaptiveTemporalInterpolatorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CacheData`, `m_ObjectName`, `m_ResampleFactor`, `m_DiscreteTimeStepInterval`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAggregateDataSetFilter
- **bl_idname**: `VTKAggregateDataSetFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_MergePoints`, `m_ObjectName`, `m_NumberOfTargetProcesses`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAlignImageDataSetFilter
- **bl_idname**: `VTKAlignImageDataSetFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_MinimumExtent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAngularPeriodicFilter
- **bl_idname**: `VTKAngularPeriodicFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeRotationsOnTheFly`, `m_ObjectName`, `m_RotationArrayName`, `m_NumberOfPeriods`, `m_RotationAngle`, `e_IterationMode`, `e_RotationAxis`, `e_RotationMode`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAnimateModes
- **bl_idname**: `VTKAnimateModesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AnimateVibrations`, `m_DisplacementPreapplied`, `m_ObjectName`, `m_ModeShape`, `m_DisplacementMagnitude`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAnnotationLayersAlgorithm
- **bl_idname**: `VTKAnnotationLayersAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAppendArcLength
- **bl_idname**: `VTKAppendArcLengthType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAppendCompositeDataLeaves
- **bl_idname**: `VTKAppendCompositeDataLeavesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AppendFieldData`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAppendDataSets
- **bl_idname**: `VTKAppendDataSetsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_MergePoints`, `m_ToleranceIsAbsolute`, `m_ObjectName`, `m_OutputDataSetType`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAppendFilter
- **bl_idname**: `VTKAppendFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_MergePoints`, `m_ToleranceIsAbsolute`, `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAppendLocationAttributes
- **bl_idname**: `VTKAppendLocationAttributesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AppendCellCenters`, `m_AppendPointLocations`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAppendPoints
- **bl_idname**: `VTKAppendPointsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_InputIdArrayName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAppendPolyData
- **bl_idname**: `VTKAppendPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ParallelStreaming`, `m_UserManagedInputs`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAppendSelection
- **bl_idname**: `VTKAppendSelectionType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AppendByUnion`, `m_Inverse`, `m_UserManagedInputs`, `m_Expression`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkArcPlotter
- **bl_idname**: `VTKArcPlotterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseDefaultNormal`, `m_ObjectName`, `m_FieldDataArray`, `m_PlotComponent`, `m_Height`, `m_Offset`, `m_Radius`, `e_PlotMode`, `m_DefaultNormal`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkArrayCalculator
- **bl_idname**: `VTKArrayCalculatorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CoordinateResults`, `m_IgnoreMissingArrays`, `m_ReplaceInvalidValues`, `m_ResultNormals`, `m_ResultTCoords`, `m_Function`, `m_ObjectName`, `m_ResultArrayName`, `m_ResultArrayType`, `m_ReplacementValue`, `e_AttributeType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkArrayDataAlgorithm
- **bl_idname**: `VTKArrayDataAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkArrayRename
- **bl_idname**: `VTKArrayRenameType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAssignAttribute
- **bl_idname**: `VTKAssignAttributeType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAttributeDataToFieldDataFilter
- **bl_idname**: `VTKAttributeDataToFieldDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PassAttributeData`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBinnedDecimation
- **bl_idname**: `VTKBinnedDecimationType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutoAdjustNumberOfDivisions`, `m_ProduceCellData`, `m_ProducePointData`, `m_ObjectName`, `m_NumberOfXDivisions`, `m_NumberOfYDivisions`, `m_NumberOfZDivisions`, `e_PointGenerationMode`, `m_DivisionOrigin`, `m_DivisionSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBlankStructuredGrid
- **bl_idname**: `VTKBlankStructuredGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ArrayName`, `m_ObjectName`, `m_ArrayId`, `m_Component`, `m_MaxBlankingValue`, `m_MinBlankingValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBlockIdScalars
- **bl_idname**: `VTKBlockIdScalarsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBrownianPoints
- **bl_idname**: `VTKBrownianPointsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_MaximumSpeed`, `m_MinimumSpeed`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkButterflySubdivisionFilter
- **bl_idname**: `VTKButterflySubdivisionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CheckForTriangles`, `m_ObjectName`, `m_NumberOfSubdivisions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCastToConcrete
- **bl_idname**: `VTKCastToConcreteType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCellCenters
- **bl_idname**: `VTKCellCentersType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CopyArrays`, `m_VertexCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCellDataToPointData
- **bl_idname**: `VTKCellDataToPointDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PassCellData`, `m_ProcessAllArrays`, `m_ObjectName`, `m_ContributingCellOption`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCellDerivatives
- **bl_idname**: `VTKCellDerivativesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `e_TensorMode`, `e_VectorMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCellQuality
- **bl_idname**: `VTKCellQualityType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_UndefinedQuality`, `m_UnsupportedGeometry`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCellSizeFilter
- **bl_idname**: `VTKCellSizeFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeArea`, `m_ComputeLength`, `m_ComputeSum`, `m_ComputeVertexCount`, `m_ComputeVolume`, `m_AreaArrayName`, `m_LengthArrayName`, `m_ObjectName`, `m_VertexCountArrayName`, `m_VolumeArrayName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCellValidator
- **bl_idname**: `VTKCellValidatorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCheckerboardSplatter
- **bl_idname**: `VTKCheckerboardSplatterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Capping`, `m_NormalWarping`, `m_ScalarWarping`, `m_ObjectName`, `m_Footprint`, `m_MaximumDimension`, `m_ParallelSplatCrossover`, `m_CapValue`, `m_Eccentricity`, `m_ExponentFactor`, `m_NullValue`, `m_Radius`, `m_ScaleFactor`, `e_AccumulationMode`, `e_OutputScalarType`, `m_SampleDimensions`, `m_ModelBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCleanPolyData
- **bl_idname**: `VTKCleanPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ConvertLinesToPoints`, `m_ConvertPolysToLines`, `m_ConvertStripsToPolys`, `m_PieceInvariant`, `m_PointMerging`, `m_ToleranceIsAbsolute`, `m_ObjectName`, `m_AbsoluteTolerance`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkClipClosedSurface
- **bl_idname**: `VTKClipClosedSurfaceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateFaces`, `m_GenerateOutline`, `m_PassPointData`, `m_TriangulationErrorDisplay`, `m_ObjectName`, `m_ActivePlaneId`, `m_Tolerance`, `e_ScalarMode`, `m_ActivePlaneColor`, `m_BaseColor`, `m_ClipColor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkClipConvexPolyData
- **bl_idname**: `VTKClipConvexPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCollectGraph
- **bl_idname**: `VTKCollectGraphType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PassThrough`, `m_ObjectName`, `m_OutputType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCollectPolyData
- **bl_idname**: `VTKCollectPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PassThrough`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCollectTable
- **bl_idname**: `VTKCollectTableType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PassThrough`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCompositeCutter
- **bl_idname**: `VTKCompositeCutterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateCutScalars`, `m_GenerateTriangles`, `m_ObjectName`, `m_NumberOfContours`, `e_SortBy`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCompositeDataGeometryFilter
- **bl_idname**: `VTKCompositeDataGeometryFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCompositeDataSetAlgorithm
- **bl_idname**: `VTKCompositeDataSetAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkComputeQuantiles
- **bl_idname**: `VTKComputeQuantilesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfIntervals`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkComputeQuartiles
- **bl_idname**: `VTKComputeQuartilesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfIntervals`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkConnectedPointsFilter
- **bl_idname**: `VTKConnectedPointsFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AlignedNormals`, `m_ScalarConnectivity`, `m_ObjectName`, `m_NormalAngle`, `m_Radius`, `e_ExtractionMode`, `m_ClosestPoint`, `m_ScalarRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkConnectivityFilter
- **bl_idname**: `VTKConnectivityFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ColorRegions`, `m_ScalarConnectivity`, `m_ObjectName`, `m_RegionIdAssignmentMode`, `e_ExtractionMode`, `m_ClosestPoint`, `m_ScalarRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkConstrainedSmoothingFilter
- **bl_idname**: `VTKConstrainedSmoothingFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateErrorScalars`, `m_GenerateErrorVectors`, `m_ObjectName`, `m_NumberOfIterations`, `m_ConstraintDistance`, `m_Convergence`, `m_RelaxationFactor`, `e_ConstraintStrategy`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkContour3DLinearGrid
- **bl_idname**: `VTKContour3DLinearGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeNormals`, `m_ComputeScalars`, `m_InterpolateAttributes`, `m_MergePoints`, `m_SequentialProcessing`, `m_ObjectName`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkContourFilter
- **bl_idname**: `VTKContourFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_GenerateTriangles`, `m_ObjectName`, `m_ArrayComponent`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkContourGrid
- **bl_idname**: `VTKContourGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeNormals`, `m_ComputeScalars`, `m_GenerateTriangles`, `m_ObjectName`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkContourLoopExtraction
- **bl_idname**: `VTKContourLoopExtractionType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CleanPoints`, `m_ScalarThresholding`, `m_ObjectName`, `e_LoopClosure`, `e_OutputMode`, `m_Normal`, `m_ScalarRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkContourTriangulator
- **bl_idname**: `VTKContourTriangulatorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_TriangulationErrorDisplay`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkConvertToMultiBlockDataSet
- **bl_idname**: `VTKConvertToMultiBlockDataSetType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkConvertToPartitionedDataSetCollection
- **bl_idname**: `VTKConvertToPartitionedDataSetCollectionType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkConvertToPointCloud
- **bl_idname**: `VTKConvertToPointCloudType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_CellGenerationMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkConvertToPolyhedra
- **bl_idname**: `VTKConvertToPolyhedraType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_OutputAllCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCountFaces
- **bl_idname**: `VTKCountFacesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_OutputArrayName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCountVertices
- **bl_idname**: `VTKCountVerticesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_OutputArrayName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCurvatures
- **bl_idname**: `VTKCurvaturesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_InvertMeanCurvature`, `m_ObjectName`, `e_CurvatureType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCutMaterial
- **bl_idname**: `VTKCutMaterialType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ArrayName`, `m_MaterialArrayName`, `m_ObjectName`, `m_Material`, `m_UpVector`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCutter
- **bl_idname**: `VTKCutterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateCutScalars`, `m_GenerateTriangles`, `m_ObjectName`, `m_NumberOfContours`, `e_SortBy`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataObjectAlgorithm
- **bl_idname**: `VTKDataObjectAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataObjectToDataSetFilter
- **bl_idname**: `VTKDataObjectToDataSetFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_DefaultNormalize`, `m_ObjectName`, `e_DataSetType`, `m_Dimensions`, `m_Origin`, `m_Spacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataSetAlgorithm
- **bl_idname**: `VTKDataSetAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataSetGradient
- **bl_idname**: `VTKDataSetGradientType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_ResultArrayName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataSetGradientPrecompute
- **bl_idname**: `VTKDataSetGradientPrecomputeType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataSetRegionSurfaceFilter
- **bl_idname**: `VTKDataSetRegionSurfaceFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Delegation`, `m_FastMode`, `m_PassThroughCellIds`, `m_PassThroughPointIds`, `m_SingleSided`, `m_UseStrips`, `m_InterfaceIDsName`, `m_MaterialIDsName`, `m_MaterialPIDsName`, `m_MaterialPropertiesName`, `m_ObjectName`, `m_OriginalCellIdsName`, `m_OriginalPointIdsName`, `m_RegionArrayName`, `m_NonlinearSubdivisionLevel`, `m_PieceInvariant`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataSetSurfaceFilter
- **bl_idname**: `VTKDataSetSurfaceFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Delegation`, `m_FastMode`, `m_PassThroughCellIds`, `m_PassThroughPointIds`, `m_UseStrips`, `m_ObjectName`, `m_OriginalCellIdsName`, `m_OriginalPointIdsName`, `m_NonlinearSubdivisionLevel`, `m_PieceInvariant`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataSetToDataObjectFilter
- **bl_idname**: `VTKDataSetToDataObjectFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CellData`, `m_FieldData`, `m_Geometry`, `m_LegacyTopology`, `m_ModernTopology`, `m_PointData`, `m_Topology`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataSetTriangleFilter
- **bl_idname**: `VTKDataSetTriangleFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_TetrahedraOnly`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDateToNumeric
- **bl_idname**: `VTKDateToNumericType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_DateFormat`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDecimatePolylineFilter
- **bl_idname**: `VTKDecimatePolylineFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_MaximumError`, `m_TargetReduction`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDecimatePro
- **bl_idname**: `VTKDecimateProType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AccumulateError`, `m_BoundaryVertexDeletion`, `m_PreSplitMesh`, `m_PreserveTopology`, `m_Splitting`, `m_ObjectName`, `m_Degree`, `m_ErrorIsAbsolute`, `m_AbsoluteError`, `m_FeatureAngle`, `m_InflectionPointRatio`, `m_MaximumError`, `m_SplitAngle`, `m_TargetReduction`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDeflectNormals
- **bl_idname**: `VTKDeflectNormalsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseUserNormal`, `m_ObjectName`, `m_ScaleFactor`, `m_UserNormal`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDelaunay3D
- **bl_idname**: `VTKDelaunay3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AlphaLines`, `m_AlphaTets`, `m_AlphaTris`, `m_AlphaVerts`, `m_BoundingTriangulation`, `m_ObjectName`, `m_Alpha`, `m_Offset`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDensifyPointCloudFilter
- **bl_idname**: `VTKDensifyPointCloudFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_InterpolateAttributeData`, `m_ObjectName`, `m_MaximumNumberOfIterations`, `m_MaximumNumberOfPoints`, `m_NumberOfClosestPoints`, `m_Radius`, `m_TargetDistance`, `e_NeighborhoodType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDensifyPolyData
- **bl_idname**: `VTKDensifyPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfSubdivisions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDepthSortPolyData
- **bl_idname**: `VTKDepthSortPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_SortScalars`, `m_ObjectName`, `e_DepthSortMode`, `e_Direction`, `m_Origin`, `m_Vector`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDijkstraGraphGeodesicPath
- **bl_idname**: `VTKDijkstraGraphGeodesicPathType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_RepelPathFromVertices`, `m_StopWhenEndReached`, `m_UseScalarWeights`, `m_ObjectName`, `m_EndVertex`, `m_StartVertex`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDijkstraImageGeodesicPath
- **bl_idname**: `VTKDijkstraImageGeodesicPathType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_RepelPathFromVertices`, `m_StopWhenEndReached`, `m_UseScalarWeights`, `m_ObjectName`, `m_EndVertex`, `m_StartVertex`, `m_CurvatureWeight`, `m_EdgeLengthWeight`, `m_ImageWeight`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDirectedGraphAlgorithm
- **bl_idname**: `VTKDirectedGraphAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDiscreteFlyingEdges2D
- **bl_idname**: `VTKDiscreteFlyingEdges2DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeScalars`, `m_ObjectName`, `m_ArrayComponent`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDiscreteFlyingEdges3D
- **bl_idname**: `VTKDiscreteFlyingEdges3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_InterpolateAttributes`, `m_ObjectName`, `m_ArrayComponent`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDiscreteFlyingEdgesClipper2D
- **bl_idname**: `VTKDiscreteFlyingEdgesClipper2DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeScalars`, `m_ObjectName`, `m_ArrayComponent`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDiscreteMarchingCubes
- **bl_idname**: `VTKDiscreteMarchingCubesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeAdjacentScalars`, `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_ObjectName`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDistributedDataFilter
- **bl_idname**: `VTKDistributedDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ClipCells`, `m_IncludeAllIntersectingCells`, `m_RetainKdtree`, `m_Timing`, `m_UseMinimalMemory`, `m_ObjectName`, `m_MinimumGhostLevel`, `e_BoundaryMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDuplicatePolyData
- **bl_idname**: `VTKDuplicatePolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Synchronous`, `m_ObjectName`, `m_ClientFlag`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEdgePoints
- **bl_idname**: `VTKEdgePointsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Value`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkElevationFilter
- **bl_idname**: `VTKElevationFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_HighPoint`, `m_LowPoint`, `m_ScalarRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEuclideanClusterExtraction
- **bl_idname**: `VTKEuclideanClusterExtractionType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ColorClusters`, `m_ScalarConnectivity`, `m_ObjectName`, `m_Radius`, `e_ExtractionMode`, `m_ClosestPoint`, `m_ScalarRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEvenlySpacedStreamlines2D
- **bl_idname**: `VTKEvenlySpacedStreamlines2DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeVorticity`, `m_ObjectName`, `m_IntegrationStepUnit`, `m_MaximumNumberOfSteps`, `m_MinimumNumberOfLoopPoints`, `m_ClosedLoopMaximumDistance`, `m_InitialIntegrationStep`, `m_LoopAngle`, `m_SeparatingDistance`, `m_SeparatingDistanceRatio`, `m_TerminalSpeed`, `e_IntegratorType`, `m_StartPosition`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExpandMarkedElements
- **bl_idname**: `VTKExpandMarkedElementsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfLayers`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExplicitStructuredGridAlgorithm
- **bl_idname**: `VTKExplicitStructuredGridAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExplicitStructuredGridCrop
- **bl_idname**: `VTKExplicitStructuredGridCropType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExplicitStructuredGridSurfaceFilter
- **bl_idname**: `VTKExplicitStructuredGridSurfaceFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PassThroughCellIds`, `m_PassThroughPointIds`, `m_ObjectName`, `m_OriginalCellIdsName`, `m_OriginalPointIdsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExplicitStructuredGridToUnstructuredGrid
- **bl_idname**: `VTKExplicitStructuredGridToUnstructuredGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractArray
- **bl_idname**: `VTKExtractArrayType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Index`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractBlock
- **bl_idname**: `VTKExtractBlockType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_MaintainStructure`, `m_PruneOutput`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractBlockUsingDataAssembly
- **bl_idname**: `VTKExtractBlockUsingDataAssemblyType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PruneDataAssembly`, `m_SelectSubtrees`, `m_AssemblyName`, `m_ObjectName`, `m_Selector`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractCTHPart
- **bl_idname**: `VTKExtractCTHPartType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Capping`, `m_GenerateSolidGeometry`, `m_GenerateTriangles`, `m_RemoveGhostCells`, `m_ObjectName`, `m_VolumeFractionSurfaceValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractCells
- **bl_idname**: `VTKExtractCellsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AssumeSortedAndUniqueIds`, `m_ExtractAllCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractCellsByType
- **bl_idname**: `VTKExtractCellsByTypeType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractDataArraysOverTime
- **bl_idname**: `VTKExtractDataArraysOverTimeType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ReportStatisticsOnly`, `m_UseGlobalIDs`, `m_ObjectName`, `m_FieldAssociation`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractDataOverTime
- **bl_idname**: `VTKExtractDataOverTimeType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_PointIndex`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractDataSets
- **bl_idname**: `VTKExtractDataSetsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractEdges
- **bl_idname**: `VTKExtractEdgesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseAllPoints`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractExodusGlobalTemporalVariables
- **bl_idname**: `VTKExtractExodusGlobalTemporalVariablesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutoDetectGlobalTemporalDataArrays`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractGeometry
- **bl_idname**: `VTKExtractGeometryType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ExtractBoundaryCells`, `m_ExtractInside`, `m_ExtractOnlyBoundaryCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractGhostCells
- **bl_idname**: `VTKExtractGhostCellsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_OutputGhostArrayName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractGrid
- **bl_idname**: `VTKExtractGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_IncludeBoundary`, `m_ObjectName`, `m_SampleRate`, `m_VOI`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractHistogram
- **bl_idname**: `VTKExtractHistogramType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Accumulation`, `m_CalculateAverages`, `m_CenterBinsAroundMinAndMax`, `m_Normalize`, `m_UseCustomBinRanges`, `m_BinAccumulationArrayName`, `m_BinExtentsArrayName`, `m_BinValuesArrayName`, `m_ObjectName`, `m_BinCount`, `m_Component`, `m_CustomBinRanges`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractLevel
- **bl_idname**: `VTKExtractLevelType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractPiece
- **bl_idname**: `VTKExtractPieceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractPointCloudPiece
- **bl_idname**: `VTKExtractPointCloudPieceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ModuloOrdering`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractPolyDataGeometry
- **bl_idname**: `VTKExtractPolyDataGeometryType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ExtractBoundaryCells`, `m_ExtractInside`, `m_PassPoints`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractPolyDataPiece
- **bl_idname**: `VTKExtractPolyDataPieceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CreateGhostCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractRectilinearGrid
- **bl_idname**: `VTKExtractRectilinearGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_IncludeBoundary`, `m_ObjectName`, `m_SampleRate`, `m_VOI`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractSubsetWithSeed
- **bl_idname**: `VTKExtractSubsetWithSeedType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `e_Direction`, `m_Seed`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractSurface
- **bl_idname**: `VTKExtractSurfaceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_HoleFilling`, `m_ObjectName`, `m_Radius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractTensorComponents
- **bl_idname**: `VTKExtractTensorComponentsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ExtractNormals`, `m_ExtractScalars`, `m_ExtractTCoords`, `m_ExtractVectors`, `m_NormalizeNormals`, `m_PassTensorsToOutput`, `m_ObjectName`, `m_NumberOfTCoords`, `m_OutputPrecision`, `e_ScalarMode`, `m_NormalComponents`, `m_ScalarComponents`, `m_TCoordComponents`, `m_VectorComponents`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractTimeSteps
- **bl_idname**: `VTKExtractTimeStepsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseRange`, `m_ObjectName`, `m_TimeStepInterval`, `e_TimeEstimationMode`, `m_Range`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractUnstructuredGrid
- **bl_idname**: `VTKExtractUnstructuredGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CellClipping`, `m_ExtentClipping`, `m_Merging`, `m_PointClipping`, `m_ObjectName`, `m_CellMaximum`, `m_CellMinimum`, `m_PointMaximum`, `m_PointMinimum`, `m_Extent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractUnstructuredGridPiece
- **bl_idname**: `VTKExtractUnstructuredGridPieceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CreateGhostCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractUserDefinedPiece
- **bl_idname**: `VTKExtractUserDefinedPieceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CreateGhostCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractVOI
- **bl_idname**: `VTKExtractVOIType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_IncludeBoundary`, `m_ObjectName`, `m_SampleRate`, `m_VOI`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFeatureEdges
- **bl_idname**: `VTKFeatureEdgesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_BoundaryEdges`, `m_Coloring`, `m_FeatureEdges`, `m_ManifoldEdges`, `m_NonManifoldEdges`, `m_PassLines`, `m_RemoveGhostInterfaces`, `m_ObjectName`, `m_FeatureAngle`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFieldDataToAttributeDataFilter
- **bl_idname**: `VTKFieldDataToAttributeDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_DefaultNormalize`, `m_ObjectName`, `e_InputField`, `e_OutputAttributeData`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFillHolesFilter
- **bl_idname**: `VTKFillHolesFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_HoleSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFiniteElementFieldDistributor
- **bl_idname**: `VTKFiniteElementFieldDistributorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFlyingEdges2D
- **bl_idname**: `VTKFlyingEdges2DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeScalars`, `m_ObjectName`, `m_ArrayComponent`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFlyingEdges3D
- **bl_idname**: `VTKFlyingEdges3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_InterpolateAttributes`, `m_ObjectName`, `m_ArrayComponent`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFlyingEdgesPlaneCutter
- **bl_idname**: `VTKFlyingEdgesPlaneCutterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeNormals`, `m_InterpolateAttributes`, `m_ObjectName`, `m_ArrayComponent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkForceTime
- **bl_idname**: `VTKForceTimeType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_IgnorePipelineTime`, `m_ObjectName`, `m_ForcedTime`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGaussianSplatter
- **bl_idname**: `VTKGaussianSplatterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Capping`, `m_NormalWarping`, `m_ScalarWarping`, `m_ObjectName`, `m_CapValue`, `m_Eccentricity`, `m_ExponentFactor`, `m_NullValue`, `m_Radius`, `m_ScaleFactor`, `e_AccumulationMode`, `m_SampleDimensions`, `m_ModelBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenerateGlobalIds
- **bl_idname**: `VTKGenerateGlobalIdsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenerateTimeSteps
- **bl_idname**: `VTKGenerateTimeStepsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericContourFilter
- **bl_idname**: `VTKGenericContourFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_ObjectName`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericCutter
- **bl_idname**: `VTKGenericCutterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateCutScalars`, `m_ObjectName`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericDataSetTessellator
- **bl_idname**: `VTKGenericDataSetTessellatorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_KeepCellIds`, `m_Merging`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericGeometryFilter
- **bl_idname**: `VTKGenericGeometryFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CellClipping`, `m_ExtentClipping`, `m_Merging`, `m_PassThroughCellIds`, `m_PointClipping`, `m_ObjectName`, `m_CellMaximum`, `m_CellMinimum`, `m_PointMaximum`, `m_PointMinimum`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericOutlineFilter
- **bl_idname**: `VTKGenericOutlineFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGhostCellsGenerator
- **bl_idname**: `VTKGhostCellsGeneratorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_BuildIfRequired`, `m_ObjectName`, `m_NumberOfGhostLayers`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGradientFilter
- **bl_idname**: `VTKGradientFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeDivergence`, `m_ComputeGradient`, `m_ComputeQCriterion`, `m_ComputeVorticity`, `m_FasterApproximation`, `m_DivergenceArrayName`, `m_ObjectName`, `m_QCriterionArrayName`, `m_ResultArrayName`, `m_VorticityArrayName`, `m_ContributingCellOption`, `m_ReplacementValueOption`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGraphAlgorithm
- **bl_idname**: `VTKGraphAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGraphLayoutFilter
- **bl_idname**: `VTKGraphLayoutFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutomaticBoundsComputation`, `m_ThreeDimensionalLayout`, `m_ObjectName`, `m_MaxNumberOfIterations`, `m_CoolDownRate`, `m_GraphBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGraphToGlyphs
- **bl_idname**: `VTKGraphToGlyphsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Filled`, `m_Scaling`, `m_ObjectName`, `m_GlyphType`, `m_ScreenSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGraphToPoints
- **bl_idname**: `VTKGraphToPointsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGraphWeightEuclideanDistanceFilter
- **bl_idname**: `VTKGraphWeightEuclideanDistanceFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGreedyTerrainDecimation
- **bl_idname**: `VTKGreedyTerrainDecimationType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_BoundaryVertexDeletion`, `m_ComputeNormals`, `m_ObjectName`, `m_NumberOfTriangles`, `m_AbsoluteError`, `m_Reduction`, `m_RelativeError`, `e_ErrorMeasure`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGridSynchronizedTemplates3D
- **bl_idname**: `VTKGridSynchronizedTemplates3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_GenerateTriangles`, `m_ObjectName`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGroupDataSetsFilter
- **bl_idname**: `VTKGroupDataSetsFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `e_OutputType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGroupTimeStepsFilter
- **bl_idname**: `VTKGroupTimeStepsFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHedgeHog
- **bl_idname**: `VTKHedgeHogType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_ScaleFactor`, `e_VectorMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHierarchicalBinningFilter
- **bl_idname**: `VTKHierarchicalBinningFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Automatic`, `m_ObjectName`, `m_NumberOfLevels`, `m_Divisions`, `m_Bounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHierarchicalBoxDataSetAlgorithm
- **bl_idname**: `VTKHierarchicalBoxDataSetAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHierarchicalDataExtractDataSets
- **bl_idname**: `VTKHierarchicalDataExtractDataSetsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHierarchicalDataExtractLevel
- **bl_idname**: `VTKHierarchicalDataExtractLevelType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHierarchicalDataLevelFilter
- **bl_idname**: `VTKHierarchicalDataLevelFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHierarchicalDataSetGeometryFilter
- **bl_idname**: `VTKHierarchicalDataSetGeometryFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHull
- **bl_idname**: `VTKHullType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperStreamline
- **bl_idname**: `VTKHyperStreamlineType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_LogScaling`, `m_ObjectName`, `m_NumberOfSides`, `m_IntegrationStepLength`, `m_MaximumPropagationDistance`, `m_Radius`, `m_StepLength`, `m_TerminalEigenvalue`, `e_IntegrationDirection`, `e_IntegrationEigenvector`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridAxisClip
- **bl_idname**: `VTKHyperTreeGridAxisClipType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_InsideOut`, `m_ObjectName`, `m_PlaneNormalAxis`, `m_PlanePosition`, `e_ClipType`, `m_Bounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridAxisCut
- **bl_idname**: `VTKHyperTreeGridAxisCutType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_PlaneNormalAxis`, `m_PlanePosition`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridAxisReflection
- **bl_idname**: `VTKHyperTreeGridAxisReflectionType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Center`, `e_Plane`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridCellCenters
- **bl_idname**: `VTKHyperTreeGridCellCentersType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CopyArrays`, `m_VertexCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridContour
- **bl_idname**: `VTKHyperTreeGridContourType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridDepthLimiter
- **bl_idname**: `VTKHyperTreeGridDepthLimiterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_JustCreateNewMask`, `m_ObjectName`, `m_Depth`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridEvaluateCoarse
- **bl_idname**: `VTKHyperTreeGridEvaluateCoarseType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Operator`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridGeometry
- **bl_idname**: `VTKHyperTreeGridGeometryType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Merging`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridGhostCellsGenerator
- **bl_idname**: `VTKHyperTreeGridGhostCellsGeneratorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridGradient
- **bl_idname**: `VTKHyperTreeGridGradientType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_ResultArrayName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridOutlineFilter
- **bl_idname**: `VTKHyperTreeGridOutlineFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateFaces`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridPlaneCutter
- **bl_idname**: `VTKHyperTreeGridPlaneCutterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Dual`, `m_ObjectName`, `m_Plane`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridThreshold
- **bl_idname**: `VTKHyperTreeGridThresholdType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_JustCreateNewMask`, `m_ObjectName`, `m_LowerThreshold`, `m_UpperThreshold`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridToDualGrid
- **bl_idname**: `VTKHyperTreeGridToDualGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridToUnstructuredGrid
- **bl_idname**: `VTKHyperTreeGridToUnstructuredGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AddOriginalIds`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkIconGlyphFilter
- **bl_idname**: `VTKIconGlyphFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PassScalars`, `m_UseIconSize`, `m_ObjectName`, `e_Gravity`, `e_IconScaling`, `m_DisplaySize`, `m_IconSheetSize`, `m_IconSize`, `m_Offset`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkIdFilter
- **bl_idname**: `VTKIdFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CellIds`, `m_FieldData`, `m_PointIds`, `m_CellIdsArrayName`, `m_ObjectName`, `m_PointIdsArrayName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageAnisotropicDiffusion2D
- **bl_idname**: `VTKImageAnisotropicDiffusion2DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Corners`, `m_Edges`, `m_EnableSMP`, `m_Faces`, `m_GlobalDefaultEnableSMP`, `m_GradientMagnitudeThreshold`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfIterations`, `m_NumberOfThreads`, `m_DiffusionFactor`, `m_DiffusionThreshold`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageAnisotropicDiffusion3D
- **bl_idname**: `VTKImageAnisotropicDiffusion3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Corners`, `m_Edges`, `m_EnableSMP`, `m_Faces`, `m_GlobalDefaultEnableSMP`, `m_GradientMagnitudeThreshold`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfIterations`, `m_NumberOfThreads`, `m_DiffusionFactor`, `m_DiffusionThreshold`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageAppend
- **bl_idname**: `VTKImageAppendType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_PreserveExtents`, `m_ObjectName`, `m_AppendAxis`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageAppendComponents
- **bl_idname**: `VTKImageAppendComponentsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageBSplineCoefficients
- **bl_idname**: `VTKImageBSplineCoefficientsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Bypass`, `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_SplineDegree`, `e_OutputScalarType`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageButterworthHighPass
- **bl_idname**: `VTKImageButterworthHighPassType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Order`, `m_XCutOff`, `m_YCutOff`, `m_ZCutOff`, `e_SplitMode`, `m_MinimumPieceSize`, `m_CutOff`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageButterworthLowPass
- **bl_idname**: `VTKImageButterworthLowPassType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Order`, `m_XCutOff`, `m_YCutOff`, `m_ZCutOff`, `e_SplitMode`, `m_MinimumPieceSize`, `m_CutOff`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageCacheFilter
- **bl_idname**: `VTKImageCacheFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_CacheSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageCast
- **bl_idname**: `VTKImageCastType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ClampOverflow`, `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_OutputScalarType`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageCityBlockDistance
- **bl_idname**: `VTKImageCityBlockDistanceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageClip
- **bl_idname**: `VTKImageClipType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ClipData`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageConstantPad
- **bl_idname**: `VTKImageConstantPadType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_OutputNumberOfScalarComponents`, `m_Constant`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageContinuousDilate3D
- **bl_idname**: `VTKImageContinuousDilate3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_KernelSize`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageContinuousErode3D
- **bl_idname**: `VTKImageContinuousErode3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_KernelSize`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageConvolve
- **bl_idname**: `VTKImageConvolveType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageCursor3D
- **bl_idname**: `VTKImageCursor3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_CursorRadius`, `m_CursorValue`, `m_CursorPosition`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDataGeometryFilter
- **bl_idname**: `VTKImageDataGeometryFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_OutputTriangles`, `m_ThresholdCells`, `m_ThresholdValue`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDataOutlineFilter
- **bl_idname**: `VTKImageDataOutlineFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateFaces`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDataStreamer
- **bl_idname**: `VTKImageDataStreamerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfStreamDivisions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDataToExplicitStructuredGrid
- **bl_idname**: `VTKImageDataToExplicitStructuredGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDataToHyperTreeGrid
- **bl_idname**: `VTKImageDataToHyperTreeGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_DepthMax`, `m_NbColors`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDataToPointSet
- **bl_idname**: `VTKImageDataToPointSetType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDataToUniformGrid
- **bl_idname**: `VTKImageDataToUniformGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Reverse`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDilateErode3D
- **bl_idname**: `VTKImageDilateErode3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_DilateValue`, `m_ErodeValue`, `e_SplitMode`, `m_KernelSize`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDivergence
- **bl_idname**: `VTKImageDivergenceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageEuclideanDistance
- **bl_idname**: `VTKImageEuclideanDistanceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ConsiderAnisotropy`, `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_Initialize`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `m_MaximumDistance`, `e_Algorithm`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageEuclideanToPolar
- **bl_idname**: `VTKImageEuclideanToPolarType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_ThetaMaximum`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageExtractComponents
- **bl_idname**: `VTKImageExtractComponentsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageFFT
- **bl_idname**: `VTKImageFFTType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageFourierCenter
- **bl_idname**: `VTKImageFourierCenterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageGaussianSmooth
- **bl_idname**: `VTKImageGaussianSmoothType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`, `m_RadiusFactors`, `m_StandardDeviations`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageGradient
- **bl_idname**: `VTKImageGradientType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_HandleBoundaries`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageGradientMagnitude
- **bl_idname**: `VTKImageGradientMagnitudeType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_HandleBoundaries`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageHSIToRGB
- **bl_idname**: `VTKImageHSIToRGBType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Maximum`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageHSVToRGB
- **bl_idname**: `VTKImageHSVToRGBType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Maximum`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageHybridMedian2D
- **bl_idname**: `VTKImageHybridMedian2DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageIdealHighPass
- **bl_idname**: `VTKImageIdealHighPassType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_XCutOff`, `m_YCutOff`, `m_ZCutOff`, `e_SplitMode`, `m_MinimumPieceSize`, `m_CutOff`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageIdealLowPass
- **bl_idname**: `VTKImageIdealLowPassType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_XCutOff`, `m_YCutOff`, `m_ZCutOff`, `e_SplitMode`, `m_MinimumPieceSize`, `m_CutOff`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageIslandRemoval2D
- **bl_idname**: `VTKImageIslandRemoval2DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_SquareNeighborhood`, `m_ObjectName`, `m_AreaThreshold`, `m_IslandValue`, `m_ReplaceValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageLaplacian
- **bl_idname**: `VTKImageLaplacianType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageLogarithmicScale
- **bl_idname**: `VTKImageLogarithmicScaleType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Constant`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageLuminance
- **bl_idname**: `VTKImageLuminanceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMagnify
- **bl_idname**: `VTKImageMagnifyType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_Interpolate`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MagnificationFactors`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMagnitude
- **bl_idname**: `VTKImageMagnitudeType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMapToColors
- **bl_idname**: `VTKImageMapToColorsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_PassAlphaToOutput`, `m_ObjectName`, `m_ActiveComponent`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_OutputFormat`, `e_SplitMode`, `m_MinimumPieceSize`, `m_NaNColor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMapToRGBA
- **bl_idname**: `VTKImageMapToRGBAType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_PassAlphaToOutput`, `m_ObjectName`, `m_ActiveComponent`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_OutputFormat`, `e_SplitMode`, `m_MinimumPieceSize`, `m_NaNColor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMapToWindowLevelColors
- **bl_idname**: `VTKImageMapToWindowLevelColorsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_PassAlphaToOutput`, `m_ObjectName`, `m_ActiveComponent`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Level`, `m_Window`, `e_OutputFormat`, `e_SplitMode`, `m_MinimumPieceSize`, `m_NaNColor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMarchingCubes
- **bl_idname**: `VTKImageMarchingCubesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_ObjectName`, `m_InputMemoryLimit`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMaskBits
- **bl_idname**: `VTKImageMaskBitsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_Operation`, `e_SplitMode`, `m_Masks`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMathematics
- **bl_idname**: `VTKImageMathematicsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_DivideByZeroToC`, `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_ConstantC`, `m_ConstantK`, `e_Operation`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMedian3D
- **bl_idname**: `VTKImageMedian3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_KernelSize`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMirrorPad
- **bl_idname**: `VTKImageMirrorPadType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_OutputNumberOfScalarComponents`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageNormalize
- **bl_idname**: `VTKImageNormalizeType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageOpenClose3D
- **bl_idname**: `VTKImageOpenClose3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_CloseValue`, `m_OpenValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImagePadFilter
- **bl_idname**: `VTKImagePadFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_OutputNumberOfScalarComponents`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageQuantizeRGBToIndex
- **bl_idname**: `VTKImageQuantizeRGBToIndexType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_SortIndexByLuminance`, `m_ObjectName`, `m_NumberOfColors`, `m_BuildTreeExecuteTime`, `m_InitializeExecuteTime`, `m_LookupIndexExecuteTime`, `m_SamplingRate`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageRFFT
- **bl_idname**: `VTKImageRFFTType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageRGBToHSI
- **bl_idname**: `VTKImageRGBToHSIType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Maximum`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageRGBToHSV
- **bl_idname**: `VTKImageRGBToHSVType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Maximum`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageRGBToYIQ
- **bl_idname**: `VTKImageRGBToYIQType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Maximum`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageRange3D
- **bl_idname**: `VTKImageRange3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_KernelSize`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageResize
- **bl_idname**: `VTKImageResizeType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Border`, `m_Cropping`, `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_Interpolate`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_ResizeMethod`, `e_SplitMode`, `m_MinimumPieceSize`, `m_OutputDimensions`, `m_MagnificationFactors`, `m_OutputSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageSeedConnectivity
- **bl_idname**: `VTKImageSeedConnectivityType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Dimensionality`, `m_InputConnectValue`, `m_OutputConnectedValue`, `m_OutputUnconnectedValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageSeparableConvolution
- **bl_idname**: `VTKImageSeparableConvolutionType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageShiftScale
- **bl_idname**: `VTKImageShiftScaleType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ClampOverflow`, `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Scale`, `m_Shift`, `e_OutputScalarType`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageShrink3D
- **bl_idname**: `VTKImageShrink3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Averaging`, `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_Maximum`, `m_Mean`, `m_Median`, `m_Minimum`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`, `m_Shift`, `m_ShrinkFactors`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageSkeleton2D
- **bl_idname**: `VTKImageSkeleton2DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_Prune`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfIterations`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageSlab
- **bl_idname**: `VTKImageSlabType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_MultiSliceOutput`, `m_TrapezoidIntegration`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_Operation`, `e_Orientation`, `e_SplitMode`, `m_MinimumPieceSize`, `m_SliceRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageSobel2D
- **bl_idname**: `VTKImageSobel2DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageSobel3D
- **bl_idname**: `VTKImageSobel3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageSpatialAlgorithm
- **bl_idname**: `VTKImageSpatialAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageStencilAlgorithm
- **bl_idname**: `VTKImageStencilAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageStencilSource
- **bl_idname**: `VTKImageStencilSourceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_OutputWholeExtent`, `m_OutputOrigin`, `m_OutputSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageStencilToImage
- **bl_idname**: `VTKImageStencilToImageType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_InsideValue`, `m_OutsideValue`, `e_OutputScalarType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageThreshold
- **bl_idname**: `VTKImageThresholdType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ReplaceIn`, `m_ReplaceOut`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_InValue`, `m_OutValue`, `e_OutputScalarType`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageToAMR
- **bl_idname**: `VTKImageToAMRType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_MaximumNumberOfBlocks`, `m_NumberOfLevels`, `m_RefinementRatio`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageToImageStencil
- **bl_idname**: `VTKImageToImageStencilType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_LowerThreshold`, `m_UpperThreshold`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageToPolyDataFilter
- **bl_idname**: `VTKImageToPolyDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Decimation`, `m_Smoothing`, `m_ObjectName`, `m_Error`, `m_NumberOfSmoothingIterations`, `m_SubImageSize`, `m_DecimationError`, `e_ColorMode`, `e_OutputStyle`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageToStructuredGrid
- **bl_idname**: `VTKImageToStructuredGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageTranslateExtent
- **bl_idname**: `VTKImageTranslateExtentType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Translation`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageVariance3D
- **bl_idname**: `VTKImageVariance3DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_KernelSize`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageWeightedSum
- **bl_idname**: `VTKImageWeightedSumType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_NormalizeByWeight`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageWrapPad
- **bl_idname**: `VTKImageWrapPadType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_OutputNumberOfScalarComponents`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageYIQToRGB
- **bl_idname**: `VTKImageYIQToRGBType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Maximum`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitModeller
- **bl_idname**: `VTKImplicitModellerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AdjustBounds`, `m_Capping`, `m_ScaleToMaximumDistance`, `m_ObjectName`, `m_LocatorMaxLevel`, `m_NumberOfThreads`, `m_AdjustDistance`, `m_CapValue`, `m_MaximumDistance`, `e_OutputScalarType`, `e_ProcessMode`, `m_SampleDimensions`, `m_ModelBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitTextureCoords
- **bl_idname**: `VTKImplicitTextureCoordsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_FlipTexture`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkIntegrateAttributes
- **bl_idname**: `VTKIntegrateAttributesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_DivideAllCellDataByVolume`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkInterpolateDataSetAttributes
- **bl_idname**: `VTKInterpolateDataSetAttributesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_T`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkKdTreeSelector
- **bl_idname**: `VTKKdTreeSelectorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_SingleSelection`, `m_ObjectName`, `m_SelectionFieldName`, `m_SelectionAttribute`, `m_SingleSelectionThreshold`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLabelHierarchyAlgorithm
- **bl_idname**: `VTKLabelHierarchyAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLabelSizeCalculator
- **bl_idname**: `VTKLabelSizeCalculatorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_LabelSizeArrayName`, `m_ObjectName`, `m_DPI`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLengthDistribution
- **bl_idname**: `VTKLengthDistributionType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_SortSample`, `m_ObjectName`, `m_SampleSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLevelIdScalars
- **bl_idname**: `VTKLevelIdScalarsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLinearCellExtrusionFilter
- **bl_idname**: `VTKLinearCellExtrusionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_MergeDuplicatePoints`, `m_UseUserVector`, `m_ObjectName`, `m_ScaleFactor`, `m_UserVector`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLinearExtrusionFilter
- **bl_idname**: `VTKLinearExtrusionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Capping`, `m_ObjectName`, `m_ScaleFactor`, `e_ExtrusionType`, `m_ExtrusionPoint`, `m_Vector`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLinearSelector
- **bl_idname**: `VTKLinearSelectorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_IncludeVertices`, `m_ObjectName`, `m_Tolerance`, `m_VertexEliminationTolerance`, `m_EndPoint`, `m_StartPoint`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLinearSubdivisionFilter
- **bl_idname**: `VTKLinearSubdivisionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CheckForTriangles`, `m_ObjectName`, `m_NumberOfSubdivisions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLinearToQuadraticCellsFilter
- **bl_idname**: `VTKLinearToQuadraticCellsFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLinkEdgels
- **bl_idname**: `VTKLinkEdgelsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_GradientThreshold`, `m_LinkThreshold`, `m_PhiThreshold`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLoopSubdivisionFilter
- **bl_idname**: `VTKLoopSubdivisionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CheckForTriangles`, `m_ObjectName`, `m_NumberOfSubdivisions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMapArrayValues
- **bl_idname**: `VTKMapArrayValuesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PassArray`, `m_InputArrayName`, `m_ObjectName`, `m_OutputArrayName`, `m_FieldType`, `m_OutputArrayType`, `m_FillValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMarchingContourFilter
- **bl_idname**: `VTKMarchingContourFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_ObjectName`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMarchingCubes
- **bl_idname**: `VTKMarchingCubesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_ObjectName`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMarchingSquares
- **bl_idname**: `VTKMarchingSquaresType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMarkBoundaryFilter
- **bl_idname**: `VTKMarkBoundaryFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateBoundaryFaces`, `m_BoundaryCellsName`, `m_BoundaryFacesName`, `m_BoundaryPointsName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMaskFields
- **bl_idname**: `VTKMaskFieldsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMaskPoints
- **bl_idname**: `VTKMaskPointsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateVertices`, `m_ProportionalMaximumNumberOfPoints`, `m_RandomMode`, `m_SingleVertexPerCell`, `m_ObjectName`, `m_MaximumNumberOfPoints`, `m_Offset`, `m_OnRatio`, `m_RandomModeType`, `m_RandomSeed`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMaskPolyData
- **bl_idname**: `VTKMaskPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Offset`, `m_OnRatio`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMatricizeArray
- **bl_idname**: `VTKMatricizeArrayType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_SliceDimension`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMatrixMathFilter
- **bl_idname**: `VTKMatrixMathFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `e_Operation`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMemoryLimitImageDataStreamer
- **bl_idname**: `VTKMemoryLimitImageDataStreamerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_MemoryLimit`, `m_NumberOfStreamDivisions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMergeArrays
- **bl_idname**: `VTKMergeArraysType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMergeFields
- **bl_idname**: `VTKMergeFieldsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfComponents`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMergeTimeFilter
- **bl_idname**: `VTKMergeTimeFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseIntersection`, `m_UseRelativeTolerance`, `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMergeVectorComponents
- **bl_idname**: `VTKMergeVectorComponentsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_OutputVectorName`, `m_XArrayName`, `m_YArrayName`, `m_ZArrayName`, `e_AttributeType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMeshQuality
- **bl_idname**: `VTKMeshQualityType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CompatibilityMode`, `m_LinearApproximation`, `m_Ratio`, `m_SaveCellQuality`, `m_Volume`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMoleculeAlgorithm
- **bl_idname**: `VTKMoleculeAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMoleculeAppend
- **bl_idname**: `VTKMoleculeAppendType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_MergeCoincidentAtoms`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMoleculeToAtomBallFilter
- **bl_idname**: `VTKMoleculeToAtomBallFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_RadiusSource`, `m_Resolution`, `m_RadiusScale`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMoleculeToBondStickFilter
- **bl_idname**: `VTKMoleculeToBondStickFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMoleculeToLinesFilter
- **bl_idname**: `VTKMoleculeToLinesFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMultiBlockDataGroupFilter
- **bl_idname**: `VTKMultiBlockDataGroupFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMultiBlockDataSetAlgorithm
- **bl_idname**: `VTKMultiBlockDataSetAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMultiBlockFromTimeSeriesFilter
- **bl_idname**: `VTKMultiBlockFromTimeSeriesFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMultiBlockMergeFilter
- **bl_idname**: `VTKMultiBlockMergeFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMultiObjectMassProperties
- **bl_idname**: `VTKMultiObjectMassPropertiesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_SkipValidityCheck`, `m_ObjectIdsArrayName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMultiThreshold
- **bl_idname**: `VTKMultiThresholdType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkNonOverlappingAMRAlgorithm
- **bl_idname**: `VTKNonOverlappingAMRAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkNormalizeMatrixVectors
- **bl_idname**: `VTKNormalizeMatrixVectorsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_VectorDimension`, `m_PValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOBBDicer
- **bl_idname**: `VTKOBBDicerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_FieldData`, `m_ObjectName`, `m_MemoryLimit`, `m_NumberOfPieces`, `m_NumberOfPointsPerPiece`, `e_DiceMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOpenGLImageGradient
- **bl_idname**: `VTKOpenGLImageGradientType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_HandleBoundaries`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOutlineCornerFilter
- **bl_idname**: `VTKOutlineCornerFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_CornerFactor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOutlineFilter
- **bl_idname**: `VTKOutlineFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateFaces`, `m_ObjectName`, `e_CompositeStyle`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOverlappingAMRAlgorithm
- **bl_idname**: `VTKOverlappingAMRAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOverlappingAMRLevelIdScalars
- **bl_idname**: `VTKOverlappingAMRLevelIdScalarsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOverlappingCellsDetector
- **bl_idname**: `VTKOverlappingCellsDetectorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_NumberOfOverlapsPerCellArrayName`, `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPCAAnalysisFilter
- **bl_idname**: `VTKPCAAnalysisFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPCACurvatureEstimation
- **bl_idname**: `VTKPCACurvatureEstimationType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_SampleSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPCANormalEstimation
- **bl_idname**: `VTKPCANormalEstimationType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_FlipNormals`, `m_ObjectName`, `m_SampleSize`, `e_NormalOrientation`, `m_OrientationPoint`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPCellDataToPointData
- **bl_idname**: `VTKPCellDataToPointDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PassCellData`, `m_PieceInvariant`, `m_ProcessAllArrays`, `m_ObjectName`, `m_ContributingCellOption`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPComputeQuantiles
- **bl_idname**: `VTKPComputeQuantilesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfIntervals`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPComputeQuartiles
- **bl_idname**: `VTKPComputeQuartilesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfIntervals`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPConvertToMultiBlockDataSet
- **bl_idname**: `VTKPConvertToMultiBlockDataSetType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPExtractDataArraysOverTime
- **bl_idname**: `VTKPExtractDataArraysOverTimeType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ReportStatisticsOnly`, `m_UseGlobalIDs`, `m_ObjectName`, `m_FieldAssociation`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPExtractExodusGlobalTemporalVariables
- **bl_idname**: `VTKPExtractExodusGlobalTemporalVariablesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutoDetectGlobalTemporalDataArrays`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPLinearExtrusionFilter
- **bl_idname**: `VTKPLinearExtrusionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Capping`, `m_PieceInvariant`, `m_ObjectName`, `m_ScaleFactor`, `e_ExtrusionType`, `m_ExtrusionPoint`, `m_Vector`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPMaskPoints
- **bl_idname**: `VTKPMaskPointsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateVertices`, `m_ProportionalMaximumNumberOfPoints`, `m_RandomMode`, `m_SingleVertexPerCell`, `m_ObjectName`, `m_MaximumNumberOfPoints`, `m_Offset`, `m_OnRatio`, `m_RandomModeType`, `m_RandomSeed`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPMergeArrays
- **bl_idname**: `VTKPMergeArraysType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPOutlineCornerFilter
- **bl_idname**: `VTKPOutlineCornerFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_CornerFactor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPOutlineFilter
- **bl_idname**: `VTKPOutlineFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPPolyDataNormals
- **bl_idname**: `VTKPPolyDataNormalsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutoOrientNormals`, `m_ComputeCellNormals`, `m_ComputePointNormals`, `m_Consistency`, `m_FlipNormals`, `m_NonManifoldTraversal`, `m_PieceInvariant`, `m_Splitting`, `m_ObjectName`, `m_FeatureAngle`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPProjectSphereFilter
- **bl_idname**: `VTKPProjectSphereFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_KeepPolePoints`, `m_TranslateZ`, `m_ObjectName`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPReflectionFilter
- **bl_idname**: `VTKPReflectionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CopyInput`, `m_FlipAllInputArrays`, `m_ObjectName`, `m_Center`, `e_Plane`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPResampleFilter
- **bl_idname**: `VTKPResampleFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseInputBounds`, `m_ObjectName`, `m_SamplingDimension`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPResampleToImage
- **bl_idname**: `VTKPResampleToImageType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseInputBounds`, `m_ObjectName`, `m_SamplingDimensions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPTextureMapToSphere
- **bl_idname**: `VTKPTextureMapToSphereType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutomaticSphereGeneration`, `m_PreventSeam`, `m_ObjectName`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPYoungsMaterialInterface
- **bl_idname**: `VTKPYoungsMaterialInterfaceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AxisSymetric`, `m_FillMaterial`, `m_InverseNormal`, `m_OnionPeel`, `m_ReverseMaterialOrder`, `m_UseAllBlocks`, `m_UseFractionAsDistance`, `m_ObjectName`, `m_NumberOfMaterials`, `m_VolumeFractionRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParallelVectors
- **bl_idname**: `VTKParallelVectorsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_FirstVectorFieldName`, `m_ObjectName`, `m_SecondVectorFieldName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPartitionBalancer
- **bl_idname**: `VTKPartitionBalancerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `e_Mode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPassArrays
- **bl_idname**: `VTKPassArraysType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_RemoveArrays`, `m_UseFieldTypes`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPassInputTypeAlgorithm
- **bl_idname**: `VTKPassInputTypeAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPassSelectedArrays
- **bl_idname**: `VTKPassSelectedArraysType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Enabled`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPassThrough
- **bl_idname**: `VTKPassThroughType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AllowNullInput`, `m_DeepCopyInput`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPassThroughFilter
- **bl_idname**: `VTKPassThroughFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPieceRequestFilter
- **bl_idname**: `VTKPieceRequestFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfPieces`, `m_Piece`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPieceScalars
- **bl_idname**: `VTKPieceScalarsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_RandomMode`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPiecewiseFunctionAlgorithm
- **bl_idname**: `VTKPiecewiseFunctionAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPiecewiseFunctionShiftScale
- **bl_idname**: `VTKPiecewiseFunctionShiftScaleType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_PositionScale`, `m_PositionShift`, `m_ValueScale`, `m_ValueShift`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPlaneCutter
- **bl_idname**: `VTKPlaneCutterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_BuildHierarchy`, `m_BuildTree`, `m_ComputeNormals`, `m_GeneratePolygons`, `m_InterpolateAttributes`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointConnectivityFilter
- **bl_idname**: `VTKPointConnectivityFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointDataToCellData
- **bl_idname**: `VTKPointDataToCellDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CategoricalData`, `m_PassPointData`, `m_ProcessAllArrays`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointDensityFilter
- **bl_idname**: `VTKPointDensityFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradient`, `m_ScalarWeighting`, `m_ObjectName`, `m_AdjustDistance`, `m_Radius`, `m_RelativeRadius`, `e_DensityEstimate`, `e_DensityForm`, `m_SampleDimensions`, `m_ModelBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointOccupancyFilter
- **bl_idname**: `VTKPointOccupancyFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_EmptyValue`, `m_OccupiedValue`, `m_SampleDimensions`, `m_ModelBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointSetAlgorithm
- **bl_idname**: `VTKPointSetAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointSetToLabelHierarchy
- **bl_idname**: `VTKPointSetToLabelHierarchyType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_BoundedSizeArrayName`, `m_IconIndexArrayName`, `m_LabelArrayName`, `m_ObjectName`, `m_OrientationArrayName`, `m_PriorityArrayName`, `m_SizeArrayName`, `m_MaximumDepth`, `m_TargetLabelCount`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointSetToMoleculeFilter
- **bl_idname**: `VTKPointSetToMoleculeFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ConvertLinesIntoBonds`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointSmoothingFilter
- **bl_idname**: `VTKPointSmoothingFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputePackingRadius`, `m_EnableConstraints`, `m_GenerateConstraintNormals`, `m_GenerateConstraintScalars`, `m_ObjectName`, `m_NeighborhoodSize`, `m_NumberOfIterations`, `m_NumberOfSubIterations`, `m_AttractionFactor`, `m_BoundaryAngle`, `m_Convergence`, `m_FixedAngle`, `m_MaximumStepSize`, `m_PackingFactor`, `m_PackingRadius`, `e_MotionConstraint`, `e_SmoothingMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPoissonDiskSampler
- **bl_idname**: `VTKPoissonDiskSamplerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Radius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataAlgorithm
- **bl_idname**: `VTKPolyDataAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataConnectivityFilter
- **bl_idname**: `VTKPolyDataConnectivityFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ColorRegions`, `m_FullScalarConnectivity`, `m_MarkVisitedPointIds`, `m_ScalarConnectivity`, `m_ObjectName`, `e_ExtractionMode`, `m_ClosestPoint`, `m_ScalarRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataNormals
- **bl_idname**: `VTKPolyDataNormalsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutoOrientNormals`, `m_ComputeCellNormals`, `m_ComputePointNormals`, `m_Consistency`, `m_FlipNormals`, `m_NonManifoldTraversal`, `m_Splitting`, `m_ObjectName`, `m_FeatureAngle`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataPlaneCutter
- **bl_idname**: `VTKPolyDataPlaneCutterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeNormals`, `m_InterpolateAttributes`, `m_ObjectName`, `m_BatchSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataPointSampler
- **bl_idname**: `VTKPolyDataPointSamplerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateEdgePoints`, `m_GenerateInteriorPoints`, `m_GenerateVertexPoints`, `m_GenerateVertices`, `m_InterpolatePointData`, `m_ObjectName`, `m_Distance`, `e_PointGenerationMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataSilhouette
- **bl_idname**: `VTKPolyDataSilhouetteType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_BorderEdges`, `m_PieceInvariant`, `m_ObjectName`, `m_EnableFeatureAngle`, `m_FeatureAngle`, `e_Direction`, `m_Origin`, `m_Vector`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataStreamer
- **bl_idname**: `VTKPolyDataStreamerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ColorByPiece`, `m_ObjectName`, `m_NumberOfStreamDivisions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataTangents
- **bl_idname**: `VTKPolyDataTangentsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeCellTangents`, `m_ComputePointTangents`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataToImageStencil
- **bl_idname**: `VTKPolyDataToImageStencilType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Tolerance`, `m_OutputWholeExtent`, `m_OutputOrigin`, `m_OutputSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataToReebGraphFilter
- **bl_idname**: `VTKPolyDataToReebGraphFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_FieldId`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProcessIdScalars
- **bl_idname**: `VTKProcessIdScalarsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_RandomMode`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProcrustesAlignmentFilter
- **bl_idname**: `VTKProcrustesAlignmentFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_StartFromCentroid`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProgrammableAttributeDataFilter
- **bl_idname**: `VTKProgrammableAttributeDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProgrammableFilter
- **bl_idname**: `VTKProgrammableFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CopyArrays`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProjectPointsToPlane
- **bl_idname**: `VTKProjectPointsToPlaneType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `e_ProjectionType`, `m_Normal`, `m_Origin`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProjectSphereFilter
- **bl_idname**: `VTKProjectSphereFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_KeepPolePoints`, `m_TranslateZ`, `m_ObjectName`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProjectedTexture
- **bl_idname**: `VTKProjectedTextureType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_MirrorSeparation`, `e_CameraMode`, `m_AspectRatio`, `m_Position`, `m_SRange`, `m_TRange`, `m_Up`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProteinRibbonFilter
- **bl_idname**: `VTKProteinRibbonFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_DrawSmallMoleculesAsSpheres`, `m_ObjectName`, `m_SphereResolution`, `m_SubdivideFactor`, `m_CoilWidth`, `m_HelixWidth`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkQuadRotationalExtrusionFilter
- **bl_idname**: `VTKQuadRotationalExtrusionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Capping`, `m_ObjectName`, `m_Resolution`, `m_DefaultAngle`, `m_DeltaRadius`, `m_Translation`, `e_Axis`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkQuadraturePointInterpolator
- **bl_idname**: `VTKQuadraturePointInterpolatorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkQuadraturePointsGenerator
- **bl_idname**: `VTKQuadraturePointsGeneratorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkQuadratureSchemeDictionaryGenerator
- **bl_idname**: `VTKQuadratureSchemeDictionaryGeneratorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkQuadricClustering
- **bl_idname**: `VTKQuadricClusteringType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutoAdjustNumberOfDivisions`, `m_CopyCellData`, `m_PreventDuplicateCells`, `m_UseFeatureEdges`, `m_UseFeaturePoints`, `m_UseInputPoints`, `m_UseInternalTriangles`, `m_ObjectName`, `m_NumberOfXDivisions`, `m_NumberOfYDivisions`, `m_NumberOfZDivisions`, `m_FeaturePointsAngle`, `m_DivisionOrigin`, `m_DivisionSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkQuadricDecimation
- **bl_idname**: `VTKQuadricDecimationType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AttributeErrorMetric`, `m_NormalsAttribute`, `m_ScalarsAttribute`, `m_TCoordsAttribute`, `m_TensorsAttribute`, `m_VectorsAttribute`, `m_VolumePreservation`, `m_ObjectName`, `m_NormalsWeight`, `m_ScalarsWeight`, `m_TCoordsWeight`, `m_TargetReduction`, `m_TensorsWeight`, `m_VectorsWeight`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkQuantizePolyDataPoints
- **bl_idname**: `VTKQuantizePolyDataPointsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ConvertLinesToPoints`, `m_ConvertPolysToLines`, `m_ConvertStripsToPolys`, `m_PieceInvariant`, `m_PointMerging`, `m_ToleranceIsAbsolute`, `m_ObjectName`, `m_AbsoluteTolerance`, `m_QFactor`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRandomAttributeGenerator
- **bl_idname**: `VTKRandomAttributeGeneratorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AttributesConstantPerBlock`, `m_GenerateCellArray`, `m_GenerateCellNormals`, `m_GenerateCellScalars`, `m_GenerateCellTCoords`, `m_GenerateCellTensors`, `m_GenerateCellVectors`, `m_GenerateFieldArray`, `m_GeneratePointArray`, `m_GeneratePointNormals`, `m_GeneratePointScalars`, `m_GeneratePointTCoords`, `m_GeneratePointTensors`, `m_GeneratePointVectors`, `m_ObjectName`, `m_NumberOfComponents`, `m_NumberOfTuples`, `m_MaximumComponentValue`, `m_MinimumComponentValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRearrangeFields
- **bl_idname**: `VTKRearrangeFieldsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRectilinearGridAlgorithm
- **bl_idname**: `VTKRectilinearGridAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRectilinearGridClip
- **bl_idname**: `VTKRectilinearGridClipType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ClipData`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRectilinearGridGeometryFilter
- **bl_idname**: `VTKRectilinearGridGeometryFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Extent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRectilinearGridOutlineFilter
- **bl_idname**: `VTKRectilinearGridOutlineFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRectilinearGridPartitioner
- **bl_idname**: `VTKRectilinearGridPartitionerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_DuplicateNodes`, `m_ObjectName`, `m_NumberOfGhostLayers`, `m_NumberOfPartitions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRectilinearGridToPointSet
- **bl_idname**: `VTKRectilinearGridToPointSetType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRectilinearGridToTetrahedra
- **bl_idname**: `VTKRectilinearGridToTetrahedraType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_RememberVoxelId`, `m_ObjectName`, `e_TetraPerCell`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRectilinearSynchronizedTemplates
- **bl_idname**: `VTKRectilinearSynchronizedTemplatesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_GenerateTriangles`, `m_ObjectName`, `m_ArrayComponent`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRecursiveDividingCubes
- **bl_idname**: `VTKRecursiveDividingCubesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Increment`, `m_Distance`, `m_Value`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRedistributeDataSetFilter
- **bl_idname**: `VTKRedistributeDataSetFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_EnableDebugging`, `m_ExpandExplicitCuts`, `m_GenerateGlobalCellIds`, `m_LoadBalanceAcrossAllBlocks`, `m_PreservePartitionsInOutput`, `m_UseExplicitCuts`, `m_ObjectName`, `m_NumberOfPartitions`, `e_BoundaryMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkReflectionFilter
- **bl_idname**: `VTKReflectionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CopyInput`, `m_FlipAllInputArrays`, `m_ObjectName`, `m_Center`, `e_Plane`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRemoveDuplicatePolys
- **bl_idname**: `VTKRemoveDuplicatePolysType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRemoveGhosts
- **bl_idname**: `VTKRemoveGhostsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRemovePolyData
- **bl_idname**: `VTKRemovePolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ExactMatch`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRemoveUnusedPoints
- **bl_idname**: `VTKRemoveUnusedPointsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateOriginalPointIds`, `m_ObjectName`, `m_OriginalPointIdsArrayName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkResampleToImage
- **bl_idname**: `VTKResampleToImageType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseInputBounds`, `m_ObjectName`, `m_SamplingDimensions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkReverseSense
- **bl_idname**: `VTKReverseSenseType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ReverseCells`, `m_ReverseNormals`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRibbonFilter
- **bl_idname**: `VTKRibbonFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseDefaultNormal`, `m_VaryWidth`, `m_ObjectName`, `m_Angle`, `m_TextureLength`, `m_Width`, `m_WidthFactor`, `e_GenerateTCoords`, `m_DefaultNormal`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRotationFilter
- **bl_idname**: `VTKRotationFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CopyInput`, `m_ObjectName`, `m_NumberOfCopies`, `m_Angle`, `e_Axis`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRotationalExtrusionFilter
- **bl_idname**: `VTKRotationalExtrusionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Capping`, `m_ObjectName`, `m_Resolution`, `m_Angle`, `m_DeltaRadius`, `m_Translation`, `m_RotationAxis`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRuledSurfaceFilter
- **bl_idname**: `VTKRuledSurfaceFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CloseSurface`, `m_OrientLoops`, `m_PassLines`, `m_ObjectName`, `m_Offset`, `m_OnRatio`, `m_DistanceFactor`, `e_RuledMode`, `m_Resolution`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSMPContourGrid
- **bl_idname**: `VTKSMPContourGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeNormals`, `m_ComputeScalars`, `m_GenerateTriangles`, `m_MergePieces`, `m_ObjectName`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSampleImplicitFunctionFilter
- **bl_idname**: `VTKSampleImplicitFunctionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_GradientArrayName`, `m_ObjectName`, `m_ScalarArrayName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSelectionAlgorithm
- **bl_idname**: `VTKSelectionAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkShepardMethod
- **bl_idname**: `VTKShepardMethodType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_MaximumDistance`, `m_NullValue`, `m_PowerParameter`, `m_SampleDimensions`, `m_ModelBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkShrinkFilter
- **bl_idname**: `VTKShrinkFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_ShrinkFactor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkShrinkPolyData
- **bl_idname**: `VTKShrinkPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_ShrinkFactor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSignedDistance
- **bl_idname**: `VTKSignedDistanceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Radius`, `m_Dimensions`, `m_Bounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSimpleBondPerceiver
- **bl_idname**: `VTKSimpleBondPerceiverType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_IsToleranceAbsolute`, `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSimpleElevationFilter
- **bl_idname**: `VTKSimpleElevationFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Vector`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSimpleImageFilterExample
- **bl_idname**: `VTKSimpleImageFilterExampleType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSpatialRepresentationFilter
- **bl_idname**: `VTKSpatialRepresentationFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_GenerateLeaves`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSphereTreeFilter
- **bl_idname**: `VTKSphereTreeFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_TreeHierarchy`, `m_ObjectName`, `m_Level`, `e_ExtractionMode`, `m_Normal`, `m_Point`, `m_Ray`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSphericalHarmonics
- **bl_idname**: `VTKSphericalHarmonicsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSplineFilter
- **bl_idname**: `VTKSplineFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_MaximumNumberOfSubdivisions`, `m_NumberOfSubdivisions`, `m_Length`, `m_TextureLength`, `e_GenerateTCoords`, `e_Subdivide`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSplitByCellScalarFilter
- **bl_idname**: `VTKSplitByCellScalarFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PassAllPoints`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSplitColumnComponents
- **bl_idname**: `VTKSplitColumnComponentsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CalculateMagnitudes`, `m_ObjectName`, `e_NamingMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSplitField
- **bl_idname**: `VTKSplitFieldType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStaticCleanPolyData
- **bl_idname**: `VTKStaticCleanPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AveragePointData`, `m_ConvertLinesToPoints`, `m_ConvertPolysToLines`, `m_ConvertStripsToPolys`, `m_PieceInvariant`, `m_ProduceMergeMap`, `m_RemoveUnusedPoints`, `m_ToleranceIsAbsolute`, `m_MergingArray`, `m_ObjectName`, `m_AbsoluteTolerance`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStaticCleanUnstructuredGrid
- **bl_idname**: `VTKStaticCleanUnstructuredGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AveragePointData`, `m_PieceInvariant`, `m_ProduceMergeMap`, `m_RemoveUnusedPoints`, `m_ToleranceIsAbsolute`, `m_MergingArray`, `m_ObjectName`, `m_AbsoluteTolerance`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStrahlerMetric
- **bl_idname**: `VTKStrahlerMetricType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Normalize`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStripper
- **bl_idname**: `VTKStripperType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_JoinContiguousSegments`, `m_PassCellDataAsFieldData`, `m_PassThroughCellIds`, `m_PassThroughPointIds`, `m_ObjectName`, `m_MaximumLength`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredGridAlgorithm
- **bl_idname**: `VTKStructuredGridAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredGridAppend
- **bl_idname**: `VTKStructuredGridAppendType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredGridClip
- **bl_idname**: `VTKStructuredGridClipType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ClipData`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredGridGeometryFilter
- **bl_idname**: `VTKStructuredGridGeometryFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Extent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredGridGhostDataGenerator
- **bl_idname**: `VTKStructuredGridGhostDataGeneratorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfGhostLayers`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredGridOutlineFilter
- **bl_idname**: `VTKStructuredGridOutlineFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredGridPartitioner
- **bl_idname**: `VTKStructuredGridPartitionerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_DuplicateNodes`, `m_ObjectName`, `m_NumberOfGhostLayers`, `m_NumberOfPartitions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSubdivideTetra
- **bl_idname**: `VTKSubdivideTetraType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSurfaceNets2D
- **bl_idname**: `VTKSurfaceNets2DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeScalars`, `m_DataCaching`, `m_Smoothing`, `m_ObjectName`, `m_ArrayComponent`, `m_NumberOfContours`, `m_NumberOfLabels`, `m_BackgroundLabel`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSurfaceReconstructionFilter
- **bl_idname**: `VTKSurfaceReconstructionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NeighborhoodSize`, `m_SampleSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSynchronizedTemplates2D
- **bl_idname**: `VTKSynchronizedTemplates2DType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeScalars`, `m_ObjectName`, `m_ArrayComponent`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTableAlgorithm
- **bl_idname**: `VTKTableAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTableFFT
- **bl_idname**: `VTKTableFFTType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AverageFft`, `m_CreateFrequencyColumn`, `m_Normalize`, `m_OptimizeForRealInput`, `m_PrefixOutputArrays`, `m_ObjectName`, `m_BlockSize`, `m_NumberOfBlock`, `m_WindowingFunction`, `m_DefaultSampleRate`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTableToPolyData
- **bl_idname**: `VTKTableToPolyDataType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Create2DPoints`, `m_PreserveCoordinateColumnsAsDataArrays`, `m_ObjectName`, `m_XColumn`, `m_YColumn`, `m_ZColumn`, `m_XColumnIndex`, `m_XComponent`, `m_YColumnIndex`, `m_YComponent`, `m_ZColumnIndex`, `m_ZComponent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTableToStructuredGrid
- **bl_idname**: `VTKTableToStructuredGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_XColumn`, `m_YColumn`, `m_ZColumn`, `m_XComponent`, `m_YComponent`, `m_ZComponent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTemporalArrayOperatorFilter
- **bl_idname**: `VTKTemporalArrayOperatorFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_OutputArrayNameSuffix`, `m_FirstTimeStepIndex`, `m_Operator`, `m_SecondTimeStepIndex`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTemporalDataSetCache
- **bl_idname**: `VTKTemporalDataSetCacheType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CacheInMemkind`, `m_IsASource`, `m_ObjectName`, `m_CacheSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTemporalInterpolator
- **bl_idname**: `VTKTemporalInterpolatorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CacheData`, `m_ObjectName`, `m_ResampleFactor`, `m_DiscreteTimeStepInterval`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTemporalShiftScale
- **bl_idname**: `VTKTemporalShiftScaleType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Periodic`, `m_PeriodicEndCorrection`, `m_ObjectName`, `m_MaximumNumberOfPeriods`, `m_PostShift`, `m_PreShift`, `m_Scale`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTemporalSnapToTimeStep
- **bl_idname**: `VTKTemporalSnapToTimeStepType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `e_SnapMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTemporalStatistics
- **bl_idname**: `VTKTemporalStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeAverage`, `m_ComputeMaximum`, `m_ComputeMinimum`, `m_ComputeStandardDeviation`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTessellatorFilter
- **bl_idname**: `VTKTessellatorFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_MergePoints`, `m_ObjectName`, `m_MaximumNumberOfSubdivisions`, `m_OutputDimension`, `m_ChordError`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTextureMapToCylinder
- **bl_idname**: `VTKTextureMapToCylinderType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutomaticCylinderGeneration`, `m_PreventSeam`, `m_ObjectName`, `m_Point1`, `m_Point2`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTextureMapToPlane
- **bl_idname**: `VTKTextureMapToPlaneType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutomaticPlaneGeneration`, `m_ObjectName`, `m_Normal`, `m_Origin`, `m_Point1`, `m_Point2`, `m_SRange`, `m_TRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTextureMapToSphere
- **bl_idname**: `VTKTextureMapToSphereType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutomaticSphereGeneration`, `m_PreventSeam`, `m_ObjectName`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkThreshold
- **bl_idname**: `VTKThresholdType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AllScalars`, `m_Invert`, `m_UseContinuousCellRange`, `m_ObjectName`, `m_SelectedComponent`, `m_ThresholdFunction`, `m_LowerThreshold`, `m_UpperThreshold`, `e_AttributeMode`, `e_ComponentMode`, `e_PointsDataType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkThresholdPoints
- **bl_idname**: `VTKThresholdPointsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_InputArrayComponent`, `m_LowerThreshold`, `m_UpperThreshold`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkThresholdTextureCoords
- **bl_idname**: `VTKThresholdTextureCoordsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_TextureDimension`, `m_InTextureCoord`, `m_OutTextureCoord`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransformCoordinateSystems
- **bl_idname**: `VTKTransformCoordinateSystemsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `e_InputCoordinateSystem`, `e_OutputCoordinateSystem`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransformFilter
- **bl_idname**: `VTKTransformFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_TransformAllInputVectors`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransformPolyDataFilter
- **bl_idname**: `VTKTransformPolyDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransformTextureCoords
- **bl_idname**: `VTKTransformTextureCoordsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_FlipR`, `m_FlipS`, `m_FlipT`, `m_ObjectName`, `m_Origin`, `m_Position`, `m_Scale`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransmitImageDataPiece
- **bl_idname**: `VTKTransmitImageDataPieceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CreateGhostCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransmitPolyDataPiece
- **bl_idname**: `VTKTransmitPolyDataPieceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CreateGhostCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransmitRectilinearGridPiece
- **bl_idname**: `VTKTransmitRectilinearGridPieceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CreateGhostCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransmitStructuredDataPiece
- **bl_idname**: `VTKTransmitStructuredDataPieceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CreateGhostCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransmitStructuredGridPiece
- **bl_idname**: `VTKTransmitStructuredGridPieceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CreateGhostCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransmitUnstructuredGridPiece
- **bl_idname**: `VTKTransmitUnstructuredGridPieceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CreateGhostCells`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransposeTable
- **bl_idname**: `VTKTransposeTableType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AddIdColumn`, `m_UseIdColumn`, `m_IdColumnName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTreeAlgorithm
- **bl_idname**: `VTKTreeAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTriangleFilter
- **bl_idname**: `VTKTriangleFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_PassLines`, `m_PassVerts`, `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTriangleMeshPointNormals
- **bl_idname**: `VTKTriangleMeshPointNormalsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTriangularTCoords
- **bl_idname**: `VTKTriangularTCoordsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTubeBender
- **bl_idname**: `VTKTubeBenderType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Radius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTubeFilter
- **bl_idname**: `VTKTubeFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Capping`, `m_SidesShareVertices`, `m_UseDefaultNormal`, `m_ObjectName`, `m_NumberOfSides`, `m_Offset`, `m_OnRatio`, `m_Radius`, `m_RadiusFactor`, `m_TextureLength`, `e_GenerateTCoords`, `e_VaryRadius`, `m_DefaultNormal`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUncertaintyTubeFilter
- **bl_idname**: `VTKUncertaintyTubeFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfSides`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUndirectedGraphAlgorithm
- **bl_idname**: `VTKUndirectedGraphAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUniformGridAMRAlgorithm
- **bl_idname**: `VTKUniformGridAMRAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUniformGridGhostDataGenerator
- **bl_idname**: `VTKUniformGridGhostDataGeneratorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfGhostLayers`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUniformGridPartitioner
- **bl_idname**: `VTKUniformGridPartitionerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_DuplicateNodes`, `m_ObjectName`, `m_NumberOfGhostLayers`, `m_NumberOfPartitions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUnsignedDistance
- **bl_idname**: `VTKUnsignedDistanceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AdjustBounds`, `m_Capping`, `m_ObjectName`, `m_AdjustDistance`, `m_CapValue`, `m_Radius`, `e_OutputScalarType`, `m_Dimensions`, `m_Bounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUnstructuredGridAlgorithm
- **bl_idname**: `VTKUnstructuredGridAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUnstructuredGridBaseAlgorithm
- **bl_idname**: `VTKUnstructuredGridBaseAlgorithmType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUnstructuredGridGeometryFilter
- **bl_idname**: `VTKUnstructuredGridGeometryFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CellClipping`, `m_DuplicateGhostCellClipping`, `m_ExtentClipping`, `m_Merging`, `m_PassThroughCellIds`, `m_PassThroughPointIds`, `m_PointClipping`, `m_ObjectName`, `m_OriginalCellIdsName`, `m_OriginalPointIdsName`, `m_CellMaximum`, `m_CellMinimum`, `m_PointMaximum`, `m_PointMinimum`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUnstructuredGridGhostCellsGenerator
- **bl_idname**: `VTKUnstructuredGridGhostCellsGeneratorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_BuildIfRequired`, `m_HasGlobalCellIds`, `m_UseGlobalPointIds`, `m_GlobalCellIdsArrayName`, `m_GlobalPointIdsArrayName`, `m_ObjectName`, `m_MinimumNumberOfGhostLevels`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUnstructuredGridQuadricDecimation
- **bl_idname**: `VTKUnstructuredGridQuadricDecimationType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_ScalarsName`, `m_AutoAddCandidates`, `m_NumberOfCandidates`, `m_NumberOfEdgesToDecimate`, `m_NumberOfTetsOutput`, `m_AutoAddCandidatesThreshold`, `m_BoundaryWeight`, `m_TargetReduction`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUnstructuredGridToExplicitStructuredGrid
- **bl_idname**: `VTKUnstructuredGridToExplicitStructuredGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVectorDot
- **bl_idname**: `VTKVectorDotType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_MapScalars`, `m_ObjectName`, `m_ScalarRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVectorNorm
- **bl_idname**: `VTKVectorNormType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Normalize`, `m_ObjectName`, `e_AttributeMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVertexGlyphFilter
- **bl_idname**: `VTKVertexGlyphFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVolumeOfRevolutionFilter
- **bl_idname**: `VTKVolumeOfRevolutionFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_Resolution`, `m_SweepAngle`, `m_AxisDirection`, `m_AxisPosition`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVolumeRayCastSpaceLeapingImageFilter
- **bl_idname**: `VTKVolumeRayCastSpaceLeapingImageFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradientOpacity`, `m_ComputeMinMax`, `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_UpdateGradientOpacityFlags`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_IndependentComponents`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`, `m_TableSize`, `m_TableScale`, `m_TableShift`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVortexCore
- **bl_idname**: `VTKVortexCoreType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_FasterApproximation`, `m_HigherOrderMethod`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVoxelContoursToSurfaceFilter
- **bl_idname**: `VTKVoxelContoursToSurfaceFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_MemoryLimitInBytes`, `m_Spacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVoxelGrid
- **bl_idname**: `VTKVoxelGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfPointsPerBin`, `e_ConfigurationStyle`, `m_Divisions`, `m_LeafSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVoxelModeller
- **bl_idname**: `VTKVoxelModellerType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_BackgroundValue`, `m_ForegroundValue`, `m_MaximumDistance`, `e_ScalarType`, `m_SampleDimensions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkWarpLens
- **bl_idname**: `VTKWarpLensType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_ImageHeight`, `m_ImageWidth`, `m_FormatHeight`, `m_FormatWidth`, `m_K1`, `m_K2`, `m_Kappa`, `m_P1`, `m_P2`, `m_Center`, `m_PrincipalPoint`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkWarpScalar
- **bl_idname**: `VTKWarpScalarType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseNormal`, `m_XYPlane`, `m_ObjectName`, `m_ScaleFactor`, `m_Normal`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkWarpTo
- **bl_idname**: `VTKWarpToType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_Absolute`, `m_ObjectName`, `m_ScaleFactor`, `m_Position`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkWarpVector
- **bl_idname**: `VTKWarpVectorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_ScaleFactor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkWeightedTransformFilter
- **bl_idname**: `VTKWeightedTransformFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AddInputValues`, `m_CellDataTransformIndexArray`, `m_CellDataWeightArray`, `m_ObjectName`, `m_TransformIndexArray`, `m_WeightArray`, `m_NumberOfTransforms`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkWindowedSincPolyDataFilter
- **bl_idname**: `VTKWindowedSincPolyDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_BoundarySmoothing`, `m_FeatureEdgeSmoothing`, `m_GenerateErrorScalars`, `m_GenerateErrorVectors`, `m_NonManifoldSmoothing`, `m_NormalizeCoordinates`, `m_ObjectName`, `m_NumberOfIterations`, `m_EdgeAngle`, `m_FeatureAngle`, `m_PassBand`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkYoungsMaterialInterface
- **bl_idname**: `VTKYoungsMaterialInterfaceType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AxisSymetric`, `m_FillMaterial`, `m_InverseNormal`, `m_OnionPeel`, `m_ReverseMaterialOrder`, `m_UseAllBlocks`, `m_UseFractionAsDistance`, `m_ObjectName`, `m_NumberOfMaterials`, `m_VolumeFractionRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmAverageToCells
- **bl_idname**: `VTKmAverageToCellsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmAverageToPoints
- **bl_idname**: `VTKmAverageToPointsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmCleanGrid
- **bl_idname**: `VTKmCleanGridType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CompactPoints`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmClip
- **bl_idname**: `VTKmClipType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeScalars`, `m_ForceVTKm`, `m_ObjectName`, `m_ClipValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmContour
- **bl_idname**: `VTKmContourType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeGradients`, `m_ComputeNormals`, `m_ComputeScalars`, `m_GenerateTriangles`, `m_ObjectName`, `m_ArrayComponent`, `m_NumberOfContours`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmCoordinateSystemTransform
- **bl_idname**: `VTKmCoordinateSystemTransformType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmExternalFaces
- **bl_idname**: `VTKmExternalFacesType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CompactPoints`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmExtractVOI
- **bl_idname**: `VTKmExtractVOIType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ForceVTKm`, `m_IncludeBoundary`, `m_ObjectName`, `m_SampleRate`, `m_VOI`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmGradient
- **bl_idname**: `VTKmGradientType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ComputeDivergence`, `m_ComputeGradient`, `m_ComputeQCriterion`, `m_ComputeVorticity`, `m_FasterApproximation`, `m_ForceVTKm`, `m_DivergenceArrayName`, `m_ObjectName`, `m_QCriterionArrayName`, `m_ResultArrayName`, `m_VorticityArrayName`, `m_ContributingCellOption`, `m_ReplacementValueOption`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmHistogram
- **bl_idname**: `VTKmHistogramType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_CenterBinsAroundMinAndMax`, `m_UseCustomBinRanges`, `m_ObjectName`, `m_NumberOfBins`, `m_CustomBinRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmImageConnectivity
- **bl_idname**: `VTKmImageConnectivityType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmLevelOfDetail
- **bl_idname**: `VTKmLevelOfDetailType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_NumberOfXDivisions`, `m_NumberOfYDivisions`, `m_NumberOfZDivisions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmNDHistogram
- **bl_idname**: `VTKmNDHistogramType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmPointElevation
- **bl_idname**: `VTKmPointElevationType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ForceVTKm`, `m_ObjectName`, `m_HighPoint`, `m_LowPoint`, `m_ScalarRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmPointTransform
- **bl_idname**: `VTKmPointTransformType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmPolyDataNormals
- **bl_idname**: `VTKmPolyDataNormalsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AutoOrientNormals`, `m_ComputeCellNormals`, `m_ComputePointNormals`, `m_Consistency`, `m_FlipNormals`, `m_ForceVTKm`, `m_NonManifoldTraversal`, `m_Splitting`, `m_ObjectName`, `m_FeatureAngle`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmThreshold
- **bl_idname**: `VTKmThresholdType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_AllScalars`, `m_ForceVTKm`, `m_Invert`, `m_UseContinuousCellRange`, `m_ObjectName`, `m_SelectedComponent`, `m_ThresholdFunction`, `m_LowerThreshold`, `m_UpperThreshold`, `e_AttributeMode`, `e_ComponentMode`, `e_PointsDataType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmTriangleMeshPointNormals
- **bl_idname**: `VTKmTriangleMeshPointNormalsType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ForceVTKm`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmWarpScalar
- **bl_idname**: `VTKmWarpScalarType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_UseNormal`, `m_XYPlane`, `m_ObjectName`, `m_ScaleFactor`, `m_Normal`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmWarpVector
- **bl_idname**: `VTKmWarpVectorType`
- **module**: `generated_nodes/gen_VTKFilters1.py`
- **properties**: `m_ObjectName`, `m_ScaleFactor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

## Filter2

### vtkApplyColors
- **bl_idname**: `VTKApplyColorsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ScaleCellLookupTable`, `m_ScalePointLookupTable`, `m_UseCellLookupTable`, `m_UseCurrentAnnotationColor`, `m_UsePointLookupTable`, `m_CellColorOutputArrayName`, `m_ObjectName`, `m_PointColorOutputArrayName`, `m_DefaultCellOpacity`, `m_DefaultPointOpacity`, `m_SelectedCellOpacity`, `m_SelectedPointOpacity`, `m_DefaultCellColor`, `m_DefaultPointColor`, `m_SelectedCellColor`, `m_SelectedPointColor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkApplyIcons
- **bl_idname**: `VTKApplyIconsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_UseLookupTable`, `m_IconOutputArrayName`, `m_ObjectName`, `m_AttributeType`, `m_DefaultIcon`, `m_SelectedIcon`, `e_SelectionMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAreaContourSpectrumFilter
- **bl_idname**: `VTKAreaContourSpectrumFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`, `m_ArcId`, `m_FieldId`, `m_NumberOfSamples`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBinCellDataFilter
- **bl_idname**: `VTKBinCellDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ComputeTolerance`, `m_SpatialMatch`, `m_StoreNumberOfNonzeroBins`, `m_NumberOfNonzeroBinsArrayName`, `m_ObjectName`, `m_ArrayComponent`, `m_CellOverlapMethod`, `m_NumberOfBins`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBlankStructuredGridWithImage
- **bl_idname**: `VTKBlankStructuredGridWithImageType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCellDistanceSelector
- **bl_idname**: `VTKCellDistanceSelectorType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_AddIntermediate`, `m_IncludeSeed`, `m_ObjectName`, `m_Distance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCompositeDataProbeFilter
- **bl_idname**: `VTKCompositeDataProbeFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_CategoricalData`, `m_ComputeTolerance`, `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPartialArrays`, `m_PassPointArrays`, `m_SpatialMatch`, `m_ObjectName`, `m_ValidPointMaskArrayName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkConvertSelection
- **bl_idname**: `VTKConvertSelectionType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_AllowMissingArray`, `m_MatchAnyValues`, `m_ArrayName`, `m_ObjectName`, `m_InputFieldType`, `m_OutputType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCookieCutter
- **bl_idname**: `VTKCookieCutterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_PassCellData`, `m_PassPointData`, `m_ObjectName`, `e_PointInterpolation`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDeformPointSet
- **bl_idname**: `VTKDeformPointSetType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_InitializeWeights`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDelaunay2D
- **bl_idname**: `VTKDelaunay2DType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_BoundingTriangulation`, `m_ObjectName`, `m_ProjectionPlaneMode`, `m_Alpha`, `m_Offset`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDepthImageToPointCloud
- **bl_idname**: `VTKDepthImageToPointCloudType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_CullFarPoints`, `m_CullNearPoints`, `m_ProduceColorScalars`, `m_ProduceVertexCellArray`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractCellsAlongPolyLine
- **bl_idname**: `VTKExtractCellsAlongPolyLineType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractFunctionalBagPlot
- **bl_idname**: `VTKExtractFunctionalBagPlotType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractParticlesOverTime
- **bl_idname**: `VTKExtractParticlesOverTimeType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_IdChannelArray`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractSelectedArraysOverTime
- **bl_idname**: `VTKExtractSelectedArraysOverTimeType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ReportStatisticsOnly`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractSelectedBlock
- **bl_idname**: `VTKExtractSelectedBlockType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_PreserveTopology`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractSelectedFrustum
- **bl_idname**: `VTKExtractSelectedFrustumType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_InsideOut`, `m_PreserveTopology`, `m_ShowBounds`, `m_ObjectName`, `m_ContainingCells`, `m_FieldType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractSelectedIds
- **bl_idname**: `VTKExtractSelectedIdsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_PreserveTopology`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractSelectedLocations
- **bl_idname**: `VTKExtractSelectedLocationsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_PreserveTopology`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractSelectedPolyDataIds
- **bl_idname**: `VTKExtractSelectedPolyDataIdsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractSelectedThresholds
- **bl_idname**: `VTKExtractSelectedThresholdsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_PreserveTopology`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExtractSelection
- **bl_idname**: `VTKExtractSelectionType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_PreserveTopology`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFastSplatter
- **bl_idname**: `VTKFastSplatterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`, `m_MaxValue`, `m_MinValue`, `e_LimitMode`, `m_OutputDimensions`, `m_ModelBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFiberSurface
- **bl_idname**: `VTKFiberSurfaceType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFitToHeightMapFilter
- **bl_idname**: `VTKFitToHeightMapFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_UseHeightMapOffset`, `m_ObjectName`, `e_FittingStrategy`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericGlyph3DFilter
- **bl_idname**: `VTKGenericGlyph3DFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_Clamping`, `m_GeneratePointIds`, `m_Orient`, `m_Scaling`, `m_ObjectName`, `m_PointIdsName`, `m_ScaleFactor`, `e_ColorMode`, `e_IndexMode`, `e_ScaleMode`, `e_VectorMode`, `m_Range`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericProbeFilter
- **bl_idname**: `VTKGenericProbeFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericStreamTracer
- **bl_idname**: `VTKGenericStreamTracerType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ComputeVorticity`, `m_ObjectName`, `m_MaximumNumberOfSteps`, `m_MaximumError`, `m_RotationScale`, `m_TerminalSpeed`, `e_InitialIntegrationStepUnit`, `e_IntegrationDirection`, `e_IntegratorType`, `e_MaximumIntegrationStepUnit`, `e_MaximumPropagationUnit`, `e_MinimumIntegrationStepUnit`, `m_StartPosition`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGeometryFilter
- **bl_idname**: `VTKGeometryFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_CellClipping`, `m_Delegation`, `m_ExtentClipping`, `m_FastMode`, `m_Merging`, `m_PassThroughCellIds`, `m_PassThroughPointIds`, `m_PointClipping`, `m_RemoveGhostInterfaces`, `m_ObjectName`, `m_OriginalCellIdsName`, `m_OriginalPointIdsName`, `m_CellMaximum`, `m_CellMinimum`, `m_Degree`, `m_NonlinearSubdivisionLevel`, `m_PieceInvariant`, `m_PointMaximum`, `m_PointMinimum`, `m_Extent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGlyph2D
- **bl_idname**: `VTKGlyph2DType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_Clamping`, `m_FillCellData`, `m_GeneratePointIds`, `m_Orient`, `m_Scaling`, `m_ObjectName`, `m_PointIdsName`, `m_ScaleFactor`, `e_ColorMode`, `e_IndexMode`, `e_ScaleMode`, `e_VectorMode`, `m_Range`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGlyph3D
- **bl_idname**: `VTKGlyph3DType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_Clamping`, `m_FillCellData`, `m_GeneratePointIds`, `m_Orient`, `m_Scaling`, `m_ObjectName`, `m_PointIdsName`, `m_ScaleFactor`, `e_ColorMode`, `e_IndexMode`, `e_ScaleMode`, `e_VectorMode`, `m_Range`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageAccumulate
- **bl_idname**: `VTKImageAccumulateType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_IgnoreZero`, `m_ReverseStencil`, `m_ObjectName`, `m_ComponentOrigin`, `m_ComponentSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageBlend
- **bl_idname**: `VTKImageBlendType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_CompoundAlpha`, `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_CompoundThreshold`, `e_BlendMode`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageChangeInformation
- **bl_idname**: `VTKImageChangeInformationType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_CenterImage`, `m_ObjectName`, `m_ExtentTranslation`, `m_OutputExtentStart`, `m_OriginScale`, `m_OriginTranslation`, `m_OutputOrigin`, `m_OutputSpacing`, `m_SpacingScale`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageCheckerboard
- **bl_idname**: `VTKImageCheckerboardType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`, `m_NumberOfDivisions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageCorrelation
- **bl_idname**: `VTKImageCorrelationType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDataLIC2D
- **bl_idname**: `VTKImageDataLIC2DType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`, `m_Magnification`, `m_Steps`, `m_StepSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDifference
- **bl_idname**: `VTKImageDifferenceType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_AllowShift`, `m_Averaging`, `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_Threshold`, `m_AverageThresholdFactor`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageDotProduct
- **bl_idname**: `VTKImageDotProductType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageHistogram
- **bl_idname**: `VTKImageHistogramType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_AutomaticBinning`, `m_EnableSMP`, `m_GenerateHistogramImage`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_ActiveComponent`, `m_DesiredBytesPerPiece`, `m_MaximumNumberOfBins`, `m_NumberOfBins`, `m_NumberOfThreads`, `m_BinOrigin`, `m_BinSpacing`, `e_HistogramImageScale`, `e_SplitMode`, `m_HistogramImageSize`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageHistogramStatistics
- **bl_idname**: `VTKImageHistogramStatisticsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_AutomaticBinning`, `m_EnableSMP`, `m_GenerateHistogramImage`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_ActiveComponent`, `m_DesiredBytesPerPiece`, `m_MaximumNumberOfBins`, `m_NumberOfBins`, `m_NumberOfThreads`, `m_BinOrigin`, `m_BinSpacing`, `e_HistogramImageScale`, `e_SplitMode`, `m_HistogramImageSize`, `m_MinimumPieceSize`, `m_AutoRangeExpansionFactors`, `m_AutoRangePercentiles`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageLogic
- **bl_idname**: `VTKImageLogicType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_OutputTrueValue`, `e_Operation`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMask
- **bl_idname**: `VTKImageMaskType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_NotMask`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `m_MaskAlpha`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageNonMaximumSuppression
- **bl_idname**: `VTKImageNonMaximumSuppressionType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_HandleBoundaries`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_Dimensionality`, `m_NumberOfThreads`, `e_SplitMode`, `m_MinimumPieceSize`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageProbeFilter
- **bl_idname**: `VTKImageProbeFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageRectilinearWipe
- **bl_idname**: `VTKImageRectilinearWipeType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_EnableSMP`, `m_GlobalDefaultEnableSMP`, `m_ObjectName`, `m_DesiredBytesPerPiece`, `m_NumberOfThreads`, `e_SplitMode`, `e_Wipe`, `m_Axis`, `m_MinimumPieceSize`, `m_Position`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageThresholdConnectivity
- **bl_idname**: `VTKImageThresholdConnectivityType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ReplaceIn`, `m_ReplaceOut`, `m_ObjectName`, `m_ActiveComponent`, `m_InValue`, `m_NeighborhoodFraction`, `m_OutValue`, `m_SliceRangeX`, `m_SliceRangeY`, `m_SliceRangeZ`, `m_NeighborhoodRadius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageToPoints
- **bl_idname**: `VTKImageToPointsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageToStructuredPoints
- **bl_idname**: `VTKImageToStructuredPointsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkJoinTables
- **bl_idname**: `VTKJoinTablesType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_LeftKey`, `m_ObjectName`, `m_RightKey`, `m_Mode`, `m_ReplacementValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMergeDataObjectFilter
- **bl_idname**: `VTKMergeDataObjectFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`, `e_OutputField`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPExtractSelectedArraysOverTime
- **bl_idname**: `VTKPExtractSelectedArraysOverTimeType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ReportStatisticsOnly`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPProbeFilter
- **bl_idname**: `VTKPProbeFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_CategoricalData`, `m_ComputeTolerance`, `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPartialArrays`, `m_PassPointArrays`, `m_SpatialMatch`, `m_ObjectName`, `m_ValidPointMaskArrayName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPResampleWithDataSet
- **bl_idname**: `VTKPResampleWithDataSetType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_CategoricalData`, `m_ComputeTolerance`, `m_MarkBlankPointsAndCells`, `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPartialArrays`, `m_PassPointArrays`, `m_UseBalancedPartitionForPointsLookup`, `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParallelCoordinatesHistogramRepresentation
- **bl_idname**: `VTKParallelCoordinatesHistogramRepresentationType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_Selectable`, `m_ShowOutliers`, `m_UseCurves`, `m_UseHistograms`, `m_ObjectName`, `m_SelectionArrayName`, `m_CurveResolution`, `m_LabelRenderMode`, `m_NumberOfAxisLabels`, `m_PreferredNumberOfOutliers`, `m_SelectionType`, `m_AngleBrushThreshold`, `m_FontSize`, `m_FunctionBrushThreshold`, `m_LineOpacity`, `m_NumberOfHistogramBins`, `m_AxisColor`, `m_AxisLabelColor`, `m_HistogramLookupTableRange`, `m_LineColor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParallelCoordinatesRepresentation
- **bl_idname**: `VTKParallelCoordinatesRepresentationType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_Selectable`, `m_UseCurves`, `m_ObjectName`, `m_SelectionArrayName`, `m_CurveResolution`, `m_LabelRenderMode`, `m_NumberOfAxisLabels`, `m_SelectionType`, `m_AngleBrushThreshold`, `m_FontSize`, `m_FunctionBrushThreshold`, `m_LineOpacity`, `m_AxisColor`, `m_AxisLabelColor`, `m_LineColor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParticlePathFilter
- **bl_idname**: `VTKParticlePathFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ComputeVorticity`, `m_DisableResetCache`, `m_EnableParticleWriting`, `m_ForceSerialExecution`, `m_IgnorePipelineTime`, `m_ObjectName`, `m_ParticleFileName`, `m_ForceReinjectionEveryNSteps`, `m_IntegratorType`, `m_StaticMesh`, `m_StaticSeeds`, `m_RotationScale`, `m_StartTime`, `m_TerminalSpeed`, `m_TerminationTime`, `e_MeshOverTime`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParticleTracer
- **bl_idname**: `VTKParticleTracerType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ComputeVorticity`, `m_DisableResetCache`, `m_EnableParticleWriting`, `m_ForceSerialExecution`, `m_IgnorePipelineTime`, `m_ObjectName`, `m_ParticleFileName`, `m_ForceReinjectionEveryNSteps`, `m_IntegratorType`, `m_StaticMesh`, `m_StaticSeeds`, `m_RotationScale`, `m_StartTime`, `m_TerminalSpeed`, `m_TerminationTime`, `e_MeshOverTime`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointInterpolator
- **bl_idname**: `VTKPointInterpolatorType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPointArrays`, `m_PromoteOutputArrays`, `m_ObjectName`, `m_ValidPointsMaskArrayName`, `m_NullValue`, `e_NullPointsStrategy`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointInterpolator2D
- **bl_idname**: `VTKPointInterpolator2DType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_InterpolateZ`, `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPointArrays`, `m_PromoteOutputArrays`, `m_ObjectName`, `m_ValidPointsMaskArrayName`, `m_ZArrayName`, `m_NullValue`, `e_NullPointsStrategy`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataEdgeConnectivityFilter
- **bl_idname**: `VTKPolyDataEdgeConnectivityFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_BarrierEdges`, `m_CellRegionAreas`, `m_ColorRegions`, `m_ScalarConnectivity`, `m_ObjectName`, `m_LargeRegionThreshold`, `e_ExtractionMode`, `e_RegionGrowing`, `m_BarrierEdgeLength`, `m_ClosestPoint`, `m_ScalarRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProbeFilter
- **bl_idname**: `VTKProbeFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_CategoricalData`, `m_ComputeTolerance`, `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPointArrays`, `m_SpatialMatch`, `m_ObjectName`, `m_ValidPointMaskArrayName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProbeLineFilter
- **bl_idname**: `VTKProbeLineFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_AggregateAsPolyData`, `m_ComputeTolerance`, `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPartialArrays`, `m_PassPointArrays`, `m_ObjectName`, `m_LineResolution`, `m_SamplingPattern`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProbePolyhedron
- **bl_idname**: `VTKProbePolyhedronType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ProbeCellData`, `m_ProbePointData`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProbeSelectedLocations
- **bl_idname**: `VTKProbeSelectedLocationsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_PreserveTopology`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProgrammableGlyphFilter
- **bl_idname**: `VTKProgrammableGlyphFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`, `e_ColorMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProjectedTerrainPath
- **bl_idname**: `VTKProjectedTerrainPathType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`, `m_MaximumNumberOfLines`, `m_HeightOffset`, `m_HeightTolerance`, `e_ProjectionMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkResampleWithDataSet
- **bl_idname**: `VTKResampleWithDataSetType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_CategoricalData`, `m_ComputeTolerance`, `m_MarkBlankPointsAndCells`, `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPartialArrays`, `m_PassPointArrays`, `m_UseBalancedPartitionForPointsLookup`, `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSPHInterpolator
- **bl_idname**: `VTKSPHInterpolatorType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ComputeShepardSum`, `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPointArrays`, `m_PromoteOutputArrays`, `m_ShepardNormalization`, `m_CutoffArrayName`, `m_DensityArrayName`, `m_MassArrayName`, `m_ObjectName`, `m_ShepardSumArrayName`, `m_ValidPointsMaskArrayName`, `m_NullValue`, `e_NullPointsStrategy`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSelectEnclosedPoints
- **bl_idname**: `VTKSelectEnclosedPointsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_CheckSurface`, `m_InsideOut`, `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSmoothPolyDataFilter
- **bl_idname**: `VTKSmoothPolyDataFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_BoundarySmoothing`, `m_FeatureEdgeSmoothing`, `m_GenerateErrorScalars`, `m_GenerateErrorVectors`, `m_ObjectName`, `m_NumberOfIterations`, `m_Convergence`, `m_EdgeAngle`, `m_FeatureAngle`, `m_RelaxationFactor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStreaklineFilter
- **bl_idname**: `VTKStreaklineFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ComputeVorticity`, `m_DisableResetCache`, `m_EnableParticleWriting`, `m_ForceSerialExecution`, `m_IgnorePipelineTime`, `m_ObjectName`, `m_ParticleFileName`, `m_ForceReinjectionEveryNSteps`, `m_IntegratorType`, `m_StaticMesh`, `m_StaticSeeds`, `m_RotationScale`, `m_StartTime`, `m_TerminalSpeed`, `m_TerminationTime`, `e_MeshOverTime`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStreamSurface
- **bl_idname**: `VTKStreamSurfaceType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ComputeVorticity`, `m_ForceSerialExecution`, `m_SurfaceStreamlines`, `m_UseIterativeSeeding`, `m_UseLocalSeedSource`, `m_ObjectName`, `m_IntegrationStepUnit`, `m_MaximumNumberOfSteps`, `m_InitialIntegrationStep`, `m_MaximumError`, `m_MaximumIntegrationStep`, `m_MaximumPropagation`, `m_MinimumIntegrationStep`, `m_RotationScale`, `m_TerminalSpeed`, `e_IntegrationDirection`, `e_IntegratorType`, `m_StartPosition`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStreamTracer
- **bl_idname**: `VTKStreamTracerType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ComputeVorticity`, `m_ForceSerialExecution`, `m_SurfaceStreamlines`, `m_UseLocalSeedSource`, `m_ObjectName`, `m_IntegrationStepUnit`, `m_MaximumNumberOfSteps`, `m_InitialIntegrationStep`, `m_MaximumError`, `m_MaximumIntegrationStep`, `m_MaximumPropagation`, `m_MinimumIntegrationStep`, `m_RotationScale`, `m_TerminalSpeed`, `e_IntegrationDirection`, `e_IntegratorType`, `m_StartPosition`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSubPixelPositionEdgels
- **bl_idname**: `VTKSubPixelPositionEdgelsType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_TargetFlag`, `m_ObjectName`, `m_TargetValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSynchronizeTimeFilter
- **bl_idname**: `VTKSynchronizeTimeFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`, `m_RelativeTolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTensorGlyph
- **bl_idname**: `VTKTensorGlyphType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ClampScaling`, `m_ColorGlyphs`, `m_ExtractEigenvalues`, `m_Scaling`, `m_Symmetric`, `m_ThreeGlyphs`, `m_ObjectName`, `m_Length`, `m_MaxScaleFactor`, `m_ScaleFactor`, `e_ColorMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTrimmedExtrusionFilter
- **bl_idname**: `VTKTrimmedExtrusionFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_Capping`, `m_ObjectName`, `e_CappingStrategy`, `e_ExtrusionStrategy`, `m_ExtrusionDirection`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVolumeContourSpectrumFilter
- **bl_idname**: `VTKVolumeContourSpectrumFilterType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_ObjectName`, `m_ArcId`, `m_FieldId`, `m_NumberOfSamples`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkmProbe
- **bl_idname**: `VTKmProbeType`
- **module**: `generated_nodes/gen_VTKFilters2.py`
- **properties**: `m_PassCellArrays`, `m_PassFieldArrays`, `m_PassPointArrays`, `m_ObjectName`, `m_ValidCellMaskArrayName`, `m_ValidPointMaskArrayName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

## ImplicitFunc

### vtkBox
- **bl_idname**: `VTKBoxType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCone
- **bl_idname**: `VTKConeType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_Angle`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCoordinateFrame
- **bl_idname**: `VTKCoordinateFrameType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_Origin`, `m_XAxis`, `m_YAxis`, `m_ZAxis`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCylinder
- **bl_idname**: `VTKCylinderType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_Radius`, `m_Axis`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitBoolean
- **bl_idname**: `VTKImplicitBooleanType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `e_OperationType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitDataSet
- **bl_idname**: `VTKImplicitDataSetType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_OutValue`, `m_OutGradient`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitHalo
- **bl_idname**: `VTKImplicitHaloType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_FadeOut`, `m_Radius`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitPolyDataDistance
- **bl_idname**: `VTKImplicitPolyDataDistanceType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_NoValue`, `m_Tolerance`, `m_NoClosestPoint`, `m_NoGradient`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitProjectOnPlaneDistance
- **bl_idname**: `VTKImplicitProjectOnPlaneDistanceType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_Tolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitSelectionLoop
- **bl_idname**: `VTKImplicitSelectionLoopType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_AutomaticNormalGeneration`, `m_ObjectName`, `m_Normal`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitSum
- **bl_idname**: `VTKImplicitSumType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_NormalizeByWeight`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitVolume
- **bl_idname**: `VTKImplicitVolumeType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_OutValue`, `m_OutGradient`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitWindowFunction
- **bl_idname**: `VTKImplicitWindowFunctionType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_WindowRange`, `m_WindowValues`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPerlinNoise
- **bl_idname**: `VTKPerlinNoiseType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_Amplitude`, `m_Frequency`, `m_Phase`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPlane
- **bl_idname**: `VTKPlaneType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_Normal`, `m_Origin`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPlanes
- **bl_idname**: `VTKPlanesType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPlanesIntersection
- **bl_idname**: `VTKPlanesIntersectionType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyPlane
- **bl_idname**: `VTKPolyPlaneType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkQuadric
- **bl_idname**: `VTKQuadricType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSphere
- **bl_idname**: `VTKSphereType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`, `m_Radius`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSpheres
- **bl_idname**: `VTKSpheresType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSuperquadric
- **bl_idname**: `VTKSuperquadricType`
- **module**: `generated_nodes/gen_VTKImplicitFunc.py`
- **properties**: `m_Toroidal`, `m_ObjectName`, `m_PhiRoundness`, `m_Size`, `m_ThetaRoundness`, `m_Thickness`, `m_Center`, `m_Scale`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

## Integrator

### vtkRungeKutta2
- **bl_idname**: `VTKRungeKutta2Type`
- **module**: `generated_nodes/gen_VTKIntegrator.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRungeKutta4
- **bl_idname**: `VTKRungeKutta4Type`
- **module**: `generated_nodes/gen_VTKIntegrator.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRungeKutta45
- **bl_idname**: `VTKRungeKutta45Type`
- **module**: `generated_nodes/gen_VTKIntegrator.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

## ParametricFunc

### vtkParametricBohemianDome
- **bl_idname**: `VTKParametricBohemianDomeType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_A`, `m_B`, `m_C`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricBour
- **bl_idname**: `VTKParametricBourType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricBoy
- **bl_idname**: `VTKParametricBoyType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`, `m_ZScale`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricCatalanMinimal
- **bl_idname**: `VTKParametricCatalanMinimalType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricConicSpiral
- **bl_idname**: `VTKParametricConicSpiralType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_A`, `m_B`, `m_C`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`, `m_N`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricCrossCap
- **bl_idname**: `VTKParametricCrossCapType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricDini
- **bl_idname**: `VTKParametricDiniType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_A`, `m_B`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricEllipsoid
- **bl_idname**: `VTKParametricEllipsoidType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`, `m_XRadius`, `m_YRadius`, `m_ZRadius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricEnneper
- **bl_idname**: `VTKParametricEnneperType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricFigure8Klein
- **bl_idname**: `VTKParametricFigure8KleinType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`, `m_Radius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricHenneberg
- **bl_idname**: `VTKParametricHennebergType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricKlein
- **bl_idname**: `VTKParametricKleinType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricKuen
- **bl_idname**: `VTKParametricKuenType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_DeltaV0`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricMobius
- **bl_idname**: `VTKParametricMobiusType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`, `m_Radius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricPluckerConoid
- **bl_idname**: `VTKParametricPluckerConoidType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_N`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricPseudosphere
- **bl_idname**: `VTKParametricPseudosphereType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricRandomHills
- **bl_idname**: `VTKParametricRandomHillsType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_AllowRandomGeneration`, `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_NumberOfHills`, `m_RandomSeed`, `m_AmplitudeScaleFactor`, `m_HillAmplitude`, `m_HillXVariance`, `m_HillYVariance`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`, `m_XVarianceScaleFactor`, `m_YVarianceScaleFactor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricRoman
- **bl_idname**: `VTKParametricRomanType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`, `m_Radius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricSpline
- **bl_idname**: `VTKParametricSplineType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_Closed`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_ParameterizeByLength`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_LeftConstraint`, `m_RightConstraint`, `m_LeftValue`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`, `m_RightValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricSuperEllipsoid
- **bl_idname**: `VTKParametricSuperEllipsoidType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`, `m_N1`, `m_N2`, `m_XRadius`, `m_YRadius`, `m_ZRadius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricSuperToroid
- **bl_idname**: `VTKParametricSuperToroidType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_CrossSectionRadius`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`, `m_N1`, `m_N2`, `m_RingRadius`, `m_XRadius`, `m_YRadius`, `m_ZRadius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricTorus
- **bl_idname**: `VTKParametricTorusType`
- **module**: `generated_nodes/gen_VTKParametricFunc.py`
- **properties**: `m_ClockwiseOrdering`, `m_DerivativesAvailable`, `m_JoinU`, `m_JoinV`, `m_JoinW`, `m_TwistU`, `m_TwistV`, `m_TwistW`, `m_ObjectName`, `m_CrossSectionRadius`, `m_MaximumU`, `m_MaximumV`, `m_MaximumW`, `m_MinimumU`, `m_MinimumV`, `m_MinimumW`, `m_RingRadius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

## Reader

### vtkAMREnzoParticlesReader
- **bl_idname**: `VTKAMREnzoParticlesReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FilterLocation`, `m_FileName`, `m_ObjectName`, `m_Frequency`, `m_ParticleType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAMREnzoReader
- **bl_idname**: `VTKAMREnzoReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ConvertToCGS`, `m_EnableCaching`, `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAMRFlashParticlesReader
- **bl_idname**: `VTKAMRFlashParticlesReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FilterLocation`, `m_FileName`, `m_ObjectName`, `m_Frequency`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAMRFlashReader
- **bl_idname**: `VTKAMRFlashReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_EnableCaching`, `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAMRVelodyneReader
- **bl_idname**: `VTKAMRVelodyneReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_EnableCaching`, `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAMReXGridReader
- **bl_idname**: `VTKAMReXGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_EnableCaching`, `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAMReXParticlesReader
- **bl_idname**: `VTKAMReXParticlesReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ObjectName`, `m_ParticleType`, `m_PlotFileName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAVSucdReader
- **bl_idname**: `VTKAVSucdReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_BinaryFile`, `m_FileName`, `m_ObjectName`, `e_ByteOrder`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkArrayDataReader
- **bl_idname**: `VTKArrayDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_FileName`, `m_InputString`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkArrayReader
- **bl_idname**: `VTKArrayReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_FileName`, `m_InputString`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBMPReader
- **bl_idname**: `VTKBMPReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_Allow8BitBMP`, `m_FileLowerLeft`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_ScalarArrayName`, `m_DataMask`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataVOI`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBYUReader
- **bl_idname**: `VTKBYUReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadDisplacement`, `m_ReadScalar`, `m_ReadTexture`, `m_DisplacementFileName`, `m_FileName`, `m_GeometryFileName`, `m_ObjectName`, `m_ScalarFileName`, `m_TextureFileName`, `m_PartNumber`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBiomTableReader
- **bl_idname**: `VTKBiomTableReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCGNSFileSeriesReader
- **bl_idname**: `VTKCGNSFileSeriesReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_IgnoreReaderTime`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCGNSReader
- **bl_idname**: `VTKCGNSReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_CacheConnectivity`, `m_CacheMesh`, `m_CreateEachSolutionAsBlock`, `m_DistributeBlocks`, `m_DoublePrecisionMesh`, `m_IgnoreFlowSolutionPointers`, `m_LoadBndPatch`, `m_LoadMesh`, `m_Use3DVector`, `m_UseUnsteadyPattern`, `m_FileName`, `m_ObjectName`, `m_DataLocation`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCMLMoleculeReader
- **bl_idname**: `VTKCMLMoleculeReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCONVERGECFDReader
- **bl_idname**: `VTKCONVERGECFDReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCPExodusIIInSituReader
- **bl_idname**: `VTKCPExodusIIInSituReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_CurrentTimeStep`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkChacoGraphReader
- **bl_idname**: `VTKChacoGraphReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkChacoReader
- **bl_idname**: `VTKChacoReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_GenerateEdgeWeightArrays`, `m_GenerateGlobalElementIdArray`, `m_GenerateGlobalNodeIdArray`, `m_GenerateVertexWeightArrays`, `m_BaseName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCityGMLReader
- **bl_idname**: `VTKCityGMLReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_UseTransparencyAsOpacity`, `m_FileName`, `m_ObjectName`, `m_BeginBuildingIndex`, `m_EndBuildingIndex`, `m_LOD`, `m_NumberOfBuildings`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCompositeDataReader
- **bl_idname**: `VTKCompositeDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDEMReader
- **bl_idname**: `VTKDEMReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `e_ElevationReference`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDICOMImageReader
- **bl_idname**: `VTKDICOMImageReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_DirectoryName`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDIMACSGraphReader
- **bl_idname**: `VTKDIMACSGraphReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_EdgeAttributeArrayName`, `m_FileName`, `m_ObjectName`, `m_VertexAttributeArrayName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataObjectReader
- **bl_idname**: `VTKDataObjectReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataReader
- **bl_idname**: `VTKDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataSetReader
- **bl_idname**: `VTKDataSetReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDelimitedTextReader
- **bl_idname**: `VTKDelimitedTextReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_AddTabFieldDelimiter`, `m_DetectNumericColumns`, `m_ForceDouble`, `m_GeneratePedigreeIds`, `m_HaveHeaders`, `m_MergeConsecutiveDelimiters`, `m_OutputPedigreeIds`, `m_ReadFromInputString`, `m_TrimWhitespacePriorToNumericConversion`, `m_UseStringDelimiter`, `m_FieldDelimiterCharacters`, `m_FileName`, `m_ObjectName`, `m_PedigreeIdArrayName`, `m_StringDelimiter`, `m_UTF8FieldDelimiters`, `m_UTF8RecordDelimiters`, `m_UTF8StringDelimiters`, `m_UnicodeCharacterSet`, `m_DefaultIntegerValue`, `m_MaxRecords`, `m_ReplacementCharacter`, `m_DefaultDoubleValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEnSight6BinaryReader
- **bl_idname**: `VTKEnSight6BinaryReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ParticleCoordinatesByIndex`, `m_ReadAllVariables`, `m_CaseFileName`, `m_FilePath`, `m_ObjectName`, `m_TimeValue`, `e_ByteOrder`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEnSight6Reader
- **bl_idname**: `VTKEnSight6ReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ParticleCoordinatesByIndex`, `m_ReadAllVariables`, `m_CaseFileName`, `m_FilePath`, `m_ObjectName`, `m_TimeValue`, `e_ByteOrder`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEnSightGoldBinaryReader
- **bl_idname**: `VTKEnSightGoldBinaryReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ParticleCoordinatesByIndex`, `m_ReadAllVariables`, `m_CaseFileName`, `m_FilePath`, `m_ObjectName`, `m_TimeValue`, `e_ByteOrder`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEnSightGoldReader
- **bl_idname**: `VTKEnSightGoldReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ParticleCoordinatesByIndex`, `m_ReadAllVariables`, `m_CaseFileName`, `m_FilePath`, `m_ObjectName`, `m_TimeValue`, `e_ByteOrder`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEnSightMasterServerReader
- **bl_idname**: `VTKEnSightMasterServerReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ParticleCoordinatesByIndex`, `m_ReadAllVariables`, `m_CaseFileName`, `m_FilePath`, `m_ObjectName`, `m_CurrentPiece`, `m_TimeValue`, `e_ByteOrder`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExodusIIReader
- **bl_idname**: `VTKExodusIIReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_AnimateModeShapes`, `m_ApplyDisplacements`, `m_GenerateFileIdArray`, `m_GenerateGlobalElementIdArray`, `m_GenerateGlobalNodeIdArray`, `m_GenerateImplicitElementIdArray`, `m_GenerateImplicitNodeIdArray`, `m_GenerateObjectIdCellArray`, `m_HasModeShapes`, `m_IgnoreFileTime`, `m_SqueezePoints`, `m_UseLegacyBlockNames`, `m_FileName`, `m_ObjectName`, `m_XMLFileName`, `m_DisplayType`, `m_FileId`, `m_TimeStep`, `m_CacheSize`, `m_DisplacementMagnitude`, `m_ModeShapeTime`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFLUENTReader
- **bl_idname**: `VTKFLUENTReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `e_DataByteOrder`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFacetReader
- **bl_idname**: `VTKFacetReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFixedWidthTextReader
- **bl_idname**: `VTKFixedWidthTextReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_HaveHeaders`, `m_StripWhiteSpace`, `m_FileName`, `m_ObjectName`, `m_FieldWidth`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGAMBITReader
- **bl_idname**: `VTKGAMBITReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGESignaReader
- **bl_idname**: `VTKGESignaReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_Date`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ImageNumber`, `m_Modality`, `m_ObjectName`, `m_PatientID`, `m_PatientName`, `m_Series`, `m_Study`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGLTFReader
- **bl_idname**: `VTKGLTFReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ApplyDeformationsToGeometry`, `m_FileName`, `m_ObjectName`, `m_CurrentScene`, `m_FrameRate`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGaussianCubeReader
- **bl_idname**: `VTKGaussianCubeReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_BScale`, `m_HBScale`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGaussianCubeReader2
- **bl_idname**: `VTKGaussianCubeReader2Type`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericDataObjectReader
- **bl_idname**: `VTKGenericDataObjectReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericEnSightReader
- **bl_idname**: `VTKGenericEnSightReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ParticleCoordinatesByIndex`, `m_ReadAllVariables`, `m_CaseFileName`, `m_FilePath`, `m_ObjectName`, `m_TimeValue`, `e_ByteOrder`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGeoJSONReader
- **bl_idname**: `VTKGeoJSONReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_OutlinePolygons`, `m_StringInputMode`, `m_TriangulatePolygons`, `m_FileName`, `m_ObjectName`, `m_SerializedPropertiesArrayName`, `m_StringInput`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGraphReader
- **bl_idname**: `VTKGraphReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkH5PartReader
- **bl_idname**: `VTKH5PartReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_CombineVectorComponents`, `m_GenerateVertexCells`, `m_MaskOutOfTimeRangeOutput`, `m_FileName`, `m_ObjectName`, `m_Xarray`, `m_Yarray`, `m_Zarray`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkH5RageReader
- **bl_idname**: `VTKH5RageReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_CurrentTimeStep`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHDFReader
- **bl_idname**: `VTKHDFReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_MaximumLevelsToReadByDefaultForAMR`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHDRReader
- **bl_idname**: `VTKHDRReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_ScalarArrayName`, `m_DataMask`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataVOI`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkIOSSReader
- **bl_idname**: `VTKIOSSReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ApplyDisplacements`, `m_GenerateFileId`, `m_ReadGlobalFields`, `m_ReadIds`, `m_ReadQAAndInformationRecords`, `m_RemoveUnusedPoints`, `m_ScanForRelatedFiles`, `m_DatabaseTypeOverride`, `m_FileName`, `m_ObjectName`, `m_Selector`, `m_FileStride`, `m_DisplacementMagnitude`, `m_FileRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkISIReader
- **bl_idname**: `VTKISIReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_Delimiter`, `m_FileName`, `m_ObjectName`, `m_MaxRecords`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageReader
- **bl_idname**: `VTKImageReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_ScalarArrayName`, `m_DataMask`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataVOI`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageReader2
- **bl_idname**: `VTKImageReader2Type`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkJPEGReader
- **bl_idname**: `VTKJPEGReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLSDynaReader
- **bl_idname**: `VTKLSDynaReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_DeformedMesh`, `m_DeletedCellsAsGhostArray`, `m_RemoveDeletedCells`, `m_DatabaseDirectory`, `m_FileName`, `m_InputDeck`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMCubesReader
- **bl_idname**: `VTKMCubesReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FlipNormals`, `m_Normals`, `m_SwapBytes`, `m_FileName`, `m_LimitsFileName`, `m_ObjectName`, `m_HeaderSize`, `e_DataByteOrder`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMFIXReader
- **bl_idname**: `VTKMFIXReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMINCImageReader
- **bl_idname**: `VTKMINCImageReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_RescaleRealValues`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `m_TimeStep`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMNIObjectReader
- **bl_idname**: `VTKMNIObjectReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMNITagPointReader
- **bl_idname**: `VTKMNITagPointReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMNITransformReader
- **bl_idname**: `VTKMNITransformReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMPASReader
- **bl_idname**: `VTKMPASReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_IsAtmosphere`, `m_IsZeroCentered`, `m_ProjectLatLon`, `m_ShowMultilayerView`, `m_UseDimensionedArrayNames`, `m_FileName`, `m_ObjectName`, `m_VerticalDimension`, `m_LayerThickness`, `m_VerticalLevel`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMRCReader
- **bl_idname**: `VTKMRCReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMedicalImageReader2
- **bl_idname**: `VTKMedicalImageReader2Type`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_Date`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ImageNumber`, `m_Modality`, `m_ObjectName`, `m_PatientID`, `m_PatientName`, `m_Series`, `m_Study`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMetaImageReader
- **bl_idname**: `VTKMetaImageReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMotionFXCFGReader
- **bl_idname**: `VTKMotionFXCFGReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_TimeResolution`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMultiBlockPLOT3DReader
- **bl_idname**: `VTKMultiBlockPLOT3DReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_AutoDetectFormat`, `m_BinaryFile`, `m_DoublePrecision`, `m_ForceRead`, `m_HasByteCount`, `m_IBlanking`, `m_MultiGrid`, `m_PreserveIntermediateFunctions`, `m_TwoDimensionalGeometry`, `m_FileName`, `m_FunctionFileName`, `m_ObjectName`, `m_QFileName`, `m_XYZFileName`, `m_ScalarFunctionNumber`, `m_VectorFunctionNumber`, `m_Gamma`, `m_R`, `e_ByteOrder`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMultiNewickTreeReader
- **bl_idname**: `VTKMultiNewickTreeReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkNIFTIImageReader
- **bl_idname**: `VTKNIFTIImageReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_PlanarRGB`, `m_SwapBytes`, `m_TimeAsVector`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkNetCDFCFReader
- **bl_idname**: `VTKNetCDFCFReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReplaceFillValueWithNan`, `m_SphericalCoordinates`, `m_FileName`, `m_ObjectName`, `m_VerticalBias`, `m_VerticalScale`, `e_OutputType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkNetCDFPOPReader
- **bl_idname**: `VTKNetCDFPOPReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_Stride`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkNetCDFReader
- **bl_idname**: `VTKNetCDFReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReplaceFillValueWithNan`, `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkNewickTreeReader
- **bl_idname**: `VTKNewickTreeReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkNrrdReader
- **bl_idname**: `VTKNrrdReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_ScalarArrayName`, `m_DataMask`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataVOI`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOBJReader
- **bl_idname**: `VTKOBJReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOMETIFFReader
- **bl_idname**: `VTKOMETIFFReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_IgnoreColorMap`, `m_OriginSpecifiedFlag`, `m_SpacingSpecifiedFlag`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `m_OrientationType`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOMFReader
- **bl_idname**: `VTKOMFReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ColumnMajorOrdering`, `m_WriteOutTextures`, `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOpenFOAMReader
- **bl_idname**: `VTKOpenFOAMReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_AddDimensionsToArrayNames`, `m_CacheMesh`, `m_CopyDataToCellZones`, `m_CreateCellToPoint`, `m_DecomposePolyhedra`, `m_ListTimeStepsByControlDict`, `m_PositionsIsIn13Format`, `m_ReadZones`, `m_SkipZeroTime`, `m_Use64BitFloats`, `m_Use64BitLabels`, `m_FileName`, `m_ObjectName`, `m_TimeValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPChacoReader
- **bl_idname**: `VTKPChacoReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_GenerateEdgeWeightArrays`, `m_GenerateGlobalElementIdArray`, `m_GenerateGlobalNodeIdArray`, `m_GenerateVertexWeightArrays`, `m_BaseName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPDBReader
- **bl_idname**: `VTKPDBReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_BScale`, `m_HBScale`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPDataSetReader
- **bl_idname**: `VTKPDataSetReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPExodusIIReader
- **bl_idname**: `VTKPExodusIIReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_AnimateModeShapes`, `m_ApplyDisplacements`, `m_GenerateFileIdArray`, `m_GenerateGlobalElementIdArray`, `m_GenerateGlobalNodeIdArray`, `m_GenerateImplicitElementIdArray`, `m_GenerateImplicitNodeIdArray`, `m_GenerateObjectIdCellArray`, `m_HasModeShapes`, `m_IgnoreFileTime`, `m_SqueezePoints`, `m_UseLegacyBlockNames`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_XMLFileName`, `m_DisplayType`, `m_FileId`, `m_TimeStep`, `m_CacheSize`, `m_DisplacementMagnitude`, `m_ModeShapeTime`, `m_VariableCacheSize`, `m_FileRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPIOReader
- **bl_idname**: `VTKPIOReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_Float64`, `m_HyperTreeGrid`, `m_Tracers`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_CurrentTimeStep`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPLSDynaReader
- **bl_idname**: `VTKPLSDynaReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_DeformedMesh`, `m_DeletedCellsAsGhostArray`, `m_RemoveDeletedCells`, `m_DatabaseDirectory`, `m_FileName`, `m_InputDeck`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPLYReader
- **bl_idname**: `VTKPLYReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_DuplicatePointsForFaceTexture`, `m_ReadFromInputString`, `m_FileName`, `m_ObjectName`, `m_FaceTextureTolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPNGReader
- **bl_idname**: `VTKPNGReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_ReadSpacingFromFile`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPNMReader
- **bl_idname**: `VTKPNMReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_ScalarArrayName`, `m_DataMask`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataVOI`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPOpenFOAMReader
- **bl_idname**: `VTKPOpenFOAMReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_AddDimensionsToArrayNames`, `m_CacheMesh`, `m_CopyDataToCellZones`, `m_CreateCellToPoint`, `m_DecomposePolyhedra`, `m_ListTimeStepsByControlDict`, `m_PositionsIsIn13Format`, `m_ReadZones`, `m_SkipZeroTime`, `m_Use64BitFloats`, `m_Use64BitLabels`, `m_FileName`, `m_ObjectName`, `m_TimeValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPTSReader
- **bl_idname**: `VTKPTSReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_CreateCells`, `m_IncludeColorAndLuminance`, `m_LimitReadToBounds`, `m_LimitToMaxNumberOfPoints`, `m_OutputDataTypeIsDouble`, `m_FileName`, `m_ObjectName`, `m_MaxNumberOfPoints`, `m_ReadBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParticleReader
- **bl_idname**: `VTKParticleReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_HasScalar`, `m_SwapBytes`, `m_FileName`, `m_ObjectName`, `e_DataByteOrder`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPhyloXMLTreeReader
- **bl_idname**: `VTKPhyloXMLTreeReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPlot3DMetaReader
- **bl_idname**: `VTKPlot3DMetaReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataReader
- **bl_idname**: `VTKPolyDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProStarReader
- **bl_idname**: `VTKProStarReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_ScaleFactor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRISReader
- **bl_idname**: `VTKRISReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_Delimiter`, `m_FileName`, `m_ObjectName`, `m_MaxRecords`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRTXMLPolyDataReader
- **bl_idname**: `VTKRTXMLPolyDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRectilinearGridReader
- **bl_idname**: `VTKRectilinearGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSEPReader
- **bl_idname**: `VTKSEPReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_ExtentSplitMode`, `m_OutputGridDimension`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSLACParticleReader
- **bl_idname**: `VTKSLACParticleReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSLACReader
- **bl_idname**: `VTKSLACReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadExternalSurface`, `m_ReadInternalVolume`, `m_ReadMidpoints`, `m_MeshFileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSLCReader
- **bl_idname**: `VTKSLCReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSQLiteToTableReader
- **bl_idname**: `VTKSQLiteToTableReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSTLReader
- **bl_idname**: `VTKSTLReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_Merging`, `m_ScalarTags`, `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSegYReader
- **bl_idname**: `VTKSegYReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_Force2D`, `m_StructuredGrid`, `m_FileName`, `m_ObjectName`, `m_VerticalCRS`, `m_XCoordByte`, `m_YCoordByte`, `e_XYCoordMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSimplePointsReader
- **bl_idname**: `VTKSimplePointsReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredGridReader
- **bl_idname**: `VTKStructuredGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredPointsReader
- **bl_idname**: `VTKStructuredPointsReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTGAReader
- **bl_idname**: `VTKTGAReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTIFFReader
- **bl_idname**: `VTKTIFFReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileLowerLeft`, `m_IgnoreColorMap`, `m_OriginSpecifiedFlag`, `m_SpacingSpecifiedFlag`, `m_SwapBytes`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_FileNameSliceOffset`, `m_FileNameSliceSpacing`, `m_HeaderSize`, `m_MemoryBufferLength`, `m_NumberOfScalarComponents`, `m_OrientationType`, `e_DataByteOrder`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTRUCHASReader
- **bl_idname**: `VTKTRUCHASReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTableReader
- **bl_idname**: `VTKTableReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTecplotReader
- **bl_idname**: `VTKTecplotReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTecplotTableReader
- **bl_idname**: `VTKTecplotTableReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_GeneratePedigreeIds`, `m_OutputPedigreeIds`, `m_FileName`, `m_ObjectName`, `m_PedigreeIdArrayName`, `m_ColumnNamesOnLine`, `m_HeaderLines`, `m_MaxRecords`, `m_SkipColumnNames`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTemporalDelimitedTextReader
- **bl_idname**: `VTKTemporalDelimitedTextReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_AddTabFieldDelimiter`, `m_DetectNumericColumns`, `m_ForceDouble`, `m_GeneratePedigreeIds`, `m_HaveHeaders`, `m_MergeConsecutiveDelimiters`, `m_OutputPedigreeIds`, `m_ReadFromInputString`, `m_RemoveTimeStepColumn`, `m_TrimWhitespacePriorToNumericConversion`, `m_UseStringDelimiter`, `m_FieldDelimiterCharacters`, `m_FileName`, `m_ObjectName`, `m_PedigreeIdArrayName`, `m_StringDelimiter`, `m_TimeColumnName`, `m_UTF8FieldDelimiters`, `m_UTF8RecordDelimiters`, `m_UTF8StringDelimiters`, `m_UnicodeCharacterSet`, `m_DefaultIntegerValue`, `m_MaxRecords`, `m_ReplacementCharacter`, `m_TimeColumnId`, `m_DefaultDoubleValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTreeReader
- **bl_idname**: `VTKTreeReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTulipReader
- **bl_idname**: `VTKTulipReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUnstructuredGridReader
- **bl_idname**: `VTKUnstructuredGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadAllColorScalars`, `m_ReadAllFields`, `m_ReadAllNormals`, `m_ReadAllScalars`, `m_ReadAllTCoords`, `m_ReadAllTensors`, `m_ReadAllVectors`, `m_ReadFromInputString`, `m_FieldDataName`, `m_FileName`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVASPAnimationReader
- **bl_idname**: `VTKVASPAnimationReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVASPTessellationReader
- **bl_idname**: `VTKVASPTessellationReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVPICReader
- **bl_idname**: `VTKVPICReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_Stride`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVeraOutReader
- **bl_idname**: `VTKVeraOutReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVolume16Reader
- **bl_idname**: `VTKVolume16ReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_SwapBytes`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_DataMask`, `m_HeaderSize`, `e_DataByteOrder`, `m_DataDimensions`, `m_ImageRange`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkWindBladeReader
- **bl_idname**: `VTKWindBladeReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_Filename`, `m_ObjectName`, `m_SubExtent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXGMLReader
- **bl_idname**: `VTKXGMLReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLGenericDataObjectReader
- **bl_idname**: `VTKXMLGenericDataObjectReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLHierarchicalBoxDataReader
- **bl_idname**: `VTKXMLHierarchicalBoxDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_MaximumLevelsToReadByDefault`, `m_PieceDistribution`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLHierarchicalDataReader
- **bl_idname**: `VTKXMLHierarchicalDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_PieceDistribution`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLHyperTreeGridReader
- **bl_idname**: `VTKXMLHyperTreeGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_FixedLevel`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLImageDataReader
- **bl_idname**: `VTKXMLImageDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_WholeSlices`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLMultiBlockDataReader
- **bl_idname**: `VTKXMLMultiBlockDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_PieceDistribution`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLMultiGroupDataReader
- **bl_idname**: `VTKXMLMultiGroupDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_PieceDistribution`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPHyperTreeGridReader
- **bl_idname**: `VTKXMLPHyperTreeGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPImageDataReader
- **bl_idname**: `VTKXMLPImageDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPPolyDataReader
- **bl_idname**: `VTKXMLPPolyDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPRectilinearGridReader
- **bl_idname**: `VTKXMLPRectilinearGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPStructuredGridReader
- **bl_idname**: `VTKXMLPStructuredGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPTableReader
- **bl_idname**: `VTKXMLPTableReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPUnstructuredGridReader
- **bl_idname**: `VTKXMLPUnstructuredGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPartitionedDataSetCollectionReader
- **bl_idname**: `VTKXMLPartitionedDataSetCollectionReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_PieceDistribution`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPartitionedDataSetReader
- **bl_idname**: `VTKXMLPartitionedDataSetReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_PieceDistribution`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPolyDataReader
- **bl_idname**: `VTKXMLPolyDataReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLRectilinearGridReader
- **bl_idname**: `VTKXMLRectilinearGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_WholeSlices`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLStructuredGridReader
- **bl_idname**: `VTKXMLStructuredGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_WholeSlices`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLTableReader
- **bl_idname**: `VTKXMLTableReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLTreeReader
- **bl_idname**: `VTKXMLTreeReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_GenerateEdgePedigreeIds`, `m_GenerateVertexPedigreeIds`, `m_MaskArrays`, `m_ReadCharData`, `m_ReadTagName`, `m_EdgePedigreeIdArrayName`, `m_FileName`, `m_ObjectName`, `m_VertexPedigreeIdArrayName`, `m_XMLString`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLUniformGridAMRReader
- **bl_idname**: `VTKXMLUniformGridAMRReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_MaximumLevelsToReadByDefault`, `m_PieceDistribution`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLUnstructuredGridReader
- **bl_idname**: `VTKXMLUnstructuredGridReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_ActiveTimeDataArrayName`, `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_TimeStepRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXYZMolReader
- **bl_idname**: `VTKXYZMolReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_TimeStep`, `m_BScale`, `m_HBScale`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXYZMolReader2
- **bl_idname**: `VTKXYZMolReader2Type`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXdmfReader
- **bl_idname**: `VTKXdmfReaderType`
- **module**: `generated_nodes/gen_VTKReaders.py`
- **properties**: `m_ReadFromInputString`, `m_DomainName`, `m_FileName`, `m_ObjectName`, `m_Stride`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

## Source

### vtkAMRGaussianPulseSource
- **bl_idname**: `VTKAMRGaussianPulseSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_PulseAmplitude`, `m_PulseOrigin`, `m_PulseWidth`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkArcSource
- **bl_idname**: `VTKArcSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Negative`, `m_UseNormalAndAngle`, `m_ObjectName`, `m_Resolution`, `m_Angle`, `m_Center`, `m_Normal`, `m_Point1`, `m_Point2`, `m_PolarVector`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkArrowSource
- **bl_idname**: `VTKArrowSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Invert`, `m_ObjectName`, `m_ShaftResolution`, `m_TipResolution`, `m_ShaftRadius`, `m_TipLength`, `m_TipRadius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkAxes
- **bl_idname**: `VTKAxesType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ComputeNormals`, `m_Symmetric`, `m_ObjectName`, `m_ScaleFactor`, `m_Origin`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBooleanTexture
- **bl_idname**: `VTKBooleanTextureType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_Thickness`, `m_XSize`, `m_YSize`, `m_InIn`, `m_InOn`, `m_InOut`, `m_OnIn`, `m_OnOn`, `m_OnOut`, `m_OutIn`, `m_OutOn`, `m_OutOut`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBoundedPointSource
- **bl_idname**: `VTKBoundedPointSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ProduceCellOutput`, `m_ProduceRandomScalars`, `m_ObjectName`, `m_NumberOfPoints`, `m_Bounds`, `m_ScalarRange`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCameraHandleSource
- **bl_idname**: `VTKCameraHandleSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Directional`, `m_ObjectName`, `m_Size`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCapsuleSource
- **bl_idname**: `VTKCapsuleSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_LatLongTessellation`, `m_ObjectName`, `m_PhiResolution`, `m_ThetaResolution`, `m_CylinderLength`, `m_Radius`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCellTypeSource
- **bl_idname**: `VTKCellTypeSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_CompleteQuadraticSimplicialElements`, `m_ObjectName`, `m_CellOrder`, `m_CellType`, `m_OutputPrecision`, `m_PolynomialFieldOrder`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkConeSource
- **bl_idname**: `VTKConeSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Capping`, `m_ObjectName`, `m_Resolution`, `m_Angle`, `m_Height`, `m_Radius`, `m_Center`, `m_Direction`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCubeSource
- **bl_idname**: `VTKCubeSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_XLength`, `m_YLength`, `m_ZLength`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCursor2D
- **bl_idname**: `VTKCursor2DType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Axes`, `m_Outline`, `m_Point`, `m_TranslationMode`, `m_Wrap`, `m_ObjectName`, `m_Radius`, `m_ModelBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCursor3D
- **bl_idname**: `VTKCursor3DType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Axes`, `m_Outline`, `m_TranslationMode`, `m_Wrap`, `m_XShadows`, `m_YShadows`, `m_ZShadows`, `m_ObjectName`, `m_ModelBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCylinderSource
- **bl_idname**: `VTKCylinderSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Capping`, `m_ObjectName`, `m_Resolution`, `m_Height`, `m_Radius`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataObjectGenerator
- **bl_idname**: `VTKDataObjectGeneratorType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_Program`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDiagonalMatrixSource
- **bl_idname**: `VTKDiagonalMatrixSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ColumnLabel`, `m_ObjectName`, `m_RowLabel`, `m_ArrayType`, `m_Extents`, `m_Diagonal`, `m_SubDiagonal`, `m_SuperDiagonal`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDiskSource
- **bl_idname**: `VTKDiskSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_CircumferentialResolution`, `m_RadialResolution`, `m_InnerRadius`, `m_OuterRadius`, `m_Center`, `m_Normal`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEarthSource
- **bl_idname**: `VTKEarthSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Outline`, `m_ObjectName`, `m_OnRatio`, `m_Radius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEllipseArcSource
- **bl_idname**: `VTKEllipseArcSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Close`, `m_ObjectName`, `m_Resolution`, `m_Ratio`, `m_SegmentAngle`, `m_StartAngle`, `m_Center`, `m_MajorRadiusVector`, `m_Normal`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEllipticalButtonSource
- **bl_idname**: `VTKEllipticalButtonSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_TwoSided`, `m_ObjectName`, `m_CircumferentialResolution`, `m_ShoulderResolution`, `m_TextureResolution`, `m_Depth`, `m_Height`, `m_RadialRatio`, `m_Width`, `e_TextureStyle`, `m_TextureDimensions`, `m_Center`, `m_ShoulderTextureCoordinate`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEnsembleSource
- **bl_idname**: `VTKEnsembleSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_CurrentMember`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFrustumSource
- **bl_idname**: `VTKFrustumSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ShowLines`, `m_ObjectName`, `m_LinesLength`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGlyphSource2D
- **bl_idname**: `VTKGlyphSource2DType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Cross`, `m_Dash`, `m_Filled`, `m_ObjectName`, `m_Resolution`, `m_RotationAngle`, `m_Scale`, `m_Scale2`, `e_GlyphType`, `m_Center`, `m_Color`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridPreConfiguredSource
- **bl_idname**: `VTKHyperTreeGridPreConfiguredSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_CustomDepth`, `m_CustomDim`, `m_CustomFactor`, `m_CustomSubdivisions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHyperTreeGridSource
- **bl_idname**: `VTKHyperTreeGridSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_GenerateInterfaceFields`, `m_TransposedRootIndexing`, `m_UseDescriptor`, `m_UseMask`, `m_Descriptor`, `m_Mask`, `m_ObjectName`, `m_BranchFactor`, `m_MaxDepth`, `m_GridScale`, `m_Origin`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageCanvasSource2D
- **bl_idname**: `VTKImageCanvasSource2DType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_DefaultZ`, `m_NumberOfScalarComponents`, `e_ScalarType`, `m_DrawColor`, `m_Ratio`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageEllipsoidSource
- **bl_idname**: `VTKImageEllipsoidSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_InValue`, `m_OutValue`, `e_OutputScalarType`, `m_Center`, `m_Radius`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageGaussianSource
- **bl_idname**: `VTKImageGaussianSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_Maximum`, `m_StandardDeviation`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageGridSource
- **bl_idname**: `VTKImageGridSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_FillValue`, `m_LineValue`, `e_DataScalarType`, `m_GridOrigin`, `m_GridSpacing`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageImport
- **bl_idname**: `VTKImageImportType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_ScalarArrayName`, `m_NumberOfScalarComponents`, `e_DataScalarType`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageMandelbrotSource
- **bl_idname**: `VTKImageMandelbrotSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ConstantSize`, `m_ObjectName`, `m_MaximumNumberOfIterations`, `m_SubsampleRate`, `m_ProjectionAxes`, `m_OriginCX`, `m_SampleCX`, `m_SizeCX`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageNoiseSource
- **bl_idname**: `VTKImageNoiseSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_Maximum`, `m_Minimum`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageSinusoidSource
- **bl_idname**: `VTKImageSinusoidSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_Amplitude`, `m_Period`, `m_Phase`, `m_Direction`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImplicitFunctionToImageStencil
- **bl_idname**: `VTKImplicitFunctionToImageStencilType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_Threshold`, `m_OutputWholeExtent`, `m_OutputOrigin`, `m_OutputSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLassoStencilSource
- **bl_idname**: `VTKLassoStencilSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_SliceOrientation`, `e_Shape`, `m_OutputWholeExtent`, `m_OutputOrigin`, `m_OutputSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLineSource
- **bl_idname**: `VTKLineSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_UseRegularRefinement`, `m_ObjectName`, `m_NumberOfRefinementRatios`, `m_Resolution`, `m_Point1`, `m_Point2`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOutlineCornerSource
- **bl_idname**: `VTKOutlineCornerSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_GenerateFaces`, `m_ObjectName`, `m_CornerFactor`, `e_BoxType`, `m_Bounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOutlineSource
- **bl_idname**: `VTKOutlineSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_GenerateFaces`, `m_ObjectName`, `e_BoxType`, `m_Bounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPSphereSource
- **bl_idname**: `VTKPSphereSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_GenerateNormals`, `m_LatLongTessellation`, `m_ObjectName`, `m_PhiResolution`, `m_ThetaResolution`, `m_EndPhi`, `m_EndTheta`, `m_Radius`, `m_StartPhi`, `m_StartTheta`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkParametricFunctionSource
- **bl_idname**: `VTKParametricFunctionSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_GenerateNormals`, `m_GenerateTextureCoordinates`, `m_ObjectName`, `m_UResolution`, `m_VResolution`, `m_WResolution`, `e_ScalarMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPartitionedDataSetCollectionSource
- **bl_idname**: `VTKPartitionedDataSetCollectionSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_NumberOfShapes`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPartitionedDataSetSource
- **bl_idname**: `VTKPartitionedDataSetSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_NumberOfPartitions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPlaneSource
- **bl_idname**: `VTKPlaneSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_XResolution`, `m_YResolution`, `m_Center`, `m_Normal`, `m_Origin`, `m_Point1`, `m_Point2`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPlatonicSolidSource
- **bl_idname**: `VTKPlatonicSolidSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `e_SolidType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointHandleSource
- **bl_idname**: `VTKPointHandleSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Directional`, `m_ObjectName`, `m_Size`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointLoad
- **bl_idname**: `VTKPointLoadType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ComputeEffectiveStress`, `m_ObjectName`, `m_LoadValue`, `m_PoissonsRatio`, `m_ModelBounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPointSource
- **bl_idname**: `VTKPointSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_NumberOfPoints`, `m_Lambda`, `m_Radius`, `e_Distribution`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyLineSource
- **bl_idname**: `VTKPolyLineSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Closed`, `m_ObjectName`, `m_NumberOfPoints`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyPointSource
- **bl_idname**: `VTKPolyPointSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_NumberOfPoints`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkProgrammableDataObjectSource
- **bl_idname**: `VTKProgrammableDataObjectSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkROIStencilSource
- **bl_idname**: `VTKROIStencilSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `e_Shape`, `m_OutputWholeExtent`, `m_Bounds`, `m_OutputOrigin`, `m_OutputSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRTAnalyticSource
- **bl_idname**: `VTKRTAnalyticSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_SubsampleRate`, `m_Maximum`, `m_StandardDeviation`, `m_XFreq`, `m_XMag`, `m_YFreq`, `m_YMag`, `m_ZFreq`, `m_ZMag`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRandomHyperTreeGridSource
- **bl_idname**: `VTKRandomHyperTreeGridSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_MaxDepth`, `m_Seed`, `m_SplitFraction`, `m_Dimensions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRectangularButtonSource
- **bl_idname**: `VTKRectangularButtonSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_TwoSided`, `m_ObjectName`, `m_BoxRatio`, `m_Depth`, `m_Height`, `m_TextureHeightRatio`, `m_TextureRatio`, `m_Width`, `e_TextureStyle`, `m_TextureDimensions`, `m_Center`, `m_ShoulderTextureCoordinate`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRegularPolygonSource
- **bl_idname**: `VTKRegularPolygonSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_GeneratePolygon`, `m_GeneratePolyline`, `m_ObjectName`, `m_NumberOfSides`, `m_Radius`, `m_Center`, `m_Normal`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkResizingWindowToImageFilter
- **bl_idname**: `VTKResizingWindowToImageFilterType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_SizeLimit`, `e_InputBufferType`, `m_Size`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRowQueryToTable
- **bl_idname**: `VTKRowQueryToTableType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSQLDatabaseTableSource
- **bl_idname**: `VTKSQLDatabaseTableSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_GeneratePedigreeIds`, `m_ObjectName`, `m_PedigreeIdArrayName`, `m_Query`, `m_URL`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSampleFunction
- **bl_idname**: `VTKSampleFunctionType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Capping`, `m_ComputeNormals`, `m_NormalArrayName`, `m_ObjectName`, `m_ScalarArrayName`, `m_CapValue`, `e_OutputScalarType`, `m_SampleDimensions`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSectorSource
- **bl_idname**: `VTKSectorSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_CircumferentialResolution`, `m_RadialResolution`, `m_EndAngle`, `m_InnerRadius`, `m_OuterRadius`, `m_StartAngle`, `m_ZCoord`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSelectionSource
- **bl_idname**: `VTKSelectionSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Expression`, `m_ObjectName`, `m_ElementType`, `m_FieldType`, `m_NumberOfNodes`, `m_ProcessID`, `e_FieldTypeOption`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSpherePuzzle
- **bl_idname**: `VTKSpherePuzzleType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSpherePuzzleArrows
- **bl_idname**: `VTKSpherePuzzleArrowsType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSphereSource
- **bl_idname**: `VTKSphereSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_GenerateNormals`, `m_LatLongTessellation`, `m_ObjectName`, `m_PhiResolution`, `m_ThetaResolution`, `m_EndPhi`, `m_EndTheta`, `m_Radius`, `m_StartPhi`, `m_StartTheta`, `m_Center`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSuperquadricSource
- **bl_idname**: `VTKSuperquadricSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Toroidal`, `m_ObjectName`, `m_AxisOfSymmetry`, `m_PhiResolution`, `m_ThetaResolution`, `m_PhiRoundness`, `m_Size`, `m_ThetaRoundness`, `m_Thickness`, `m_Center`, `m_Scale`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTemporalFractal
- **bl_idname**: `VTKTemporalFractalType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_AdaptiveSubdivision`, `m_DiscreteTimeSteps`, `m_GenerateRectilinearGrids`, `m_GhostLevels`, `m_TwoDimensional`, `m_ObjectName`, `m_Asymmetric`, `m_Dimensions`, `m_MaximumLevel`, `m_FractalValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTessellatedBoxSource
- **bl_idname**: `VTKTessellatedBoxSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_DuplicateSharedPoints`, `m_Quads`, `m_ObjectName`, `m_Level`, `m_Bounds`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTextSource
- **bl_idname**: `VTKTextSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Backing`, `m_ObjectName`, `m_Text`, `m_BackgroundColor`, `m_ForegroundColor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTexturedSphereSource
- **bl_idname**: `VTKTexturedSphereSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_PhiResolution`, `m_ThetaResolution`, `m_Phi`, `m_Radius`, `m_Theta`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTimeSourceExample
- **bl_idname**: `VTKTimeSourceExampleType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_Analytic`, `m_Growing`, `m_ObjectName`, `m_XAmplitude`, `m_YAmplitude`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransformToGrid
- **bl_idname**: `VTKTransformToGridType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `e_GridScalarType`, `m_GridExtent`, `m_GridOrigin`, `m_GridSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTriangularTexture
- **bl_idname**: `VTKTriangularTextureType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_TexturePattern`, `m_XSize`, `m_YSize`, `m_ScaleFactor`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTrivialProducer
- **bl_idname**: `VTKTrivialProducerType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUniformHyperTreeGridSource
- **bl_idname**: `VTKUniformHyperTreeGridSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_GenerateInterfaceFields`, `m_TransposedRootIndexing`, `m_UseDescriptor`, `m_UseMask`, `m_Descriptor`, `m_Mask`, `m_ObjectName`, `m_BranchFactor`, `m_MaxDepth`, `m_GridScale`, `m_Origin`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVectorText
- **bl_idname**: `VTKVectorTextType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_ObjectName`, `m_Text`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkVideoSource
- **bl_idname**: `VTKVideoSourceType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_AutoAdvance`, `m_ObjectName`, `m_FrameBufferSize`, `m_FrameCount`, `m_NumberOfOutputFrames`, `m_FrameRate`, `m_Opacity`, `m_StartTimeStamp`, `e_OutputFormat`, `m_FrameSize`, `m_OutputWholeExtent`, `m_DataOrigin`, `m_DataSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkWindowToImageFilter
- **bl_idname**: `VTKWindowToImageFilterType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_FixBoundary`, `m_ReadFrontBuffer`, `m_ShouldRerender`, `m_ObjectName`, `e_InputBufferType`, `m_Scale`, `m_Viewport`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkWordCloud
- **bl_idname**: `VTKWordCloudType`
- **module**: `generated_nodes/gen_VTKSources.py`
- **properties**: `m_BWMask`, `m_BackgroundColorName`, `m_ColorSchemeName`, `m_FileName`, `m_FontFileName`, `m_MaskColorName`, `m_MaskFileName`, `m_ObjectName`, `m_StopListFileName`, `m_Title`, `m_WordColorName`, `m_DPI`, `m_FontMultiplier`, `m_Gap`, `m_MaxFontSize`, `m_MinFontSize`, `m_MinFrequency`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

## Transform

### vtkBSplineTransform
- **bl_idname**: `VTKBSplineTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_ObjectName`, `m_InverseIterations`, `m_DisplacementScale`, `m_InverseTolerance`, `e_BorderMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCylindricalTransform
- **bl_idname**: `VTKCylindricalTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_ObjectName`, `m_InverseIterations`, `m_InverseTolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGeneralTransform
- **bl_idname**: `VTKGeneralTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGridTransform
- **bl_idname**: `VTKGridTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_ObjectName`, `m_InverseIterations`, `m_DisplacementScale`, `m_DisplacementShift`, `m_InverseTolerance`, `e_InterpolationMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkIdentityTransform
- **bl_idname**: `VTKIdentityTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkIterativeClosestPointTransform
- **bl_idname**: `VTKIterativeClosestPointTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_CheckMeanDistance`, `m_StartByMatchingCentroids`, `m_ObjectName`, `m_MaximumNumberOfIterations`, `m_MaximumNumberOfLandmarks`, `m_MaximumMeanDistance`, `e_MeanDistanceMode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkLandmarkTransform
- **bl_idname**: `VTKLandmarkTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_ObjectName`, `e_Mode`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMatrixToHomogeneousTransform
- **bl_idname**: `VTKMatrixToHomogeneousTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMatrixToLinearTransform
- **bl_idname**: `VTKMatrixToLinearTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPerspectiveTransform
- **bl_idname**: `VTKPerspectiveTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSphericalTransform
- **bl_idname**: `VTKSphericalTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_ObjectName`, `m_InverseIterations`, `m_InverseTolerance`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkThinPlateSplineTransform
- **bl_idname**: `VTKThinPlateSplineTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_RegularizeBulkTransform`, `m_ObjectName`, `m_InverseIterations`, `m_InverseTolerance`, `m_Sigma`, `e_Basis`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTransform
- **bl_idname**: `VTKTransformType`
- **module**: `generated_nodes/gen_VTKTransform.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

## Writer

### vtkArrayDataWriter
- **bl_idname**: `VTKArrayDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_Binary`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkArrayWriter
- **bl_idname**: `VTKArrayWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_Binary`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBMPWriter
- **bl_idname**: `VTKBMPWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteToMemory`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkBYUWriter
- **bl_idname**: `VTKBYUWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteDisplacement`, `m_WriteScalar`, `m_WriteTexture`, `m_DisplacementFileName`, `m_GeometryFileName`, `m_ObjectName`, `m_ScalarFileName`, `m_TextureFileName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCesium3DTilesWriter
- **bl_idname**: `VTKCesium3DTilesWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_ContentGLTF`, `m_MergeTilePolyData`, `m_SaveTextures`, `m_SaveTiles`, `m_CRS`, `m_DirectoryName`, `m_ObjectName`, `m_TextureBaseDirectory`, `m_InputType`, `m_NumberOfFeaturesPerTile`, `m_Offset`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCesiumPointCloudWriter
- **bl_idname**: `VTKCesiumPointCloudWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkCompositeDataWriter
- **bl_idname**: `VTKCompositeDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDIMACSGraphWriter
- **bl_idname**: `VTKDIMACSGraphWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataObjectWriter
- **bl_idname**: `VTKDataObjectWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteToOutputString`, `m_FieldDataName`, `m_FileName`, `m_Header`, `m_ObjectName`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataSetWriter
- **bl_idname**: `VTKDataSetWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDataWriter
- **bl_idname**: `VTKDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkDelimitedTextWriter
- **bl_idname**: `VTKDelimitedTextWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_UseStringDelimiter`, `m_WriteToOutputString`, `m_FieldDelimiter`, `m_FileName`, `m_ObjectName`, `m_StringDelimiter`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkEnSightWriter
- **bl_idname**: `VTKEnSightWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_TransientGeometry`, `m_BaseName`, `m_FileName`, `m_ObjectName`, `m_Path`, `m_GhostLevel`, `m_NumberOfBlocks`, `m_ProcessNumber`, `m_TimeStep`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkExodusIIWriter
- **bl_idname**: `VTKExodusIIWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_IgnoreMetaDataWarning`, `m_WriteAllTimeSteps`, `m_WriteOutBlockIdArray`, `m_WriteOutGlobalElementIdArray`, `m_WriteOutGlobalNodeIdArray`, `m_BlockIdArrayName`, `m_FileName`, `m_ObjectName`, `m_GhostLevel`, `m_StoreDoubles`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkFacetWriter
- **bl_idname**: `VTKFacetWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGLTFWriter
- **bl_idname**: `VTKGLTFWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_InlineData`, `m_SaveActivePointColor`, `m_SaveBatchId`, `m_SaveNormal`, `m_SaveTextures`, `m_FileName`, `m_ObjectName`, `m_TextureBaseDirectory`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGenericDataObjectWriter
- **bl_idname**: `VTKGenericDataObjectWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGeoJSONWriter
- **bl_idname**: `VTKGeoJSONWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_ScalarFormat`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkGraphWriter
- **bl_idname**: `VTKGraphWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkHoudiniPolyDataWriter
- **bl_idname**: `VTKHoudiniPolyDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkIOSSWriter
- **bl_idname**: `VTKIOSSWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_OffsetGlobalIds`, `m_PreserveInputEntityGroups`, `m_FileName`, `m_ObjectName`, `m_MaximumTimeStepsPerFile`, `m_DisplacementMagnitude`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkIVWriter
- **bl_idname**: `VTKIVWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkImageWriter
- **bl_idname**: `VTKImageWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkJPEGWriter
- **bl_idname**: `VTKJPEGWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_Progressive`, `m_WriteToMemory`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_Quality`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkJSONDataSetWriter
- **bl_idname**: `VTKJSONDataSetWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkJSONImageWriter
- **bl_idname**: `VTKJSONImageWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_ArrayName`, `m_FileName`, `m_ObjectName`, `m_Slice`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkJavaScriptDataWriter
- **bl_idname**: `VTKJavaScriptDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_IncludeFieldNames`, `m_FileName`, `m_ObjectName`, `m_VariableName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMCubesWriter
- **bl_idname**: `VTKMCubesWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_LimitsFileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMINCImageWriter
- **bl_idname**: `VTKMINCImageWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_StrictValidation`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_HistoryAddition`, `m_ObjectName`, `m_FileDimensionality`, `m_RescaleIntercept`, `m_RescaleSlope`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMNIObjectWriter
- **bl_idname**: `VTKMNIObjectWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_ObjectName`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMNITagPointWriter
- **bl_idname**: `VTKMNITagPointWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_Comments`, `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMNITransformWriter
- **bl_idname**: `VTKMNITransformWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_Comments`, `m_FileName`, `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkMetaImageWriter
- **bl_idname**: `VTKMetaImageWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_Compression`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_RAWFileName`, `m_FileDimensionality`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkNIFTIImageWriter
- **bl_idname**: `VTKNIFTIImageWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_PlanarRGB`, `m_Description`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_NIFTIVersion`, `m_TimeDimension`, `m_QFac`, `m_RescaleIntercept`, `m_RescaleSlope`, `m_TimeSpacing`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkNetCDFCFWriter
- **bl_idname**: `VTKNetCDFCFWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FillBlankedAttributes`, `m_CellArrayNamePostfix`, `m_FileName`, `m_ObjectName`, `m_AttributeType`, `m_FillValue`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkNewickTreeWriter
- **bl_idname**: `VTKNewickTreeWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_EdgeWeightArrayName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NodeNameArrayName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOBJWriter
- **bl_idname**: `VTKOBJWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_ObjectName`, `m_TextureFileName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkOggTheoraWriter
- **bl_idname**: `VTKOggTheoraWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_Subsampling`, `m_FileName`, `m_ObjectName`, `m_Quality`, `m_Rate`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPDataSetWriter
- **bl_idname**: `VTKPDataSetWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_UseRelativeFileNames`, `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_FilePattern`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_EndPiece`, `m_FileVersion`, `m_GhostLevel`, `m_NumberOfPieces`, `m_StartPiece`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPExodusIIWriter
- **bl_idname**: `VTKPExodusIIWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_IgnoreMetaDataWarning`, `m_WriteAllTimeSteps`, `m_WriteOutBlockIdArray`, `m_WriteOutGlobalElementIdArray`, `m_WriteOutGlobalNodeIdArray`, `m_BlockIdArrayName`, `m_FileName`, `m_ObjectName`, `m_GhostLevel`, `m_StoreDoubles`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPImageWriter
- **bl_idname**: `VTKPImageWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `m_MemoryLimit`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPLYWriter
- **bl_idname**: `VTKPLYWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EnableAlpha`, `m_WriteToOutputString`, `m_ArrayName`, `m_FileName`, `m_ObjectName`, `m_Alpha`, `m_Component`, `e_ColorMode`, `e_DataByteOrder`, `e_FileType`, `e_TextureCoordinatesName`, `m_Color`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPNGWriter
- **bl_idname**: `VTKPNGWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteToMemory`, `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_CompressionLevel`, `m_FileDimensionality`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPNMWriter
- **bl_idname**: `VTKPNMWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPhyloXMLTreeWriter
- **bl_idname**: `VTKPhyloXMLTreeWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_EdgeWeightArrayName`, `m_FileName`, `m_NodeNameArrayName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_NumberOfTimeSteps`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPolyDataWriter
- **bl_idname**: `VTKPolyDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkPostScriptWriter
- **bl_idname**: `VTKPostScriptWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkRectilinearGridWriter
- **bl_idname**: `VTKRectilinearGridWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteExtent`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSTLWriter
- **bl_idname**: `VTKSTLWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_Header`, `m_ObjectName`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkSimplePointsWriter
- **bl_idname**: `VTKSimplePointsWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_DecimalPrecision`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredGridWriter
- **bl_idname**: `VTKStructuredGridWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteExtent`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkStructuredPointsWriter
- **bl_idname**: `VTKStructuredPointsWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteExtent`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTIFFWriter
- **bl_idname**: `VTKTIFFWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_FileName`, `m_FilePattern`, `m_FilePrefix`, `m_ObjectName`, `m_FileDimensionality`, `e_Compression`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTableToSQLiteWriter
- **bl_idname**: `VTKTableToSQLiteWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_ObjectName`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTableWriter
- **bl_idname**: `VTKTableWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkTreeWriter
- **bl_idname**: `VTKTreeWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkUnstructuredGridWriter
- **bl_idname**: `VTKUnstructuredGridWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_WriteArrayMetaData`, `m_WriteToOutputString`, `m_EdgeFlagsName`, `m_FieldDataName`, `m_FileName`, `m_GlobalIdsName`, `m_Header`, `m_LookupTableName`, `m_NormalsName`, `m_ObjectName`, `m_PedigreeIdsName`, `m_ScalarsName`, `m_TCoordsName`, `m_TensorsName`, `m_VectorsName`, `m_FileVersion`, `e_FileType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLDataObjectWriter
- **bl_idname**: `VTKXMLDataObjectWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_NumberOfTimeSteps`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLDataSetWriter
- **bl_idname**: `VTKXMLDataSetWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_NumberOfTimeSteps`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLDataWriterHelper
- **bl_idname**: `VTKXMLDataWriterHelperType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_NumberOfTimeSteps`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLHierarchicalBoxDataWriter
- **bl_idname**: `VTKXMLHierarchicalBoxDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_GhostLevel`, `m_NumberOfTimeSteps`, `m_WriteMetaFile`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLHyperTreeGridWriter
- **bl_idname**: `VTKXMLHyperTreeGridWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_NumberOfTimeSteps`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLImageDataWriter
- **bl_idname**: `VTKXMLImageDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_WritePiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`, `m_WriteExtent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLMultiBlockDataWriter
- **bl_idname**: `VTKXMLMultiBlockDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_GhostLevel`, `m_NumberOfTimeSteps`, `m_WriteMetaFile`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPDataSetWriter
- **bl_idname**: `VTKXMLPDataSetWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_UseSubdirectory`, `m_WriteSummaryFile`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_EndPiece`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_StartPiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPHierarchicalBoxDataWriter
- **bl_idname**: `VTKXMLPHierarchicalBoxDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_GhostLevel`, `m_NumberOfTimeSteps`, `m_WriteMetaFile`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPHyperTreeGridWriter
- **bl_idname**: `VTKXMLPHyperTreeGridWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_UseSubdirectory`, `m_WriteSummaryFile`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_EndPiece`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_StartPiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPImageDataWriter
- **bl_idname**: `VTKXMLPImageDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_UseSubdirectory`, `m_WriteSummaryFile`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_EndPiece`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_StartPiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPMultiBlockDataWriter
- **bl_idname**: `VTKXMLPMultiBlockDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_StartPiece`, `m_WriteMetaFile`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPPartitionedDataSetWriter
- **bl_idname**: `VTKXMLPPartitionedDataSetWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_NumberOfGhostLevels`, `m_NumberOfPieces`, `m_StartPiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPPolyDataWriter
- **bl_idname**: `VTKXMLPPolyDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_UseSubdirectory`, `m_WriteSummaryFile`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_EndPiece`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_StartPiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPRectilinearGridWriter
- **bl_idname**: `VTKXMLPRectilinearGridWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_UseSubdirectory`, `m_WriteSummaryFile`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_EndPiece`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_StartPiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPStructuredGridWriter
- **bl_idname**: `VTKXMLPStructuredGridWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_UseSubdirectory`, `m_WriteSummaryFile`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_EndPiece`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_StartPiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPTableWriter
- **bl_idname**: `VTKXMLPTableWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_UseSubdirectory`, `m_WriteSummaryFile`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_EndPiece`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_StartPiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPUniformGridAMRWriter
- **bl_idname**: `VTKXMLPUniformGridAMRWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_GhostLevel`, `m_NumberOfTimeSteps`, `m_WriteMetaFile`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPUnstructuredGridWriter
- **bl_idname**: `VTKXMLPUnstructuredGridWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_UseSubdirectory`, `m_WriteSummaryFile`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_EndPiece`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_StartPiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPartitionedDataSetCollectionWriter
- **bl_idname**: `VTKXMLPartitionedDataSetCollectionWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_NumberOfGhostLevels`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPartitionedDataSetWriter
- **bl_idname**: `VTKXMLPartitionedDataSetWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_NumberOfGhostLevels`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLPolyDataWriter
- **bl_idname**: `VTKXMLPolyDataWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_WritePiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLRectilinearGridWriter
- **bl_idname**: `VTKXMLRectilinearGridWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_WritePiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`, `m_WriteExtent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLStructuredGridWriter
- **bl_idname**: `VTKXMLStructuredGridWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_WritePiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`, `m_WriteExtent`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLTableWriter
- **bl_idname**: `VTKXMLTableWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_WritePiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLUniformGridAMRWriter
- **bl_idname**: `VTKXMLUniformGridAMRWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_GhostLevel`, `m_NumberOfTimeSteps`, `m_WriteMetaFile`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXMLUnstructuredGridWriter
- **bl_idname**: `VTKXMLUnstructuredGridWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_EncodeAppendedData`, `m_WriteToOutputString`, `m_FileName`, `m_ObjectName`, `m_BlockSize`, `m_CompressionLevel`, `m_GhostLevel`, `m_NumberOfPieces`, `m_NumberOfTimeSteps`, `m_WritePiece`, `e_ByteOrder`, `e_DataMode`, `e_HeaderType`, `e_IdType`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

### vtkXdmfWriter
- **bl_idname**: `VTKXdmfWriterType`
- **module**: `generated_nodes/gen_VTKWriters.py`
- **properties**: `m_MeshStaticOverTime`, `m_WriteAllTimeSteps`, `m_FileName`, `m_HeavyDataFileName`, `m_HeavyDataGroupName`, `m_ObjectName`, `m_LightDataLimit`
- **connections**:
  - **inputs**: []
  - **outputs**: []
  - **observers**: []
  - **other**: []

