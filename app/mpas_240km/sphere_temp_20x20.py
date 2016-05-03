
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
      renderView1.CameraPosition = [18902712.533687532, -15309317.892430089, 15885961.777218876]
      renderView1.CameraFocalPoint = [-4.6823529984804343e-12, -2.2393128102107749e-12, 53281.749999999993]
      renderView1.CameraViewUp = [-4.1466462534001103e-05, 0.71886393279384542, 0.69515080695392872]
      renderView1.CameraParallelScale = 10998063.655783894
      renderView1.Background = [0.32000000000000001, 0.34000000000000002, 0.42999999999999999]

      # register the view with coprocessor
      # and provide it with information such as the filename to use,
      # how frequently to write the images, etc.
      coprocessor.RegisterView(renderView1,
          filename='image_%t.png', freq=1, fittoscreen=0, magnification=1, width=963, height=770, cinema={"camera":"Spherical", "phi":[-180,-162,-144,-126,-108,-90,-72,-54,-36,-18,0,18,36,54,72,90,108,126,144,162], "theta":[-180,-162,-144,-126,-108,-90,-72,-54,-36,-18,0,18,36,54,72,90,108,126,144,162] })

      # ----------------------------------------------------------------
      # setup the data processing pipelines
      # ----------------------------------------------------------------

      # create a new 'XML Partitioned Unstructured Grid Reader'
      # create a producer from a simulation input
      mpas_data_1pvtu = coprocessor.CreateProducer(datadescription, 'X_Y_Z_1LAYER-primal')

      # ----------------------------------------------------------------
      # setup color maps and opacity mapes used in the visualization
      # note: the Get..() functions create a new object, if needed
      # ----------------------------------------------------------------

      # get color transfer function/color map for 'temperature'
      temperatureLUT = GetColorTransferFunction('temperature')
      temperatureLUT.RGBPoints = [15.979462484959978, 0.231373, 0.298039, 0.75294099999999997, 3.0413812013454221e+34, 0.86500299999999997, 0.86500299999999997, 0.86500299999999997, 6.0827624026908442e+34, 0.70588200000000001, 0.0156863, 0.14902000000000001]
      temperatureLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'temperature'
      temperaturePWF = GetOpacityTransferFunction('temperature')
      temperaturePWF.Points = [15.979462484959978, 0.0, 0.5, 0.0, 6.0827624026908442e+34, 1.0, 0.5, 0.0]
      temperaturePWF.ScalarRangeInitialized = 1

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from mpas_data_1pvtu
      mpas_data_1pvtuDisplay = Show(mpas_data_1pvtu, renderView1)
      # trace defaults for the display properties.
      mpas_data_1pvtuDisplay.ColorArrayName = ['CELLS', 'temperature']
      mpas_data_1pvtuDisplay.LookupTable = temperatureLUT
      mpas_data_1pvtuDisplay.ScalarOpacityUnitDistance = 1469170.6394257464

      # show color legend
      mpas_data_1pvtuDisplay.SetScalarBarVisibility(renderView1, True)

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for temperatureLUT in view renderView1
      temperatureLUTColorBar = GetScalarBar(temperatureLUT, renderView1)
      temperatureLUTColorBar.Title = 'temperature'
      temperatureLUTColorBar.ComponentTitle = 'Magnitude'
    return Pipeline()

  class CoProcessor(coprocessing.CoProcessor):
    def CreatePipeline(self, datadescription):
      self.Pipeline = _CreatePipeline(self, datadescription)

  coprocessor = CoProcessor()
  # these are the frequencies at which the coprocessor updates.
  freqs = {'X_Y_Z_1LAYER-primal': [1]}
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
