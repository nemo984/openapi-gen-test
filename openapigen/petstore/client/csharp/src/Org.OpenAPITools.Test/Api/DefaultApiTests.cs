/*
 * Swagger Petstore
 *
 * A sample API that uses a petstore as an example to demonstrate features in the OpenAPI 3.0 specification
 *
 * The version of the OpenAPI document: 1.0.0
 * Contact: apiteam@swagger.io
 * Generated by: https://github.com/openapitools/openapi-generator.git
 */

using System;
using System.IO;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Linq;
using System.Reflection;
using RestSharp;
using NUnit.Framework;

using Org.OpenAPITools.Client;
using Org.OpenAPITools.Api;
using Org.OpenAPITools.Model;

namespace Org.OpenAPITools.Test
{
    /// <summary>
    ///  Class for testing DefaultApi
    /// </summary>
    /// <remarks>
    /// This file is automatically generated by OpenAPI Generator (https://openapi-generator.tech).
    /// Please update the test case below to test the API endpoint.
    /// </remarks>
    public class DefaultApiTests
    {
        private DefaultApi instance;

        /// <summary>
        /// Setup before each unit test
        /// </summary>
        [SetUp]
        public void Init()
        {
            instance = new DefaultApi();
        }

        /// <summary>
        /// Clean up after each unit test
        /// </summary>
        [TearDown]
        public void Cleanup()
        {

        }

        /// <summary>
        /// Test an instance of DefaultApi
        /// </summary>
        [Test]
        public void InstanceTest()
        {
            // TODO uncomment below to test 'IsInstanceOf' DefaultApi
            //Assert.IsInstanceOf(typeof(DefaultApi), instance);
        }

        
        /// <summary>
        /// Test AddPet
        /// </summary>
        [Test]
        public void AddPetTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //NewPet newPet = null;
            //var response = instance.AddPet(newPet);
            //Assert.IsInstanceOf(typeof(Pet), response, "response is Pet");
        }
        
        /// <summary>
        /// Test DeletePet
        /// </summary>
        [Test]
        public void DeletePetTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //long id = null;
            //instance.DeletePet(id);
            
        }
        
        /// <summary>
        /// Test FindPetById
        /// </summary>
        [Test]
        public void FindPetByIdTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //long id = null;
            //var response = instance.FindPetById(id);
            //Assert.IsInstanceOf(typeof(Pet), response, "response is Pet");
        }
        
        /// <summary>
        /// Test FindPets
        /// </summary>
        [Test]
        public void FindPetsTest()
        {
            // TODO uncomment below to test the method and replace null with proper value
            //List<string> tags = null;
            //int? limit = null;
            //var response = instance.FindPets(tags, limit);
            //Assert.IsInstanceOf(typeof(List<Pet>), response, "response is List<Pet>");
        }
        
    }

}
