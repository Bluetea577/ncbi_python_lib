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

from ncbi.datasets.openapi.models.v2reports_annotation import V2reportsAnnotation

class TestV2reportsAnnotation(unittest.TestCase):
    """V2reportsAnnotation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2reportsAnnotation:
        """Test V2reportsAnnotation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2reportsAnnotation`
        """
        model = V2reportsAnnotation()
        if include_optional:
            return V2reportsAnnotation(
                assembly_accession = '',
                assembly_name = '',
                annotation_name = '',
                annotation_release_date = '',
                genomic_locations = [
                    ncbi.datasets.openapi.models.v2reports_genomic_location.v2reportsGenomicLocation(
                        genomic_accession_version = '', 
                        sequence_name = '', 
                        genomic_range = ncbi.datasets.openapi.models.v2reports_range.v2reportsRange(
                            begin = '', 
                            end = '', 
                            orientation = 'none', 
                            order = 56, 
                            ribosomal_slippage = 56, ), 
                        exons = [
                            ncbi.datasets.openapi.models.v2reports_range.v2reportsRange(
                                begin = '', 
                                end = '', 
                                order = 56, 
                                ribosomal_slippage = 56, )
                            ], )
                    ]
            )
        else:
            return V2reportsAnnotation(
        )
        """

    def testV2reportsAnnotation(self):
        """Test V2reportsAnnotation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
