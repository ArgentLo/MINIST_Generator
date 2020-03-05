import os
import numpy as np
import cv2

from utils import *

def create_digit_sequence(number):
        global args
        generatorMachine = GeneratorMachine(args)
        out_img = generatorMachine.gen_one_img(number)
        return out_img

if __name__ == "__main__":

    # CLI Arguments Parser
    cliParser = Command_Parser()
    args = cliParser.parse_Args()

    # Generate A SET of (imgs, labels)
    if args.auto_gen == True:
        generatorMachine = GeneratorMachine(args)
        out_imgs, out_labels = generatorMachine.gen_dataset()
        
        print("Output Shape: ", out_imgs.shape, len(out_labels))

        # save imgs
        cv2.imwrite( args.out_path + '/dataset_{0}.{1}'.format(args.gen_number, args.out_format), out_imgs)
        # save imgs + labels
        np.savez( args.out_path + '/dataset_{0}'.format(args.gen_number), out_imgs=out_imgs, out_labels=out_labels)
        

    # Generate a SINGLE (img, label)
    else: 
        # Start Generating
        out_img = create_digit_sequence(args.number)

        # save as PNG
        cv2.imwrite( args.out_path + '/{0}.{1}'.format(args.number, args.out_format), out_img)

