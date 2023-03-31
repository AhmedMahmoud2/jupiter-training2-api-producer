# ------------------------ #
# ----- EASIKit Core ----- #
# ------------------------ #

# this file is the core of the deployment
# it sets the core variables, merges variables with the decrypted secrets
# then calls the modules in ../../module, which is where all the actual
# terraform logic should be (this should only define environment specific things)

# to personalise this target:
# - set up your environment specific variables in terraform.tfvars.json
#   - they should be added either to the config or env maps in that json file
# - add your secrets (perhaps using 'z deploy secret') to secrets/
# - decrypt your secrets in secrets.tf
# - add your secrets to the appropriate locals map below - probably env_secrets

locals {
  config_secrets = {
    #password = sensitive(data.ansiblevault_path.password.value)
  }

  env_secrets = {
    #DB_PASSWORD = sensitive(data.ansiblevault_path.db_password.value)
  }
}

# here we do a deep merge of those maps, in case you want to separate out
# env vars for one lambda from those for another, doing this retains that structure
# although in practice, you probably don't need to read this bit...

module "merge_config" {
  source  = "Invicton-Labs/deepmerge/null"
  maps = [var.config, local.config_secrets]
}
module "merge_envvars" {
  source  = "Invicton-Labs/deepmerge/null"
  maps = [var.env_vars, local.env_secrets]
}
locals {
  full_deploy_config = module.merge_config.merged
  full_deploy_envvars = module.merge_envvars.merged
}


# this is the only thing that might need to be changed per target but even then
# this is kind of the point of the target, right?
variable "env" {
  description = "Will be used in the name and to determine configuration files."
  type = string
  nullable = false
}

variable "service_domain" {
  description = "Used to help create namespaced deployments in case of shared account."
  type = string
  nullable = false
}

variable "aws_profile" {
  description = "The domain for which this is being deployed, should be in ~/.aws/config"
  type = string
  nullable = true
}

variable "aws_region" {
  default     = "eu-west-2"
  description = "Where this will be deployed to - probably gonna be eu-west-2."
  type = string
  nullable = false
}


# the environment agnostic wrapper module which defines to totality of 
# this particular terraform deployment, outlined in main.tf over in modules
# with the below variables defined in variables.tf over in modules
module "deployment" {
    source          = "../../modules"

    # core, specific variables
    env             = var.env
    serv            = var.service_domain
    vrsn            = var.deploy_version

    # the config map of all other variables
    # the deployment module should then divvy them up
    # amongst the further child modules
    target_config   = local.full_deploy_config
    target_envvars  = local.full_deploy_envvars
}

