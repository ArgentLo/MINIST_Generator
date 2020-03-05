# MNIST Digits Sequence Generator 
This is the implementation of **Digits Sequence Generator**, where digits are randomly sampled from the [*MNIST*](http://yann.lecun.com/exdb/mnist/) dataset. 
The main purpose is to generate a whole set of random digits sequences for further **Machine Learning Training**, e.g. "digits detection".


## Environment Requirement

The code has been tested running under Python 3.6. The required packages are as follows:

```
Python == 3.6
numpy
cv2
argparse
tqdm
```

## Output Example

- This CLI API allows users to define `image_width`, `min_spacing` and `max_spacing`. A sample output is as follows:
<p align="center">
<img src="./res/gen_example1.png" alt="example1" style="zoom:15%;" />
</p>

- When `--auto_gen=False`, the CLI API generates a single image for a given `--number`.
![example_single](./res/example_single.png)

- When `--auto_gen=True`, the CLI API generates a set of digits sequences.
<p align="center">
<img src="./res/example_seq.png" alt="example_seq" style="zoom:0.001%;" />
</p>
- When `--auto_gen=False` and `min_length=3, max_length=7`, the CLI API generates a set of digits sequences with random lengths.
<p align="center">
<img src="./res/example_seq2.png" alt="example_seq2" style="zoom:15%;" />
</p>

## Usage

### Quick Start for CLI API
Two execution examples are provided, simply run:
```shell
# Single Digit Output
sh gen_single.sh
```

```shell
# Sequences Output
sh gen_set.sh
```

----

### Code Structure
```shell
.
├── dataset
│   ├── labels_dict.npz
│   ├── train-images.idx3-ubyte
│   └── train-labels.idx1-ubyte
├── generated_imgs
├── gen_set.sh
├── gen_single.sh
├── mnist_generator.py
└── utils
    ├── command_parser.py
    ├── generator.py
    ├── __init__.py
    └── mnist_parser.py

```

### CLI Instruction
```shell
$ python3 mnist_generator.py -h
usage: mnist_generator.py [-h] --number NUMBER --image_width IMAGE_WIDTH
                          --min_spacing MIN_SPACING --max_spacing MAX_SPACING
                          [--out_format {png,jpg}]
                          [--mnist_dataset MNIST_DATASET]
                          [--out_path OUT_PATH] [--auto_gen]
                          [--gen_number GEN_NUMBER] [--min_length MIN_LENGTH]
                          [--max_length MAX_LENGTH]

Config for Generating MNIST Sequence Digits

optional arguments:
  -h, --help            show this help message and exit
  --number NUMBER       Desired Number Sequence. e.g. "12345".
  --image_width IMAGE_WIDTH
                        Desired Output Image Width (pixels). e.g. "200".
  --min_spacing MIN_SPACING
                        Minimun Spacing allowed btw digits (pixels). e.g. "5".
  --max_spacing MAX_SPACING
                        Maximum Spacing allowed btw digits (pixels). e.g.
                        "20".
  --out_format {png,jpg}
  --mnist_dataset MNIST_DATASET
                        Path to the MNIST dataset.
  --out_path OUT_PATH   Path to store generated image.
  --auto_gen            Auto Generate a whole set of MNIST Sequences.
  --gen_number GEN_NUMBER
                        Number of Training Examples needed. e.g. "1000".
  --min_length MIN_LENGTH
                        Min Length of Digits desired. e.g. "3", then sequences
                        of length 3~ would be randomly generated.
  --max_length MAX_LENGTH
                        Max Length of Digits desired. e.g. "6", then sequences
                        of length ~6 would be randomly generated.
```
