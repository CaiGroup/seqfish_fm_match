Usage
======

Installation
------------
To install this package clone it with

```
clone https://github.com/CaiGroup/seqfish_fm_match.git
```

then you are in the package root directory, run

```
pip install .
```


Usage Notes
-------

To run fiducial marker matching alignment, first read in dataframes
containing lists of the coordinates and brightness of fiducial markers in the
initial reference image (taken before all of the hybridization cycles),
a DataFrame listing coordinates, hybridization, and brightness of fiducial markers (and possibly other dots).
If using auto parameter setting, you will also need a list of ficducial markers found in the final
fiducial marker reference image (taken after all of the hybridization cycles).a

The DataFrames must have columns
``` hyb x y z int```
