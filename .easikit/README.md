# Integration title

## Links to useful documents

- [HLD](https://wiki.ucl.ac.uk/display/API/High+level+design)
- [EASIKit Documentation](https://github.com/ucl-isd/easikit-core) development

{Please add any other relevant documentation link which is shared by any stakeholder which describes the requirement in their own standard.
eg - Functional specification document}

## Pre-requisites

- .vault pass - LastPass/integration-shared EASIKit Vault Password
- environment variables need to be reset every run


## Deployment

- Azure App Registration names:
    Dev: identity-person-dev
    UAT: identity-person-uat

- Database objects
  - view 1: ./database/exemplar_tables.sql
  - view 2: ./database/exemplar_tables.sql


## Functional components

### Sequence diagram

![Screenshot](sequence.jpg)

{optional depending on complexity of solution}


### Development architecture overview

This development uses [EASIKit standard MVC pattern](https://github.com/ucl-isd/easikit-core/blob/readme/development-standards/mvc.md)

## Entity relationship mapping

This uses entities:

- person (EDM readme)[https://github.com/ucl-isd/.../tree/main/edm-schemas/...]


### Unit testing 

## Secrets

ODS API_PERSON_USER password
- ./terraform/target/{target}/secrets/DB_PASSWORD

## Config

### Module level

The following are specified at root level:

- Context path


The following at target/envionrment level:

- API version
- resource path



