import copy
import random

class Hat:
    def __init__(self, **colors):
        self.colors = colors
        self.contents = []
        
        for col, val in self.colors.items():
            self.contents += [col] * val
        
    '''def create_contents(self):
        contents = []
        for col, val in self.colors.items():
            contents += [col] * val
        return contents
    '''
    
    def draw (self):
        max_balls = len(self.contents)
        if 5 > max_balls:
            return self.contents
        else:
            drawn_indices = random.sample(range(0,len(self.contents)), 5)
            drawn_indices.sort(reverse=True)
            drawn_list = []
            
                

            for index in drawn_indices:
                drawn_list += self.contents[index]
                self.contents.pop(index)
            
            return drawn_list
        
        
        

    def __str__(self):
        output =  f'\n{self.colors}\n'
        output += f'\n{self.contents}\n{self.draw()}'
        return output


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


hat1 = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat1,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
hat2 = Hat(red=5, orange=4)
hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
print(hat1)
#print(hat2)
#print(hat3)

list = ['black', 'black', 'black', 'black', 'black', 'black', 'red', 'red', 'red', 'red', 'green', 'green', 'green']

def get_rand_index():
    return random.randrange(5)

rand_index = get_rand_index()
print('\n\n\n\n')
print(rand_index)
print(list[rand_index])
list.pop(rand_index)
print(list)


