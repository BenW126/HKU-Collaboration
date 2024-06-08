from manim import * 

class IcoSolid(ThreeDScene): 
        def construct(self):
            self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)

            #opening
            title = Tex(r'The 2017 Putnam Competition', font_size = 40)
            title_1 = Tex(r'Problem A6', font_size = 35)
            subtitle = Tex(r'An Icosahedral Edge Coloring Problem', font_size = 35)
            opening = VGroup(title, title_1, subtitle).arrange(DOWN, buff=0.5)
            t0 = Tex(r'\underline{The 30 edges of an icosahedron are distinguished by labeling them $1, 2, \cdots , 30$.} \par \vspace{0.1cm} \underline{How many different ways are there to paint each edge red, yellow, or blue such} \par \vspace{0.1cm} \underline{that each of the 20 triangular faces of the icosahedron has two edges of the} \par \vspace{0.1cm} \underline{same color and a third edge of a different color?}',
                     font_size = 35, tex_environment="flushleft")
            t0[0][109:112].color = RED
            t0[0][113:119].color = YELLOW
            t0[0][122:126].color = BLUE
            t1 = Tex(r'What is an icosahedron?', font_size = 35)
            t2 = Tex(r'Recall that an icosahedron is a polyhedron with $20$ faces, $30$ edges and \par \vspace{0.1cm} $12$ vertices such that each vertex is shared by five faces. \par \vspace{0.1cm}', r'The best known one is probably the convex regular icosahedron, as one of the \par \vspace{0.1cm} Platonic solids, a convex solid where each of its $20$ faces is an identical \par \vspace{0.1cm} equilateral triangle.', 
                     font_size = 32, tex_environment="flushleft")
            self.add_fixed_in_frame_mobjects(title)
            self.play(Write(title), run_time=2)
            self.wait()
            self.add_fixed_in_frame_mobjects(title_1)
            self.play(Write(title_1), run_time=1)
            self.wait()
            self.add_fixed_in_frame_mobjects(subtitle)
            self.play(Write(subtitle), run_time=2)
            self.wait()
            self.play(FadeOut(opening))
            self.wait(2)
            self.add_fixed_in_frame_mobjects(t0)
            self.play(Write(t0), run_time=12)
            self.wait(6)
            self.play(FadeOut(t0, scale=0.5))
            self.wait(2)
            self.add_fixed_in_frame_mobjects(t1.to_edge(UP, buff=0.9))
            self.play(Write(t1))
            self.wait(2)
            self.add_fixed_in_frame_mobjects(t2[0].next_to(t1, DOWN, buff=0.4))
            self.play(Write(t2[0]), run_time=7)
            self.wait(2)
    
            self.add_fixed_in_frame_mobjects(t2[1].next_to(t2[0], DOWN, buff=0.2, aligned_edge=LEFT))
            self.play(Write(t2[1]), run_time=8)
            self.wait(2)

            #IcosahedronSolid
            ico = Icosahedron(edge_length=1.5).move_to(np.array([4,2.2,0]))
            for mob in ico.faces:
                mob.set_color(WHITE)

            self.play(DrawBorderThenFill(ico), run_time=4)
            self.play(Rotate(ico, angle=PI, rate_func=linear), run_time=5)
            self.wait()

            self.play(FadeOut(t1, t2, ico, scale=0.5))
            self.wait()


