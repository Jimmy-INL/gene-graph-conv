import os
import csv
import pickle


def record_result(results, experiment, filename):
    results = results.append(experiment, ignore_index=True)
    results_dir = "/".join(filename.split('/')[0:-1])

    if not os.path.isdir(results_dir):
        os.makedirs(results_dir)
    pickle.dump(results, open(filename, "wb"))
    return results

def symbol_map(gene_symbols):
    # This gene code map was generated on February 18th, 2019
    # at this URL: https://www.genenames.org/cgi-bin/download/custom?col=gd_app_sym&col=gd_prev_sym&status=Approved&status=Entry%20Withdrawn&hgnc_dbtag=on&order_by=gd_app_sym_sort&format=text&submit=submit
    # it enables us to map the gene names to the newest version of the gene labels
    with open('gene_code_map.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter='\t')
        line_count = 0
        x = {row[0]: row[1] for row in csv_reader}

        map = {}
        for key, val in x.items():
            for v in val.split(", "):
                if key not in gene_symbols:
                    map[v] = key
    return map
