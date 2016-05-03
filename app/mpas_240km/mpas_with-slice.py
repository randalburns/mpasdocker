
from paraview.simple import *
from paraview import coprocessing


#--------------------------------------------------------------
# Code generated from cpstate.py to create the CoProcessor.
# ParaView 4.3.1-367-ge45b928 64 bits


# ----------------------- CoProcessor definition -----------------------

def CreateCoProcessor():
  def _CreatePipeline(coprocessor, datadescription):
    class Pipeline:
      # state file generated using paraview version 4.3.1-367-ge45b928

      # ----------------------------------------------------------------
      # setup views used in the visualization
      # ----------------------------------------------------------------

      #### disable automatic camera reset on 'Show'
      paraview.simple._DisableFirstRenderCameraReset()

      # Create a new 'Render View'
      renderView1 = CreateView('RenderView')
      renderView1.ViewSize = [963, 770]
      renderView1.CenterOfRotation = [0.0, 0.0, 53281.75]
      renderView1.StereoType = 0
      renderView1.CameraPosition = [35630120.340991102, -20426710.853056714, -10851795.964901553]
      renderView1.CameraFocalPoint = [-1.8350501912214275e-12, 3.6269227308847037e-11, 53281.75]
      renderView1.CameraViewUp = [0.34720803363132668, 0.8342773749057858, -0.42828476870206178]
      renderView1.CameraParallelScale = 10998063.655783894
      renderView1.Background = [0.32000000000000001, 0.34000000000000002, 0.42999999999999999]

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='image_%t.png', freq=1, fittoscreen=0, magnification=1, width=963, height=770, cinema={"camera":"Spherical", "phi":[-180,-150,-120,-90,-60,-30,0,30,60,90,120,150], "theta":[-180,-150,-120,-90,-60,-30,0,30,60,90,120,150] })

      # ----------------------------------------------------------------
      # setup the data processing pipelines
      # ----------------------------------------------------------------

      # create a new 'XML Partitioned Unstructured Grid Reader'
      # create a producer from a simulation input
      mpas_data_1pvtu = coprocessor.CreateProducer(datadescription, 'X_Y_Z_NLAYER-primal')

      # create a new 'Slice'
      slice1 = Slice(Input=mpas_data_1pvtu)
      slice1.SliceType = 'Plane'
      slice1.SliceOffsetValues = [0.0]

      # init the 'Plane' selected for 'SliceType'
      slice1.SliceType.Origin = [0.0, 0.0, 53281.75]

      # register the filter with the coprocessor's cinema generator
      coprocessor.RegisterCinemaTrack('slice', slice1, 'SliceOffsetValues', [-10998100.0, -8554080.0, -6110060.0, -3666030.0, -1222010.0, 1222010.0, 3666030.0, 6110060.0, 8554080.0, 10998100.0])

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # get color transfer function/color map for 'temperature'
      temperatureLUT = GetColorTransferFunction('temperature')
      temperatureLUT.RGBPoints = [-9.999999790214768e+33, 0.231373, 0.298039, 0.75294099999999997, -4.999999895107384e+33, 0.86500299999999997, 0.86500299999999997, 0.86500299999999997, 0.0, 0.70588200000000001, 0.0156863, 0.14902000000000001]
      temperatureLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'temperature'
      temperaturePWF = GetOpacityTransferFunction('temperature')
      temperaturePWF.Points = [-9.999999790214768e+33, 0.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0]
      temperaturePWF.ScalarRangeInitialized = 1

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from slice1
      slice1Display = Show(slice1, renderView1)
      # trace defaults for the display properties.
      slice1Display.ColorArrayName = ['CELLS', 'temperature']
      slice1Display.LookupTable = temperatureLUT

      # show color legend
      slice1Display.SetScalarBarVisibility(renderView1, True)

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for temperatureLUT in view renderView1
      temperatureLUTColorBar = GetScalarBar(temperatureLUT, renderView1)
      temperatureLUTColorBar.Title = 'temperature'
      temperatureLUTColorBar.ComponentTitle = ''
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'X_Y_Z_NLAYER-primal': [1, 1]}
  coprocessor.SetUpdateFrequencies(freqs)
  return coprocessor

#--------------------------------------------------------------
# Global variables that will hold the pipeline for each timestep
# Creating the CoProcessor object, doesn't actually create the ParaView pipeline.
# It will be automatically setup when coprocessor.UpdateProducers() is called the
# first time.
coprocessor = CreateCoProcessor()

#--------------------------------------------------------------
# Enable Live-Visualizaton with ParaView
coprocessor.EnableLiveVisualization(False, 1)


# ---------------------- Data Selection method ----------------------

def RequestDataDescription(datadescription):
    "Callback to populate the request for current timestep"
    global coprocessor
    if datadescription.GetForceOutput() == True:
        # We are just going to request all fields and meshes from the simulation
        # code/adaptor.
        for i in range(datadescription.GetNumberOfInputDescriptions()):
            datadescription.GetInputDescription(i).AllFieldsOn()
            datadescription.GetInputDescription(i).GenerateMeshOn()
        return

    # setup requests for all inputs based on the requirements of the
    # pipeline.
    coprocessor.LoadRequestedData(datadescription)

# ------------------------ Processing method ------------------------

def DoCoProcessing(datadescription):
    "Callback to do co-processing for current timestep"
    global coprocessor

    # Update the coprocessor by providing it the newly generated simulation data.
    # If the pipeline hasn't been setup yet, this will setup the pipeline.
    coprocessor.UpdateProducers(datadescription)

    # Write output data, if appropriate.
    coprocessor.WriteData(datadescription);

    # Write image capture (Last arg: rescale lookup table), if appropriate.
    coprocessor.WriteImages(datadescription, rescale_lookuptable=False)

    # Live Visualization, if enabled.
    coprocessor.DoLiveVisualization(datadescription, "localhost", 22222)
