package main

import (
	"context"
	"encoding/json"
	"log"

	chroma "github.com/amikos-tech/chroma-go"
)

func main() {
	// // Crear una nueva función de embedding de OpenAI
	// openaiEf, err := openai.NewOpenAIEmbeddingFunction(os.Getenv("OPENAI_API_KEY"))
	// if err != nil {
	// 	log.Fatalf("Error creando la función de embedding de OpenAI: %s \n", err)
	// }

	// Crear un nuevo cliente Chroma
	client, err := chroma.NewClient("http://localhost:8000")
	if err != nil {
		log.Fatalf("Error creando el cliente Chroma: %s \n", err)
	}

	/* Version */
	// Obtener la versión del cliente
	version, err := client.Version(context.Background())
	if err != nil {
		log.Fatalf("Error obteniendo la versión del cliente: %s \n", err)
	}

	log.Printf("Chroma Client Version: %s\n", version)

	/* Heartbeat */

	// Obtener el heartbeat del cliente
	heartbeat, err := client.Heartbeat(context.Background())
	if err != nil {
		log.Fatalf("Error obteniendo el heartbeat del cliente: %s \n", err)
	}

	// Convertir el heartbeat a un formato legible
	heartbeatJSON, err := json.MarshalIndent(heartbeat, "", "  ")
	if err != nil {
		log.Fatalf("Error convirtiendo el heartbeat a JSON: %s \n", err)
	}

	log.Printf("Chroma Client Heartbeat: %s\n", string(heartbeatJSON))

	// // Crear una nueva colección con opciones
	// newCollection, err := client.NewCollection(
	// 	context.TODO(),
	// 	collection.WithName("test-collection"),
	// 	collection.WithMetadata("key1", "value1"),
	// 	collection.WithEmbeddingFunction(openaiEf),
	// 	collection.WithHNSWDistanceFunction(types.L2),
	// )
	// if err != nil {
	// 	log.Fatalf("Error creando la colección: %s \n", err)
	// }

	// // Crear un nuevo conjunto de registros para contener los registros a insertar
	// rs, err := types.NewRecordSet(
	// 	types.WithEmbeddingFunction(openaiEf),
	// 	types.WithIDGenerator(types.NewULIDGenerator()),
	// )
	// if err != nil {
	// 	log.Fatalf("Error creando el conjunto de registros: %s \n", err)
	// }

	// // Agregar algunos registros al conjunto de registros
	// rs.WithRecord(types.WithDocument("My name is John. And I have two dogs."), types.WithMetadata("key1", "value1"))
	// rs.WithRecord(types.WithDocument("My name is Jane. I am a data scientist."), types.WithMetadata("key2", "value2"))

	// // Construir y validar el conjunto de registros (esto creará embeddings si no están ya presentes)
	// _, err = rs.BuildAndValidate(context.TODO())
	// if err != nil {
	// 	log.Fatalf("Error validando el conjunto de registros: %s \n", err)
	// }

	// // Agregar los registros a la colección
	// _, err = newCollection.AddRecords(context.Background(), rs)
	// if err != nil {
	// 	log.Fatalf("Error agregando documentos: %s \n", err)
	// }

	// // Contar el número de documentos en la colección
	// countDocs, qrerr := newCollection.Count(context.TODO())
	// if qrerr != nil {
	// 	log.Fatalf("Error contando documentos: %s \n", qrerr)
	// }

	// // Consultar la colección
	// fmt.Printf("countDocs: %v\n", countDocs) // esto debería resultar en 2
	// qr, qrerr := newCollection.Query(context.TODO(), []string{"I love dogs"}, 5, nil, nil, nil)
	// if qrerr != nil {
	// 	log.Fatalf("Error consultando documentos: %s \n", qrerr)
	// }
	// fmt.Printf("qr: %v\n", qr.Documents[0][0]) // esto debería resultar en el documento sobre perros
}
