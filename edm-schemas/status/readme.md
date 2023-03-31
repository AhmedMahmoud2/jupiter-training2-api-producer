# <ENTITY> entity

*« Tiny amount of context for the entity »*  
This entity exists at UCL and is used by humans and computer alike. This represents all entities of type entity, but none of type emnity.

## Mandatory fields returned

« *Optionally, some textural information about the returned values* »  
More fields can be returned by system API but the ones below are required for the Enterprise API.

| Name               | EDM field           | System field    |
|--------------------|---------------------|-----------------|
| Entity code        | identifier          | entity_code     |
| Entity name	     | entity_name         | entity_name     |
| Entity description | entity_description  | entity_desc     |
| Parent code        | parent_code         | parent_code     |
| Parent name        | parent_name         | parent_name     |

## Example SQL

*« Further code based examples for the developer »*

    SELECT entity_code, entity_name, entity_desc
    FROM entities
    LEFT OUTER JOIN parents
    ON entity_parent = parent_code


## Pseudocode

    items = api.get(https://system.ucl.ac.uk/api/v2/entities/?fields=parent)
    output = []
    for i in items:
        output.add({
            code: i.code,
            name: i.name,
            description: i.desc,
            parent: {
                code: i.parent.code
                name: i.parent.name
            }
        })

    return output