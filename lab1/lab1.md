# Modeling and Simulation of Systems

## Laboratory Class 1: Body moving in a uniform gravitational field
**Authors:** P. Kowalczyk, A. Lamecki

The aim of this laboratory lesson is to familiarize the students with some basics of modeling only and basics of Matlab programming. It is focused on the simplest algorithms, including: conditions, loops and elements of stochastic modeling. 
**Requirements:** basic Matlab programming

### 1 Introduction
The problem concerns a body moving in a uniform gravitational field. When an infinitesimal body moves in a uniform gravitational field, its position can be expressed in the following form (assuming $(0,0)$ as an initial point):

$$x(t)=v_{0x}t$$
$$y(t)=v_{0y}t-\frac{1}{2}gt^{2}$$

where $g=10\text{ m/s}^{2}$ is gravitational acceleration and $t$ represents time. The speeds $v_{0x}=v_{0}\cos(\alpha)$ and $v_{0y}=v_{0}\sin(\alpha)$ are obtained directly from decomposition of the initial speed vector (see Fig. 1).

Since the initial localization and speed of the body determines its trajectory, then one can determine whether an object will pass through or fall into a specific region. In Fig. 1, a simple case of such movement is presented. The initial speed value is denoted by `$v_{0}$` and its orientation in space is determined by angle `$\alpha$`. In the figure the trajectory crosses regions `$R_{1}$` and `$R_{3}$` (allowed region), but do not cross region `$R_{2}$` (forbidden region).

### 2 Exercise
1. For a given data (definitions of allowed/forbidden regions `$R_{i}$` and range of initial values `$v_{0}$` and `$\alpha$`) write a Matlab program that finds a set of pairs `$v_{0}$` and `$\alpha$` that fulfill a fixed conditions on crossing the marked regions. To this end, simulate the moving process for randomly chosen initial values of `$v_{0}$` and `$\alpha$`. If the conditions are fulfilled then plot a point on a chart of `$v_{0}$` versus `$\alpha$`. Repeat the process for the randomly chosen initial values 100,000 times. Show the obtained figure to the teacher for approval and save it (see example in Fig. 2).
2. Draw a chart containing allowed and forbidden regions (allowed with green and forbidden with red, like 1) and put on it at least 5 trajectories fulfilling the conditions. Again, show the obtained figure to the teacher for approval and save it.
3. Estimate the probability of fulfilment of the requested conditions for a single try (for initial values taken from a given sets). What does the accuracy of the estimation depends on?

### 3 Report
Please, send:
* the code,
* the obtained figures (well described),
* the answer to point 2.3

to the given e-mail address. In e-mail title please indicate the student group affiliation!

---

**Figure 1:** A trajectory of a body moving in a uniform gravitational field.

**Figure 2:** Example: 2D plot of a set of initial values (allowed `$v_{0}$` and `$\alpha$`) for which the requested conditions on objects' trajectory are fulfilled.