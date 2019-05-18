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
            LaggedStart(*map(ShrinkToCenter, connectingLine)),
        )
        self.add(point1, point2) #forces the points back on top of line
        self.wait(4)

        #Create transition title
        solution_Text = TextMobject("Formulating a solution:")
        solution_Text.to_corner(UP + LEFT)

        self.play(
            LaggedStart(*map(ShrinkToCenter, splitLine2)),
            LaggedStart(*map(ShrinkToCenter, splitLine1)),
            LaggedStart(*map(ShrinkToCenter, point1)),
            LaggedStart(*map(ShrinkToCenter, point1_lab)),
            LaggedStart(*map(ShrinkToCenter, point2)),
            LaggedStart(*map(ShrinkToCenter, point2_lab)),

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

        solution_Text = TextMobject("Formulating a solution:")
        solution_Text.to_corner(UP + LEFT)
        self.add(solution_Text)

        #Draw axes
        self.setup_axes(animate=False)
        self.wait(2)

        #Create connecting line
        x = self.coords_to_point(2,2)
        y = self.coords_to_point(8,8)
        connectingLine= Line(x, y)

        #Create transform segments
        x1 = self.coords_to_point(2,2)
        y1 = self.coords_to_point(3.5,3.5)
        connectingLineSegment1 = Line(x1,y1)

        x2 = self.coords_to_point(3.5,3.5)
        y2 = self.coords_to_point(5,5)
        connectingLineSegment2 = Line(x2,y2)

        x3 = self.coords_to_point(5,5)
        y3 = self.coords_to_point(6.5,6.5)
        connectingLineSegment3 = Line(x3,y3)

        x4 = self.coords_to_point(6.5,6.5)
        y4 = self.coords_to_point(8,8)
        connectingLineSegment4 = Line(x4,y4)

        #Draws connecting line and transform segments to screen
        self.play(
            ShowCreation(connectingLine),
        )
        self.wait(.5)

        self.add(connectingLineSegment1)
        self.add(connectingLineSegment2)
        self.add(connectingLineSegment3)
        self.add(connectingLineSegment4)

        self.play(
            FadeOut(connectingLine),
        )
        self.wait(.5)

        #Create all the Tiered line segments
        x1 = self.coords_to_point(2,2)
        y1 = self.coords_to_point(3.5,3.5)
        lineSegment1 = Line(x1,y1)

        x2 = self.coords_to_point(3.5,3.5+.5)
        y2 = self.coords_to_point(5,5+.5)
        lineSegment2 = Line(x2,y2)

        x3 = self.coords_to_point(5,5+1)
        y3 = self.coords_to_point(6.5,6.5+1)
        lineSegment3 = Line(x3,y3)

        x4 = self.coords_to_point(6.5,6.5+1.5)
        y4 = self.coords_to_point(8,8+1.5)
        lineSegment4 = Line(x4,y4)

        self.play(
            Transform(connectingLineSegment1, lineSegment1),
            Transform(connectingLineSegment2, lineSegment2),
            Transform(connectingLineSegment3, lineSegment3),
            Transform(connectingLineSegment4, lineSegment4),
        )
        self.wait()

class formulatingSolution2(GraphScene):
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

        solution_Text = TextMobject("Formulating a solution:")
        solution_Text.to_corner(UP + LEFT)
        self.add(solution_Text)

        #Draw axes
        self.setup_axes(animate=False)

        #Create line segments
        x1 = self.coords_to_point(2,2)
        y1 = self.coords_to_point(3.5,3.5)
        lineSegment1 = Line(x1,y1)

        x2 = self.coords_to_point(3.5,3.5+.5)
        y2 = self.coords_to_point(5,5+.5)
        lineSegment2 = Line(x2,y2)

        x3 = self.coords_to_point(5,5+1)
        y3 = self.coords_to_point(6.5,6.5+1)
        lineSegment3 = Line(x3,y3)

        x4 = self.coords_to_point(6.5,6.5+1.5)
        y4 = self.coords_to_point(8,8+1.5)
        lineSegment4 = Line(x4,y4)

        self.add(lineSegment1)
        self.add(lineSegment2)
        self.add(lineSegment3)
        self.add(lineSegment4)
        self.wait(2)

        #Create transform segments
        x1 = self.coords_to_point(2,2)
        y1 = self.coords_to_point(3.5,3.5)
        connectingLineSegment1 = Line(x1,y1)

        x2 = self.coords_to_point(3.5,3.5)
        y2 = self.coords_to_point(5,5)
        connectingLineSegment2 = Line(x2,y2)

        x3 = self.coords_to_point(5,5)
        y3 = self.coords_to_point(6.5,6.5)
        connectingLineSegment3 = Line(x3,y3)

        x4 = self.coords_to_point(6.5,6.5)
        y4 = self.coords_to_point(8,8)
        connectingLineSegment4 = Line(x4,y4)

        self.play(
            Transform(lineSegment1, connectingLineSegment1),
            Transform(lineSegment2, connectingLineSegment2),
            Transform(lineSegment3, connectingLineSegment3),
            Transform(lineSegment4, connectingLineSegment4),
        )
        self.wait()

class solvingProblem(GraphScene):
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

        solution_Text = TextMobject("Formulating a solution:")
        solution_Text.to_corner(UP + LEFT)
        self.add(solution_Text)

        #Draw axes
        self.setup_axes(animate=False)

        solving_text = TextMobject("Solving our problem:")
        solving_text.to_corner(UP + LEFT)

        #Create line
        x = self.coords_to_point(2,2)
        y = self.coords_to_point(8,8)
        connectingLine= Line(x, y)

        self.add(connectingLine)
        self.wait(2)

        self.play(
            Transform(solution_Text, solving_text),
        )
        self.wait(1)

        #Creates our start point and label
        point1 = Dot(self.coords_to_point(2,2))
        point1_lab = TextMobject("\\small{(Sx,Sy)}")
        point1_lab.next_to(point1,RIGHT+DOWN)

        #Creates our end point and label
        point2 = Dot(self.coords_to_point(8,8))
        point2_lab = TextMobject("\\small{(Ex,Ey)}")
        point2_lab.next_to(point2,RIGHT+DOWN)

        self.play(
            ShowCreation(point1),
            Write(point1_lab),
            ShowCreation(point2),
            Write(point2_lab),
        )
        self.wait(2)

        #But wait theres a few more points
        point3 = Dot(self.coords_to_point(5,2))
        point3_lab = TextMobject("\\small{(Sx+$\\Delta$x,Sy)}")
        point3_lab.next_to(point3,RIGHT+DOWN)

        point4 = Dot(self.coords_to_point(8,2))
        point4_lab = TextMobject("\\small{(Ex,Sy)}")
        point4_lab.next_to(point4,RIGHT+DOWN)

        point5 = Dot(self.coords_to_point(5,5))
        point5_lab = TextMobject("\\small{(Sx+$\\Delta$x,Sy+$\\Delta$y)}")
        point5_lab.next_to(point5,UP+LEFT)

        self.play(
            ShowCreation(point4),
            Write(point4_lab),
        )
        self.wait()

        #Horizontal line
        horiz_x = self.coords_to_point(2,2)
        horiz_y = self.coords_to_point(8,2)
        horizontalConnectingLine= Line(horiz_x, horiz_y)

        #Vertical line
        vert_x = self.coords_to_point(8,2)
        vert_y = self.coords_to_point(8,8)
        verticalConnectingLine= Line(vert_x, vert_y)

        #Center line
        cent_x = self.coords_to_point(5,2)
        cent_y = self.coords_to_point(5,5)
        centerLine= Line(cent_x, cent_y)

        self.play(
            ShowCreation(horizontalConnectingLine),
        )
        self.wait(.5)

        self.play(
            ShowCreation(verticalConnectingLine),
        )
        self.wait(.5)

        self.play(
            ShowCreation(point3),
            Write(point3_lab),
        )
        self.wait()

        self.play(
            ShowCreation(point5),
            Write(point5_lab),
        )
        self.wait()

        self.play(
            ShowCreation(centerLine),
        )
        self.wait(2)

        #Color stuff
        self.play(
            FadeToColor(point1, RED),
            FadeToColor(point1_lab, RED),
            FadeToColor(point2, BLUE),
            FadeToColor(point2_lab, BLUE),
            FadeToColor(point3, GREEN),
            FadeToColor(point3_lab, GREEN),
            FadeToColor(point4, ORANGE),
            FadeToColor(point4_lab, ORANGE),
            FadeToColor(point5, YELLOW),
            FadeToColor(point5_lab, YELLOW),
        )
