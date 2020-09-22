import argparse
import border_crop as bc

parser = argparse.ArgumentParser()
parser.add_argument("src", help="source image (.gif, .jpg, .png)",
                    type=str)
parser.add_argument("--output_dir", help="where to store the output",
                    default='./result', type=str)
parser.add_argument("--threshold", help="the threshold of the black border",
                    default=5, type=int)

args = parser.parse_args()

src, output_dir = args.src, args.output_dir
bc.THRESHOLD = args.threshold

bc.crop_process(src, output_dir)