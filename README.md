# Group-3-Assignment-2
## MSDS 460 Homework Assignment 2: Network Models---Project Management
Griffin Arnone, Anhua Cheng, & Bailey Scoville
## Objective
The objective of this critical path analysis problem is to utilize linear programming to determine the minimum number of hours needed to complete a sixteen-task project to develop a recommendation system for a client. Three variations of this problem were conducted to solve for the optimal expected, best-case, and worst-case minimum hours to complete the tasks. A full discussion of the problem and results are included in this [paper](https://github.com/bscov/Group-3-Assignment-2/blob/main/Paper_Homework_Assignment2.pdf).
## Tasks
The sixteen tasks have been divided into two eight-task projects, with the prototype project being nested within the larger recommendation system project:

Develop product prototype (D):
- D1: Requirements Analysis
- D2: Software Design
- D3: System Design
- D4: Coding
- D5: Write Documentation
- D6: Unit Testing
- D7: System Testing
- D8: Package Deliverables

Develop recommendation system:
- A: Describe product
- B: Develop marketing strategy
- C: Design brochure
- D: Develop product prototype - (D1-D8 detailed above)
- E: Survey potential market
- F: Develop pricing plan
- G: Develop implementation plan
- H: Write client proposal

Graph diagrams for the [prototype](https://github.com/bscov/Group-3-Assignment-2/blob/main/Graph_Diagram_Product_Prototype_Dev.png) and [recommendation system](https://github.com/bscov/Group-3-Assignment-2/blob/main/Graph_Diagram_Recommendation_System_Dev.png) are included in the repository.

## Standard Form Equation
Hourly estimates for the expected, best-case, and worst-case variations of this problem are represented in this [table](https://github.com/bscov/Group-3-Assignment-2/blob/main/Table_Tasks_Hours_Costs_Assignments.png). The expected hours are represented in the equations below.
### Develop product prototype
- Objective function: Minimize Z = - d0 + d8
- Subject to:
- -d0 + d1 >= 16
- -d5 + d8 >= 40
- -d1 + d2 >= 120
- -d1 + d3 >= 40
- d2 - d3 >= 0
- -d2 + d4 >= 80
- -d4 + d5 >= 40
- -d4 + d6 >= 40
- -d6 + d7 >= 40
- d5 - d7 >= 0

### Develop recommendation system
- Objective function: Minimize Z = - t0 + t9
- Subject to: 
- -t0 + t1 >= 8
- t7 - t8 >= 24
- -t6 + t7 >= 0
- -t1 + t8 >= 0
- -t7 + t9 >= 40
- -t0 + t2 >= 40
- -t1 + t4 >= 336
- -t1 + t3 >= 44
- -t2 + t3 >= 0
- -t4 + t8 >= 0
- -t4 + t5 >= 0
- -t3 + t5 >= 40
- -t5 + t6 >= 24

## Tools
The linear programming code utilizes the Python PuLP library and GNU Linear Programming Kit (GLPK) package to minimize the task completion hours and conduct sensitivity analysis. [Python code](https://github.com/bscov/Group-3-Assignment-2/blob/main/Code_Assignment2.py), [Python output](https://github.com/bscov/Group-3-Assignment-2/blob/main/Output_Assignment2.txt), and [sensitivity analysis](https://github.com/bscov/Group-3-Assignment-2) plain text files are included in the repository.

## Results
The results are rounded to whole integers. Total cost is estimated using a $200,000 annual salary ($100 hourly rate) for each project team member.
### Critical Path
The critical path was constant between all three hour estimates:
- Prototype: d0 - d1 - d2 - d4 - d6 - d7 - d8
  - requirements analysis, software design, coding, unit testing, system testing, package deliverables
- Recommendation System: t0 - t1 - t4 - t7 - t8 - t9
  - describing the product, developing the product prototype, developing implementation plan, writing the client proposal
### Expected Problem
- 336 hours to develop the product prototype
- 408 hours to develop the recommendation system
- $40,800 total labor cost
- [view the Gantt Chart](https://github.com/bscov/Group-3-Assignment-2/blob/main/Gantt_Timeline_Expected_Hours.png)
### Best-Case Problem
- 302 hours to develop the product prototype
- 367 hours to develop the recommendation system
- $36,700 total labor cost
- [view the Gantt Chart](https://github.com/bscov/Group-3-Assignment-2/blob/main/Gantt_Timeline_BestCase_Hours.png)
### Worst-Case Problem
- 369 hours to develop the product prototype
- 448 hours to develop the recommendation system
- $44,800 total labor cost
- [view the Gantt Chart](https://github.com/bscov/Group-3-Assignment-2/blob/main/Gantt_Timeline_WorstCase_Hours.png)
