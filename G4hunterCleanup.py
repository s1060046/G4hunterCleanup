#!/usr/bin/env python
import sys, getopt
import csv
import re
import pandas as pd

def line_prepender(filename, line):
		with open(filename, 'r+') as f:
				content = f.read()
				f.seek(0, 0)
				f.write(line.rstrip('\r\n') + '\n' + content)

def main(argv):
	 inputfile = ''
	 outputfile = ''
	 try:
			opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
	 except getopt.GetoptError:
			print('G4hunterCleanup.py -i <inputfile> -o <outputfile>')
			sys.exit(2)
	 for opt, arg in opts:
			if opt == '-h':
				 print('G4hunterCleanup.py -i <inputfile> -o <outputfile>')
				 sys.exit()
			elif opt in ("-i", "--ifile"):
				 inputfile = arg
			elif opt in ("-o", "--ofile"):
				 outputfile = arg
				
	 line_prepender(inputfile, "a\tb\tc\td\te\tf\tg")
	 input_file = open(inputfile)
	 df = pd.read_csv(inputfile, sep='\t', header= 0)
	 read_input = csv.reader(input_file, delimiter="\t")
	 next(read_input, None)
	 counter = -1
	 gene_col = {}
	 for row in read_input:
	 	counter = counter + 1
	 	if re.search("ENSMUS", str(row[0])):
	 		gene_col[counter] = row[0]
	 
	 gene_col = pd.DataFrame.from_dict(gene_col, orient='index')
	 gene_col['loop'] = gene_col.index

	 f = open(outputfile, "w+")
	 f.write("transcript, No_G4, Max_score, mean_score\n")
	 for i in range(0,len(gene_col.index)-2):
	 	print("processing {i} transcript out of {total}".format(total = len(gene_col.index)-3 i = i))
	 	current_loop = list(gene_col[i:i+2]['loop'])
	 	current_data = df[current_loop[0] : current_loop[1]]
	 	transcript_name = current_data["a"][:1].to_string()
	 	transcript_name = str(transcript_name).split(",")[1]
	 	NO_G4 = pd.to_numeric(current_data['f'], errors='coerce').max(skipna = True)
	 	max_score = abs(pd.to_numeric(current_data['e'], errors='coerce')).max(skipna = True)
	 	mean_score = abs(pd.to_numeric(current_data['e'], errors='coerce')).mean(skipna = True)
	 	f.write(("{transcript},{NO_G4}, {max_score}, {mean_score}\n").format(transcript = transcript_name, NO_G4 = NO_G4, max_score= max_score, mean_score = mean_score))



if __name__ == "__main__":
	main(sys.argv[1:])