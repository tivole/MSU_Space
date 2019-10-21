# MSU_Space

NASA Sapace Apps Azerbaijan 2019 <b>MSU_Space</b> team.

# Introduction

We are <i>“MSU_Space”</i>. Our challenge is called [“UP, OUT AND AWAY”](https://spaceapps.space.az/challenges/stars/and-away). Our main aim is to create
a simulation that will describe the motion of heaven bodies and James Webb’s trajectory to the point Lagrange2 in Solar System.

The image below describes the motion of all bodies in our system:

<p align="center">
  <img src="img/physics_model.png">
</p>

We consider a two-dimensional system consisting of the Sun, Earth, Moon and James Webb. We
assume that the Sun is motionless, and we connect the remaining bodies with the Sun by radius vectors.
We have created a system of differential equations that describes our system. However, we didn’t take
into account the radiation of the sun and that the Earth is not spherical. Due to limitations in time we
had to simplify our model.

<p align="center">
  <img src="img/formula_1.png">
</p>



Where ![G](img/G.gif) - gravitational constant and vector ![r](img/r.gif) have two components ![r_is_x_y](img/r_vec.gif), indexes E - Earth, L - Moon, S - Sun, JW - James Webb.
