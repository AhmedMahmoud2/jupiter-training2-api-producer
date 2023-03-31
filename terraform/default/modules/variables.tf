# ------------------------- #
# ------ module vars ------ #
# ------------------------- #

variable "name" {
  default     = "rmjlamm-training-api-producer"
  description = "The overarching name of this deployment (not just the lambdas therein)"
  type        = string
  nullable    = false
}



# create the local config objects for this module
# by pulling in the tfvars file (as it doesn't get read automatically in child modules)
# then doing a deep merge of the module and target vars using the below function

locals {
  tfvars = jsondecode(file("${path.module}/terraform.tfvars.json"))
  module_config = try(local.tfvars.config, {})
  module_env_vars = try(local.tfvars.env_vars, {})
}

module "merge_config" {
  source  = "Invicton-Labs/deepmerge/null"
  maps = [local.module_config, var.target_config]
}
module "merge_envvars" {
  source  = "Invicton-Labs/deepmerge/null"
  maps = [local.module_env_vars, var.target_envvars]
}

locals {
  config  = module.merge_config.merged
  env_vars = module.merge_envvars.merged
}


# ------------------------ #
# ------ core vars ------- #
# ------------------------ #

variable "env" {
  description = "The environment being deployed to, e.g. uat, production, local"
  type        = string
  nullable    = false
}

variable "serv" {
  description = "The ISD/UCL service domain responsible for this deployment."
  default     = null
  type        = string
  nullable    = true
}

variable "vrsn" {
  description = "The version of this particular deployment"
  type        = string
  nullable    = false
}

variable "target_config" {
  default     = {}
  description = "A catchall map of all variables from the target module"
  type        = any
}

variable "target_envvars" {
  default     = {}
  description = "A catchall map of all enviroment variables from the target module"
  type        = any
}