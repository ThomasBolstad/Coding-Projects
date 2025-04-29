import copy
import random

class Hat:
    def __init__(self, **colors):
        self.colors = colors
        self.contents = self.create_contents()
        
    def create_contents(self):
        contents = []
        for col, val in self.colors.items():
            contents += [col] * val
        return contents
    
    def draw(self, num_balls_drawn):
        if num_balls_drawn >= len(self.contents):
            drawn_balls = self.contents.copy()  # Return a copy of all balls
            self.contents = []  # Clear the hat's contents
            return drawn_balls
        contents_copy = self.contents.copy()
        drawn_balls = []
        indices_to_remove = random.sample(range(len(contents_copy)), num_balls_drawn)
        indices_to_remove.sort(reverse=True)
        for index in indices_to_remove:
            drawn_balls.append(contents_copy.pop(index))
        self.contents = contents_copy
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        # Count the colors in the drawn balls
        counted_balls = {}
        for ball in drawn_balls:
            counted_balls[ball] = counted_balls.get(ball, 0) + 1
        # Check if we have at least the expected number of each color
        meets_criteria = True
        for color, required_count in expected_balls.items():
            if counted_balls.get(color, 0) < required_count:
                meets_criteria = False
                break
        if meets_criteria:
            M += 1
    return M / num_experiments

# Test case
hat = Hat(black=6, red=4, green=3)
probability = experiment(
    hat=hat,
    expected_balls={'red': 2, 'green': 1},
    num_balls_drawn=5,
    num_experiments=2000
)
print(f"Times Yes: {int(probability * 2000)}")
print(f"Number of Experiments: 2000")
print(f"Draw Probability: {probability}")