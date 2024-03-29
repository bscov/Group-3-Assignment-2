#!/usr/bin/env python
# coding: utf-8

# In[1]:


#load libraries
from pulp import LpVariable, LpProblem, LpMaximize, LpMinimize, LpStatus, value, GLPK
import pulp as pulp


# # Expected Hours

# ### Product Prototype Development

# In[38]:


#define variables
d0 = LpVariable("d0", 0, None)
d1 = LpVariable("d1", 0, None)
d2 = LpVariable("d2", 0, None)
d3 = LpVariable("d3", 0, None)
d4 = LpVariable("d4", 0, None)
d5 = LpVariable("d5", 0, None)
d6 = LpVariable("d6", 0, None)
d7 = LpVariable("d7", 0, None)
d8 = LpVariable("d8", 0, None)

#define the problem that maximizes profit
probp = LpProblem("problem", LpMinimize)

#define constraints
probp += d0*(-1) + d1*1 >= 16
probp += d1*(-1) + d2*1 >= 120
probp += d1*(-1) + d3*1 >= 40
probp += d2*1 + d3*(-1) >= 0
probp += d2*(-1) + d4*1 >= 80
probp += d4*(-1) + d5*1 >= 40
probp += d4*(-1) + d6*1 >= 40
probp += d6*(-1) + d7*1 >= 40
probp += d5*1 + d7*(-1) >= 0
probp += d5*(-1) + d8*1 >= 40

 
#define objective function
probp += d8 - d0

#solve problem
probp.writeLP("probp.lp")
probp.solve(GLPK(msg=True, options=['--ranges', 'sensitivity_exp_p.txt']))
print("Status:", LpStatus[probp.status])

probp_results = []

for v in probp.variables():
    print(v.name, "=", v.varValue)
    probp_results.append(v.varValue)
    
print("Objective", value(probp.objective))
print("")


# In[39]:


prototype = probp_results[8]
prototype


# ### Recommendation System Development

# In[40]:


#define variables
t0 = LpVariable("t0", 0, None)
t1 = LpVariable("t1", 0, None)
t2 = LpVariable("t2", 0, None)
t3 = LpVariable("t3", 0, None)
t4 = LpVariable("t4", 0, None)
t5 = LpVariable("t5", 0, None)
t6 = LpVariable("t6", 0, None)
t7 = LpVariable("t7", 0, None)
t8 = LpVariable("t8", 0, None)
t9 = LpVariable("t9", 0, None)

#define the problem that maximizes profit
probr = LpProblem("problem", LpMinimize)

#define constraints
probr += t0*(-1) + t1*1 >= 8
probr += t0*(-1) + t2*1 >= 40
probr += t1*(-1) + t4*1 >= prototype_exp
probr += t1*(-1) + t3*1 >= 40
probr += t2*(-1) + t3*1 >= 0
probr += t4*(-1) + t8*1 >= 0 
probr += t4*(-1) + t5*1 >= 0 
probr += t3*(-1) + t5*1 >= 40
probr += t5*(-1) + t6*1 >= 24
probr += t7*1 + t8*(-1) >= 24
probr += t6*(-1) + t7*1 >= 0 
probr += t1*(-1) + t8*1 >= 0 
probr += t7*(-1) + t9*1 >= 40 
 
#define objective function
probr += t9 - t0

#solve problem
probr.writeLP("probr.lp")
probr.solve(GLPK(msg=True, options=['--ranges', 'sensitivity_exp_r.txt']))
print("Status:", LpStatus[probr.status])

for v in probr.variables():
    print(v.name, "=", v.varValue)
    
print("Objective", value(probr.objective))
print("")


# # Best Case Hours

# ### Product Prototype Development

# In[41]:


#define variables
d0 = LpVariable("d0", 0, None)
d1 = LpVariable("d1", 0, None)
d2 = LpVariable("d2", 0, None)
d3 = LpVariable("d3", 0, None)
d4 = LpVariable("d4", 0, None)
d5 = LpVariable("d5", 0, None)
d6 = LpVariable("d6", 0, None)
d7 = LpVariable("d7", 0, None)
d8 = LpVariable("d8", 0, None)

#define the problem that maximizes profit
probp = LpProblem("problem", LpMinimize)

#define constraints
probp += d0*(-1) + d1*1 >= 14.4
probp += d1*(-1) + d2*1 >= 108
probp += d1*(-1) + d3*1 >= 36
probp += d2*1 + d3*(-1) >= 0
probp += d2*(-1) + d4*1 >= 72
probp += d4*(-1) + d5*1 >= 36
probp += d4*(-1) + d6*1 >= 36
probp += d6*(-1) + d7*1 >= 36
probp += d5*1 + d7*(-1) >= 0
probp += d5*(-1) + d8*1 >= 36

 
#define objective function
probp += d8 - d0

