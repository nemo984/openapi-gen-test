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

import (
	"net/http"

	"github.com/gin-gonic/gin"
)

// AddPet - 
func AddPet(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{})
}

// DeletePet - 
func DeletePet(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{})
}

// FindPetById - 
func FindPetById(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{})
}

// FindPets - 
func FindPets(c *gin.Context) {
	c.JSON(http.StatusOK, gin.H{})
}
