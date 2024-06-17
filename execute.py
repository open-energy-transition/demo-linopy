import linopy

n = linopy.read_netcdf("./input/test.nc")
n.solve()
n.to_netcdf("./result/results.nc")