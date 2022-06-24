import argparse
from detection import HumanVideoDetection

parser = argparse.ArgumentParser(description="Human Detection on a Video")
parser.add_argument("-i", "--input_video", type=str, required=True)
parser.add_argument("-m", "--model", type=str, required=True)
parser.add_argument("-s", "--speed", type=str, required=True)

args = parser.parse_args()

if args.model == None:
    args.model = 'yolo'
if args.speed == None:
    args.model = 'fast'

if __name__ == "__main__":
    hvd = HumanVideoDetection(
        input_path=args.input_video,
        model=args.model,
        detection_speed=args.speed,
    )
    hvd.human_detection()
