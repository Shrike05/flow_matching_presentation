from manim import *
from manim_slides import Slide

class Presentation(Slide):
    def construct(self):
        self.slide_1()

    def slide_1(self):
        title = Text("Generating Images from Words", font_size=54)
        title_step2 = Text("Transforming Vectors to other Vectors", font_size=54)
        title_step2.to_edge(UP)

        cat_word = Text("cat", font_size=64)
        cat_word.shift(LEFT * 2)
        cat_img = ImageMobject("assets/cat.jpg")
        cat_img.set_height(3)
        cat_img.shift(RIGHT * 2)

        word_vec = Matrix([[0.21], [34.1], [8.56], ["\\vdots"]], element_alignment_corner=ORIGIN)
        word_vec.shift(LEFT * 2)
        img_vec = Matrix([[3.2], [1.1], [0.719], ["\\vdots"]], element_alignment_corner=ORIGIN)
        img_vec.shift(RIGHT * 2)

        word_vec_brace = Brace(word_vec, direction=LEFT)
        n_text = word_vec_brace.get_tex("n")

        img_vec_brace = Brace(img_vec, direction=RIGHT)
        m_text = img_vec_brace.get_tex("m")

        arrow = Arrow(start=LEFT, end=RIGHT)

        vec_view = VGroup(img_vec_brace, m_text, img_vec, cat_word, word_vec_brace, n_text, arrow)

        F = MathTex(r"F:")
        R_n = MathTex(r"\mathbb{R}^n")
        R_m = MathTex(r"\mathbb{R}^m")
        arrow2 = Arrow(start=LEFT, end=RIGHT)
        R_n.shift(LEFT*2)
        R_m.shift(RIGHT*2)
        F.next_to(R_n, LEFT)

        cat_word2 = Text("cat", font_size=64)
        cat_word2.shift(LEFT * 2)


        cats = [ImageMobject("assets/cat.jpg") for _ in range(0, 4)]
        for i, kitten in enumerate(cats):
            kitten.set_height(0.9)
            kitten.shift(RIGHT * 2)
            kitten.shift(UP*1.5)
            kitten.shift(DOWN*i)

        arrows = [Arrow(start=LEFT, end=kitten.get_left()) for kitten in cats]

        function_view = VGroup(F, R_n, R_m, arrow2).shift(DOWN)
        fn_rn_group = VGroup(F, R_n)
        multi_arrow_group = VGroup(*arrows)
        cat_imgs_group = Group(*cats)

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
        self.play(Transform(title, title_step2))

        #Arrow
        self.play(FadeIn(arrow))
        self.next_slide()

        #Move up the Vectors Visual
        self.play(vec_view.animate.scale(0.6).shift(UP))
        self.next_slide()

        #function
        self.play(FadeIn(function_view))
        self.next_slide()
        self.play(FadeOut(vec_view, lag_ratio=0.4))
        self.play(function_view.animate.shift(UP))
        self.next_slide()

        #wiggle R_n and R_m
        self.play(Wiggle(R_n))
        self.next_slide()
        self.play(Wiggle(R_m))
        self.next_slide()

        #cat can have several different outputs
        self.play(FadeTransform(R_m, cat_imgs_group), Transform(arrow2, multi_arrow_group), FadeTransform(fn_rn_group, cat_word2))

        #move up this view then create the distribution view

        #move the cats into points on this distribution view 


# Generate Images from words
# Images and words are high dimensional vectors of different shapes
# Create a function which will take a word and create an image
# But one word can have several images so we introduce randomness through a vector sampled from a gaussian
# So even more generally we want to create a function which takes one distribution to another
# velocity field
# Diffusion models successively denoise points until they resemble gaussian noise
# Flow matching is a straight beeline to the goal
