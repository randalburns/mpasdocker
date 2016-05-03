
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
      #temperatureLUT = GetColorTransferFunction('temperature')
      #temperatureLUT.RGBPoints = [15.979462484959978, 0.231373, 0.298039, 0.75294099999999997, 3.0413812013454221e+34, 0.86500299999999997, 0.86500299999999997, 0.86500299999999997, 6.0827624026908442e+34, 0.70588200000000001, 0.0156863, 0.14902000000000001]
      #temperatureLUT.ScalarRangeInitialized = 1.0

      # get opacity transfer function/opacity map for 'temperature'
      #temperaturePWF = GetOpacityTransferFunction('temperature')
      #temperaturePWF.Points = [15.979462484959978, 0.0, 0.5, 0.0, 6.0827624026908442e+34, 1.0, 0.5, 0.0]
      #temperaturePWF.ScalarRangeInitialized = 1

      # get color transfer function/color map for 'kineticEnergyCell'
      kineticEnergyCellLUT = GetColorTransferFunction('kineticEnergyCell')
      #kineticEnergyCellLUT.LockDataRange = 1
      kineticEnergyCellLUT.RGBPoints = [0.0001, 0.082353, 0.133333, 0.278431, 0.00015848931924611142, 0.105882, 0.196078, 0.321569, 0.00025118864315095795, 0.156863, 0.286275, 0.419608, 0.00039810717055349735, 0.211765, 0.396078, 0.521569, 0.000630957344480193, 0.282353, 0.505882, 0.6, 0.001, 0.34902, 0.631373, 0.701961, 0.001584893192461114, 0.439216, 0.768627, 0.8, 0.0025118864315095794, 0.517647, 0.858824, 0.847059, 0.003981071705534973, 0.596078, 0.921569, 0.878431, 0.00630957344480193, 0.709804, 0.968627, 0.905882, 0.009120108393559097, 0.803922, 0.980392, 0.929412, 0.01, 0.831373, 0.988235, 0.886275, 0.01096478196143185, 0.803922, 0.980392, 0.823529, 0.01584893192461114, 0.709804, 0.968627, 0.729412, 0.025118864315095794, 0.584314, 0.901961, 0.584314, 0.039810717055349734, 0.505882, 0.8, 0.478431, 0.0630957344480193, 0.439216, 0.701961, 0.384314, 0.0999999999999999, 0.376471, 0.6, 0.301961, 0.15848931924611143, 0.321569, 0.501961, 0.235294, 0.25118864315095796, 0.25098, 0.419608, 0.129412, 0.3981071705534973, 0.223529, 0.34902, 0.094118, 0.630957344480193, 0.231373, 0.321569, 0.105882, 1.0, 0.215686, 0.278431, 0.082353]
      kineticEnergyCellLUT.UseLogScale = 1
      kineticEnergyCellLUT.ColorSpace = 'RGB'
      kineticEnergyCellLUT.NanColor = [0.25, 0.0, 0.0]
      kineticEnergyCellLUT.ScalarRangeInitialized = 1.0


      # get opacity transfer function/opacity map for 'kineticEnergyCell'
      kineticEnergyCellPWF = GetOpacityTransferFunction('kineticEnergyCell')
      kineticEnergyCellPWF.Points = [0.0001, 0.0, 0.5, 0.0, 1.0, 1.0, 0.5, 0.0]
      kineticEnergyCellPWF.ScalarRangeInitialized = 1

      # ----------------------------------------------------------------
      # setup the visualization in view 'renderView1'
      # ----------------------------------------------------------------

      # show data from mpas_data_1pvtu
      mpas_data_1pvtuDisplay = Show(mpas_data_1pvtu, renderView1)
      # trace defaults for the display properties.
      #mpas_data_1pvtuDisplay.ColorArrayName = ['CELLS', 'temperature']
      #mpas_data_1pvtuDisplay.LookupTable = temperatureLUT
      mpas_data_1pvtuDisplay.ColorArrayName = ['CELLS', 'kineticEnergyCell']
      mpas_data_1pvtuDisplay.LookupTable = kineticEnergyCellLUT
      mpas_data_1pvtuDisplay.ScalarOpacityUnitDistance = 1469170.6394257464

      # show color legend
      mpas_data_1pvtuDisplay.SetScalarBarVisibility(renderView1, False)

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for temperatureLUT in view renderView1
      #temperatureLUTColorBar = GetScalarBar(temperatureLUT, renderView1)
      #temperatureLUTColorBar.Title = 'temperature'
      #temperatureLUTColorBar.ComponentTitle = 'Magnitude'

      # setup the color legend parameters for each legend in this view

      # get color legend/bar for kineticEnergyCellLUT in view renderView1
      #kineticEnergyCellLUTColorBar = GetScalarBar(kineticEnergyCellLUT, renderView1)
      #kineticEnergyCellLUTColorBar.Title = 'kineticEnergyCell'
      #kineticEnergyCellLUTColorBar.ComponentTitle = '0'

      # create a new 'Sphere'
      sphere1 = Sphere()
      sphere1.Radius = 6300000.0      
      sphere1.ThetaResolution = 32
      sphere1.PhiResolution = 32
      sphere1Display = Show(sphere1, renderView1) 
      sphere1Display.ColorArrayName = [None, ''] 
      sphere1Display.DiffuseColor = [0.0, 0.0, 0.0] 

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
