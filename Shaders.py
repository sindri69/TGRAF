
from OpenGL.GL import *
from math import * # trigonometry

import sys

from Base3DObjects import *

class Shader3D:
    def __init__(self):
        vert_shader = glCreateShader(GL_VERTEX_SHADER)
        shader_file = open(sys.path[0] + "/simple3D.vert")
        glShaderSource(vert_shader,shader_file.read())
        shader_file.close()
        glCompileShader(vert_shader)
        result = glGetShaderiv(vert_shader, GL_COMPILE_STATUS)
        if (result != 1): # shader didn't compile
            print("Couldn't compile vertex shader\nShader compilation Log:\n" + str(glGetShaderInfoLog(vert_shader)))

        frag_shader = glCreateShader(GL_FRAGMENT_SHADER)
        shader_file = open(sys.path[0] + "/simple3D.frag")
        glShaderSource(frag_shader,shader_file.read())
        shader_file.close()
        glCompileShader(frag_shader)
        result = glGetShaderiv(frag_shader, GL_COMPILE_STATUS)
        if (result != 1): # shader didn't compile
            print("Couldn't compile fragment shader\nShader compilation Log:\n" + str(glGetShaderInfoLog(frag_shader)))

        self.renderingProgramID = glCreateProgram()
        glAttachShader(self.renderingProgramID, vert_shader)
        glAttachShader(self.renderingProgramID, frag_shader)
        glLinkProgram(self.renderingProgramID)

        self.positionLoc = glGetAttribLocation(self.renderingProgramID, "a_position")
        glEnableVertexAttribArray(self.positionLoc)

        self.normalLoc = glGetAttribLocation(self.renderingProgramID, "a_normal")
        glEnableVertexAttribArray(self.normalLoc)
        ## ADD CODE HERE ##

        self.modelMatrixLoc			= glGetUniformLocation(self.renderingProgramID, "u_model_matrix")
        self.viewMatrixLoc = glGetUniformLocation(self.renderingProgramID, "u_view_matrix")
        self.projectionMatrixLoc = glGetUniformLocation(self.renderingProgramID, "u_projection_matrix")
        
        ##original light
        #self.colorLoc = glGetUniformLocation(self.renderingProgramID, "u_color")
        self.eyePosLoc = glGetUniformLocation(self.renderingProgramID, "u_eye_position")
        self.lightPosLoc = glGetUniformLocation(self.renderingProgramID, "u_light_position")
        self.lightDiffuseLoc = glGetUniformLocation(self.renderingProgramID, "u_light_diffuse")
        self.lightSpecLoc = glGetUniformLocation(self.renderingProgramID, "u_light_specular")
        self.lightAmbianceLoc = glGetUniformLocation(self.renderingProgramID, "u_light_ambiance")

        self.materialDiffuseLoc = glGetUniformLocation(self.renderingProgramID, "u_material_diffuse")
        self.materialSpecLoc = glGetUniformLocation(self.renderingProgramID, "u_material_specular")
        self.materialShininessLoc = glGetUniformLocation(self.renderingProgramID, "u_material_shininess")

 
        self.light1PosLoc = glGetUniformLocation(self.renderingProgramID, "u_light1_position")
        self.light1DiffuseLoc = glGetUniformLocation(self.renderingProgramID, "u_light1_diffuse")
        self.light1SpecLoc = glGetUniformLocation(self.renderingProgramID, "u_light1_specular")
        self.light1AmbianceLoc = glGetUniformLocation(self.renderingProgramID, "u_light1_ambiance")

        self.materia1lDiffuseLoc = glGetUniformLocation(self.renderingProgramID, "u_material1_diffuse")
        self.material1SpecLoc = glGetUniformLocation(self.renderingProgramID, "u_material1_specular")
        self.material1ShininessLoc = glGetUniformLocation(self.renderingProgramID, "u_material1_shininess")

   
        self.light2PosLoc = glGetUniformLocation(self.renderingProgramID, "u_light2_position")
        self.light2DiffuseLoc = glGetUniformLocation(self.renderingProgramID, "u_light2_diffuse")
        self.light2SpecLoc = glGetUniformLocation(self.renderingProgramID, "u_light2_specular")
        self.light2AmbianceLoc = glGetUniformLocation(self.renderingProgramID, "u_light2_ambiance")

        self.material2DiffuseLoc = glGetUniformLocation(self.renderingProgramID, "u_material2_diffuse")
        self.material2SpecLoc = glGetUniformLocation(self.renderingProgramID, "u_material2_specular")
        self.material2ShininessLoc = glGetUniformLocation(self.renderingProgramID, "u_material2_shininess")

    def use(self):
        try:
            glUseProgram(self.renderingProgramID)   
        except OpenGL.error.GLError:
            print(glGetProgramInfoLog(self.renderingProgramID))
            raise

    def set_model_matrix(self, matrix_array):
        glUniformMatrix4fv(self.modelMatrixLoc, 1, True, matrix_array)
    
    def set_view_matrix(self, matrix_array):
        glUniformMatrix4fv(self.viewMatrixLoc, 1, True, matrix_array)
    def set_projection_matrix(self, matrix_array):
        glUniformMatrix4fv(self.projectionMatrixLoc, 1, True, matrix_array)
    
    def set_eye_position(self, pos):
        glUniform4f(self.eyePosLoc, pos.x, pos.y, pos.z, 1.0)

    def set_light_position(self, pos):
        glUniform4f(self.lightPosLoc, pos.x, pos.y, pos.z, 1.0)
    def set_light_diffuse(self, red, green, blue):
        glUniform4f(self.lightDiffuseLoc, red, green, blue, 1.0)
    def set_light_specular(self, red, green, blue):
        glUniform4f(self.lightSpecLoc, red, green, blue, 1.0)
    def set_light_ambiance(self, red, green, blue):
        glUniform4f(self.lightAmbianceLoc, red, green, blue, 1.0)


    def set_material_diffuse(self, red, green, blue):
        glUniform4f(self.materialDiffuseLoc, red, green, blue, 1.0)
    def set_material_specular(self, red, green, blue):
        glUniform4f(self.materialSpecLoc, red, green, blue, 1.0)
    def set_material_shininess(self, shininess):
        glUniform1i(self.materialShininessLoc, shininess)

    def set_light1_position(self, pos):
          glUniform4f(self.light1PosLoc, pos.x, pos.y, pos.z, 1.0)
    def set_light1_diffuse(self, red, green, blue):
        glUniform4f(self.light1DiffuseLoc, red, green, blue, 1.0)
    def set_light1_specular(self, red, green, blue):
        glUniform4f(self.light1SpecLoc, red, green, blue, 1.0)
    def set_light1_ambiance(self, red, green, blue):
        glUniform4f(self.light1AmbianceLoc, red, green, blue, 1.0)


    def set_material1_diffuse(self, red, green, blue):
        glUniform4f(self.material1DiffuseLoc, red, green, blue, 1.0)
    def set_material1_specular(self, red, green, blue):
        glUniform4f(self.material1SpecLoc, red, green, blue, 1.0)
    def set_material1_shininess(self, shininess):
        glUniform1i(self.material1ShininessLoc, shininess)

    def set_light2_position(self, pos):
          glUniform4f(self.light2PosLoc, pos.x, pos.y, pos.z, 1.0)
    def set_light2_diffuse(self, red, green, blue):
        glUniform4f(self.light2DiffuseLoc, red, green, blue, 1.0)
    def set_light2_specular(self, red, green, blue):
        glUniform4f(self.light2SpecLoc, red, green, blue, 1.0)
    def set_light2_ambiance(self, red, green, blue):
        glUniform4f(self.light2AmbianceLoc, red, green, blue, 1.0)


    def set_material2_diffuse(self, red, green, blue):
        glUniform4f(self.material2DiffuseLoc, red, green, blue, 1.0)
    def set_material2_specular(self, red, green, blue):
        glUniform4f(self.material2SpecLoc, red, green, blue, 1.0)
    def set_material2_shininess(self, shininess):
        glUniform1i(self.material2ShininessLoc, shininess)

    def set_position_attribute(self, vertex_array):
        glVertexAttribPointer(self.positionLoc, 3, GL_FLOAT, False, 0, vertex_array)

    def set_normal_attribute(self, vertex_array):
        glVertexAttribPointer(self.normalLoc, 3, GL_FLOAT, False, 0, vertex_array)
    ## ADD CODE HERE ##
