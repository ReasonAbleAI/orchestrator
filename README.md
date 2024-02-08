# Orchestrator

The orchestrator is an app that interacts with humans, semantic networks, and abilities. When the orchestrator receives a human interaction, it will use generative AI to extract the semantic meaning from the interaction, determine if any of its semantic networks or abilities are related to the query, and then generate tasks to action the interaction.

The orchestrator will continuously improve its semantic networks by acquiring new information with the researcher abilities and updating/creating connections between concepts in semantic networks. The orchestrator can have ongoing tasks using abilities, like improving its own code base. However, interactions with humans will be a priority task.

Unlike queries directly against LLMs, the orchestrator will be inquisitive and proactive. It will be far more humble and willing to ask clarifying questions and admit ignorance. Using abilities, it may also proactively ask humans questions via Slack, for instance, asking whether a specific source it has found contains accurate information and then updating its semantic network with this new information. The orchestrator actions will be auditable as the LLM prompts it produces and responses will be logged. Hallucinations will be far less likely as the LLM prompts the orchestrator produces will be structured with appropriate context.


## Working with the repository

1. Ensure you have [pipenv](https://pipenv.pypa.io/en/latest/) installed
2. Run `pipenv install` to install the dependencies
3. Run `pipenv shell` to shell into your environment


## Containerized Deployment

Create [`settings.yaml`](https://github.com/Shopify/reasonableai/blob/main/orchestrator/settings.yaml.example) with [semantic networks](https://github.com/Shopify/reasonableai/tree/main/semantic_network), abilities (incoming...), and desires of your choosing.

```
semantic_networks:
  - name: Tigers
    url: https://tigers.domain.tld
    description: Has details about tigers, their habbits, range, etc
abilities:
  - name: Researcher
    url: https://reseracher.domain.tld
    description: Can query the internet to reserach any topic
desires:
  - name: Tigers
    priority: 10
    description: Use the Researcher ability to learn about Tigers and store that information in the Tigers semantic network
ollama_url: https://ollama-api.domain.tld
```

```bash
$ docker-compose up
```

Pull `mistral:latest` on your Ollama instance.

If running Docker container from `docker-compose.yaml`

```bash
$ docker exec -it orchestrator-ollama ollama pull mistral:latest
```

If running seperate Ollama instance.

```bash
$ curl http://<your ollama server address>/api/pull -d '{"name": "mistral:latest"}'
```
