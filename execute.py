import linopy

m = linopy.read_netcdf("./input/test.nc")
m.solve()
m.to_netcdf("./result/results.nc")