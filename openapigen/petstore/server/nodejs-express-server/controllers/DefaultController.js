/**
 * The DefaultController file is a very simple one, which does not need to be changed manually,
 * unless there's a case where business logic routes the request to an entity which is not
 * the service.
 * The heavy lifting of the Controller item is done in Request.js - that is where request
 * parameters are extracted and sent to the service, and where response is handled.
 */

const Controller = require('./Controller');
const service = require('../services/DefaultService');
const addPet = async (request, response) => {
  await Controller.handleRequest(request, response, service.addPet);
};

const deletePet = async (request, response) => {
  await Controller.handleRequest(request, response, service.deletePet);
};

const find pet by id = async (request, response) => {
  await Controller.handleRequest(request, response, service.find pet by id);
};

const findPets = async (request, response) => {
  await Controller.handleRequest(request, response, service.findPets);
};


module.exports = {
  addPet,
  deletePet,
  find pet by id,
  findPets,
};
