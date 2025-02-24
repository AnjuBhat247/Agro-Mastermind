import xarray as xr
import numpy as np
Data_rain=xr.open_dataset("H:/AgroMastermind/rain.nc")
Data_rain_monthly=Data_rain.resample(datetime='M').mean(dim='datetime')
Data_rain_monthly_avg=Data_rain_monthly.groupby('datetime.month').mean()
Data_rain_monthly_avg.precip.sel(lat=np.arange(10,20),lon=np.arange(70,80),method='nearest')
Data_rain_monthly_avg.to_netcdf("Rainy.nc")

Data_temp=xr.open_dataset("H:/AgroMastermind/1951-2013-Merged_Temp.nc")
Data_temp_monthly=Data_temp.resample(time='M').mean(dim='time')
Data_temp_monthly_avg=Data_temp_monthly.groupby('time.month').mean()
Data_temp_monthly_avg.temp.sel(lat=np.arange(10,20),lon=np.arange(70,80),method='nearest')
Data_temp_monthly_avg.to_netcdf("Temp.nc")

Data_sh=xr.open_dataset("H:/AgroMastermind/Specific_Humidity.nc")
Data_sh_monthly=Data_sh.resample(time='M').mean(dim='time')
Data_sh_monthly_avg=Data_sh_monthly.groupby('time.month').mean()
Data_sh_monthly_avg.shum.sel(lat=np.arange(10,20),lon=np.arange(70,80),method='nearest')
Data_sh_monthly_avg.to_netcdf("humidity.nc")

Data_sm=xr.open_dataset("H:/AgroMastermind/Soil_Moisture.nc")
Data_sm_monthly=Data_sm.resample(time='M').mean(dim='time')
Data_sm_monthly_avg=Data_sm_monthly.groupby('time.month').mean()
Data_sm_monthly_avg.soilw.sel(lat=np.arange(10,20),lon=np.arange(70,80),method='nearest')
Data_sm_monthly_avg.to_netcdf("soilmoist.nc")
