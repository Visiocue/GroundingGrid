from manimlib import *
Mobject
import numpy as np

# To watch one of these scenes, run the following:
# manimgl example_scenes.py OpeningManimExample
# Use -s to skip to the end and just save the final frame
# Use -w to write the animation to a file
# Use -o to write it to a file and open it once done
# Use -n <number> to skip ahead to the n'th animation of a scene.

from manimlib import TexText as Tex


class BaseManim(Scene):
    def construct(self):
        # Header text
        header_text = Tex("GroundingGrid prompting\\\\Visiocue GmbH, Filip Dimitrovski", color=YELLOW)
        header_text.to_edge(DOWN + RIGHT, buff=0.5)

        # First prompt question text
        question_text = Tex("Naive visual: Where is the square on this image?")
        question_text.to_edge(UP, buff=0.5)

        # Create a circle and square
        circle = Circle().set_fill(PINK, opacity=0.5)
        square = Square().set_fill(BLUE, opacity=0.5)

        # Position square next to circle
        square.next_to(circle, RIGHT, buff=0.5)

        # Group circle and square together
        image_group = VGroup(circle, square).scale(0.8)
        image_group.to_edge(LEFT, buff=1)

        # Add a surrounding rectangle for the image
        image_border = SurroundingRectangle(image_group, color=WHITE)
        image_label = Tex("Image").next_to(image_group, UP)

        # Curved arrow pointing to the LLM output
        arrow = CurvedArrow(start_point=2 * LEFT, end_point=2 * RIGHT, radius=-5)
        arrow.next_to(image_border, RIGHT, buff=0.5)

        # LLM output box
        llm_box = RoundedRectangle(corner_radius=0.2, width=4, height=2, color=YELLOW)
        llm_box.next_to(arrow, RIGHT, buff=0.5)
        llm_text1 = Tex("LLM Output:\\\\Next to the circle.").move_to(llm_box.get_center())

        # Add elements to the scene
        self.play(FadeIn(header_text))
        self.play(FadeIn(question_text))
        self.play(ShowCreation(image_group), ShowCreation(image_border), FadeIn(image_label))
        self.wait(0.5)

        # Show arrow and LLM output
        self.play(ShowCreation(arrow))
        self.play(FadeIn(llm_box), Write(llm_text1))
        self.wait(1)

        # Second prompt

        question_text2 = TexText("Bbox prompt: Where is the blue square as a bounding box \\\\ $[y_{\\text{min}}, x_{\\text{min}}, y_{\\text{max}}, x_{\\text{max}}]$")
        question_text2.to_edge(UP, buff=0.5)
        llm_text55 = Tex("LLM Output:\\\\").move_to(llm_box.get_center())
        llm_text2 = TexText("LLM Output:\\\\Bounding box:\\\\$[0, 0, 0.2, 0.3]$").move_to(llm_box.get_center())

        # Animate new prompt and response
        
        self.play(Transform(question_text, question_text2))
        self.play(ShowCreation(llm_text55), FadeOut(llm_text1))
        self.wait(0.5)
        self.play(FadeOut(llm_text55), ShowCreation(llm_text2))
        
        
        grid_size = 10
        
        cell_size = 0.3
        grid = VGroup()

        for i in range(grid_size):
            for j in range(grid_size):
                # Create each grid cell
                cell = Square(side_length=cell_size)
                cell.move_to(image_group.get_center() + (j - 4.5) * RIGHT * cell_size + (i - 4.5) * DOWN * cell_size)
                if 51 < i < 54 and 61 < j < 64:
                    ss = cell.set_fill(RED, opacity=0.5)
                # Numbering the cell
                num = i * grid_size + j + 1
                number = Text(str(num), font_size=18).move_to(cell.get_center())

                # Adding coordinates (i, j) as overlay text
                coordinates = Text(f"({i},{j})", font_size=12).next_to(cell, DOWN, buff=0.05)

                # Add cell, number, and coordinates to the grid
                grid.add(cell, number, coordinates)

        # Bounding box highlight
        bounding_box = SurroundingRectangle(square, color=RED)
        self.play(ShowCreation(bounding_box))
        self.wait(1)
        self.play(FadeOut(bounding_box))
        self.wait(2.3)

        # Third prompt
        question_text3 = TexText("Grid prompt:\\\\Which numbers on the grid overlay contain the\\\\")
        question_text3.to_edge(UP, buff=0.5)
        qq5 = TexText("blue square", color=TEAL)
        question_text3.add(qq5)
        qq5.move_to(question_text3.get_center())


        # question_text3.set_color_by_tex("")
        # question_text3.next_to(header_text, DOWN, buff=0.5)
        llm_text3 = Tex("LLM output:").move_to(llm_box.get_center())
        llm_text_final = Tex("Numbers\\\\ with cells:\\\\ $[ 17, 18, 24 ]$").move_to(llm_box.get_center())

        # Animate new prompt and response
        self.play(Transform(question_text, question_text3))
        # self.wait(0.5)
        self.play(FadeOut(llm_text2), ShowCreation(llm_text3))
        self.wait(1)

        # Create a 10x10 grid with padding
        grid_size = 6
        cell_size = 0.3
        grid = VGroup()

        cells = {}
        for i in range(grid_size):
            for j in range(grid_size):
                # Create each grid cell
                cell = Square(side_length=cell_size)
                cell.move_to(image_group.get_center() + (j - 4.5 + 2) * RIGHT * cell_size + (i - 4.5) * DOWN * cell_size)
                num = i * grid_size + j + 1
     
                # Numbering the cell
                num = i * grid_size + j + 1
                number = Text(str(num), font_size=18).move_to(cell.get_center())

                # Adding coordinates (i, j) as overlay text
                coordinates = Text(f"({i},{j})", font_size=12).next_to(cell, DOWN, buff=0.05)

                # Add cell, number, and coordinates to the grid
                grid.add(cell, number, )
                cells[int(num)] = {'cell': cell, 'number': number}

        # Display the grid
        self.play(FadeOut(image_label), ShowCreation(grid), FadeOut(llm_text3), ShowCreation(llm_text_final))
        self.wait(0.5)
        # image_group = VGroup(circle, square).scale(0.8)
        # image_group.to_edge(LEFT, buff=1)

        # Add a surrounding rectangle for the image
        gg = SurroundingRectangle(grid, color=WHITE)
        gg.to_edge(LEFT, buff=1)
        
        # self.play(ShowCreation(gg), FadeOut(image_border), FadeOut(image_label))
        
        # image_border = SurroundingRectangle(image_group, color=WHITE)
        # image_label = Tex("Image").next_to(image_group, UP)
        # image_label = Tex("Image").next_to(image_group, UP)


        # Highlight specific cells (55, 66, 67)
        highlight_cells = [54, 65, 66]  # Zero-indexed
        highlights = []

        for idx in [11, 13, 23]:
            self.play(FadeOut(cells[idx]['cell']))

        self.wait(0.3)
      # Display all elements in sequence
      
        # Create a surrounding rectangle that includes the grid and the image
        grid_border = SurroundingRectangle(grid, color=YELLOW)

        # self.play(FadeIn(arrow), FadeIn(llm_box), FadeIn(llm_text1))
        self.wait(0.5)
        # Create a camera frame for zooming
        frame = self.camera.frame
        
        # Get the center point of the red cells
        red_cells_center = np.array([
            cells[17]['cell'].get_center(),
            cells[18]['cell'].get_center(), 
            cells[24]['cell'].get_center()
        ]).mean(axis=0)
        for num in (17, 18, 24):
            cells[num]['cell'].set_fill(RED, opacity=0.5)
        
        # Calculate bounding box of red cells
        min_x = min(cells[n]['cell'].get_left()[0] for n in [17,18,24])
        max_x = max(cells[n]['cell'].get_right()[0] for n in [17,18,24])
        min_y = min(cells[n]['cell'].get_bottom()[1] for n in [17,18,24])
        max_y = max(cells[n]['cell'].get_top()[1] for n in [17,18,24])
        
        # Calculate zoom width/height to frame the red cells
        zoom_width = (max_x - min_x) * 2  # Add some padding
        zoom_height = (max_y - min_y) * 2
        
        # Animate zooming in
        self.play(
            frame.animate.scale(0.3).move_to(red_cells_center),
            run_time=2
        )
        
        # Highlight the red cell numbers
        for num in [17, 18, 24]:
            self.play(
                Flash(cells[num]['number'], color=RED, line_length=0.2),
                run_time=0.5
            )
            
        # Zoom back out
        self.play(
            frame.animate.scale(3.33).move_to(ORIGIN),
            run_time=2
        )
        # Show highlights
        # self.play(*[FadeIn(highlight) for highlight in highlights])
        self.wait(5)

        # Fade out everything at the end
        self.play(*[FadeOut(mob) for mob in self.mobjects])

