
all_empties = []
for empty in bpy.data.objects:
    if empty.type != "EMPTY" : continue
    all_empties.append(empty)

def percent_distance_along_x_axis(all_empties, empty):
    # Sort the empties by the x value
    sorted_empties = sorted(all_empties, key=lambda empty: empty.location[0])
    #
    min_empty_x = sorted_empties[0].location[0]
    max_empty_x = sorted_empties[-1].location[0]
    current_empty_x = empty.location[0]
    #
    total_distance = max_empty_x - min_empty_x
    total_distance
    #
    distance_from_start = current_empty_x - min_empty_x
    distance_from_start
    percent_of_total_distance = float(distance_from_start / total_distance)
    return percent_of_total_distance

def add_keyframes_to_empty(empty, percent_of_total_distance, full_animation_length):
    empty.keyframe_insert( data_path = 'scale', frame = 1 )
    empty.keyframe_insert( data_path = 'scale', frame = full_animation_length )
    #
    start_elastic_frame = int(full_animation_length * (1 - percent_of_total_distance))
    end_elsatic_frame = min(start_elastic_frame + 20, full_animation_length - 1)
    empty.keyframe_insert( data_path = 'scale', frame = end_elsatic_frame )
    empty.keyframe_insert( data_path = 'scale', frame = start_elastic_frame )
    #
    kf = empty.animation_data.action.fcurves[0].keyframe_points[1]
    kf.interpolation = 'ELASTIC'

empty = bpy.data.objects['effr.empty.005']
dist = percent_distance_along_x_axis(all_empties, empty)
add_keyframes_to_empty(empty, dist, 50)
