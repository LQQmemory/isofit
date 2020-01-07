# David R Thompson, Adam Erickson

from isofit.core.isofit import Isofit
from isofit.utils import surface_model

# Build the surface model
surface_model("configs/ang20171108t184227_surface.json")

# Run retrievals
model1 = Isofit("configs/ang20171108t173546_darklot.json")

model2 = Isofit("configs/ang20171108t173546_horse.json")

model3 = Isofit("configs/ang20171108t184227_astrored.json")

model4 = Isofit("configs/ang20171108t184227_astrogreen.json")

model5 = Isofit("configs/ang20171108t184227_beckmanlawn.json")

model6 = Isofit("configs/ang20171108t184227_beckmanlawn-oversmoothed.json")

model7 = Isofit("configs/ang20171108t184227_beckmanlawn-undersmoothed.json")
