readme file for MPAS-Ocean global statistics

stats_time.txt. contains: timeIndex, timestamp, dt, CFLNumberGlobal

All other stats_*.txt. contain the following columns.  Rows correspond to timestamps in rows of stats_time.txt
See user's guide for units associated with these variables.
    1. time, in days, using a 360 day calendar
    2. layerThickness
    3. normalVelocity
    4. tangentialVelocity
    5. layerThicknessEdge
    6. relativeVorticity
    7. enstrophy = relativeVorticity**2
    8. kineticEnergyCell
    9. normalizedAbsoluteVorticity = (relative vorticity + planetary vorticity)/layer thickness
   10. pressure
   11. montgomeryPotential
   12. vertVelocityTop vertical velocity
   13. vertAleTransportTop vertical transport
   14. lowFreqDivergence
   15. highFreqThickness
   16. Tracers: usually T, S, then others in remaining columns

A chain of simple unix commands may be used to access a specific part of the data. For example,
to view the last three values of column seven in the global average, use:
cat stats_avg.txt | awk '{print $7}' | tail -n3
