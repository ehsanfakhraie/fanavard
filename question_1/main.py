"""
- Fanavard Contest q1
- Gozar Team
- Ehsan Fakhraie, Amir Farahani, Ahamd Forooghi, Hossein Samadi
"""

# Array For Objects
objects = []
# Count Of Boxes Given
box_count = 0
# Size Of Boxes Given
box_size = 0


# Check and pack objects from j to n
def check(j):
    global box_count, box_size, objects

    # include box counts from global
    box_count_t = box_count - 1

    # Create an empty box for putting objects in it
    temp_box = 0

    # a var for counting total packaged objects
    packed_objects = 0

    # a flag to determine if selected j is not valid
    not_enough_boxes = False

    # iterate from j to n in objects
    for i in range(j, len(objects)):

        # check if selected object can be placed in box
        if temp_box + objects[i] <= box_size:
            # place the object in the box
            temp_box += objects[i]
        else:
            # create a new box and place object in it
            temp_box = objects[i]

            # decrease number of boxes
            box_count_t = box_count_t - 1

        # check if any box is left
        if box_count_t < 0:
            not_enough_boxes = True
            break
        # add object to total packed objects
        packed_objects += 1

    return packed_objects, not_enough_boxes


if __name__ == '__main__':
    # Import n,m,k
    number_of_objects, box_count, box_size = [int(b) for b in input().split(' ')]

    # Import Objects' size
    objects = [int(a) for a in input().split(' ')]

    # Create a temp array to store values of total packed objects with different j selected
    counts = []

    # Iterate through different j's from 0 to n
    for j in range(0, number_of_objects):

        # Run algorithm for each j
        ch = check(j)

        # Check if this j is valid
        if not ch[1]:
            counts.append(ch[0])

    # Print maximum packed objects
    print(max(counts))
