# Human Tracking

Human tracking implementation in python using YOLOv3.

## Install

### Clone

```bash
git clone git@github.com:Baiame/aive_test.git
cd aive_test
```

### Python

Have Python `>=3.9` installed with  `conda`.
Have make installed. For example using `brew`:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
)
brew install make
```

```bash
make install
```

Sometimes the environment is not properly activated. Try to run:

```bash
conda activate aive
```

### Models

Download [YOLOv3](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5/) and [tiny-YOLOv3](https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5/) and place them in the `models` folder.

## Run

To run the test with the default video and default mode, run:

```bash
make run
```

Otherwise, you can use the following command:

```bash
python src/main.py -i <VIDEO_PATH> -o <PATH_OUTPUT_FOLDER> -m <MODEL> -s <SPEED>
```

For the model choice, it can be:
- yolo
- tiny-yolo

For the speed, you can choose:
- normal
- fast
- faster
- flash


## Development

For code formatting, install `black` and run the formatting with `make`:

```bash
brew install black
make format
```
