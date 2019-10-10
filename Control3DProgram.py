from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

import pygame
from pygame.locals import *

import sys
import time

from Maze import * 
from Shaders import *
from Matrices import *
from BallLogic import * 

class GraphicsProgram3D:
    def __init__(self):

        pygame.init() 
        pygame.display.set_mode((800,600), pygame.OPENGL|pygame.DOUBLEBUF)

        self.shader = Shader3D()
        self.shader.use()

        self.model_matrix = ModelMatrix()

        self.view_matrix = ViewMatrix()
        self.view_matrix_mini = ViewMatrix()
        self.view_matrix.look(Point(0, 1, 0), Point(0, 1, 1), Vector(0, 1, 0))
        self.projection_matrix = ProjectionMatrix()
        #self.projection_matrix.set_orthographic(-2, 2, -2, 2, 0.5, 10)
        self.projection_matrix.set_perspective(pi/2, 4/3, 0.5, 30)
        self.shader.set_projection_matrix(self.projection_matrix.get_matrix())

        self.cube = Cube()
        self.cube.set_vertices(self.shader)

        self.sphere = Sphere()
        self.radius = 1.4
        self.clock = pygame.time.Clock()
        self.clock.tick()

        self.angle = 0

        self.UP_key_down = False  
        self.DOWN_key_down = False  
        self.LEFT_key_down = False  
        self.RIGHT_key_down = False  

        self.w_key_down = False  ## --- ADD CONTROLS FOR OTHER KEYS TO CONTROL THE CAMERA --- ##
        self.s_key_down = False  ## --- ADD CONTROLS FOR OTHER KEYS TO CONTROL THE CAMERA --- ##
        self.a_key_down = False  ## --- ADD CONTROLS FOR OTHER KEYS TO CONTROL THE CAMERA --- ##
        self.d_key_down = False  ## --- ADD CONTROLS FOR OTHER KEYS TO CONTROL THE CAMERA --- ##

        self.q_key_down = False  ## --- ADD CONTROLS FOR OTHER KEYS TO CONTROL THE CAMERA --- ##
        self.e_key_down = False  ## --- ADD CONTROLS FOR OTHER KEYS TO CONTROL THE CAMERA --- ##
        self.r_key_down = False  ## --- ADD CONTROLS FOR OTHER KEYS TO CONTROL THE CAMERA --- ##
        self.f_key_down = False  ## --- ADD CONTROLS FOR OTHER KEYS TO CONTROL THE CAMERA --- ##

        self.white_background = False
        self.size = 5
        self.maze = Maze(self.size)
        self.ballPosX = 2
        self.ballPosZ = 2
        self.ballOri = "north"
        self.speed = 5

    def update(self):
        delta_time = self.clock.tick() / 1000.0

        self.angle += pi * delta_time
        if self.angle > 2 * pi:
            self.angle -= (2 * pi)
        ballmove = ballMovement(self.maze,)
        if ballmove[0] == "north":
            pass
        self.ballCollision()
        self.playerMove(delta_time)

    def ballCollision(self):
        bla = Vector(self.view_matrix.eye.x - 3.0, 0.0, self.view_matrix.eye.z - 3.0)
        blabla = bla.__len__()
        if blabla < self.radius:
            print("sjomli")

    def playerMove(self, delta_time):
        eyePosX = (int)(self.view_matrix.eye.x + 2) // 3  
        eyePosZ = (int)(self.view_matrix.eye.z + 2) // 3
        #print(eyePosX, eyePosZ)  
        if self.w_key_down: 
            self.view_matrix.slide(0, 0, -1 * delta_time)
            if not self.maze.cells[eyePosX][eyePosZ].south:
                if self.view_matrix.eye.z < ((3 * eyePosZ) - 0.5):
                    self.view_matrix.eye.z = ((3 * eyePosZ) - 0.5)
            if not self.maze.cells[eyePosX][eyePosZ].west:
                if self.view_matrix.eye.x < ((3 * eyePosX) - 0.5):
                    self.view_matrix.eye.x = ((3 * eyePosX) - 0.5)
            if eyePosZ == (self.maze.size - 1):
                if self.view_matrix.eye.z > ((3 * eyePosZ) + 0.5):
                    self.view_matrix.eye.z = ((3 * eyePosZ) + 0.5)
            elif not self.maze.cells[eyePosX][eyePosZ + 1].south:
                if self.view_matrix.eye.z > ((3 * eyePosZ) + 0.5):
                    self.view_matrix.eye.z = ((3 * eyePosZ) + 0.5) 
            if eyePosX == (self.maze.size - 1):
                if self.view_matrix.eye.x > ((3 * eyePosX) + 0.5):
                    self.view_matrix.eye.x = ((3 * eyePosX) + 0.5)
            elif not self.maze.cells[eyePosX + 1][eyePosZ].west:
                if self.view_matrix.eye.x > ((3 * eyePosX) + 0.5):
                    self.view_matrix.eye.x = ((3 * eyePosX) + 0.5) 
        if self.s_key_down:
            self.view_matrix.slide(0, 0, 1 * delta_time)
            if not self.maze.cells[eyePosX][eyePosZ].south:
                if self.view_matrix.eye.z < ((3 * eyePosZ) - 0.5):
                    self.view_matrix.eye.z = ((3 * eyePosZ) - 0.5)
            if not self.maze.cells[eyePosX][eyePosZ].west:
                if self.view_matrix.eye.x < ((3 * eyePosX) - 0.5):
                    self.view_matrix.eye.x = ((3 * eyePosX) - 0.5)
            if eyePosZ == (self.maze.size - 1):
                if self.view_matrix.eye.z > ((3 * eyePosZ) + 0.5):
                    self.view_matrix.eye.z = ((3 * eyePosZ) + 0.5)
            elif not self.maze.cells[eyePosX][eyePosZ + 1].south:
                if self.view_matrix.eye.z > ((3 * eyePosZ) + 0.5):
                    self.view_matrix.eye.z = ((3 * eyePosZ) + 0.5) 
            if eyePosX == (self.maze.size - 1):
                if self.view_matrix.eye.x > ((3 * eyePosX) + 0.5):
                    self.view_matrix.eye.x = ((3 * eyePosX) + 0.5)
            elif not self.maze.cells[eyePosX + 1][eyePosZ].west:
                if self.view_matrix.eye.x > ((3 * eyePosX) + 0.5):
                    self.view_matrix.eye.x = ((3 * eyePosX) + 0.5)
        if self.a_key_down:
            self.view_matrix.pitch(-pi * delta_time)
        if self.d_key_down:
            self.view_matrix.pitch(pi * delta_time)
        

    def display(self):
        glEnable(GL_DEPTH_TEST)  ### --- NEED THIS FOR NORMAL 3D BUT MANY EFFECTS BETTER WITH glDisable(GL_DEPTH_TEST) ... try it! --- ###

        if self.white_background:
            glClearColor(1.0, 1.0, 1.0, 1.0)
        else:
            glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)  ### --- YOU CAN ALSO CLEAR ONLY THE COLOR OR ONLY THE DEPTH --- ###

        glViewport(0, 0, 800, 600)

        self.model_matrix.load_identity()
        #self.cube.set_vertices(self.shader)
        self.shader.set_view_matrix(self.view_matrix.get_matrix())
        self.shader.set_eye_position(self.view_matrix.eye)
        self.shader.set_light_position(Point(5, 10.0, 5))
        self.shader.set_light_diffuse(0.8, 0.3, 0.4)
        self.shader.set_light_specular(0.8, 0.3, 0.4)
        self.shader.set_light_ambiance(0.1, 0.0, 0.0)

        self.sphere.set_vertices(self.shader)
        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(3.0, 1.0, 3.0)
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.sphere.draw(self.shader)
        self.model_matrix.pop_matrix()        
        self.displayMaze()
        self.drawExtirior()

        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(5.0, -0.2, 5.0)  
        self.model_matrix.add_scale(20.0, 0.4, 20.0)  
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()
        #pygame.display.flip()
        glViewport(400, 300, 600, 500)
        glClear(GL_DEPTH_BUFFER_BIT)

        self.model_matrix.load_identity()        
        #self.cube.set_vertices(self.shader)
        self.view_matrix_mini.look(self.view_matrix.eye + Point(0, 25, 0), self.view_matrix.eye, Vector(0, 0, 1))
        self.shader.set_view_matrix(self.view_matrix_mini.get_matrix())
        self.shader.set_eye_position(self.view_matrix_mini.eye)

        self.sphere.set_vertices(self.shader)
        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(3.0, 1.0, 3.0)
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.sphere.draw(self.shader)
        self.model_matrix.pop_matrix()        
        self.displayMaze()
        self.drawExtirior()

        self.model_matrix.push_matrix()
        self.model_matrix.add_translation(5.0, -0.2, 5.0)  
        self.model_matrix.add_scale(20.0, 0.4, 20.0)  
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()
        pygame.display.flip()



    def program_loop(self):
        exiting = False
        while not exiting:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("Quitting!")
                    exiting = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        print("Escaping!")
                        exiting = True
                        
                    if event.key == K_UP:
                        self.UP_key_down = True
                    elif event.key == K_DOWN:
                        self.DOWN_key_down = True
                    elif event.key == K_LEFT:
                        self.LEFT_key_down = True
                    elif event.key == K_RIGHT:
                        self.RIGHT_key_down = True

                    if event.key == K_w:
                        self.w_key_down = True
                    elif event.key == K_s:
                        self.s_key_down = True
                    elif event.key == K_a:
                        self.a_key_down = True
                    elif event.key == K_d:
                        self.d_key_down = True

                    if event.key == K_q:
                        self.q_key_down = True
                    elif event.key == K_e:
                        self.e_key_down = True
                    elif event.key == K_r:
                        self.r_key_down = True
                    elif event.key == K_f:
                        self.r_key_down = True
                elif event.type == pygame.KEYUP:
                    if event.key == K_UP:
                        self.UP_key_down = False
                    elif event.key == K_DOWN:
                        self.DOWN_key_down = False
                    elif event.key == K_LEFT:
                        self.LEFT_key_down = False
                    elif event.key == K_RIGHT:
                        self.RIGHT_key_down = False

                    if event.key == K_w:
                        self.w_key_down = False
                    elif event.key == K_s:
                        self.s_key_down = False
                    elif event.key == K_a:
                        self.a_key_down = False
                    elif event.key == K_d:
                        self.d_key_down = False

                    if event.key == K_q:
                        self.q_key_down = False
                    elif event.key == K_e:
                        self.e_key_down = False
                    elif event.key == K_r:
                        self.r_key_down = False
                    elif event.key == K_f:
                        self.r_key_down = False
            
            self.update()
            self.display()

        #OUT OF GAME LOOP
        pygame.quit()
    def displayMaze(self):
        for i in range (self.maze.size):
            for j in range (self.maze.size):
                if self.maze.cells[i][j].south == False:
                    self.drawSouthWall(i, j)
                if self.maze.cells[i][j].west == False:
                    self.drawWestWall(i, j)

    def drawWestWall(self, x, z):
        self.model_matrix.push_matrix()
        self.model_matrix.add_scale(3.0, 3.0, 3.0)
        self.model_matrix.add_translation(x - 0.5 , 1, z)
        self.model_matrix.add_scale(0.1, 2, 1)
        self.shader.set_material_diffuse(0.3, 0.2, 0.8)
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()

    def drawSouthWall(self, x, z):
        self.model_matrix.push_matrix()
        self.model_matrix.add_scale(3.0, 3.0, 3.0)
        self.model_matrix.add_translation(x , 1 , z - 0.5)
        self.model_matrix.add_scale(1, 2, 0.1)
        self.shader.set_material_diffuse(0.3, 0.2, 0.8)
        self.shader.set_model_matrix(self.model_matrix.matrix)
        self.cube.draw(self.shader)
        self.model_matrix.pop_matrix()

    def drawExtirior(self):
        for i in range(self.size):
            self.drawSouthWall(i, self.size)
            self.drawWestWall(self.size, i)



    def start(self):
        self.program_loop()

if __name__ == "__main__":
    GraphicsProgram3D().start()