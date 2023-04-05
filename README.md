# ImageCM
Python module for generating and editing images using Pillow

# Tree

imagecm.tree(width, height)
![image](https://user-images.githubusercontent.com/84366597/230128699-fb3709e8-bef0-4a08-8e31-16d84852b203.png)

# Grid

imagecm.get_grid(width_cells_count, height_cells_count, distance_between_dots)
![image](https://user-images.githubusercontent.com/84366597/230128776-da0d1fd2-0dde-4c1d-a536-4a8db00c8b0d.png)

# Networks
imagecm.network(width, height, dots_count) # black network
imagecm.rainbow_network(width, height, dots_count) # colored network
![image](https://user-images.githubusercontent.com/84366597/230130550-e71416b4-a929-44ec-a435-1e803b4b36d5.png)


# Noises
imagecm.noise(width, height) # colored
imagecm.gray_noise(width, height) # grayscale

![image](https://user-images.githubusercontent.com/84366597/230130701-94d50493-f841-4b4f-b95e-602635a96b3e.png)


# 3D
I3d(PIL.Image)
I3d.right(k)
I3d.left(k)
I3d.up(k)
I3d.down(k)
![image](https://user-images.githubusercontent.com/84366597/230131032-d6f9bc85-9a1d-4df8-86f7-b1b1dc464132.png)
