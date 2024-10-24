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

from ncbi.datasets.openapi.models.v2_taxonomy_match import V2TaxonomyMatch

class TestV2TaxonomyMatch(unittest.TestCase):
    """V2TaxonomyMatch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2TaxonomyMatch:
        """Test V2TaxonomyMatch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2TaxonomyMatch`
        """
        model = V2TaxonomyMatch()
        if include_optional:
            return V2TaxonomyMatch(
                warnings = [
                    ncbi.datasets.openapi.models.v2reports_warning.v2reportsWarning(
                        gene_warning_code = 'UNKNOWN_GENE_WARNING_CODE', 
                        reason = '', 
                        message = '', 
                        replaced_id = ncbi.datasets.openapi.models.v2reports_warning_replaced_id.v2reportsWarningReplacedId(
                            requested = '', 
                            returned = '', ), 
                        unrecognized_identifier = '', )
                    ],
                errors = [
                    ncbi.datasets.openapi.models.v2reports_error.v2reportsError(
                        assembly_error_code = 'UNKNOWN_ASSEMBLY_ERROR_CODE', 
                        gene_error_code = 'UNKNOWN_GENE_ERROR_CODE', 
                        organelle_error_code = 'UNKNOWN_ORGANELLE_ERROR_CODE', 
                        virus_error_code = 'UNKNOWN_VIRUS_ERROR_CODE', 
                        taxonomy_error_code = 'UNKNOWN_TAXONOMY_ERROR_CODE', 
                        reason = '', 
                        message = '', 
                        invalid_identifiers = [
                            ''
                            ], )
                    ],
                query = [
                    ''
                    ],
                taxonomy = ncbi.datasets.openapi.models.v2_taxonomy_node.v2TaxonomyNode(
                    tax_id = 56, 
                    organism_name = '', 
                    common_name = '', 
                    genbank_common_name = '', 
                    acronyms = [
                        ''
                        ], 
                    genbank_acronym = '', 
                    blast_name = '', 
                    lineage = [
                        56
                        ], 
                    children = [
                        56
                        ], 
                    descendent_with_described_species_names_count = 56, 
                    rank = 'NO_RANK', 
                    has_described_species_name = True, 
                    counts = [
                        ncbi.datasets.openapi.models.v2_taxonomy_node_count_by_type.v2TaxonomyNodeCountByType(
                            type = 'COUNT_TYPE_UNSPECIFIED', 
                            count = 56, )
                        ], 
                    min_ord = 56, 
                    max_ord = 56, 
                    extinct = True, 
                    genomic_moltype = '', )
            )
        else:
            return V2TaxonomyMatch(
        )
        """

    def testV2TaxonomyMatch(self):
        """Test V2TaxonomyMatch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
