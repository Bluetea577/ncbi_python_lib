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

from ncbi.datasets.openapi.models.v2_assembly_revision_history import V2AssemblyRevisionHistory

class TestV2AssemblyRevisionHistory(unittest.TestCase):
    """V2AssemblyRevisionHistory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssemblyRevisionHistory:
        """Test V2AssemblyRevisionHistory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssemblyRevisionHistory`
        """
        model = V2AssemblyRevisionHistory()
        if include_optional:
            return V2AssemblyRevisionHistory(
                assembly_revisions = [
                    ncbi.datasets.openapi.models.v2reports_assembly_revision.v2reportsAssemblyRevision(
                        genbank_accession = '', 
                        refseq_accession = '', 
                        assembly_name = '', 
                        assembly_level = 'chromosome', 
                        release_date = '', 
                        submission_date = '', 
                        sequencing_technology = '', )
                    ],
                total_count = 56
            )
        else:
            return V2AssemblyRevisionHistory(
        )
        """

    def testV2AssemblyRevisionHistory(self):
        """Test V2AssemblyRevisionHistory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
