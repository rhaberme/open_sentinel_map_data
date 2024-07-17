import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def remap_pixel_values(channel_array):
    unique_values = np.unique(channel_array)
    print(f"Unique pixel values before mapping: {unique_values}")

    # create mapping from old values to new values
    max_val = 255
    if unique_values.size > 1:
        interval = max_val // (unique_values.size - 1)
    else:
        interval = 0

    new_values = np.arange(0, max_val + 1, interval)[:unique_values.size]
    mapping = dict(zip(unique_values, new_values))
    print(f"Mapping: {mapping}")

    # apply mapping
    for old_value, new_value in mapping.items():
        channel_array[channel_array == old_value] = new_value

    return channel_array

storing_image_path = "data"
image_name = '103956272'
image = Image.open(image_name+".png")
land_use_channel, water_roads_channel, buildings_channel = image.split()

land_use_channel_array = np.array(land_use_channel)
water_roads_channel_array = np.array(water_roads_channel)
buildings_channel_array = np.array(buildings_channel)


land_use_channel_array = remap_pixel_values(land_use_channel_array)
water_roads_channel_array = remap_pixel_values(water_roads_channel_array)
buildings_channel_array = remap_pixel_values(buildings_channel_array)

land_use_channel_image = Image.fromarray(land_use_channel_array)
water_roads_channel_image = Image.fromarray(water_roads_channel_array)
buildings_channel_image = Image.fromarray(buildings_channel_array)

land_use_channel_image.save(storing_image_path+"/"+image_name+'_modified_land_use_channel.png')
water_roads_channel_image.save(storing_image_path+"/"+image_name+'_modified_water_roads_channel.png')
buildings_channel_image.save(storing_image_path+"/"+image_name+'_modified_buildings_channel.png')


plt.imshow(land_use_channel_array)  # Using gray colormap for better visibility
plt.title('Modified Land Use Channel')
plt.show()

plt.imshow(water_roads_channel_array)  # Using gray colormap for better visibility
plt.title('Modified Water Roads Channel')
plt.show()

plt.imshow(buildings_channel_array)  # Using gray colormap for better visibility
plt.title('Modified Buildings Channel')
plt.show()
