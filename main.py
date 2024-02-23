import box
import timeit
import yaml
import argparse
from dotenv import find_dotenv, load_dotenv

from src.khmerllm.inference import interence 
from src.khmerllm.training import training
from src.khmerllm.data_preprocessor import preprocessor


# Load environment variables from .env file
load_dotenv(find_dotenv())


with open('config/khmerllm.yml', 'r', encoding='utf8') as ymlfile:
    cfg = box.Box(yaml.safe_load(ymlfile))
    
    
def parse_args() -> argparse.Namespace:
    """Parses arguments from the command line."""
    parser = argparse.ArgumentParser()
    
    parser.add_argument('--mode', choices=['train', 'infer', 'data-prep'], default='infer')
    
    return parser.parse_args()


def main():
    """Main function."""
    # parse arguments
    args = parse_args()
    
    # training the model
    if args.mode == 'train':
        training()
    elif args.mode == 'infer':
        interence()
    elif args.mode == 'data-prep':
        preprocessor()
    else:
        print("Unrecognized mode. Please use one of the following modes: 'train', 'infer', 'data-prep'")


if __name__ == '__main__':
    main()