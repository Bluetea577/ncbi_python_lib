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

from ncbi.datasets.openapi.models.v2_assembly_dataset_descriptors_filter import V2AssemblyDatasetDescriptorsFilter

class TestV2AssemblyDatasetDescriptorsFilter(unittest.TestCase):
    """V2AssemblyDatasetDescriptorsFilter unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2AssemblyDatasetDescriptorsFilter:
        """Test V2AssemblyDatasetDescriptorsFilter
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2AssemblyDatasetDescriptorsFilter`
        """
        model = V2AssemblyDatasetDescriptorsFilter()
        if include_optional:
            return V2AssemblyDatasetDescriptorsFilter(
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
                type_material_category = 'NONE'
            )
        else:
            return V2AssemblyDatasetDescriptorsFilter(
        )
        """

    def testV2AssemblyDatasetDescriptorsFilter(self):
        """Test V2AssemblyDatasetDescriptorsFilter"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()