#solve problem
probp.writeLP("probp.lp")
probp.solve(GLPK(msg=True, options=['--ranges', 'sensitivity_best_p.txt']))
print("Status:", LpStatus[probp.status])

probp_results = []

for v in probp.variables():
    print(v.name, "=", v.varValue)
    probp_results.append(v.varValue)
    
print("Objective", value(probp.objective))
print("")


# In[44]:


prototype = probp_results[8]
prototype


# ### Recommendation System Development

# In[45]:


#define variables
t0 = LpVariable("t0", 0, None)
t1 = LpVariable("t1", 0, None)
t2 = LpVariable("t2", 0, None)
t3 = LpVariable("t3", 0, None)
t4 = LpVariable("t4", 0, None)
t5 = LpVariable("t5", 0, None)
t6 = LpVariable("t6", 0, None)
t7 = LpVariable("t7", 0, None)
t8 = LpVariable("t8", 0, None)
t9 = LpVariable("t9", 0, None)

#define the problem that maximizes profit
probr = LpProblem("problem", LpMinimize)

#define constraints
probr += t0*(-1) + t1*1 >= 7.2
probr += t0*(-1) + t2*1 >= 36
probr += t1*(-1) + t4*1 >= prototype
probr += t1*(-1) + t3*1 >= 36
probr += t2*(-1) + t3*1 >= 0
probr += t4*(-1) + t8*1 >= 0 
probr += t4*(-1) + t5*1 >= 0 
probr += t3*(-1) + t5*1 >= 36
probr += t5*(-1) + t6*1 >= 21.6
probr += t7*1 + t8*(-1) >= 21.6
probr += t6*(-1) + t7*1 >= 0 
probr += t1*(-1) + t8*1 >= 0 
probr += t7*(-1) + t9*1 >= 36
 
#define objective function
probr += t9 - t0

#solve problem
probr.writeLP("probr.lp")
probr.solve(GLPK(msg=True, options=['--ranges', 'sensitivity_best_r.txt']))
print("Status:", LpStatus[probr.status])

for v in probr.variables():
    print(v.name, "=", v.varValue)
    
print("Objective", value(probr.objective))
print("")


# # Worst Case Hours

# ### Product Prototype Development

# In[46]:


#define variables
d0 = LpVariable("d0", 0, None)
d1 = LpVariable("d1", 0, None)
d2 = LpVariable("d2", 0, None)
d3 = LpVariable("d3", 0, None)
d4 = LpVariable("d4", 0, None)
d5 = LpVariable("d5", 0, None)
d6 = LpVariable("d6", 0, None)
d7 = LpVariable("d7", 0, None)
d8 = LpVariable("d8", 0, None)

#define the problem that maximizes profit
probp = LpProblem("problem", LpMinimize)

#define constraints
probp += d0*(-1) + d1*1 >= 17.6
probp += d1*(-1) + d2*1 >= 132
probp += d1*(-1) + d3*1 >= 44
probp += d2*1 + d3*(-1) >= 0
probp += d2*(-1) + d4*1 >= 88
probp += d4*(-1) + d5*1 >= 44
probp += d4*(-1) + d6*1 >= 44
probp += d6*(-1) + d7*1 >= 44
probp += d5*1 + d7*(-1) >= 0
probp += d5*(-1) + d8*1 >= 44

 
#define objective function
probp += d8 - d0

#solve problem
probp.writeLP("probp.lp")
probp.solve(GLPK(msg=True, options=['--ranges', 'sensitivity_worst_p.txt']))
print("Status:", LpStatus[probp.status])

probp_results = []

for v in probp.variables():
    print(v.name, "=", v.varValue)
    probp_results.append(v.varValue)
    
print("Objective", value(probp.objective))
print("")


# In[47]:


prototype = probp_results[8]
prototype


# ### Recommendation System Development

# In[48]:


#define variables
t0 = LpVariable("t0", 0, None)
t1 = LpVariable("t1", 0, None)
t2 = LpVariable("t2", 0, None)
t3 = LpVariable("t3", 0, None)
t4 = LpVariable("t4", 0, None)
t5 = LpVariable("t5", 0, None)
t6 = LpVariable("t6", 0, None)
t7 = LpVariable("t7", 0, None)
t8 = LpVariable("t8", 0, None)
t9 = LpVariable("t9", 0, None)

