# ------------------------ #
# ------- secrets -------- #
# ------------------------ #

# below decrypts all the secrets for this target
# all these passwords will have been encrypted by the same
# vault password file as specified in the provider
# if you used z deploy secret to initialise them, that should
# already be set to ..../secrets/vault-pass.txt

# once created, be sure to reference this password in the locals block
# in the main easikit.tf file
# data "ansiblevault_path" "db_password" {
#   path = "secrets/DB_PASSWORD"
# }