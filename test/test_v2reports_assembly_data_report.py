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

from ncbi.datasets.openapi.models.v2reports_assembly_data_report import V2reportsAssemblyDataReport

class TestV2reportsAssemblyDataReport(unittest.TestCase):
    """V2reportsAssemblyDataReport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> V2reportsAssemblyDataReport:
        """Test V2reportsAssemblyDataReport
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `V2reportsAssemblyDataReport`
        """
        model = V2reportsAssemblyDataReport()
        if include_optional:
            return V2reportsAssemblyDataReport(
                accession = '',
                current_accession = '',
                paired_accession = '',
                source_database = 'SOURCE_DATABASE_UNSPECIFIED',
                organism = ncbi.datasets.openapi.models.v2reports_organism.v2reportsOrganism(
                    tax_id = 56, 
                    sci_name = '', 
                    organism_name = '', 
                    common_name = '', 
                    lineage = [
                        ncbi.datasets.openapi.models.v2reports_lineage_organism.v2reportsLineageOrganism(
                            tax_id = 56, 
                            name = '', )
                        ], 
                    strain = '', 
                    pangolin_classification = '', 
                    infraspecific_names = ncbi.datasets.openapi.models.v2reports_infraspecific_names.v2reportsInfraspecificNames(
                        breed = '', 
                        cultivar = '', 
                        ecotype = '', 
                        isolate = '', 
                        sex = '', 
                        strain = '', ), ),
                assembly_info = ncbi.datasets.openapi.models.v2reports_assembly_info.v2reportsAssemblyInfo(
                    assembly_level = '', 
                    assembly_status = 'ASSEMBLY_STATUS_UNKNOWN', 
                    paired_assembly = ncbi.datasets.openapi.models.v2reports_paired_assembly.v2reportsPairedAssembly(
                        accession = '', 
                        status = 'ASSEMBLY_STATUS_UNKNOWN', 
                        annotation_name = '', 
                        only_genbank = '', 
                        only_refseq = '', 
                        changed = '', 
                        manual_diff = '', ), 
                    assembly_name = '', 
                    assembly_long_name = '', 
                    assembly_type = '', 
                    bioproject_lineage = [
                        ncbi.datasets.openapi.models.v2reports_bio_project_lineage.v2reportsBioProjectLineage(
                            bioprojects = [
                                ncbi.datasets.openapi.models.v2reports_bio_project.v2reportsBioProject(
                                    accession = '', 
                                    title = '', 
                                    parent_accession = '', 
                                    parent_accessions = [
                                        ''
                                        ], )
                                ], )
                        ], 
                    bioproject_accession = '', 
                    submission_date = '', 
                    release_date = '', 
                    description = '', 
                    submitter = '', 
                    refseq_category = '', 
                    synonym = '', 
                    linked_assembly = '', 
                    linked_assemblies = [
                        ncbi.datasets.openapi.models.v2reports_linked_assembly.v2reportsLinkedAssembly(
                            linked_assembly = '', 
                            assembly_type = 'LINKED_ASSEMBLY_TYPE_UNKNOWN', )
                        ], 
                    atypical = ncbi.datasets.openapi.models.v2reports_atypical_info.v2reportsAtypicalInfo(
                        is_atypical = True, 
                        warnings = [
                            ''
                            ], ), 
                    genome_notes = [
                        ''
                        ], 
                    sequencing_tech = '', 
                    assembly_method = '', 
                    grouping_method = '', 
                    biosample = ncbi.datasets.openapi.models.v2reports_bio_sample_descriptor.v2reportsBioSampleDescriptor(
                        accession = '', 
                        last_updated = '', 
                        publication_date = '', 
                        submission_date = '', 
                        sample_ids = [
                            ncbi.datasets.openapi.models.v2reports_bio_sample_id.v2reportsBioSampleId(
                                db = '', 
                                label = '', 
                                value = '', )
                            ], 
                        description = ncbi.datasets.openapi.models.v2reports_bio_sample_description.v2reportsBioSampleDescription(
                            title = '', 
                            organism = ncbi.datasets.openapi.models.v2reports_organism.v2reportsOrganism(
                                tax_id = 56, 
                                sci_name = '', 
                                organism_name = '', 
                                common_name = '', 
                                lineage = [
                                    ncbi.datasets.openapi.models.v2reports_lineage_organism.v2reportsLineageOrganism(
                                        tax_id = 56, 
                                        name = '', )
                                    ], 
                                strain = '', 
                                pangolin_classification = '', 
                                infraspecific_names = ncbi.datasets.openapi.models.v2reports_infraspecific_names.v2reportsInfraspecificNames(
                                    breed = '', 
                                    cultivar = '', 
                                    ecotype = '', 
                                    isolate = '', 
                                    sex = '', 
                                    strain = '', ), ), 
                            comment = '', ), 
                        owner = ncbi.datasets.openapi.models.v2reports_bio_sample_owner.v2reportsBioSampleOwner(
                            name = '', 
                            contacts = [
                                ncbi.datasets.openapi.models.v2reports_bio_sample_contact.v2reportsBioSampleContact(
                                    lab = '', )
                                ], ), 
                        models = [
                            ''
                            ], 
                        package = '', 
                        attributes = [
                            ncbi.datasets.openapi.models.v2reports_bio_sample_attribute.v2reportsBioSampleAttribute(
                                name = '', 
                                value = '', )
                            ], 
                        age = '', 
                        biomaterial_provider = '', 
                        breed = '', 
                        collected_by = '', 
                        collection_date = '', 
                        cultivar = '', 
                        dev_stage = '', 
                        ecotype = '', 
                        geo_loc_name = '', 
                        host = '', 
                        host_disease = '', 
                        identified_by = '', 
                        ifsac_category = '', 
                        isolate = '', 
                        isolate_name_alias = '', 
                        isolation_source = '', 
                        lat_lon = '', 
                        project_name = '', 
                        sample_name = '', 
                        serovar = '', 
                        sex = '', 
                        source_type = '', 
                        strain = '', 
                        sub_species = '', 
                        tissue = '', 
                        serotype = '', ), 
                    blast_url = '', 
                    comments = '', 
                    suppression_reason = '', 
                    diploid_role = 'LINKED_ASSEMBLY_TYPE_UNKNOWN', ),
                assembly_stats = ncbi.datasets.openapi.models.v2reports_assembly_stats.v2reportsAssemblyStats(
                    total_number_of_chromosomes = 56, 
                    total_sequence_length = '', 
                    total_ungapped_length = '', 
                    number_of_contigs = 56, 
                    contig_n50 = 56, 
                    contig_l50 = 56, 
                    number_of_scaffolds = 56, 
                    scaffold_n50 = 56, 
                    scaffold_l50 = 56, 
                    gaps_between_scaffolds_count = 56, 
                    number_of_component_sequences = 56, 
                    gc_count = '', 
                    gc_percent = 1.337, 
                    genome_coverage = '', 
                    number_of_organelles = 56, ),
                organelle_info = [
                    ncbi.datasets.openapi.models.v2reports_organelle_info.v2reportsOrganelleInfo(
                        assembly_name = '', 
                        infraspecific_name = '', 
                        bioproject = [
                            ''
                            ], 
                        description = '', 
                        total_seq_length = '', 
                        submitter = '', )
                    ],
                additional_submitters = [
                    ncbi.datasets.openapi.models.v2reports_extra_sequence_info.v2reportsExtraSequenceInfo(
                        genbank_accession = '', 
                        refseq_accession = '', 
                        chr_name = '', 
                        molecule_type = '', 
                        submitter = '', 
                        bioproject_accession = '', )
                    ],
                annotation_info = ncbi.datasets.openapi.models.v2reports_annotation_info.v2reportsAnnotationInfo(
                    name = '', 
                    provider = '', 
                    release_date = '', 
                    report_url = '', 
                    stats = ncbi.datasets.openapi.models.v2reports_feature_counts.v2reportsFeatureCounts(
                        gene_counts = ncbi.datasets.openapi.models.v2reports_gene_counts.v2reportsGeneCounts(
                            total = 56, 
                            protein_coding = 56, 
                            non_coding = 56, 
                            pseudogene = 56, 
                            other = 56, ), ), 
                    busco = ncbi.datasets.openapi.models.v2reports_busco_stat.v2reportsBuscoStat(
                        busco_lineage = '', 
                        busco_ver = '', 
                        complete = 1.337, 
                        single_copy = 1.337, 
                        duplicated = 1.337, 
                        fragmented = 1.337, 
                        missing = 1.337, 
                        total_count = '', ), 
                    method = '', 
                    pipeline = '', 
                    software_version = '', 
                    status = '', 
                    release_version = '', ),
                wgs_info = ncbi.datasets.openapi.models.v2reports_wgs_info.v2reportsWGSInfo(
                    wgs_project_accession = '', 
                    master_wgs_url = '', 
                    wgs_contigs_url = '', ),
                type_material = ncbi.datasets.openapi.models.v2reports_type_material.v2reportsTypeMaterial(
                    type_label = '', 
                    type_display_text = '', ),
                checkm_info = ncbi.datasets.openapi.models.v2reports_check_m.v2reportsCheckM(
                    checkm_marker_set = '', 
                    checkm_species_tax_id = 56, 
                    checkm_marker_set_rank = '', 
                    checkm_version = '', 
                    completeness = 1.337, 
                    contamination = 1.337, 
                    completeness_percentile = 1.337, ),
                average_nucleotide_identity = ncbi.datasets.openapi.models.v2reports_average_nucleotide_identity.v2reportsAverageNucleotideIdentity(
                    taxonomy_check_status = 'TAXONOMY_CHECK_STATUS_UNKNOWN', 
                    match_status = 'BEST_MATCH_STATUS_UNKNOWN', 
                    submitted_organism = '', 
                    submitted_species = '', 
                    category = 'ANI_CATEGORY_UNKNOWN', 
                    submitted_ani_match = ncbi.datasets.openapi.models.v2reports_ani_match.v2reportsANIMatch(
                        assembly = '', 
                        organism_name = '', 
                        ani = 1.337, 
                        assembly_coverage = 1.337, 
                        type_assembly_coverage = 1.337, ), 
                    best_ani_match = ncbi.datasets.openapi.models.v2reports_ani_match.v2reportsANIMatch(
                        assembly = '', 
                        organism_name = '', 
                        ani = 1.337, 
                        assembly_coverage = 1.337, 
                        type_assembly_coverage = 1.337, ), 
                    comment = '', )
            )
        else:
            return V2reportsAssemblyDataReport(
        )
        """

    def testV2reportsAssemblyDataReport(self):
        """Test V2reportsAssemblyDataReport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()