# coding: utf-8

"""
    NCBI Datasets API

    ### NCBI Datasets is a resource that lets you easily gather data from NCBI. The Datasets version 2 API is still in alpha, and we're updating it often to add new functionality, iron out bugs and enhance usability. For some larger downloads, you may want to download a [dehydrated zip archive](https://www.ncbi.nlm.nih.gov/datasets/docs/v2/how-tos/genomes/large-download/), and retrieve the individual data files at a later time. 

    The version of the OpenAPI document: v2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ncbi.datasets.openapi.api.organelle_api import OrganelleApi


class TestOrganelleApi(unittest.TestCase):
    """OrganelleApi unit test stubs"""

    def setUp(self) -> None:
        self.api = OrganelleApi()

    def tearDown(self) -> None:
        pass

    def test_download_organelle_package(self) -> None:
        """Test case for download_organelle_package

        Get a organelle data package by accesions
        """
        pass

    def test_download_organelle_package_by_post(self) -> None:
        """Test case for download_organelle_package_by_post

        Get a organelle data package by post
        """
        pass

    def test_organelle_datareport_by_accession(self) -> None:
        """Test case for organelle_datareport_by_accession

        Get Organelle dataset report by accession
        """
        pass

    def test_organelle_datareport_by_post(self) -> None:
        """Test case for organelle_datareport_by_post

        Get Organelle dataset report by http post
        """
        pass

    def test_organelle_datareport_by_taxon(self) -> None:
        """Test case for organelle_datareport_by_taxon

        Get Organelle dataset report by taxons
        """
        pass


if __name__ == '__main__':
    unittest.main()
