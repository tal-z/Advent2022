from utils import read_input
from day_10_solution_01 import process_instructions

def chunk_list(l, chunk_size):
    # looping till length l
    for i in range(0, len(l), chunk_size):
        yield l[i:i + chunk_size]


class Display():

    def __init__(self):
        self.display_data = ["."] * 240
        self.cycle_values = process_instructions(data)
        self.cycle_values[0] = 1


    def draw_pixels(self):
        prev_sprite_positions = {0, 1, 2}
        for cycle_num, sprite_center in sorted(self.cycle_values.items(), key=lambda x: x[0])[1:]:
            pixel_to_draw = cycle_num - 1
            row_position = cycle_num % 40 or 40
            sprite_positions = {sprite_center-1, sprite_center, sprite_center+1}

            if row_position-1 in prev_sprite_positions:
                self.display_data[pixel_to_draw] = "#"
            prev_sprite_positions = sprite_positions

        self._show()


    def _show(self):
        lines = chunk_list(self.display_data, 40)
        print()
        for line in lines:
            print(*line)

if __name__ == "__main__":

    data = read_input(10)

    d = Display()

    d.draw_pixels()
