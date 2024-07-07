# BTP Terraform inpection tool

This tool wants to help creating Terraform scripts for the Terraform provider for SAP BTP and Cloudfoundry.

It lists all (potentially):
- forgotten important Terraform variables
- forgotten BTP/Cloudfoundry resources

Just call the `run` bash script and it will scan all folders with TF scripts that you copy to a folder called `tfscripts`.

The file `scripts/libs/contants/variables.py` contains the configuration.