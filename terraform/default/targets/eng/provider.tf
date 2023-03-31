provider "aws" {
    region = var.aws_region
    profile = var.aws_profile
}

# the bucket itself must already exist and would be managed by a
# central Team AWS Account Core project, speak to your SOM/domain tech lead for details
terraform {
  # bucket should already exist, e.g. with easikit-aws-core/module/tfstate-backend
  # e.g bucket = "ucl-isd-identity-dev-terraform-state"
  #     key    = "dev/person-api-producer/terraform.tfstate
  
}

# # the terraform provider for use with localstack
# # for intial local testing before full aws deployment
# provider "aws" {
#   region  = "eu-west-2"

#   access_key                  = "test"
#   secret_key                  = "test"
#   skip_credentials_validation = true
#   skip_metadata_api_check     = true
#   skip_requesting_account_id  = true
#   s3_use_path_style = true

#   endpoints {
#     dynamodb = "http://localhost:4566"
#     kinesis = "http://localhost:4566"
#     lambda = "http://localhost:4566"
#     apigatewayv2 = "http://localhost:4566"
#     apigateway = "http://localhost:4566"
#     events = "http://localhost:4566"
#     stepfunctions = "http://localhost:4566"
#     sns = "http://localhost:4566"
#     sqs = "http://localhost:4566"
#     sts = "http://localhost:4566"
#     secretsmanager = "http://localhost:4566"
#     s3 = "http://localhost:4566"
#     iam = "http://localhost:4566"
#     cloudwatchlogs = "http://localhost:4566"
#   }
# }


terraform {
  required_providers {
    ansiblevault = {
      source  = "MeilleursAgents/ansiblevault"
      version = "2.2.0"
    }
  }
}

provider "ansiblevault" {
  vault_path  = pathexpand("../../../../.vault/vault-pass.txt")
  root_folder = path.cwd
}