class IcoGraph(Scene): 
        def construct(self):

            t2 = Tex(r'When a coloring problem is concerned, it might be convenient to consider an \par \vspace{0.1cm} associated graph. \par \vspace{0.1cm}', r'In our case, let\rq s consider the icosahedral graph.',
                       font_size = 35, tex_environment="flushleft")
            self.play(Write(t2[0]), run_time=5)
            self.wait(2)
            self.play(Write(t2[1]), run_time=3)
            self.wait(3)
            self.play(FadeOut(t2, scale=0.5))
            self.wait()

            t3 = Tex(r'Note that any face could be put in the central position of this planar graph \par \vspace{0.1cm} due to its symmetry.', font_size = 35,
                     tex_environment="flushleft")

            t3.move_to(np.array([0,2.5,0]))
            self.play(Write(t3), run_time=5)
            self.wait()

            #IcoGraph
            vertices = [1,2,3,4,5,6,7,8,9,10,11,12]
            edges = [(1,2),(1,3),(1,6),(1,11),(1,12),(2,3),(2,4),(2,5),(2,6),(3,4),(3,11),(3,8),(5,6),(6,9),(6,12),(4,5),(4,7),(4,8),
                     (5,7),(5,9),(7,8),(7,9),(7,10),(8,10),(8,11),(9,10),(9,12),(10,11),(10,12),(11,12)]
            lt = {1:[0,5,0], 2:[0,3.33141,0], 3:[-1.69135, 1.7614,0], 4:[-1,1,0], 5:[1,1,0], 6:[1.672684, 1.78516,0], 7:[0,-0.4701131,0], 8:[-2.3365, -0.595163,0], 9:[2.365388, -0.620174,0], 10:[0,-1.44551,0]
                  , 11:[-5.48181, -2.431724,0], 12:[5.605286, -2.4080338,0]}
            ico_graph =  Graph(vertices, edges, layout=lt).scale(0.5).move_to(np.array([0,-0.8,0]))

            self.play(DrawBorderThenFill(ico_graph), run_time=2)
            self.wait(2)
            self.play(FadeOut(t3, scale=0.5))
            self.wait()

            t4 = Tex(r'To satisfy conditions in our question, what are the feasible ways of coloring?', font_size = 35).move_to(np.array([0,2.5,0]))
            self.play(Write(t4), run_time=4)
            self.wait(2)

            #example

            t6 = Tex(r'As an example, the following coloring is feasible.', font_size=35)
            t6.next_to(ico_graph, UP, buff=0.5)
            self.play(Write(t6), run_time=2)

            ec = {(1,2):{"stroke_color": RED}, (1,3):{"stroke_color": RED}, (1,6):{"stroke_color": YELLOW},
                  (1,11):{"stroke_color": RED}, (1,12):{"stroke_color": BLUE}, (2,6):{"stroke_color": RED},
                  (2,3):{"stroke_color": BLUE}, (2,4):{"stroke_color": RED}, (2,5):{"stroke_color": YELLOW},
                  (3,4):{"stroke_color": RED}, (4,5):{"stroke_color": RED}, (5,6):{"stroke_color": YELLOW},
                  (3,8):{"stroke_color": BLUE}, (4,8):{"stroke_color": BLUE}, (4,7):{"stroke_color": BLUE},
                  (5,7):{"stroke_color": BLUE}, (5,9):{"stroke_color": RED}, (6,9):{"stroke_color": YELLOW},
                  (6,12):{"stroke_color": BLUE}, (7,9):{"stroke_color": RED}, (9,12):{"stroke_color": BLUE},
                  (9,10):{"stroke_color": RED}, (7,8):{"stroke_color": RED}, (7,10):{"stroke_color": BLUE},
                  (8,10):{"stroke_color": BLUE}, (10,12):{"stroke_color": BLUE}, (10,11):{"stroke_color": RED},
                  (11,12):{"stroke_color": RED}, (3,11):{"stroke_color": BLUE}, (8,11):{"stroke_color": RED}}
            ico_graph_1 =  Graph(vertices, edges, layout=lt, edge_config=ec).scale(0.5).move_to(np.array([0,-0.8,0]))

            self.play(FadeIn(ico_graph_1))
            self.wait(3)
            self.play(FadeOut(t6, scale=0.5), FadeOut(ico_graph_1))
            self.wait()

            t7 = Tex(r'In contrast, the following coloring is NOT feasible.', font_size=35)
            t7.next_to(ico_graph, UP, buff=0.5)
            self.play(Write(t7), run_time=2)

            ec = {(1,2):{"stroke_color": BLUE}, (1,3):{"stroke_color": RED}, (1,6):{"stroke_color": BLUE},
                  (1,11):{"stroke_color": RED}, (1,12):{"stroke_color": BLUE}, (2,6):{"stroke_color": RED},
                  (2,3):{"stroke_color": BLUE}, (2,4):{"stroke_color": YELLOW}, (2,5):{"stroke_color": YELLOW},
                  (3,4):{"stroke_color": RED}, (4,5):{"stroke_color": RED}, (5,6):{"stroke_color": YELLOW},
                  (3,8):{"stroke_color": RED}, (4,8):{"stroke_color": BLUE}, (4,7):{"stroke_color": BLUE},
                  (5,7):{"stroke_color": YELLOW}, (5,9):{"stroke_color": RED}, (6,9):{"stroke_color": YELLOW},
                  (6,12):{"stroke_color": BLUE}, (7,9):{"stroke_color": YELLOW}, (9,12):{"stroke_color": BLUE},
                  (9,10):{"stroke_color": RED}, (7,8):{"stroke_color": RED}, (7,10):{"stroke_color": BLUE},
                  (8,10):{"stroke_color": BLUE}, (10,12):{"stroke_color": BLUE}, (10,11):{"stroke_color": BLUE},
                  (11,12):{"stroke_color": YELLOW}, (3,11):{"stroke_color": YELLOW}, (8,11):{"stroke_color": RED}}
            ico_graph_2 =  Graph(vertices, edges, layout=lt, edge_config=ec).scale(0.5).move_to(np.array([0,-0.8,0]))

            self.play(FadeIn(ico_graph_2))
            self.wait(3)
            self.play(FadeOut(ico_graph_2), FadeOut(t7, t4, scale=0.5))
            self.wait()

            t8 = Tex(r'Now, the problem can be rephrased to be the counting of the number of \par \vspace{0.1cm} feasible colorings of the icosahedral graph.', 
                     font_size=35, tex_environment="flushleft").next_to(ico_graph, UP, buff=0.8)
            self.play(Write(t8), run_time=5)
            self.wait(3)
            self.play(*[FadeOut(mob)for mob in self.mobjects])

