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
        self.wait()

        transform_title = TextMobject("Our Problem:")
        transform_title.to_corner(UP + LEFT)

        self.play(
            Transform(basel, transform_title),
            LaggedStart(*map(FadeOutAndShiftDown, logo)),
            LaggedStart(*map(FadeOutAndShiftDown, author)),
        )
        self.wait()

class problemAtHand(GraphScene):
    #Set some graph variables
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "y_min": 0,
        "y_max": 10,
        "graph_origin": ((DOWN*3.5)+(LEFT*4)),
        "function_color": WHITE,
        "axes_color": WHITE
    }

    def construct(self):
        #Create and draw "our problem:" text
        problem_text = TextMobject("Our Problem:")
        problem_text.to_corner(UP + LEFT)
        self.add(problem_text)

        #Draw axes
        self.setup_axes(animate=True)
        self.wait()

        #Creates our start point and label
        point1 = Dot(self.coords_to_point(2,2))
        point1_lab = TextMobject("\\small{(Sx,Sy)}")
        point1_lab.next_to(point1,RIGHT+DOWN)

        #Creates our end point and label
        point2 = Dot(self.coords_to_point(8,8))
        point2_lab = TextMobject("\\small{(Ex,Ey)}")
        point2_lab.next_to(point2,RIGHT+DOWN)

        #Draws points and labels to the screen
        self.play(
            ShowCreation(point1),
            Write(point1_lab),
            ShowCreation(point2),
            Write(point2_lab),
        )
        self.wait(2)

        #Creates the line to connect the points
        x = self.coords_to_point(2,2)
        y = self.coords_to_point(8,8)
        connectingLine= Line(x, y, color=WHITE)

        #Draws line to screen
        self.play(
            ShowCreation(connectingLine),
        )
        self.add(point1, point2) #forces the points back on top of line
        self.wait(3)

        #Colors points
        self.play(
            FadeToColor(point1, RED),
            FadeToColor(point2, BLUE),
        )
        self.wait()

        #Next 3 play calls are to change color of line
        self.play(
            FadeToColor(connectingLine, RED),
        )
        self.wait(2)

        self.play(
            FadeToColor(connectingLine, BLUE),
        )
        self.wait(2)

        self.play(
            FadeToColor(connectingLine, WHITE),
        )
        self.wait(2)

        #Split connectingLine into 2
        split1 = self.coords_to_point(2,2)
        centerPoint = self.coords_to_point(5,5)
        split2 = self.coords_to_point(8,8)

        #Create split lines
        splitLine1= Line(split1, centerPoint, color=RED)
        splitLine2= Line(centerPoint, split2, color=BLUE)

        #Draw split lines to screen
        self.play(
            ShowCreation(splitLine1),
            ShowCreation(splitLine2),
        )
        self.add(point1, point2) #forces the points back on top of line
        self.wait(4)

        #Create transition title
        solution_Text = TextMobject("Formulating a solution")

        self.play(
            LaggedStart(*map(ShrinkToCenter, splitLine2)),
            LaggedStart(*map(ShrinkToCenter, splitLine1)),
            LaggedStart(*map(ShrinkToCenter, point1)),
            LaggedStart(*map(ShrinkToCenter, point1_lab)),
            LaggedStart(*map(ShrinkToCenter, point2)),
            LaggedStart(*map(ShrinkToCenter, point2_lab)),
            LaggedStart(*map(ShrinkToCenter, connectingLine)),
            Transform(problem_text, solution_Text),
        )
        self.wait()

class formulatingSolution(GraphScene):
    CONFIG = {
        "x_min": 0,
        "x_max": 10,
        "y_min": 0,
        "y_max": 10,
        "graph_origin": ((DOWN*3.5)+(LEFT*4)),
        "function_color": WHITE,
        "axes_color": WHITE
    }

    def construct(self):

        solution_Text_Start = TextMobject("Formulating a solution")
        solution_Text = TextMobject("Formulating a solution:")
        solution_Text.to_corner(UP + LEFT)
        self.add(solution_Text_Start)

        self.play(
            Transform(solution_Text_Start, solution_Text),
        )
        self.wait()
