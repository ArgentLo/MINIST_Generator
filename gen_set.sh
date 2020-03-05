python3 mnist_generator.py --number=6666 --image_width=180 --min_spacing=5 --max_spacing=20 \
--gen_number=9999 --min_length=5 --max_length=5 --auto_gen

##### required
# number = "14543"
# image_width = 200
# min_spacing = 0
# max_spacing = 60

##### optional
# --auto_gen, action='store_true'
# --gen_number, default=1
# --min_length, default=3
# --max_length, default=6

# --out_format, default="png", choices=['png', 'jpg']
# --mnist_dataset, default="./dataset/"
# --out_path, default="./generated_imgs/"