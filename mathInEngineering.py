from manimlib.imports import *

class introSequence(Scene):
    def construct(self):
        logo = ImageMobject('assets/Hughes_Sig Set_Horz/Sig_New_Horz_Hughes_reverse.png')
        logo.scale(.5)
        logo.shift(2 * UP)

        #title = TextMobject("Math in Engineering")
        basel = TextMobject("\\small{Applying math concepts} \\small{to computer science problems}")

        author = TextMobject("\\tiny{presented by Jared Kimbel}")
        author.shift(2 * DOWN)

        #VGroup(title, basel).arrange(DOWN)

        self.play(
            FadeIn(logo),
        )
        self.wait(.5)
        self.play(
            #Write(title),
            Write(basel),
            Write(author),
        )

class problemAtHand(Scene):
    def construct(self):
        title = TextMobject("This is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, basel)),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()
