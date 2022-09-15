from manim import *
import numpy as np

DOT_RADIUS = 0.02
N = 10000

def change_dots(D, old_mask, new_mask):
    Anims = []
    for (d, old_m, new_m) in zip(D, old_mask, new_mask):
        if (not old_m) and new_m :
            Anims.append(FadeOut(d))
        if old_m and (not new_m) :
            Anims.append(FadeIn(d))
    return Anims


class example(MovingCameraScene):
    def construct(self):
        X = np.arange(0, N)
        Y = np.sin(X)
        K = np.arange(N)
        axes = Axes(
            x_range = [0, N, N//10],
            y_range = [-1, 1, 0.2],
            axis_config = {"include_tip":False}
        )
        n = ValueTracker(1)
        L = always_redraw(lambda : DecimalNumber(n.get_value(), 0).next_to(axes, LEFT))

        Dots = Group(*[Dot(point=axes.c2p(x,y), radius=DOT_RADIUS) for (x, y) in zip(X, Y)])
        self.add(axes, L)
        self.wait()
        self.play(AnimationGroup(*[GrowFromCenter(d) for d in Dots], group = Dots, lag_ratio=0.001))
        self.wait()
        for i in range(2, 21):
            self.play(*change_dots(Dots, K%(i-1)!=0, K%i!=0), n.animate.set_value(i))
            self.wait()
