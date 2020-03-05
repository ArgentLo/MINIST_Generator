import argparse
import sys
import os


class Command_Parser(object):
    def __init__(self):
        pass
    
    def parse_Args(self):
        try:
            # number, image_width, min_spacing, max_spacing
            parser = argparse.ArgumentParser(description='Config for Generating MNIST Sequence Digits')
            # required args
            parser.add_argument('--number', required=True, type=str, help='Desired Number Sequence. e.g. "12345".')
            parser.add_argument('--image_width', required=True, type=int, help='Desired Output Image Width (pixels). e.g. "200".')
            parser.add_argument('--min_spacing', required=True, type=int, help='Minimun Spacing allowed btw digits (pixels). e.g. "5".')
            parser.add_argument('--max_spacing', required=True, type=int, help='Maximum Spacing allowed btw digits (pixels). e.g. "20".')
            # with default
            parser.add_argument('--out_format', default="png", type=str, choices=['png', 'jpg'])
            parser.add_argument('--mnist_dataset', default="./dataset/", type=str, help='Path to the MNIST dataset.')
            parser.add_argument('--out_path', default="./generated_imgs/", type=str, help='Path to store generated image.')


            # NEW AUGS ===> needed Sanity Check
            parser.add_argument('--auto_gen', action='store_true', help='Auto Generate a whole set of MNIST Sequences.')
            parser.add_argument('--gen_number', default=1, type=int, help='Number of Training Examples needed. e.g. "1000".')
            parser.add_argument('--min_length', default=3, type=int, \
                                help='Min Length of Digits desired. e.g. "3", then sequences of length 3~ would be randomly generated.')
            parser.add_argument('--max_length', default=6, type=int, \
                                help='Max Length of Digits desired. e.g. "6", then sequences of length ~6 would be randomly generated.')


            args = parser.parse_args()
            
            # Sanity Check: number
            if (len(args.number) < 1) or (not args.number.isdigit()):
                raise(Exception('Argument Error : \
                        please correct the number input, e.g. "12345".'))

            # Sanity Check: image_width
            minimun_width = len(args.number)*28 + args.min_spacing*(len(args.number)-1)
            if minimun_width > args.image_width:
                raise(Exception('Argument Error : \
                        Current image width is too small, please specify a greater value.'))

            # Sanity Check : Spacing
            if (args.min_spacing > args.max_spacing) or (args.min_spacing < 0):
                raise(Exception('Argument Error : \
                        Please check the min_spacing and max_spacing.'))

            # Check Output Path
            if not os.path.exists(args.out_path):
                raise(Exception('Path Not Found : \
                        output path {} does not exist.'.format(args.out_path)))

            # Check Dataset Path
            if not os.path.exists(args.mnist_dataset + "train-images.idx3-ubyte"):
                raise(Exception('Dataset Not Found : \
                        please specify the path to MNIST train image file "train-images.idx3-ubyte".'))

            if not os.path.exists(args.mnist_dataset + "train-labels.idx1-ubyte"):
                raise(Exception('Dataset Not Found : \
                        please specify the path to MNIST train label file "train-labels.idx1-ubyte".'))
            
            # Check gen_number
            if args.gen_number < 1:
                raise(Exception('Gen Number Error : Gen Number should be positive.'))

            # Check Length
            if (args.min_length > args.max_length) or (args.min_length < 0):
                raise(Exception('Argument Error : \
                        Please check the min_length and max_length.'))
                        
            return args

        except Exception as err:
            raise(err)
