# ------------------------ #
# ------ variables ------- #
# ------------------------ #

# this file shouldn't need to be changed, as all variables are
# defined in the terraform.ftvars.json file
# that file should have three root level JSON objects, which
# then map to the variables below

variable "deploy_version" {
  description = "The overarching version of this deployment (not any particular lambda)"
  type        = string
  nullable    = false
}

variable "config" {
  default     = {}
  description = "All the configuration related to the resources being created"
  type        = any
}

variable "env_vars" {
  default     = {}
  description = "All the environment variables to be passed to lambdas in the resource"
  type        = any
}