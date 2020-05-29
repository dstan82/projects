print('Floor tile price calculator\n')
width = float(input('Floor width (m):'))
height = float(input('Floor height (m):'))
tile_dimension = float(input('Enter tile side dimension (m):'))
cost_per_tile = float(input('Enter unitary cost/tile ($):'))


def calculate(width, height, tile_dimension, cost_per_tile):
    number_of_tiles = (width * height) / tile_dimension**2
    total_cost = cost_per_tile * number_of_tiles
    return f' For {round(number_of_tiles)} tiles, the total cost is ${round(total_cost,2)}'


print(calculate(width, height, tile_dimension, cost_per_tile))
