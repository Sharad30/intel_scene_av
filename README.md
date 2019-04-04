# Intel Scene Classification Challenge

This repository consists of `notebooks` containing different experiments, `ensemble.py` file containing script for ensembling, `ensemble_submissions` with all the submission files used for final ensembling (model_accuracy > 0.92) and data containing train and test images.

**How to setup train folder?**

Download the data provided in the competition page. The `train.zip` consists of train and test images inside `train` folder. We are also provided with `train.csv` and `test.csv`, which will be used to segregate the data between train and test. Place the unzipped train folder inside `train/`(containing train images and train.csv) and use the `test.csv` to copy images from `train/train/` folder to`train/test/`. This will ensure that the data directory is setup to be used with the fastai codebase.

**Notebooks**

The notebooks inside the `notebooks/` directory will act as codebase for various experiments that were conducted.

**Ensembling**

To generate final ensembling predictions, run:
```
python ensemble.py
```
