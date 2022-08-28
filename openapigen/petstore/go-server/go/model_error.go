/*
 * Swagger Petstore
 *
 * A sample API that uses a petstore as an example to demonstrate features in the OpenAPI 3.0 specification
 *
 * API version: 1.0.0
 * Contact: apiteam@swagger.io
 * Generated by: OpenAPI Generator (https://openapi-generator.tech)
 */

package openapi

type Error struct {

	Code int32 `json:"code"`

	Message string `json:"message"`
}

// AssertErrorRequired checks if the required fields are not zero-ed
func AssertErrorRequired(obj Error) error {
	elements := map[string]interface{}{
		"code": obj.Code,
		"message": obj.Message,
	}
	for name, el := range elements {
		if isZero := IsZeroValue(el); isZero {
			return &RequiredError{Field: name}
		}
	}

	return nil
}

// AssertRecurseErrorRequired recursively checks if required fields are not zero-ed in a nested slice.
// Accepts only nested slice of Error (e.g. [][]Error), otherwise ErrTypeAssertionError is thrown.
func AssertRecurseErrorRequired(objSlice interface{}) error {
	return AssertRecurseInterfaceRequired(objSlice, func(obj interface{}) error {
		aError, ok := obj.(Error)
		if !ok {
			return ErrTypeAssertionError
		}
		return AssertErrorRequired(aError)
	})
}
