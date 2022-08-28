/*
Swagger Petstore

A sample API that uses a petstore as an example to demonstrate features in the OpenAPI 3.0 specification

API version: 1.0.0
Contact: apiteam@swagger.io
*/

// Code generated by OpenAPI Generator (https://openapi-generator.tech); DO NOT EDIT.

package openapi

import (
	"encoding/json"
)

// PetAllOf struct for PetAllOf
type PetAllOf struct {
	Id int64 `json:"id"`
}

// NewPetAllOf instantiates a new PetAllOf object
// This constructor will assign default values to properties that have it defined,
// and makes sure properties required by API are set, but the set of arguments
// will change when the set of required properties is changed
func NewPetAllOf(id int64) *PetAllOf {
	this := PetAllOf{}
	this.Id = id
	return &this
}

// NewPetAllOfWithDefaults instantiates a new PetAllOf object
// This constructor will only assign default values to properties that have it defined,
// but it doesn't guarantee that properties required by API are set
func NewPetAllOfWithDefaults() *PetAllOf {
	this := PetAllOf{}
	return &this
}

// GetId returns the Id field value
func (o *PetAllOf) GetId() int64 {
	if o == nil {
		var ret int64
		return ret
	}

	return o.Id
}

// GetIdOk returns a tuple with the Id field value
// and a boolean to check if the value has been set.
func (o *PetAllOf) GetIdOk() (*int64, bool) {
	if o == nil {
		return nil, false
	}
	return &o.Id, true
}

// SetId sets field value
func (o *PetAllOf) SetId(v int64) {
	o.Id = v
}

func (o PetAllOf) MarshalJSON() ([]byte, error) {
	toSerialize := map[string]interface{}{}
	if true {
		toSerialize["id"] = o.Id
	}
	return json.Marshal(toSerialize)
}

type NullablePetAllOf struct {
	value *PetAllOf
	isSet bool
}

func (v NullablePetAllOf) Get() *PetAllOf {
	return v.value
}

func (v *NullablePetAllOf) Set(val *PetAllOf) {
	v.value = val
	v.isSet = true
}

func (v NullablePetAllOf) IsSet() bool {
	return v.isSet
}

func (v *NullablePetAllOf) Unset() {
	v.value = nil
	v.isSet = false
}

func NewNullablePetAllOf(val *PetAllOf) *NullablePetAllOf {
	return &NullablePetAllOf{value: val, isSet: true}
}

func (v NullablePetAllOf) MarshalJSON() ([]byte, error) {
	return json.Marshal(v.value)
}

func (v *NullablePetAllOf) UnmarshalJSON(src []byte) error {
	v.isSet = true
	return json.Unmarshal(src, &v.value)
}

