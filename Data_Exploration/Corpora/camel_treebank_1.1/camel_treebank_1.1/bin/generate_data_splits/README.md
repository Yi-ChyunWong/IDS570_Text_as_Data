# CoNLL-X splits generator

When the main script is run, it will prompt the user to select the desired subcorpora to be split into dev, train, and test sets.<br><br>

---

## Contents

- `File` used to read different files (i.e. CoNLL-X)
- `main` main script.
- `requirements.txt` necessary dependencies needed to run the scripts.
- `utils` utility functions used in the scripts.
- `README.md` this document.
- `LICENSE` the code's license information.
- `natural_sort` to sort file names that contain numbers
- `selection` functions to handle user choices

## Requirements

- Python 3.8 and above.

To use, you need to first install the necessary dependencies by running the following command:

```bash
pip install -r requirements.txt
```
Note: it is preferable to create a virtual environment before installing the requirements

Then while in the generate_data_splits folder, run the following command:
```
python main.py
```
to get a series of choices to generate data splits.

---


## License

conllx_splits_generator is available under the MIT license.
See the [LICENSE file](/LICENSE) for more info.