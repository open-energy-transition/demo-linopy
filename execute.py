import linopy

from linopy import Model
m = Model()

x = m.add_variables(lower=0, name='x')
y = m.add_variables(lower=0, name='y')

m.add_constraints(3*x + 7*y >= 10)
m.add_constraints(5*x + 2*y >= 3)

m.add_objective(x + 2*y)

m.to_netcdf("./input/test.nc")

n = linopy.read_netcdf("./input/test.nc")
n.solve()
n.to_netcdf("./result/results.nc")