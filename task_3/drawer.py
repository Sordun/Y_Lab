import math

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from calculator import (
    Circle,
    Rectangle,
    Square,
    Trapezoid,
    Rhombus,
    Triangle,
    Sphere,
    Parallelepiped,
    Cube,
    Cylinder,
    Cone,
    Pyramid,
)


class Drawer2D:
    @staticmethod
    def draw_circle(figure, circle: Circle):
        ax = Drawer2D.add_subplot(figure)
        theta = np.linspace(0, 2 * np.pi, 100)
        ax.plot(circle.radius * np.cos(theta), circle.radius * np.sin(theta), color="r")
        circle = plt.Circle((0, 0), circle.radius, facecolor="cyan", linewidth=1, alpha=0.25)
        ax.add_artist(circle)

    @staticmethod
    def draw_rect(figure, rect: Rectangle):
        ax = Drawer2D.add_subplot(figure)
        v = np.array([[0, 0], [rect.a, 0], [rect.a, rect.b], [0, rect.b], [0, 0]])
        ax.plot(v[:, 0], v[:, 1], "-o")
        rect = plt.Rectangle((0, 0), rect.a, rect.b, facecolor="cyan", linewidth=1, alpha=0.25)
        ax.add_artist(rect)

    @staticmethod
    def draw_quad(figure, quad: Square):
        Drawer2D.draw_rect(figure, quad)

    @staticmethod
    def draw_triangle(figure, triangle: Triangle):
        ax = Drawer2D.add_subplot(figure)
        alpha = math.asin((triangle.a**2 + triangle.b**2 - triangle.c**2) / (2 * triangle.a * triangle.b))
        x, y = triangle.b * math.sin(alpha), triangle.b * math.cos(alpha)
        v = np.array([[0, 0], [triangle.a, 0], [x, y], [0, 0]])
        ax.plot(v[:, 0], v[:, 1], "-o")
        triangle = plt.Polygon(v, facecolor="cyan", linewidth=1, alpha=0.25)
        ax.add_artist(triangle)

    @staticmethod
    def draw_trapezoid(figure, trapezoid: Trapezoid):
        ax = Drawer2D.add_subplot(figure)
        a1 = math.radians(trapezoid.left_base_angle)
        a2 = math.radians(trapezoid.right_base_angle)
        x1 = trapezoid.height / math.sin(a1) * math.cos(a1)
        x2 = trapezoid.height / math.sin(a2) * math.cos(a2)
        v = np.array(
            [
                [0, 0],
                [trapezoid.base, 0],
                [trapezoid.base - x2, trapezoid.height],
                [x1, trapezoid.height],
                [0, 0],
            ]
        )
        ax.plot(v[:, 0], v[:, 1], "-o")
        trapezoid = plt.Polygon(v, facecolor="cyan", linewidth=1, alpha=0.25)
        ax.add_artist(trapezoid)

    @staticmethod
    def draw_rhombus(figure, rhombus: Rhombus):
        ax = Drawer2D.add_subplot(figure)
        v = np.array(
            [
                [0, -rhombus.d2 / 2],
                [rhombus.d1 / 2, 0],
                [0, rhombus.d2 / 2],
                [-rhombus.d1 / 2, 0],
                [0, -rhombus.d2 / 2],
            ]
        )
        ax.plot(v[:, 0], v[:, 1], "-o")
        rhombus = plt.Polygon(v, facecolor="cyan", linewidth=1, alpha=0.25)
        ax.add_artist(rhombus)

    @staticmethod
    def add_subplot(figure):
        ax = figure.add_subplot(111)
        ax.set_aspect("equal")
        return ax


