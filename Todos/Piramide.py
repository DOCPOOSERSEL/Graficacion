import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)  # Establecer color de fondo
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1.0, 0.1, 50.0)  # Configuración de perspectiva
    glMatrixMode(GL_MODELVIEW)

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    glTranslatef(0.0, 0.0, -10)  # Mover camara

    # Empiezan los triangulos
    glBegin(GL_TRIANGLES)
    # Cara frontal que no es frontal (rojo)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)   # Punta
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    # Cara derecha (verde)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    # Cara trasera que es la frontal (azul)
    glColor3f(0.0, 0.0, 1.0)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    # Cara izquierda (amarillo)
    glColor3f(1.0, 1.0, 0.0)
    glVertex3f(0.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glEnd()

    # Base cuadrada
    glBegin(GL_QUADS)
    glColor3f(0.6, 0.3, 0.0)  # Marron
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glEnd()

    glutSwapBuffers()

def main():
    # Inicializar GLUT
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow(b'Triangulo con GLUT y Python') 
    # En caso de usar el glut para crear la ventanna se deve de formatear el string para que use codificacion en binario o algo asi dice la documentacion

    init()
    glutDisplayFunc(display)
    glutMainLoop()

if __name__ == "__main__":
    main()