#define the problem that maximizes profit
probr = LpProblem("problem", LpMinimize)

#define constraints
probr += t0*(-1) + t1*1 >= 8.8
probr += t0*(-1) + t2*1 >= 44
probr += t1*(-1) + t4*1 >= prototype
probr += t1*(-1) + t3*1 >= 44
probr += t2*(-1) + t3*1 >= 0
probr += t4*(-1) + t8*1 >= 0 
probr += t4*(-1) + t5*1 >= 0 
probr += t3*(-1) + t5*1 >= 44
probr += t5*(-1) + t6*1 >= 26.4
probr += t7*1 + t8*(-1) >= 26.4
probr += t6*(-1) + t7*1 >= 0 
probr += t1*(-1) + t8*1 >= 0 
probr += t7*(-1) + t9*1 >= 44
 
#define objective function
probr += t9 - t0

#solve problem
probr.writeLP("probr.lp")
probr.solve(GLPK(msg=True, options=['--ranges', 'sensitivity_worst_r.txt']))
print("Status:", LpStatus[probr.status])

for v in probr.variables():
    print(v.name, "=", v.varValue)
    
print("Objective", value(probr.objective))
print("")

# # Independent Contractor

# ### Product Prototype Development

# In[49]:


#define variables
d0 = LpVariable("d0", 0, None)
d1 = LpVariable("d1", 0, None)
d2 = LpVariable("d2", 0, None)
d3 = LpVariable("d3", 0, None)
d4 = LpVariable("d4", 0, None)
d5 = LpVariable("d5", 0, None)
d6 = LpVariable("d6", 0, None)
d7 = LpVariable("d7", 0, None)
d8 = LpVariable("d8", 0, None)

#define the problem that maximizes profit
probp = LpProblem("problem", LpMinimize)

#define constraints
probp += d0*(-1) + d1*1 >= 18
probp += d1*(-1) + d2*1 >= 66
probp += d1*(-1) + d3*1 >= 44
probp += d2*1 + d3*(-1) >= 0
probp += d2*(-1) + d4*1 >= 44
probp += d4*(-1) + d5*1 >= 44
probp += d4*(-1) + d6*1 >= 22
probp += d6*(-1) + d7*1 >= 22
probp += d5*1 + d7*(-1) >= 0
probp += d5*(-1) + d8*1 >= 22

 
#define objective function
probp += d8 - d0

#solve problem
probp.writeLP("probp.lp")
probp.solve(GLPK(msg=True, options=['--ranges', 'sensitivity_contract_p.txt']))
print("Status:", LpStatus[probp.status])

probp_results = []

for v in probp.variables():
    print(v.name, "=", v.varValue)
    probp_results.append(v.varValue)
    
print("Objective", value(probp.objective))
print("")


# In[50]:


prototype = probp_results[8]
prototype


# ### Recommendation System Development

# In[51]:


#define variables
t0 = LpVariable("t0", 0, None)
t1 = LpVariable("t1", 0, None)
t2 = LpVariable("t2", 0, None)
t3 = LpVariable("t3", 0, None)
t4 = LpVariable("t4", 0, None)
t5 = LpVariable("t5", 0, None)
t6 = LpVariable("t6", 0, None)
t7 = LpVariable("t7", 0, None)
t8 = LpVariable("t8", 0, None)
t9 = LpVariable("t9", 0, None)

#define the problem that maximizes profit
probr = LpProblem("problem", LpMinimize)

#define constraints
probr += t0*(-1) + t1*1 >= 9
probr += t0*(-1) + t2*1 >= 44
probr += t1*(-1) + t4*1 >= prototype
probr += t1*(-1) + t3*1 >= 44
probr += t2*(-1) + t3*1 >= 0
probr += t4*(-1) + t8*1 >= 0 
probr += t4*(-1) + t5*1 >= 0 
probr += t3*(-1) + t5*1 >= 44
probr += t5*(-1) + t6*1 >= 26
probr += t7*1 + t8*(-1) >= 26
probr += t6*(-1) + t7*1 >= 0 
probr += t1*(-1) + t8*1 >= 0 
probr += t7*(-1) + t9*1 >= 44
 
#define objective function
probr += t9 - t0

#solve problem
probr.writeLP("probr.lp")
probr.solve(GLPK(msg=True, options=['--ranges', 'sensitivity_contract_r.txt']))
print("Status:", LpStatus[probr.status])

for v in probr.variables():
    print(v.name, "=", v.varValue)
    
print("Objective", value(probr.objective))
print("")
