from kn_iris.iris_matching import *
from kn_iris.encode_iris_model import *
from kn_iris.feature_vec import *
import os
import sys
import argparse





def iris_model_train(train_db_path, train_encoding_model_path):
    if os.path.exists(train_db_path):
        if os.path.exists(train_encoding_model_path):
            iris_names = iris_test_model(train_db_path, train_encoding_model_path)
            return iris_names
        else:
            print("encoding model path not exist")
            return "encoding model path not exist"
    else:
        print("image database path not exist")
        return "image database path not exist"


def iris_model_test(test_encoding_model_path, image_path):
    if os.path.exists(test_encoding_model_path):
        if os.path.exists(image_path):
            iris_name = iris_recg(test_encoding_model_path, image_path)
            return iris_name
        else:
            print("image path not exist")
            return "image path not exist"
    else:
        print("image model path not exist")
        return "image model path not exist"


def iris_image_encoding(image_path):
    if os.path.exists(image_path):
        iris_image_encoding_result = engroup(image_path)
        return iris_image_encoding_result
    else:
        print("image path not exist")
        return "image path not exist"


def main():
    parser = argparse.ArgumentParser(
        description='CLI - iris recognition.')
    parser.add_argument('-trn', '--train_encoding_model_path', type=str, help='train encoding model path')
    parser.add_argument('-td', '--train_db_path', type=str, help='train image database path')
    parser.add_argument('-tn', '--test_encoding_model_path', type=str, help='test encoding model path')
    parser.add_argument('-i', '--image_path', type=str, help='image path')

    if len(sys.argv) < 2:
        print('Specify a key to use')
        sys.exit(1)

    # Optional bash tab completion support
    try:
        import argcomplete
        argcomplete.autocomplete(parser)
    except ImportError:
        pass

    args = parser.parse_args()
    if args.train_db_path != None and args.train_encoding_model_path != None:
        iris_model_train(args.train_db_path, args.train_encoding_model_path)
    if args.test_encoding_model_path != None and args.image_path != None:
        iris_model_test(args.test_encoding_model_path, args.image_path)
    if args.image_path != None:
        iris_image_encoding(args.image_path)




if __name__ == "__main__":
    main()

