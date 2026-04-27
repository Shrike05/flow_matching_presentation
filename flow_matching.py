from manim import *
from manim_slides import Slide

class Presentation(Slide):
    def construct(self):
        self.slide_1()

    def slide_1(self):
        title, title_step2, title_step3 = self.create_titles()

        cat_word, cat_word2, cat_img, cats = self.create_cat()

        F, R_n, R_m, arrow2, arrows = self.create_function(cats)

        word_vec, img_vec, word_vec_brace, n_text, img_vec_brace, m_text, arrow = self.create_vec()

        vec_view = VGroup(img_vec_brace, m_text, img_vec, cat_word, word_vec_brace, n_text, arrow)
        function_view = VGroup(F, R_n, R_m, arrow2).shift(DOWN)
        fn_rn_group = VGroup(F, R_n)
        multi_arrow_group = VGroup(*arrows)
        cat_imgs_group = Group(*cats)

        cats_imgs_view = Group(cat_imgs_group, multi_arrow_group, cat_word2)

        set_shape_A = ParametricFunction(
            lambda t: np.array([
                (2 + 0.3*np.sin(3*t)) * np.cos(t),
                (2 + 0.2*np.sin(6*t)) * np.sin(t),
                0
            ]), 
            t_range=[0, TAU],
            fill_opacity=0.2
        ).set_color(GREEN)
        set_shape_A.shift(LEFT * 5)

        set_shape_C = ParametricFunction(
            lambda t: np.array([
                (1.5 + 0.3*np.sin(10*t)) * np.cos(t),
                (1.5 + 0.3*np.sin(10*t)) * np.sin(t),
                0
            ]), 
            t_range=[0, TAU],
            fill_opacity=0.2
        ).set_color(GREEN)
        set_shape_C.shift(LEFT * 5)
        set_shape_C.shift(DOWN)

        set_shape_B = ParametricFunction(
            lambda t: np.array([
                (2 + 0.45*np.sin(4*t)) * np.cos(t),
                (2 + 0.5*np.sin(2*t)) * np.sin(t),
                0
            ]), 
            t_range=[0, TAU],
            fill_opacity=0.2
        ).set_color(BLUE)
        cats_subset = ParametricFunction(
            lambda t: np.array([
                (1 + 0.2*np.sin(1*t)) * np.cos(t),
                (1 + 0.2*np.sin(1*t)) * np.sin(t),
                0
            ]), 
            t_range=[0, TAU],
            fill_opacity=0.2
        ).set_color(RED)

        set_shape_B.shift(RIGHT * 5)
        sets_group = VGroup(set_shape_A, set_shape_B)
        sets_group.shift(DOWN)
        sets_group.scale(0.7)

        cats_subset.scale(0.7)
        cats_subset.move_to(set_shape_B.get_center())
        dots = [ Dot().move_to(cats_subset.get_center() + UP*np.sin(121*i) * 0.5 + RIGHT*np.sin(3413* i) * 0.5) for (i, kitten) in enumerate(cats)]
        word_dot = Dot().move_to(set_shape_A.get_center())
        random_dots = [ Dot().move_to(set_shape_C.get_center() + UP*np.sin(43152*i) * 0.8 + RIGHT*np.sin(95431* i) * 0.8) for (i, kitten) in enumerate(cats)]

        func = Text(r"F")
        idx = ValueTracker(0.)

        inp_arrow = always_redraw(lambda: CurvedArrow(
            start_point= word_dot.get_right(),
            end_point=func.get_left(),
            angle=-TAU/8
        ))

        out_arrow = always_redraw(lambda: CurvedArrow(
            start_point=func.get_right(),
            end_point= (
                    (1 - (idx.get_value()-int(idx.get_value()))) * 
                    dots[int(idx.get_value())].get_left() + 
                    (idx.get_value()-int(idx.get_value())) * 
                    dots[int(idx.get_value()+1)%len(dots)].get_left()
                ),
            angle=TAU/8
        ))

        random_inp_arrow = always_redraw(lambda: CurvedArrow(
            start_point=(
                    (1 - (idx.get_value()-int(idx.get_value()))) * 
                    random_dots[int(idx.get_value())].get_right() + 
                    (idx.get_value()-int(idx.get_value())) * 
                    random_dots[int(idx.get_value()+1)%len(dots)].get_right()
                ),
            end_point=func.get_left(),
            angle=-TAU/8
        ))

        set_A_with_dot = VGroup(word_dot, set_shape_A)

        plane = NumberPlane(
            x_range=[-7.11, 7.11, 1], # Covers the full width
            y_range=[-4, 4, 1],       # Covers the full height
            background_line_style={
                "stroke_color": BLUE_D,
                "stroke_width": 2,
                "stroke_opacity": 0.5
            }
        )

        #Show title and move it up
        self.play(Write(title))
        self.next_slide()
        self.play(title.animate.to_edge(UP))
        self.next_slide()

        #Fade in cats
        self.play(FadeIn(cat_word), FadeIn(cat_img))
        self.next_slide()
        
        #Turn cats into vectors
        self.play(Transform(cat_word, word_vec), FadeTransform(cat_img, img_vec))
        self.next_slide()
        self.play(FadeIn(img_vec_brace), FadeIn(m_text), FadeIn(word_vec_brace), FadeIn(n_text))
        self.next_slide()
        self.play(ReplacementTransform(title, title_step2))

        #Arrow
        self.play(FadeIn(arrow))
        self.next_slide()

        #Move up the Vectors Visual
        self.play(vec_view.animate.scale(0.6).shift(UP))
        self.next_slide()

        #function
        self.play(FadeIn(function_view))
        self.next_slide()
        self.play(FadeOut(vec_view, lag_ratio=0.1))
        self.play(function_view.animate.shift(UP))
        self.next_slide()

        #wiggle R_n and R_m
        self.play(Wiggle(R_n))
        self.next_slide()
        self.play(Wiggle(R_m))
        self.next_slide()

        #cat can have several different outputs
        self.play(FadeTransform(R_m, cat_imgs_group), ReplacementTransform(arrow2, multi_arrow_group), FadeTransform(fn_rn_group, cat_word2))
        self.next_slide()

        #move up this view then create the set view whilst explaining determinism
        self.play(cats_imgs_view.animate().shift(UP).scale(0.5))
        self.play(FadeIn(sets_group))
        self.next_slide()
        
        #move the cats into points on this set view 
        self.play(FadeOut(multi_arrow_group), *[FadeTransform( cat, dot ) for (cat, dot) in zip(cats, dots)], ReplacementTransform(cat_word2, word_dot))
        self.next_slide()

        #Create the io arrows
        self.play(FadeIn(func, inp_arrow, out_arrow))
        self.next_slide()

        #Move words set up and make it smaller, then add the C distribution
        self.play(set_A_with_dot.animate.shift(UP*3).scale(0.5))
        self.play(FadeIn(set_shape_C))
        self.next_slide()

        #Create the dots in C
        self.play(*[FadeIn(dot) for dot in random_dots], FadeIn(random_inp_arrow))
        
        #Cycle through the points and show how the function maps them
        self.next_slide(loop=True)
        for i in range(1, len(random_dots)):
            self.play(idx.animate.set_value(i))
            self.wait(0.2)
        self.play(idx.animate.set_value(0))
        self.next_slide()

        #Show the distribution of the cats
        self.play(FadeIn(cats_subset))
        self.next_slide()

        #Transform title
        self.play(ReplacementTransform(title_step2, title_step3))
        self.next_slide()

        #Remove everything except the two distributions
        self.play(FadeOut(set_A_with_dot), FadeOut(inp_arrow), FadeOut(out_arrow), FadeOut(random_inp_arrow), FadeOut(func))
        self.next_slide()

        #keep only points add coordinate system
        self.play(FadeOut(set_shape_C), FadeOut(set_shape_B), FadeOut(cats_subset), FadeOut(title_step3))
        self.play(FadeIn(plane), *[dot.animate.shift(UP*2) for dot in dots])
        self.next_slide()

        #add lines connecting dots
        lines = [Line(start= r_dot.get_center(), end=o_dot.get_center(), color=GREEN, stroke_width=2 ) for (r_dot, o_dot) in zip(random_dots, dots)]
        self.play(*[FadeIn(line) for line in lines])
        self.next_slide()

        #create velocity field, good luck
        field = ArrowVectorField(lambda p: np.mean([  (dot.get_center() - p) for dot in dots], axis=0))
        self.play(*[FadeOut(line) for line in lines])
        self.play(FadeIn(field))
        self.next_slide()

        #Outro Slide
        self.play(FadeOut(field), FadeOut(plane), *[FadeOut(dot) for dot in random_dots], *[FadeOut(dot) for dot in dots])
        self.play(FadeIn(Text("Flow matching", font_size=54)))

    def gravity(p, x):
        vec = x - p
        weight = np.mean(vec)
        if weight == 0:
            return np.array([0,0,0])
        return vec/(weight**2)

    def create_titles(self):
        title = Text("Generating Images from Words", font_size=54)
        title_step2 = Text("Transforming Vectors to other Vectors", font_size=54)
        title_step3 = Text("Transforming Distribution A to Distribution B", font_size=34)

        title_step2.to_edge(UP)
        title_step3.to_edge(UP)
        return title, title_step2, title_step3

    def create_cat(self): 
        cat_word = Text("cat", font_size=64)
        cat_word.shift(LEFT * 2)
        cat_word2 = Text("cat", font_size=64)
        cat_word2.shift(LEFT * 2)

        cat_img = ImageMobject("assets/cat.jpg")
        cat_img.set_height(3)
        cat_img.shift(RIGHT * 2)
        

        cats = [ImageMobject("assets/cat.jpg") for _ in range(0, 4)]
        for i, kitten in enumerate(cats):
            kitten.set_height(0.9)
            kitten.shift(RIGHT * 2)
            kitten.shift(UP*1.5)
            kitten.shift(DOWN*i)

        return cat_word, cat_word2, cat_img, cats

    def create_function(self, cats):
        F = MathTex(r"F:")
        R_n = MathTex(r"\mathbb{R}^n")
        R_m = MathTex(r"\mathbb{R}^m")
        arrow = Arrow(start=LEFT, end=RIGHT)
        R_n.shift(LEFT*2)
        R_m.shift(RIGHT*2)
        F.next_to(R_n, LEFT)

        arrows = [Arrow(start=LEFT, end=kitten.get_left()) for kitten in cats]

        return F, R_n, R_m, arrow, arrows

    def create_vec(self):
        word_vec = Matrix([[0.21], [34.1], [8.56], ["\\vdots"]], element_alignment_corner=ORIGIN)
        word_vec.shift(LEFT * 2)
        img_vec = Matrix([[3.2], [1.1], [0.719], ["\\vdots"]], element_alignment_corner=ORIGIN)
        img_vec.shift(RIGHT * 2)

        word_vec_brace = Brace(word_vec, direction=LEFT)
        n_text = word_vec_brace.get_tex("n")

        img_vec_brace = Brace(img_vec, direction=RIGHT)
        m_text = img_vec_brace.get_tex("m")

        arrow = Arrow(start=LEFT, end=RIGHT)


        return word_vec, img_vec, word_vec_brace, n_text, img_vec_brace, m_text, arrow



# Generate Images from words
# Images and words are high dimensional vectors of different shapes
# Create a function which will take a word and create an image
# But one word can have several images so we introduce randomness through a vector sampled from a gaussian
# So even more generally we want to create a function which takes one distribution to another
# velocity field
# Diffusion models successively denoise points until they resemble gaussian noise
# Flow matching is a straight beeline to the goal
