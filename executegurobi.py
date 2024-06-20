import linopy

n = linopy.read_netcdf("./input/test.nc")
linopy.solvers.run_gurobi(n)
n.to_netcdf("./result/results.nc")