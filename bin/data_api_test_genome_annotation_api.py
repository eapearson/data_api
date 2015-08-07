#!/usr/bin/env python
import sys
import os

paths = sys.path[:]
my_location = os.path.split(os.path.dirname(__file__))[0]
lib_path = sorted([(x, len(os.path.commonprefix([x, my_location]))) for x in paths], cmp=lambda x,y: cmp(x[1],y[1]))[-1][0]
sys.path.insert(1,lib_path)

import biokbase.data_api.tests.test_genome_annotation_api as test_api
test_api.test_get_cds_by_mrna()
test_api.test_get_mrna_by_cds()
test_api.test_get_gene_by_mrna()
test_api.test_get_gene_by_cds()
