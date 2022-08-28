server:
	openapi-generator-cli generate -i petstore.yaml -g $(g) -o ./openapigen/petstore/server/$(g)

client:
	openapi-generator-cli generate -i petstore.yaml -g $(g) -o ./openapigen/petstore/client/$(g)
