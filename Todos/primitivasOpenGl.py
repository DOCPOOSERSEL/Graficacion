import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glEnable(GL_DEPTH_TEST)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 50.0)
    glMatrixMode(GL_MODELVIEW)


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -15)  # alejar cámara para ver todo

    # toroide
    glPushMatrix()
    glTranslatef(-4.0, 3.0, 0.0)
    glColor3f(1.0, 0.0, 0.0)
    glutWireTorus(0.5, 1.5, 20, 20)
    glPopMatrix()

    #Cubo
    glPushMatrix()
    glTranslatef(4.0, 3.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glutWireCube(3)
    glPopMatrix()

    # Cono
    glPushMatrix()
    glTranslatef(-4.0, -3.0, 0.0)
    glRotatef(-90, 1, 0, 0)
    glColor3f(0.0, 0.0, 1.0)
    glutWireCone(1.5, 3.0, 20, 20)
    glPopMatrix()

    # Esfera
    glPushMatrix()
    glTranslatef(4.0, -3.0, 0.0)
    glColor3f(1.0, 1.0, 0.0)
    glutWireSphere(1.8, 20, 20)
    glPopMatrix()

    glutSwapBuffers()


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b'Primitivas GLUT distribuidas por coordenadas')

    init()
    glutDisplayFunc(display)
    glutMainLoop()


if __name__ == "__main__":
    main()