class SolutionPart1(Scene): 
        def construct(self):

            t1 = Tex(r'Linear algebra could be employed to address this problem.', font_size = 35)

            self.play(Write(t1), run_time=2)
            self.wait(2)
            self.play(FadeOut(t1, scale=0.5))
            self.wait()

            t2 = Tex(r'Let $\mathbb{F}_3 = \{0,1,2\}$ be the finite field with $3$ elements, each corresponds \par \vspace{0.1cm} to “Red”, “Blue”, and “Yellow” respectively.', 
                     font_size = 35, tex_environment="flushleft", tex_to_color_map = {"Red": RED, "Blue": BLUE, "Yellow": YELLOW}).move_to(UP)
            t4 = Tex(r'Since an icosahedron has $30$ edges, a coloring of edges can be identified \par \vspace{0.1cm} as a vector in the vector space ${\mathbb{F}_3}^{30}$.',
                     font_size = 35, tex_environment="flushleft").next_to(t2, DOWN, buff=0.5, aligned_edge=LEFT)

            self.play(Write(t2), run_time=6)
            self.wait(2)
            self.play(Write(t4), run_time=4)
            self.wait(2)

            self.play(FadeOut(t2, scale=0.5), t4.animate.to_edge(UP, buff=1))
            self.wait(2)

            t5 = Tex(r'Label $20$ faces of the icosahedron $1, 2, \cdots , 20$. ', r'For the $i$-th face, define \par \vspace{0.1cm} a function $f_{i}:{\mathbb{F}_3}^{30} \longrightarrow \mathbb{F}_3$ by $f_{i}(v) =$ the sum of edges color in face $i$.', font_size = 35,
                     tex_environment="flushleft").next_to(t4, DOWN, buff=0.7, aligned_edge=LEFT)
            t5_1 = Tex(r'With these functions, we define a linear map $T : {\mathbb{F}_3}^{30} \longrightarrow {\mathbb{F}_3}^{20} $ by $$T(v)=(f_1(v), f_2(v),...,f_{20}(v)).$$', 
                       font_size = 35).next_to(t5, DOWN, buff=0.7, aligned_edge=LEFT)

            self.play(Write(t5[0]), run_time=2)
            self.wait()
            self.play(Write(t5[1]), run_time=3)
            self.wait(2)
            self.play(Write(t5_1), run_time=5)
            self.wait(3)

            self.play(FadeOut(VGroup(t4, t5), scale=0.5), t5_1.animate.to_edge(UP, buff=0.5))
            self.wait(2)

            t6 = Tex(r'For example, let $v_1 \in {\mathbb{F}_3}^{30}$ be a coloring \par \vspace{0.1cm} as shown, and $i$ be the face drawn at \par \vspace{0.1cm} the center of the icosahedral graph.', font_size = 35, 
                     tex_environment="flushleft").move_to(np.array([3,1,0]))
            self.play(Write(t6), run_time=4)

            vertices = [1,2,3,4,5,6,7,8,9,10,11,12]
            edges = [(1,2),(1,3),(1,6),(1,11),(1,12),(2,3),(2,4),(2,5),(2,6),(3,4),(3,11),(3,8),(5,6),(6,9),(6,12),(4,5),(4,7),(4,8),
                     (5,7),(5,9),(7,8),(7,9),(7,10),(8,10),(8,11),(9,10),(9,12),(10,11),(10,12),(11,12)]
            lt = {1:[0,5,0], 2:[0,3.33141,0], 3:[-1.69135, 1.7614,0], 4:[-1,1,0], 5:[1,1,0], 6:[1.672684, 1.78516,0], 7:[0,-0.4701131,0], 8:[-2.3365, -0.595163,0], 9:[2.365388, -0.620174,0], 10:[0,-1.44551,0]
                  , 11:[-5.48181, -2.431724,0], 12:[5.605286, -2.4080338,0]}
            ec = {(1,2):{"stroke_color": BLUE}, (1,3):{"stroke_color": RED}, (1,6):{"stroke_color": BLUE},
                  (1,11):{"stroke_color": RED}, (1,12):{"stroke_color": BLUE}, (2,6):{"stroke_color": RED},
                  (2,3):{"stroke_color": BLUE}, (2,4):{"stroke_color": YELLOW}, (2,5):{"stroke_color": YELLOW},
                  (3,4):{"stroke_color": RED}, (4,5):{"stroke_color": RED}, (5,6):{"stroke_color": YELLOW},
                  (3,8):{"stroke_color": RED}, (4,8):{"stroke_color": BLUE}, (4,7):{"stroke_color": BLUE},
                  (5,7):{"stroke_color": BLUE}, (5,9):{"stroke_color": RED}, (6,9):{"stroke_color": YELLOW},
                  (6,12):{"stroke_color": BLUE}, (7,9):{"stroke_color": YELLOW}, (9,12):{"stroke_color": BLUE},
                  (9,10):{"stroke_color": RED}, (7,8):{"stroke_color": RED}, (7,10):{"stroke_color": BLUE},
                  (8,10):{"stroke_color": BLUE}, (10,12):{"stroke_color": BLUE}, (10,11):{"stroke_color": BLUE},
                  (11,12):{"stroke_color": YELLOW}, (3,11):{"stroke_color": YELLOW}, (8,11):{"stroke_color": RED}}
            ico_graph =  Graph(vertices, edges, layout=lt, edge_config=ec).scale(0.5).next_to(t5_1, DOWN, buff=0.8, aligned_edge=LEFT)

            ec = {(1,2):{"stroke_color": WHITE}, (1,3):{"stroke_color": WHITE}, (1,6):{"stroke_color": WHITE},
                  (1,11):{"stroke_color": WHITE}, (1,12):{"stroke_color": WHITE}, (2,6):{"stroke_color": WHITE},
                  (2,3):{"stroke_color": WHITE}, (2,4):{"stroke_color": WHITE}, (2,5):{"stroke_color": WHITE},
                  (3,4):{"stroke_color": WHITE}, (4,5):{"stroke_color": RED}, (5,6):{"stroke_color": WHITE},
                  (3,8):{"stroke_color": WHITE}, (4,8):{"stroke_color": WHITE}, (4,7):{"stroke_color": BLUE},
                  (5,7):{"stroke_color": BLUE}, (5,9):{"stroke_color": WHITE}, (6,9):{"stroke_color": WHITE},
                  (6,12):{"stroke_color": WHITE}, (7,9):{"stroke_color": WHITE}, (9,12):{"stroke_color": WHITE},
                  (9,10):{"stroke_color": WHITE}, (7,8):{"stroke_color": WHITE}, (7,10):{"stroke_color": WHITE},
                  (8,10):{"stroke_color": WHITE}, (10,12):{"stroke_color": WHITE}, (10,11):{"stroke_color": WHITE},
                  (11,12):{"stroke_color": WHITE}, (3,11):{"stroke_color": WHITE}, (8,11):{"stroke_color": WHITE}}

            ico_graph_c =  Graph(vertices, edges, layout=lt, edge_config=ec).scale(0.5).next_to(t5_1, DOWN, buff=0.8, aligned_edge=LEFT)

            t7 = MathTex(r'i', font_size = 35).move_to(ico_graph.get_center()+DOWN*0.4)

            labels = MathTex(r'v_1', r'v_2', r'v_3', r'v_4', font_size=35)

            labels[0].next_to(ico_graph, UP, buff=0.1)

            self.play(DrawBorderThenFill(ico_graph), FadeIn(t7, labels[0]))
            self.wait(2)

            vertices_t = [1,2,3]
            edges_t = [(1,2), (2,3), (1,3)]
            lt_t = {1:[-1,1,0], 2:[1,1,0], 3:[0,-0.4701131,0]} 
            ec_t = {(1,2):{"stroke_color": RED}, (1,3):{"stroke_color": BLUE}, (2,3):{"stroke_color": BLUE}}

            tri = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t).scale(0.5).next_to(t6, DOWN, buff=0.5)
            t7_copy = t7.copy().move_to(tri.get_center()+UP*0.1)
            tri_labels = Tex(r'1', r'1' ,r'0', font_size = 35)

            tri_labels[2].next_to(t7, UP, buff=0.2)
            tri_labels[0].move_to(t7.get_center()+np.array([-0.4,-0.2,0]))
            tri_labels[1].move_to(t7.get_center()+np.array([0.4,-0.2,0]))

            #self.play(FadeIn(VGroup(tri, t7_copy), target_position=ico_graph.get_center()+DOWN*0.5), FadeOut(t6, scale=0.5))
            self.play(FadeOut(t6, scale=0.5))
            self.wait()

            t8 = Tex(r'Then $f_i(v_1) = 1 + 1 + 0 = 2 \in \mathbb{F}_3$ \par \vspace{0.1cm} since two edges are in blue and one \par \vspace{0.1cm} in red in face $i$.', font_size = 35, 
                     tex_environment="flushleft").move_to(np.array([3,1,0]))
            self.play(FadeIn(tri_labels))
            self.play(FadeIn(ico_graph_c), FadeOut(ico_graph)) 
            self.play(Write(t8), run_time=4)
            self.wait(2)

            ec = {(1,2):{"stroke_color": YELLOW}, (1,3):{"stroke_color": RED}, (1,6):{"stroke_color": BLUE},
                  (1,11):{"stroke_color": RED}, (1,12):{"stroke_color": RED}, (2,6):{"stroke_color": BLUE},
                  (2,3):{"stroke_color": BLUE}, (2,4):{"stroke_color": YELLOW}, (2,5):{"stroke_color": YELLOW},
                  (3,4):{"stroke_color": RED}, (4,5):{"stroke_color": YELLOW}, (5,6):{"stroke_color": YELLOW},
                  (3,8):{"stroke_color": YELLOW}, (4,8):{"stroke_color": BLUE}, (4,7):{"stroke_color": RED},
                  (5,7):{"stroke_color": YELLOW}, (5,9):{"stroke_color": RED}, (6,9):{"stroke_color": YELLOW},
                  (6,12):{"stroke_color": YELLOW}, (7,9):{"stroke_color": RED}, (9,12):{"stroke_color": RED},
                  (9,10):{"stroke_color": RED}, (7,8):{"stroke_color": RED}, (7,10):{"stroke_color": BLUE},
                  (8,10):{"stroke_color": BLUE}, (10,12):{"stroke_color": BLUE}, (10,11):{"stroke_color": RED},
                  (11,12):{"stroke_color": BLUE}, (3,11):{"stroke_color": YELLOW}, (8,11):{"stroke_color": RED}}
            ico_graph_1 =  Graph(vertices, edges, layout=lt, edge_config=ec).scale(0.5).next_to(t5_1, DOWN, buff=0.8, aligned_edge=LEFT)
            labels[1].next_to(ico_graph_1, UP, buff=0.1)

            ec = {(1,2):{"stroke_color": WHITE}, (1,3):{"stroke_color": WHITE}, (1,6):{"stroke_color": WHITE},
                  (1,11):{"stroke_color": WHITE}, (1,12):{"stroke_color": WHITE}, (2,6):{"stroke_color": WHITE},
                  (2,3):{"stroke_color": WHITE}, (2,4):{"stroke_color": WHITE}, (2,5):{"stroke_color": WHITE},
                  (3,4):{"stroke_color": WHITE}, (4,5):{"stroke_color": YELLOW}, (5,6):{"stroke_color": WHITE},
                  (3,8):{"stroke_color": WHITE}, (4,8):{"stroke_color": WHITE}, (4,7):{"stroke_color": RED},
                  (5,7):{"stroke_color": YELLOW}, (5,9):{"stroke_color": WHITE}, (6,9):{"stroke_color": WHITE},
                  (6,12):{"stroke_color": WHITE}, (7,9):{"stroke_color": WHITE}, (9,12):{"stroke_color": WHITE},
                  (9,10):{"stroke_color": WHITE}, (7,8):{"stroke_color": WHITE}, (7,10):{"stroke_color": WHITE},
                  (8,10):{"stroke_color": WHITE}, (10,12):{"stroke_color": WHITE}, (10,11):{"stroke_color": WHITE},
                  (11,12):{"stroke_color": WHITE}, (3,11):{"stroke_color": WHITE}, (8,11):{"stroke_color": WHITE}}
            ico_graph_1_c =  Graph(vertices, edges, layout=lt, edge_config=ec).scale(0.5).next_to(t5_1, DOWN, buff=0.8, aligned_edge=LEFT)

            t9 = Tex(r'Let\rq s look at one more example, \par \vspace{0.1cm} $v_2 \in {\mathbb{F}_3}^{30}, f_i(v_2) = 2 + 2 + 0 = 1 \in \mathbb{F}_3.$', font_size = 35,
                     tex_environment="flushleft").move_to(np.array([3,1,0]))

            self.play(FadeOut(VGroup(ico_graph, ico_graph_c ,labels[0], t7, tri_labels), scale=0.5), 
                      FadeOut(t8, scale=0.5))
            self.wait()
            self.play(FadeIn(VGroup(ico_graph_1, labels[1], t7), scale=0.5))
            self.wait()

            ec_t = {(1,2):{"stroke_color": YELLOW}, (1,3):{"stroke_color": RED}, (2,3):{"stroke_color": YELLOW}}
            tri = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t).scale(0.5).move_to(tri.get_center())

            tri_labels = Tex(r'0', r'2' ,r'2', font_size = 35)
            tri_labels[2].next_to(t7, UP, buff=0.2)
            tri_labels[0].move_to(t7.get_center()+np.array([-0.4,-0.2,0]))
            tri_labels[1].move_to(t7.get_center()+np.array([0.4,-0.2,0]))

            #self.play(FadeIn(VGroup(tri, t7_copy), target_position=ico_graph.get_center()+DOWN*0.5))
            self.play(Write(t9), run_time=4)
            self.play(FadeOut(ico_graph_1), FadeIn(ico_graph_1_c, tri_labels))
            self.wait(2)
            self.play(FadeOut(VGroup(ico_graph_1_c, labels[1], t7, tri_labels), scale=0.5), 
                      FadeOut(t9, scale=0.5))
            self.wait()

            t10 = Tex(r'Notably, the condition that face $i$ has two edges of the same color and \par \vspace{0.1cm} a third edge of a different color is just equivalent to \par \vspace{0.1cm}', r'$$f_i(v) = 1 \mbox{ or } 2 \neq 0.$$',
                      font_size = 35, tex_environment="flushleft").next_to(t5_1, DOWN, buff=0.7, aligned_edge=LEFT)
            t10[1].next_to(t10[0], DOWN, buff=0.3)
            t10[1][0:-1].color = YELLOW
            self.play(Write(t10), run_time=5)
            self.wait(2)

            t11 = Tex(r'Let\rq s look into some more cases:', font_size=35,
                      tex_environment="flushleft").next_to(t10, DOWN, buff=0.7, aligned_edge=LEFT)
            self.play(Write(t11), run_time=2)
            self.wait(2)
            self.play(FadeOut(VGroup(t5_1, t10), scale=0.5), t11.animate.to_edge(UP, buff=1))
            self.wait()

            ec = {(1,2):{"stroke_color": YELLOW}, (1,3):{"stroke_color": RED}, (1,6):{"stroke_color": BLUE},
                  (1,11):{"stroke_color": RED}, (1,12):{"stroke_color": RED}, (2,6):{"stroke_color": BLUE},
                  (2,3):{"stroke_color": BLUE}, (2,4):{"stroke_color": YELLOW}, (2,5):{"stroke_color": YELLOW},
                  (3,4):{"stroke_color": RED}, (4,5):{"stroke_color": YELLOW}, (5,6):{"stroke_color": YELLOW},
                  (3,8):{"stroke_color": YELLOW}, (4,8):{"stroke_color": BLUE}, (4,7):{"stroke_color": YELLOW},
                  (5,7):{"stroke_color": YELLOW}, (5,9):{"stroke_color": RED}, (6,9):{"stroke_color": YELLOW},
                  (6,12):{"stroke_color": YELLOW}, (7,9):{"stroke_color": RED}, (9,12):{"stroke_color": RED},
                  (9,10):{"stroke_color": RED}, (7,8):{"stroke_color": RED}, (7,10):{"stroke_color": BLUE},
                  (8,10):{"stroke_color": BLUE}, (10,12):{"stroke_color": BLUE}, (10,11):{"stroke_color": RED},
                  (11,12):{"stroke_color": BLUE}, (3,11):{"stroke_color": YELLOW}, (8,11):{"stroke_color": RED}}
            
            ico_graph_2 =  Graph(vertices, edges, layout=lt, edge_config=ec).scale(0.5).next_to(t5_1, DOWN, buff=0.8, aligned_edge=LEFT)
            labels[2].next_to(ico_graph_2, UP, buff=0.1)

            ec = {(1,2):{"stroke_color": WHITE}, (1,3):{"stroke_color": WHITE}, (1,6):{"stroke_color": WHITE},
                  (1,11):{"stroke_color": WHITE}, (1,12):{"stroke_color": WHITE}, (2,6):{"stroke_color": WHITE},
                  (2,3):{"stroke_color": WHITE}, (2,4):{"stroke_color": WHITE}, (2,5):{"stroke_color": WHITE},
                  (3,4):{"stroke_color": WHITE}, (4,5):{"stroke_color": YELLOW}, (5,6):{"stroke_color": WHITE},
                  (3,8):{"stroke_color": WHITE}, (4,8):{"stroke_color": WHITE}, (4,7):{"stroke_color": YELLOW},
                  (5,7):{"stroke_color": YELLOW}, (5,9):{"stroke_color": WHITE}, (6,9):{"stroke_color": WHITE},
                  (6,12):{"stroke_color": WHITE}, (7,9):{"stroke_color": WHITE}, (9,12):{"stroke_color": WHITE},
                  (9,10):{"stroke_color": WHITE}, (7,8):{"stroke_color": WHITE}, (7,10):{"stroke_color": WHITE},
                  (8,10):{"stroke_color": WHITE}, (10,12):{"stroke_color": WHITE}, (10,11):{"stroke_color": WHITE},
                  (11,12):{"stroke_color": WHITE}, (3,11):{"stroke_color": WHITE}, (8,11):{"stroke_color": WHITE}}
            ico_graph_2_c =  Graph(vertices, edges, layout=lt, edge_config=ec).scale(0.5).next_to(t5_1, DOWN, buff=0.8, aligned_edge=LEFT)

            t12 = Tex(r'An example when face $i$ has three \par \vspace{0.1cm} edges of the same color, $v_3 \in {\mathbb{F}_3}^{30}$, \par \vspace{0.1cm} $f_i(v_3) = 2 + 2 + 2 = 0 \in \mathbb{F}_3.$', 
                      font_size = 35, tex_environment="flushleft").move_to(np.array([3,1,0]))
            
            ec_t = {(1,2):{"stroke_color": YELLOW}, (1,3):{"stroke_color": YELLOW}, (2,3):{"stroke_color": YELLOW}}
            tri = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t).scale(0.5).move_to(tri.get_center())

            tri_labels = Tex(r'2', r'2' ,r'2', font_size = 35)
            tri_labels[2].next_to(t7, UP, buff=0.2)
            tri_labels[0].move_to(t7.get_center()+np.array([-0.4,-0.2,0]))
            tri_labels[1].move_to(t7.get_center()+np.array([0.4,-0.2,0]))


            self.play(FadeIn(VGroup(ico_graph_2, labels[2], t7), scale=0.5))
            #self.play(FadeIn(VGroup(tri, t7_copy), target_position=ico_graph.get_center()+DOWN*0.5))
            self.play(Write(t12), run_time=5)
            self.play(FadeOut(ico_graph_2), FadeIn(ico_graph_2_c, tri_labels))
            self.wait(2)

            self.play(FadeOut(VGroup(ico_graph_2_c, labels[2], t7, tri_labels), scale=0.5), 
                      FadeOut(t12, scale=0.5))
            self.wait(2)

            ec = {(1,2):{"stroke_color": YELLOW}, (1,3):{"stroke_color": RED}, (1,6):{"stroke_color": YELLOW},
                  (1,11):{"stroke_color": YELLOW}, (1,12):{"stroke_color": RED}, (2,6):{"stroke_color": BLUE},
                  (2,3):{"stroke_color": BLUE}, (2,4):{"stroke_color": YELLOW}, (2,5):{"stroke_color": YELLOW},
                  (3,4):{"stroke_color": RED}, (4,5):{"stroke_color": YELLOW}, (5,6):{"stroke_color": RED},
                  (3,8):{"stroke_color": YELLOW}, (4,8):{"stroke_color": BLUE}, (4,7):{"stroke_color": BLUE},
                  (5,7):{"stroke_color": RED}, (5,9):{"stroke_color": RED}, (6,9):{"stroke_color": YELLOW},
                  (6,12):{"stroke_color": YELLOW}, (7,9):{"stroke_color": RED}, (9,12):{"stroke_color": RED},
                  (9,10):{"stroke_color": BLUE}, (7,8):{"stroke_color": RED}, (7,10):{"stroke_color": BLUE},
                  (8,10):{"stroke_color": BLUE}, (10,12):{"stroke_color": BLUE}, (10,11):{"stroke_color": RED},
                  (11,12):{"stroke_color": YELLOW}, (3,11):{"stroke_color": YELLOW}, (8,11):{"stroke_color": YELLOW}}
            
            ico_graph_3 =  Graph(vertices, edges, layout=lt, edge_config=ec).scale(0.5).next_to(t5_1, DOWN, buff=0.8, aligned_edge=LEFT)
            labels[3].next_to(ico_graph_3, UP, buff=0.1)

            ec = {(1,2):{"stroke_color": WHITE}, (1,3):{"stroke_color": WHITE}, (1,6):{"stroke_color": WHITE},
                  (1,11):{"stroke_color": WHITE}, (1,12):{"stroke_color": WHITE}, (2,6):{"stroke_color": WHITE},
                  (2,3):{"stroke_color": WHITE}, (2,4):{"stroke_color": WHITE}, (2,5):{"stroke_color": WHITE},
                  (3,4):{"stroke_color": WHITE}, (4,5):{"stroke_color": YELLOW}, (5,6):{"stroke_color": WHITE},
                  (3,8):{"stroke_color": WHITE}, (4,8):{"stroke_color": WHITE}, (4,7):{"stroke_color": BLUE},
                  (5,7):{"stroke_color": RED}, (5,9):{"stroke_color": WHITE}, (6,9):{"stroke_color": WHITE},
                  (6,12):{"stroke_color": WHITE}, (7,9):{"stroke_color": WHITE}, (9,12):{"stroke_color": WHITE},
                  (9,10):{"stroke_color": WHITE}, (7,8):{"stroke_color": WHITE}, (7,10):{"stroke_color": WHITE},
                  (8,10):{"stroke_color": WHITE}, (10,12):{"stroke_color": WHITE}, (10,11):{"stroke_color": WHITE},
                  (11,12):{"stroke_color": WHITE}, (3,11):{"stroke_color": WHITE}, (8,11):{"stroke_color": WHITE}}
            ico_graph_3_c =  Graph(vertices, edges, layout=lt, edge_config=ec).scale(0.5).next_to(t5_1, DOWN, buff=0.8, aligned_edge=LEFT)

            t13 = Tex(r'An example when face $i$ has three \par \vspace{0.1cm} edges of all different colors, $v_4 \in {\mathbb{F}_3}^{30}$, \par \vspace{0.1cm} $f_i(v_4) = 0 + 1 + 2 = 0 \in \mathbb{F}_3.$', 
                      font_size = 35, tex_environment="flushleft").move_to(np.array([3,1,0]))
            ec_t = {(1,2):{"stroke_color": YELLOW}, (1,3):{"stroke_color": BLUE}, (2,3):{"stroke_color": RED}}
            tri = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t).scale(0.5).move_to(tri.get_center())

            tri_labels = Tex(r'1', r'0' ,r'2', font_size = 35)
            tri_labels[2].next_to(t7, UP, buff=0.2)
            tri_labels[0].move_to(t7.get_center()+np.array([-0.4,-0.2,0]))
            tri_labels[1].move_to(t7.get_center()+np.array([0.4,-0.2,0]))

            self.play(FadeIn(VGroup(ico_graph_3, labels[3], t7), scale=0.5))
            self.play(Write(t13), run_time=4)
            #self.play(FadeIn(VGroup(tri, t7_copy), target_position=ico_graph.get_center()+DOWN*0.5))
            self.play(FadeIn(tri_labels, ico_graph_3_c), FadeOut(ico_graph_3))
            self.wait(2)

            self.play(FadeOut(VGroup(ico_graph_3, ico_graph_3_c, labels[3], t7, tri_labels), scale=0.5), 
                      FadeOut(t11, scale=0.5),
                      FadeOut(t13, scale=0.5))
            self.wait(2)

            t14 = Tex(r'We check and summarize all cases in the following table:',font_size = 35, tex_environment="flushleft")
            self.play(Write(t14[0]), run_time=3)
            self.play(t14.animate.to_edge(UP, buff=1.5))
            self.wait(2)

            vertices_t = [1,2,3]
            edges_t = [(1,2), (2,3), (1,3)]
            lt_t = {1:[-1,1,0], 2:[1,1,0], 3:[0,-0.4701131,0]} 

            ec_t_1 = {(1,2):{"stroke_color": RED}, (1,3):{"stroke_color": BLUE}, (2,3):{"stroke_color": BLUE}}
            tri_1 = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t_1).scale(0.5)

            ec_t_2 = {(1,2):{"stroke_color": YELLOW}, (1,3):{"stroke_color": BLUE}, (2,3):{"stroke_color": BLUE}}
            tri_2 = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t_2).scale(0.5)

            ec_t_3 = {(1,2):{"stroke_color": RED}, (1,3):{"stroke_color": YELLOW}, (2,3):{"stroke_color": YELLOW}}
            tri_3 = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t_3).scale(0.5)

            ec_t_4 = {(1,2):{"stroke_color": BLUE}, (1,3):{"stroke_color": YELLOW}, (2,3):{"stroke_color": YELLOW}}
            tri_4 = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t_4).scale(0.5)

            ec_t_5 = {(1,2):{"stroke_color": YELLOW}, (1,3):{"stroke_color": RED}, (2,3):{"stroke_color": RED}}
            tri_5 = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t_5).scale(0.5)

            ec_t_6 = {(1,2):{"stroke_color": BLUE}, (1,3):{"stroke_color": RED}, (2,3):{"stroke_color": RED}}
            tri_6 = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t_6).scale(0.5)

            ec_t_7 = {(1,2):{"stroke_color": BLUE}, (1,3):{"stroke_color": BLUE}, (2,3):{"stroke_color": BLUE}}
            tri_7 = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t_7).scale(0.5)

            ec_t_8 = {(1,2):{"stroke_color": YELLOW}, (1,3):{"stroke_color": YELLOW}, (2,3):{"stroke_color": YELLOW}}
            tri_8 = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t_8).scale(0.5)

            ec_t_9 = {(1,2):{"stroke_color": RED}, (1,3):{"stroke_color": RED}, (2,3):{"stroke_color": RED}}
            tri_9 = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t_9).scale(0.5)

            ec_t_10 = {(1,2):{"stroke_color": BLUE}, (1,3):{"stroke_color": RED}, (2,3):{"stroke_color": YELLOW}}
            tri_10 = Graph(vertices_t, edges_t, layout=lt_t, edge_config=ec_t_10).scale(0.5)


            tri_table = MobjectTable([[tri_1, tri_2, tri_3, tri_4, tri_5, tri_6, tri_7, tri_8, tri_9, tri_10],
                                      [Tex(r'2'), Tex(r'1'), Tex(r'1'), Tex(r'2'), Tex(r'2'), Tex(r'1'), Tex(r'0'), Tex(r'0'), Tex(r'0'), Tex(r'0')]], 
                                     h_buff=0.7,
                                     row_labels=[Tex(r'Face $i$'), MathTex(r'f_i(v)')],
                                     include_outer_lines=True).scale(0.7).next_to(t14, DOWN, buff=0.7)

            self.play(Create(tri_table), run_time=5)
            self.wait(3)

            self.play(FadeOut(t14, scale=0.5), tri_table.animate.to_edge(UP, buff=1.5))

            t15 = Tex(r'Since face $i$ has two edges of the same color and a third edge of a different \par \vspace{0.1cm} color is equivalent to $f_i(v) = 1 \mbox{ or } 2$, the number of feasible coloring is just', r'$$|T^{-1}(\{1,2\}^{20})|.$$',
                      font_size = 35, tex_environment="flushleft").next_to(tri_table, DOWN, buff=0.7)
            t15[1].next_to(t15[0], DOWN, buff=0.3)
            t15[1][0:-1].color = YELLOW
            rec = SurroundingRectangle(tri_table.get_columns()[1:7], color=TEAL_E, buff=0.1)
            self.play(Create(rec))
            self.play(Write(t15), run_time=8)
            self.wait(3)
            self.play(*[FadeOut(mob)for mob in self.mobjects])
            self.wait()

