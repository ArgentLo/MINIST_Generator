import numpy as np
import os
from tqdm import tqdm
from .command_parser import Command_Parser
from .mnist_parser import read_idx


class GeneratorMachine(object):

    def __init__(self, args):
        # init parameters from argparser
        # CLI Arguments Parser

        self.number, self.image_width, self.min_spacing, self.max_spacing, self.out_path, self.out_format = \
            args.number, args.image_width, args.min_spacing, args.max_spacing, args.out_path, args.out_format

        img_path = args.mnist_dataset + "train-images.idx3-ubyte"
        label_path = args.mnist_dataset + "train-labels.idx1-ubyte"

        self.mnist_imgs = read_idx(img_path)
        self.mnist_labels = read_idx(label_path)
        
        
        # read label -> ids
        if os.path.exists(args.mnist_dataset + 'labels_dict.npz'):
            self.labels_dict = np.load(args.mnist_dataset + 'labels_dict.npz', allow_pickle=True)
            self.labels_dict = self.labels_dict['labels_dict'].tolist()
        else: 
            # lables_dice = {"0": [ids], ... }
            self.labels_dict = dict()
            for cur_label in np.arange(10):
                self.labels_dict[cur_label] = np.where( self.mnist_labels == cur_label )[0]
            # save
            np.savez(args.mnist_dataset + 'labels_dict', labels_dict=labels_dict)


        self.gen_number = args.gen_number
        self.min_length = args.min_length
        self.max_length = args.max_length


    def gen_dataset(self):
        
        out_imgs = np.empty((0, self.image_width), dtype=np.uint8)
        out_labels = []
        for i in tqdm(range(self.gen_number)):

            # random number up to min_lenght
            random_length = np.random.randint(self.min_length, self.max_length+1)
            random_number = ''
            for _ in range(random_length):
                random_number += str(np.random.randint(10)) 
            # gen_one_img and concatenate
            gen_img = self.gen_one_img(random_number)
            out_imgs = np.concatenate((out_imgs, gen_img), axis=0)
            out_labels.append(random_number)
        
        return out_imgs, out_labels


    def gen_one_img(self, number):

        # initialize vars
        out_img = np.empty((28, 0), dtype=np.uint8)
        min_patch = np.zeros([28, self.min_spacing], dtype=np.uint8)
        spacing_region = self.max_spacing - self.min_spacing

        minimun_width = len(number) * 28 + (len(number)-1) * self.min_spacing
        possible_spacing = self.image_width - minimun_width
        # print("possible_spacing: ", possible_spacing)
        
        for i in range(len(number)):
            num = number[i]
            # randomly sample digits
            sample_idx = np.random.choice(self.labels_dict[int(num)])
            sample_img = self.mnist_imgs[sample_idx]
            
            # append random spacein + min_patch
            if i != (len(number)-1):
                
                if possible_spacing > 0:
                    spacing = np.random.randint(0, min(spacing_region, possible_spacing))
                else:
                    spacing = 0
                
                possible_spacing -= spacing
                
                spacing = np.zeros([28, spacing], dtype=np.uint8)
                out_img = np.hstack((out_img, sample_img, min_patch, spacing))
            else:
                out_img = np.hstack((out_img, sample_img))

        # Expand left+right to output "image_width"
        if possible_spacing > 0:
            left_space = np.random.randint(0, possible_spacing)
            left_patch = np.zeros([28, left_space], dtype=np.uint8)
            right_patch = np.zeros([28, (possible_spacing-left_space)], dtype=np.uint8)
            out_img = np.hstack((left_patch, out_img, right_patch))

        return out_img