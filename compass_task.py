while True:
    facing_position = str(input('Enter current position: ')).upper()
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
    if facing_position not in directions:
        print ('Incorrect facing position. Try again.')
        continue
    turning_position = int(input('Enter turning position: '))
    if turning_position < -1080:
        print ('Turning position is smaller than it should be. Try again.')
        continue
    if turning_position > 1080:
        print ('Turning position higher than it should be. Try again.')
        continue
    if (turning_position % 45) != 0:
        print ('Turning position is not divisible by 45. Try again.')
        continue

    def direction (facing, turning):
        turns = turning // 45
        init_position = directions.index(facing)
        end_position = (init_position + turns) % len(directions)
        return directions[end_position]

    direction(facing_position, turning_position)
    break