'''
tc=Tex(r'Discussed as a warm-up question in Wong's School gathering')
tc=Tex(r'Attendees of the gathering: ')
tc=Tex(r'Video production: ')
                 
'''

class SolutionPart2(Scene): 
        def construct(self):
            t1 = Tex(r'Now, how do we compute $|T^{-1}(\{1,2\}^{20})|$?', font_size=35)

            self.play(Write(t1), run_time=2)
            self.wait(2)
            self.play(FadeOut(t1, scale=0.5))


            t2 = Tex(r'First, we shall see that $T : {\mathbb{F}_3}^{30} \longrightarrow {\mathbb{F}_3}^{20} $ is surjective.',
                       font_size=35)
            t3 = Tex(r'To demonstrate the surjectivity of $T$, we could show for a standard \par \vspace{0.1cm} basis of ${\mathbb{F}_3}^{20}$, each vector has a non-empty preimage.',
                       font_size = 35, tex_environment="flushleft")
            t4 = Tex(r'It can be done by finding an edge coloring for a given face such \par \vspace{0.1cm} that the edge-color-sum in that face is $1$, while the edge-color-sum \par \vspace{0.1cm} in other faces are all $0$.',
                       font_size = 35, tex_environment="flushleft")
            t5 = Tex(r'By transitive icosahedral symmetry, it suffices to do so for just one face.',
                       font_size = 35)
            g = VGroup(t2, t3, t4, t5).arrange(DOWN, buff=0.7, center=False, aligned_edge = LEFT).move_to(ORIGIN)

            self.play(Write(t2), run_time=3)
            self.wait(2)
            self.play(Write(t3), run_time=5)
            self.wait(3)
            self.play(Write(t4), run_time=6)
            self.wait(3)
            self.play(Write(t5), run_time=3)
            self.wait(3)

            self.play(FadeOut(t2, t3, t4, scale=0.5), t5.animate.to_edge(UP, buff=1))
            self.wait(2)

            t6 = Tex(r'Here is a specific edge coloring in $\mathbb{F}_3^{30}$ that would be mapped by $T$ to a \par \vspace{0.1cm} standard basis vector in $\mathbb{F}_3^{20}$ as desired:', 
                     font_size=35, tex_environment="flushleft").next_to(t5, DOWN, buff=0.7, aligned_edge=LEFT)

            self.play(Write(t6), run_time=5)

            vertices = [1,2,3,4,5,6,7,8,9,10,11,12]
            edges = [(1,2),(1,3),(1,6),(1,11),(1,12),(2,3),(2,4),(2,5),(2,6),(3,4),(3,11),(3,8),(5,6),(6,9),(6,12),(4,5),(4,7),(4,8),
                     (5,7),(5,9),(7,8),(7,9),(7,10),(8,10),(8,11),(9,10),(9,12),(10,11),(10,12),(11,12)]
            lt = {1:[0,5,0], 2:[0,3.33141,0], 3:[-1.69135, 1.7614,0], 4:[-1,1,0], 5:[1,1,0], 6:[1.672684, 1.78516,0], 7:[0,-0.4701131,0], 8:[-2.3365, -0.595163,0], 9:[2.365388, -0.620174,0], 10:[0,-1.44551,0]
                  , 11:[-5.48181, -2.431724,0], 12:[5.605286, -2.4080338,0]}
            ec = {(1,2):{"stroke_color": RED}, (1,3):{"stroke_color": RED}, (1,6):{"stroke_color": BLUE},
                  (1,11):{"stroke_color": RED}, (1,12):{"stroke_color": RED}, (2,6):{"stroke_color": YELLOW},
                  (2,3):{"stroke_color": RED}, (2,4):{"stroke_color": RED}, (2,5):{"stroke_color": RED},
                  (3,4):{"stroke_color": RED}, (4,5):{"stroke_color": RED}, (5,6):{"stroke_color": BLUE},
                  (3,8):{"stroke_color": RED}, (4,8):{"stroke_color": RED}, (4,7):{"stroke_color": RED},
                  (5,7):{"stroke_color": BLUE}, (5,9):{"stroke_color": BLUE}, (6,9):{"stroke_color": BLUE},
                  (6,12):{"stroke_color": YELLOW}, (7,9):{"stroke_color": BLUE}, (9,12):{"stroke_color": RED},
                  (9,10):{"stroke_color": BLUE}, (7,8):{"stroke_color": RED}, (7,10):{"stroke_color": BLUE},
                  (8,10):{"stroke_color": YELLOW}, (10,12):{"stroke_color": YELLOW}, (10,11):{"stroke_color": BLUE},
                  (11,12):{"stroke_color": RED}, (3,11):{"stroke_color": RED}, (8,11):{"stroke_color": RED}}
            ico_graph =  Graph(vertices, edges, layout=lt, edge_config=ec).scale(0.5).next_to(t6, DOWN, buff=0.5)

            self.play(DrawBorderThenFill(ico_graph))
            self.wait(3)

            self.play(FadeOut(t5, t6, ico_graph, scale=0.5))
            self.wait()

            t7 = Tex(r'By the first isomorphism theorem and the surjectivity of $T : {\mathbb{F}_3}^{30} \longrightarrow {\mathbb{F}_3}^{20} $, \par \vspace{0.1cm} we have', r'$${\mathbb{F}_3}^{30}/\ker(T) \cong {\mathbb{F}_3}^{20}.$$', font_size=35,
                     tex_environment="flushleft").move_to(t6.get_center())
            #t7[0][63:-1].color = YELLOW

            t8 = Tex(r'Hence, the required cardinality $|T^{-1}(\{1,2\}^{20})| = |\{1,2\}^{20}| \cdot |\ker(T)|$ ', r'where \par \vspace{0.1cm} $|\ker(T)| = \frac{|{\mathbb{F}_{3}}^{30}|}{|{\mathbb{F}_{3}}^{20}|} = 3^{10}.$ ', r'That is, $|T^{-1}(\{1,2\}^{20})| = 2^{20} \cdot 3^{10}$.',
                     font_size=35, tex_environment="flushleft").next_to(t1, DOWN, buff=0.7).next_to(t7, DOWN, buff=0.7, aligned_edge=LEFT)
            self.play(Write(t7[0]), run_time=3)
            self.wait()
            self.play(Write(t7[1]), run_time=2)
            self.wait(3)
            self.play(Write(t8[0][:28]), run_time=2)
            self.play(FadeIn(t8[0][28:42], shift=UP))
            self.play(Write(t8[0][42:]), run_time=2)
            self.wait(2)
            self.play(Write(t8[1]), run_time=3)
            self.wait(2)
            self.play(Write(t8[2]), run_time=3)
            self.wait(3)

            t9 = Tex(r'The answer is now $2^{20} \cdot 3^{10} = 61,917,364,224.$', font_size = 40)
            #t9[0][22:-1].color = YELLOW
            self.play(FadeOut(t7, t8, scale=0.5))
            self.wait()
            self.play(GrowFromCenter(t9))
            self.wait(3)
            self.play(*[FadeOut(mob)for mob in self.mobjects])
            self.wait()