class Drawer3D:
    POINTS_COUNT = 20

    @staticmethod
    def draw_pyramid(figure, pyramid: Pyramid) -> None:
        x = pyramid.x
        height = pyramid.h
        ax = figure.add_subplot(111, projection="3d")
        v = np.array([[0, 0, 0], [x, 0, 0], [x, x, 0], [0, x, 0], [x / 2, x / 2, height]])

        polygons = [
            [v[0], v[1], v[4]],
            [v[0], v[3], v[4]],
            [v[2], v[1], v[4]],
            [v[2], v[3], v[4]],
            [v[0], v[1], v[2], v[3]],
        ]

        ax.add_collection3d(Poly3DCollection(polygons, facecolors="cyan", linewidths=1, edgecolors="r", alpha=0.25))
        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])

        Drawer3D.set_labels(ax)

    @staticmethod
    def draw_cone(figure, cone: Cone):
        ax = figure.add_subplot(111, projection="3d")
        v = [[0, 0, cone.h]]
        v.extend(Drawer3D.get_circle_points(cone.radius))
        v = np.array(v)

        polygons = []
        for i in range(1, Drawer3D.POINTS_COUNT):
            polygons.append([v[0], v[i], v[i + 1]])
        polygons.append([v[0], v[1], v[len(v) - 1]])
        polygons.append(v[1:])
        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
        ax.add_collection3d(Poly3DCollection(polygons, facecolors="cyan", linewidths=1, edgecolors="r", alpha=0.25))

        Drawer3D.set_labels(ax)

    @staticmethod
    def draw_cylinder(figure, cylinder: Cylinder):
        ax = figure.add_subplot(111, projection="3d")

        v = Drawer3D.get_circle_points(cylinder.radius, 0)
        v.extend(Drawer3D.get_circle_points(cylinder.radius, cylinder.h))
        v = np.array(v)

        polygons = []
        for i in range(Drawer3D.POINTS_COUNT - 1):
            polygons.append(
                [
                    v[i],
                    v[i + 1],
                    v[Drawer3D.POINTS_COUNT + 1 + i],
                    v[Drawer3D.POINTS_COUNT + i],
                ]
            )

        polygons.append(
            [
                v[0],
                v[Drawer3D.POINTS_COUNT - 1],
                v[Drawer3D.POINTS_COUNT * 2 - 1],
                v[Drawer3D.POINTS_COUNT],
            ]
        )
        polygons.append(v[: Drawer3D.POINTS_COUNT])
        polygons.append(v[Drawer3D.POINTS_COUNT:])

        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
        ax.add_collection3d(Poly3DCollection(polygons, facecolors="cyan", linewidths=1, edgecolors="r", alpha=0.25))

        Drawer3D.set_labels(ax)

    @staticmethod
    def draw_sphere(figure, sphere: Sphere):
        ax = figure.add_subplot(111, projection="3d")
        u, v = np.mgrid[
            0: 2 * np.pi: Drawer3D.POINTS_COUNT * 1j,
            0: np.pi: Drawer3D.POINTS_COUNT * 1j,
        ]

        x = np.cos(u) * np.sin(v) * sphere.r
        y = np.sin(u) * np.sin(v) * sphere.r
        z = np.cos(v) * sphere.r

        ax.scatter3D(x, y, z)
        ax.plot_surface(x, y, z, color="cyan", alpha=0.25)
        ax.plot_wireframe(x, y, z, color="r", linewidth=1)

        Drawer3D.set_labels(ax)

    @staticmethod
    def draw_parallelepiped(figure, parallelepiped: Parallelepiped):
        ax = figure.add_subplot(111, projection="3d")

        v = [
            [0, 0, 0],
            [1, 0, 0],
            [1, 1, 0],
            [0, 1, 0],
            [0, 0, 1],
            [1, 0, 1],
            [1, 1, 1],
            [0, 1, 1],
        ]
        v = np.array(
            [
                [
                    x[0] * parallelepiped.a,
                    x[1] * parallelepiped.b,
                    x[2] * parallelepiped.h,
                ]
                for x in v
            ]
        )

        polygons = [
            [v[0], v[1], v[2], v[3]],
            [v[4], v[5], v[6], v[7]],
            [v[0], v[1], v[5], v[4]],
            [v[1], v[2], v[6], v[5]],
            [v[2], v[3], v[7], v[6]],
            [v[3], v[0], v[4], v[7]],
        ]

        ax.scatter3D(v[:, 0], v[:, 1], v[:, 2])
        ax.add_collection3d(Poly3DCollection(polygons, facecolors="cyan", linewidths=1, edgecolors="r", alpha=0.25))

        Drawer3D.set_labels(ax)

    @staticmethod
    def draw_cube(figure, cube: Cube):
        Drawer3D.draw_parallelepiped(figure, cube)

    @staticmethod
    def get_circle_points(radius, z=0.0, points_count=POINTS_COUNT):
        v = []
        for i in range(0, points_count):
            angle = (2 * math.pi / points_count) * i
            x, y = math.cos(angle) * radius, math.sin(angle) * radius
            v.append([x, y, z])
        return v

    @staticmethod
    def set_labels(ax):
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        Drawer3D.set_axes_equal(ax)

    @staticmethod
    def set_axes_equal(ax):
        """Make axes of 3D plot have equal scale so that spheres appear as spheres,
        cubes as cubes, etc..  This is one possible solution to Matplotlib's
        ax.set_aspect('equal') and ax.axis('equal') not working for 3D.
        Input
          ax: a matplotlib axis, e.g., as output from plt.gca().
        """

        x_limits = ax.get_xlim3d()
        y_limits = ax.get_ylim3d()
        z_limits = ax.get_zlim3d()

        x_range = abs(x_limits[1] - x_limits[0])
        x_middle = np.mean(x_limits)
        y_range = abs(y_limits[1] - y_limits[0])
        y_middle = np.mean(y_limits)
        z_range = abs(z_limits[1] - z_limits[0])
        z_middle = np.mean(z_limits)

        # The plot bounding box is a sphere in the sense of the infinity
        # norm, hence I call half the max range the plot radius.
        plot_radius = 0.5 * max([x_range, y_range, z_range])

        ax.set_xlim3d([x_middle - plot_radius, x_middle + plot_radius])
        ax.set_ylim3d([y_middle - plot_radius, y_middle + plot_radius])
        ax.set_zlim3d([z_middle - plot_radius, z_middle + plot_radius])
