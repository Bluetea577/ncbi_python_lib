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

from ncbi.datasets.openapi.models.v2reports_average_nucleotide_identity import V2reportsAverageNucleotideIdentity

class TestV2reportsAverageNucleotideIdentity(unittest.TestCase):
    """V2reportsAverageNucleotideIdentity unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2reportsAverageNucleotideIdentity:
        """Test V2reportsAverageNucleotideIdentity
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2reportsAverageNucleotideIdentity`
        """
        model = V2reportsAverageNucleotideIdentity()
        if include_optional:
            return V2reportsAverageNucleotideIdentity(
                taxonomy_check_status = 'TAXONOMY_CHECK_STATUS_UNKNOWN',
                match_status = 'BEST_MATCH_STATUS_UNKNOWN',
                submitted_organism = '',
                submitted_species = '',
                category = 'ANI_CATEGORY_UNKNOWN',
                submitted_ani_match = ncbi.datasets.openapi.models.v2reports_ani_match.v2reportsANIMatch(
                    assembly = '', 
                    organism_name = '', 
                    category = 'ANI_CATEGORY_UNKNOWN', 
                    ani = 1.337, 
                    assembly_coverage = 1.337, 
                    type_assembly_coverage = 1.337, ),
                best_ani_match = ncbi.datasets.openapi.models.v2reports_ani_match.v2reportsANIMatch(
                    assembly = '', 
                    organism_name = '', 
                    category = 'ANI_CATEGORY_UNKNOWN', 
                    ani = 1.337, 
                    assembly_coverage = 1.337, 
                    type_assembly_coverage = 1.337, ),
                comment = ''
            )
        else:
            return V2reportsAverageNucleotideIdentity(
        )
        """

    def testV2reportsAverageNucleotideIdentity(self):
        """Test V2reportsAverageNucleotideIdentity"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