class Ending(Scene): 
        def construct(self):
              tc_1 = Tex(r'Discussed as a warm-up exercise in Wong\rq s School summer gathering in 2023:', font_size = 30)
              tc_2 = Tex(r'Early Attendees: A.M.W. Hui, H.F. Law, Y.K. Tai, P.P.W. Wong;', font_size = 30)
              tc_3 = Tex(r'More Attendees: K.Y. Chan, Y.M. Chan.', font_size = 30)
              tc_4 = Tex(r'Video Production: Ben Wong Kin Fung.', font_size = 30)
              tc_5 = Tex(r'Financial Support for Production: Innovation and Technology Commission.', font_size = 30)

              g = VGroup(tc_1, tc_2, tc_3, tc_4, tc_5).arrange(DOWN, buff=0.7, center=False, aligned_edge = LEFT).move_to(ORIGIN)

              self.play(FadeIn(tc_1, shift=UP), run_time=2)
              self.wait()
              self.play(FadeIn(tc_2, shift=UP), run_time=2)
              self.wait()
              self.play(FadeIn(tc_3, shift=UP), run_time=2)
              self.wait()
              self.play(FadeIn(tc_4, shift=UP), run_time=2)
              self.wait()
              self.play(FadeIn(tc_5, shift=UP), run_time=2)
              self.wait()
              self.play(*[FadeOut(mob)for mob in self.mobjects])
              self.wait()
