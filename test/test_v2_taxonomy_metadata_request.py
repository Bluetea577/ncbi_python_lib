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

from ncbi.datasets.openapi.models.v2_taxonomy_metadata_request import V2TaxonomyMetadataRequest

class TestV2TaxonomyMetadataRequest(unittest.TestCase):
    """V2TaxonomyMetadataRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2TaxonomyMetadataRequest:
        """Test V2TaxonomyMetadataRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2TaxonomyMetadataRequest`
        """
        model = V2TaxonomyMetadataRequest()
        if include_optional:
            return V2TaxonomyMetadataRequest(
                taxons = [
                    ''
                    ],
                returned_content = 'COMPLETE',
                page_size = 56,
                include_tabular_header = 'INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY',
                page_token = '',
                table_format = 'SUMMARY',
                children = True,
                ranks = [
                    'NO_RANK'
                    ]
            )
        else:
            return V2TaxonomyMetadataRequest(
        )
        """

    def testV2TaxonomyMetadataRequest(self):
        """Test V2TaxonomyMetadataRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
