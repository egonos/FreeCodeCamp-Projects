import numpy as np

def calculate(lst):

  if len(lst) != 9:
      
    raise ValueError('List must contain nine numbers.')
    
  lst = np.array(lst)
  lst = lst.reshape((3,3))
  
  vert_mean = list(lst.mean(axis = 0))
  hor_mean = list(lst.mean(axis = 1))
  flat_mean = lst.ravel().mean()
  means = [vert_mean,hor_mean,flat_mean]
  
  vert_var = list(lst.var(axis = 0))
  hor_var = list(lst.var(axis = 1))
  flat_var = lst.ravel().var()
  vars = [vert_var,hor_var,flat_var]
  
  vert_std = list(lst.std(axis = 0))
  hor_std = list(lst.std(axis = 1))
  flat_std = lst.ravel().std()
  stds = [vert_std,hor_std,flat_std]
  
  vert_max = list(lst.max(axis = 0))
  hor_max = list(lst.max(axis = 1))
  flat_max = lst.ravel().max()
  maxs = [vert_max,hor_max,flat_max]

  vert_min = list(lst.min(axis = 0))
  hor_min = list(lst.min(axis = 1))
  flat_min = lst.ravel().min()
  mins = [vert_min,hor_min,flat_min]

  vert_sum = list(lst.sum(axis = 0))
  hor_sum = list(lst.sum(axis = 1))
  flat_sum = lst.ravel().sum()
  sums = [vert_sum,hor_sum,flat_sum]

  calculations = {
  'mean': means,
  'variance': vars,
  'standard deviation': stds,
  'max': maxs,
  'min': mins,
  'sum': sums
}




  return calculations

