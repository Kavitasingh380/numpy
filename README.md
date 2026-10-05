# NumPy practice

These are my practice notes for NumPy, plus two small data-analysis projects that use pandas and Plotly.

Most examples are commented out. To run one, uncomment that block, run the file, then comment it out again.

## Setup

```bash
pip install numpy pandas matplotlib seaborn plotly statsmodels
```

`statsmodels` is only needed for `trendline="ols"` in the Plotly scatter charts.

## Files

### NumPy notes

| File | What it covers |
| --- | --- |
| [basic.py](basic.py) | NumPy basics, split into 8 numbered sections (see below) |
| [numpy_functions.py](numpy_functions.py) | ufuncs (universal functions), maths and rounding, LCM/GCD, trigonometry, and set operations |
| [plotting_distribution.py](plotting_distribution.py) | Random number distributions, plotted with seaborn |

**basic.py**

1. Creating arrays and checking their properties (`shape`, `size`, `ndim`, `dtype`, `itemsize`, `nbytes`)
2. Indexing and slicing, including negative indexes
3. Data types
4. Reshaping and iterating
5. Joining arrays
6. Splitting arrays
7. Searching and sorting
8. Random numbers

**numpy_functions.py**

- Making your own ufunc with `np.frompyfunc()`, and checking whether a function is a ufunc
- Arithmetic: `add`, `subtract`, `multiply`, `divide`, `power`, `mod`, `remainder`, `divmod`, `absolute`
- Rounding: `trunc`, `fix`, `around`, `floor`, `ceil`
- Sums and products: `sum`, `cumsum`, `prod`, `cumprod`, `diff`
- `lcm`, `gcd`, and their `.reduce()` versions
- Trigonometry: `sin`, `deg2rad`, `rad2deg`, `arctanh`
- Set operations: `unique`, `union1d`, `intersect1d`, `setdiff1d`, `setxor1d`

**plotting_distribution.py**

Each example draws random numbers with `numpy.random` and plots them with seaborn. It covers these distributions: normal (Gaussian), binomial, Poisson, uniform, logistic, chi-square, Pareto and Zipf. There is also a chart that puts normal and Poisson side by side to compare them.

### Data analysis projects

| File | Dataset | What it does |
| --- | --- | --- |
| [iphonedataAnalysis.py](iphonedataAnalysis.py) | [apple_products.csv](apple_products.csv) | Finds the 10 highest-rated iPhones on Flipkart. It then charts their ratings and reviews, and how sale price and discount relate to the number of ratings. |
| [screentimeAnalysid.py](screentimeAnalysid.py) | [Screentime-App-Details-Dataset.csv](Screentime-App-Details-Dataset.csv) | Charts daily usage, notifications and times opened for each app, and how notifications relate to usage. |

These two scripts load their CSV files from an absolute path (`/Users/kavitasingh/...`). If you move the folder, change the path in `pd.read_csv(...)` to match.

## Running a file

```bash
cd numpy
python3 numpy_functions.py
```

The charts in the plotting and analysis scripts open in a separate window (matplotlib) or in the browser (Plotly).
