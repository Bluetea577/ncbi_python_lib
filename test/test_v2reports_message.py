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

from ncbi.datasets.openapi.models.v2reports_message import V2reportsMessage

class TestV2reportsMessage(unittest.TestCase):
    """V2reportsMessage unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2reportsMessage:
        """Test V2reportsMessage
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2reportsMessage`
        """
        model = V2reportsMessage()
        if include_optional:
            return V2reportsMessage(
                error = ncbi.datasets.openapi.models.v2reports_error.v2reportsError(
                    assembly_error_code = 'UNKNOWN_ASSEMBLY_ERROR_CODE', 
                    gene_error_code = 'UNKNOWN_GENE_ERROR_CODE', 
                    organelle_error_code = 'UNKNOWN_ORGANELLE_ERROR_CODE', 
                    virus_error_code = 'UNKNOWN_VIRUS_ERROR_CODE', 
                    taxonomy_error_code = 'UNKNOWN_TAXONOMY_ERROR_CODE', 
                    reason = '', 
                    message = '', 
                    invalid_identifiers = [
                        ''
                        ], ),
                warning = ncbi.datasets.openapi.models.v2reports_warning.v2reportsWarning(
                    gene_warning_code = 'UNKNOWN_GENE_WARNING_CODE', 
                    reason = '', 
                    message = '', 
                    replaced_id = ncbi.datasets.openapi.models.v2reports_warning_replaced_id.v2reportsWarningReplacedId(
                        requested = '', 
                        returned = '', ), 
                    unrecognized_identifier = '', )
            )
        else:
            return V2reportsMessage(
        )
        """

    def testV2reportsMessage(self):
        """Test V2reportsMessage"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()