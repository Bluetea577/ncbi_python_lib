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

from ncbi.datasets.openapi.models.v2_assembly_dataset_reports_request import V2AssemblyDatasetReportsRequest

class TestV2AssemblyDatasetReportsRequest(unittest.TestCase):
    """V2AssemblyDatasetReportsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssemblyDatasetReportsRequest:
        """Test V2AssemblyDatasetReportsRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssemblyDatasetReportsRequest`
        """
        model = V2AssemblyDatasetReportsRequest()
        if include_optional:
            return V2AssemblyDatasetReportsRequest(
                taxons = [
                    ''
                    ],
                bioprojects = [
                    ''
                    ],
                biosample_ids = [
                    ''
                    ],
                assembly_names = [
                    ''
                    ],
                wgs_accessions = [
                    ''
                    ],
                accessions = [
                    ''
                    ],
                filters = ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter.v2AssemblyDatasetDescriptorsFilter(
                    reference_only = True, 
                    assembly_source = 'all', 
                    has_annotation = True, 
                    exclude_paired_reports = True, 
                    exclude_atypical = True, 
                    assembly_version = 'current', 
                    assembly_level = [
                        'chromosome'
                        ], 
                    first_release_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    last_release_date = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    search_text = [
                        ''
                        ], 
                    is_metagenome_derived = 'METAGENOME_DERIVED_UNSET', 
                    is_type_material = True, 
                    is_ictv_exemplar = True, 
                    exclude_multi_isolate = True, 
                    type_material_category = 'NONE', ),
                tax_exact_match = True,
                chromosomes = [
                    ''
                    ],
                table_fields = [
                    ''
                    ],
                returned_content = 'COMPLETE',
                page_size = 56,
                page_token = '',
                sort = [
                    ncbi.datasets.openapi.models.v2_sort_field.v2SortField(
                        field = '', 
                        direction = 'SORT_DIRECTION_UNSPECIFIED', )
                    ],
                include_tabular_header = 'INCLUDE_TABULAR_HEADER_FIRST_PAGE_ONLY',
                table_format = ''
            )
        else:
            return V2AssemblyDatasetReportsRequest(
        )
        """

    def testV2AssemblyDatasetReportsRequest(self):
        """Test V2AssemblyDatasetReportsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()