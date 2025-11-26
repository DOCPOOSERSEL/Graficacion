import glfw
import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Variables globales para la cámara
camX, camY, camZ = 0.0, 0.0, 5.0  # posición inicial
camSpeed = 0.2  # velocidad de movimiento

# --- NUEVO: teclado con GLFW ---
def teclado_glfw(window, key, scancode, action, mods):
    global camX, camY, camZ, camSpeed

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_W:
            camZ -= camSpeed
        elif key == glfw.KEY_S:
            camZ += camSpeed
        elif key == glfw.KEY_A:
            camX -= camSpeed
        elif key == glfw.KEY_D:
            camX += camSpeed

def init():
    glClearColor(0.5, 0.8, 1.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    gluPerspective(60, 1, 6, 100.0)
    glMatrixMode(GL_MODELVIEW)

def draw_cube():
    glBegin(GL_QUADS)
    glColor3f(0.8, 0.5, 0.2)

    # Frente
    glVertex3f(-1, 0, 1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 5, 1)
    glVertex3f(-1, 5, 1)

    # Atrás
    glVertex3f(-1, 0, -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 5, -1)
    glVertex3f(-1, 5, -1)

    # Izquierda
    glVertex3f(-1, 0, -1)
    glVertex3f(-1, 0, 1)
    glVertex3f(-1, 5, 1)
    glVertex3f(-1, 5, -1)

    # Derecha
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(1, 5, 1)
    glVertex3f(1, 5, -1)

    # Arriba
    glColor3f(0.9, 0.6, 0.3)
    glVertex3f(-1, 5, -1)
    glVertex3f(1, 5, -1)
    glVertex3f(1, 5, 1)
    glVertex3f(-1, 5, 1)

    # Abajo
    glColor3f(0.6, 0.4, 0.2)
    glVertex3f(-1,0 , -1)
    glVertex3f(1, 0, -1)
    glVertex3f(1, 0, 1)
    glVertex3f(-1, 0, 1)
    glEnd()

def draw_roof():
    glBegin(GL_TRIANGLES)
    glColor3f(0.9, 0.1, 0.1)

    # Frente
    glVertex3f(-1, 5, 1)
    glVertex3f(1, 5, 1)
    glVertex3f(0, 9, 0)

    # Atrás
    glVertex3f(-1, 5, -1)
    glVertex3f(1, 5, -1)
    glVertex3f(0, 9, 0)

    # Izquierda
    glVertex3f(-1, 5, -1)
    glVertex3f(-1, 5, 1)
    glVertex3f(0, 9, 0)

    # Derecha
    glVertex3f(1, 5, -1)
    glVertex3f(1, 5, 1)
    glVertex3f(0, 9, 0)
    glEnd()

def draw_ground():
    glBegin(GL_QUADS)
    glColor3f(0.3, 0.3, 0.3)

    glVertex3f(-20, 0, 20)
    glVertex3f(20, 0, 20)
    glVertex3f(20, 0, -20)
    glVertex3f(-20, 0, -20)
    glEnd()

def draw_house():
    draw_cube()
    draw_roof()

def draw_scene():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # --- NUEVO: cámara usando variables de movimiento ---
    gluLookAt(camX, camY, camZ,   # posición cámara
              0, 0, 0,            # mira al centro
              0, 1, 0)            # UP

    draw_ground()

    positions = [
        (-5, 0, -5),
        (5, 0, -5),
        (-5, 0, 5),
        (5, 0, 5),
        (0, 0, 0),
    ]

    for pos in positions:
        glPushMatrix()
        glTranslatef(*pos)
        draw_house()
        glPopMatrix()

    glfw.swap_buffers(window)

def main():
    global window

    if not glfw.init():
        sys.exit()
    
    width, height = 800, 600
    window = glfw.create_window(width, height, "Escena con 4 casas", None, None)
    if not window:
        glfw.terminate()
        sys.exit()

    glfw.make_context_current(window)
    glViewport(0, 0, width, height)
    init()

    # ya pa q vea
    glfw.set_key_callback(window, teclado_glfw)

    while not glfw.window_should_close(window):
        draw_scene()
        glfw.poll_events()

    glfw.terminate()

if __name__ == "__main__":
    main()
