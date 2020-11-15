# G4hunterCleanup
result clean up after running G4Hunter on multiple sequences (https://github.com/AnimaTardeb/G4Hunter) using script by JocelynSP (see files commited)

combines G4 detection for each sequence and reports
number of G4 region detected,
Maximum absolute G4 score
Mean absolute G4 score
for genome-wide analysis

## Usage
```
python G4hunterCleanup.py -i <inputfile> -o <outputfile>
```

Requires pandas version 0.25.1 and python 3.7.4
<inputfile> is the merged output from G4Hunter
<outputfile> for output file.
  
