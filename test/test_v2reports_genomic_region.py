# coding: utf-8

"""
    NCBI Datasets API

    ### NCBI Datasets is a resource that lets you easily gather data from NCBI. The Datasets version 2 API is still in alpha, and we're updating it often to add new functionality, iron out bugs and enhance usability. For some larger downloads, you may want to download a [dehydrated zip archive](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/how-tos/genomes/large-download/), and retrieve the individual data files at a later time. 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from ncbi.datasets.openapi.models.v2reports_genomic_region import V2reportsGenomicRegion

class TestV2reportsGenomicRegion(unittest.TestCase):
    """V2reportsGenomicRegion unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2reportsGenomicRegion:
        """Test V2reportsGenomicRegion
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2reportsGenomicRegion`
        """
        model = V2reportsGenomicRegion()
        if include_optional:
            return V2reportsGenomicRegion(
                gene_range = ncbi.datasets.openapi.models.v2reports_seq_range_set.v2reportsSeqRangeSet(
                    accession_version = '', 
                    range = [
                        ncbi.datasets.openapi.models.v2reports_range.v2reportsRange(
                            begin = '', 
                            end = '', 
                            orientation = 'none', 
                            order = 56, 
                            ribosomal_slippage = 56, )
                        ], ),
                type = 'UNKNOWN'
            )
        else:
            return V2reportsGenomicRegion(
        )
        """

    def testV2reportsGenomicRegion(self):
        """Test V2reportsGenomicRegion"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()