
import matplotlib.pyplot as plt
import xarray as xr

d, c, t = xr.open_dataset("Ret_677_20200227v0.9.h5")[["AOD", "CloudFlag", "MFRTime"]].to_array()
plt.plot(t.T, d.where(c == 0).T, ".")
plt.show()
