import pandas as pd
from sklearn.model_selection import train_test_split
import random


def split(data, labels, train_size, columns, random_state, train_path, test_path):
    # Shuffle data
    data_train = []
    data_test = []

    temp = list(zip(data, labels))
    random.shuffle(temp)
    data, labels = zip(*temp)

    # Split images
    # X_train, X_test, y_train, y_test
    train_data, test_data, train_labels, test_labels = train_test_split(data, labels,
                                                                        train_size=train_size,
                                                                        random_state=random_state)
    for i in range(len(train_data)):
        data_train.append([train_data[i], train_labels[i]])

    for i in range(len(test_data)):
        data_test.append([test_data[i], test_labels[i]])

    train_df = pd.DataFrame(data_train, columns=columns, index=None)
    train_df.to_csv(train_path, index=False)

    test_df = pd.DataFrame(data_test, columns=columns, index=None)
    test_df.to_csv(test_path, index=False)

    print("Train data: " + str(len(train_data)))
    print("Test data: " + str(len(test_data)))
    print("------------------------")
    print(train_df[columns[1]].value_counts())


def multi_split(data, labels, train_size, columns, random_state, train_path, test_path):
    data_train = []
    data_test = []

    train_data, test_data, train_labels, test_labels = train_test_split(data, labels,
                                                                        train_size=train_size,
                                                                        random_state=random_state,
                                                                        shuffle=True)

    for i in range(len(train_data)):
        data_train.append([
            list(train_data["Image"])[i],
            list(train_data["Audio"])[i],
            list(train_labels)[i]
        ])

    for i in range(len(test_data)):
        data_test.append([
            list(test_data["Image"])[i],
            list(test_data["Audio"])[i],
            list(test_labels)[i]
        ])

    train_df = pd.DataFrame(data_train, columns=columns, index=None)
    train_df.to_csv(train_path, index=False)

    test_df = pd.DataFrame(data_test, columns=columns, index=None)
    test_df.to_csv(test_path, index=False)

    print("Train Data")
    print(train_labels.value_counts())
    print("Test Data")
    print(test_labels.value_counts())


audio_path = "../data/training/all_audio_data.csv"
image_path = "../data/training/all_image_data.csv"
multi_path = "../data/training/all_multi_data.csv"
columns_ = ["Species", "Label"]
columns1_ = ["Image", "Audio", "Label"]
TRAIN_SPLIT = 0.8

image_df = pd.read_csv(image_path)
audio_df = pd.read_csv(audio_path)
multi_df = pd.read_csv(multi_path)

image_files = image_df["Species"].tolist()
image_labels = image_df["Label"].tolist()
print("Total Images: " + str(len(image_files)))

audio_files = audio_df["Species"].tolist()
audio_labels = audio_df["Label"].tolist()
print("Total Audio: " + str(len(audio_files)))

multi_files = multi_df[['Image', 'Audio']]
multi_labels = multi_df['Label']

# Image split
# split(image_files, image_labels, TRAIN_SPLIT, columns_, 200, "../data/training/image/train.csv",
#       "../data/training/image/test.csv")

# Audio split
# split(audio_files, audio_labels, TRAIN_SPLIT, columns_, 12, "../data/training/audio/train.csv",
#       "../data/training/audio/test.csv")

# Multi split
multi_split(multi_files, multi_labels, TRAIN_SPLIT, columns1_, 12, "../data/training/multi/train.csv",
            "../data/training/multi/test.csv")
