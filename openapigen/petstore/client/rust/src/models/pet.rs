/*
 * Swagger Petstore
 *
 * A sample API that uses a petstore as an example to demonstrate features in the OpenAPI 3.0 specification
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: apiteam@swagger.io
 * Generated by: https://openapi-generator.tech
 */




#[derive(Clone, Debug, PartialEq, Default, Serialize, Deserialize)]
pub struct Pet {
    #[serde(rename = "name")]
    pub name: String,
    #[serde(rename = "tag", skip_serializing_if = "Option::is_none")]
    pub tag: Option<String>,
    #[serde(rename = "id")]
    pub id: i64,
}

impl Pet {
    pub fn new(name: String, id: i64) -> Pet {
        Pet {
            name,
            tag: None,
            id,
        }
    }
}


