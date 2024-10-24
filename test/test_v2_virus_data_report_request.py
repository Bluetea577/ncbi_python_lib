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

from ncbi.datasets.openapi.models.v2_virus_data_report_request import V2VirusDataReportRequest

class TestV2VirusDataReportRequest(unittest.TestCase):
    """V2VirusDataReportRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2VirusDataReportRequest:
        """Test V2VirusDataReportRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2VirusDataReportRequest`
        """
        model = V2VirusDataReportRequest()
        if include_optional:
            return V2VirusDataReportRequest(
                filter = ncbi.datasets.openapi.models.v2_virus_dataset_filter.v2VirusDatasetFilter(
                    accessions = [
                        ''
                        ], 
                    taxon = '', 
                    refseq_only = True, 
                    annotated_only = True, 
                    released_since = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    updated_since = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    host = '', 
                    pangolin_classification = '', 
                    geo_location = '', 
                    usa_state = '', 
                    complete_only = True, ),
                returned_content = 'COMPLETE',
                table_fields = [
                    ''
                    ],
                table_format = '',
                page_size = 56,
                page_token = ''
            )
        else:
            return V2VirusDataReportRequest(
        )
        """

    def testV2VirusDataReportRequest(self):
        """Test V2VirusDataReportRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
