from simple_graphql_client import GraphQLClient
from datetime import datetime

client = GraphQLClient("https://arweave.net/graphql")

limestone_query = """
query transactions(
  $type: String!
  $token: String!
  $version: String!
  $minBlock: Int!
) {
  transactions(
    tags: [
      { name: "app", values: "Limestone" }
      { name: "type", values: [$type] }
      { name: "token", values: [$token] }
      { name: "version", values: [$version] }
    ]
    block: { min: $minBlock }
    first: 1
  ) {
    edges {
      node {
        tags {
          name
          value
        }
      }
    }
  }
}
"""


def _query(type: str, token: str, version: str, min_block: int):
    # specify return object
    ret = {}

    # query limestone data
    variables = {
        "type": type,
        "token": token,
        "version": version,
        "minBlock": min_block
    }

    result = client.query(limestone_query, variables=variables)
    edges = result.get("data").get("transactions").get("edges")
    # we can get the first item because it is specified in the query
    node = edges[0].get("node")
    for tag in node.get("tags"):
        name = tag.get("name")
        value = tag.get("value")

        if name == "value":
            ret['price'] = float(value)
        if name == "time":
            timestamp = datetime.fromtimestamp(float(value) / 1000)
            ret['updated'] = datetime.isoformat(timestamp)

    return ret


def get_price(token: str, min_block: int = 0):
    return _query(type="data-latest", token=token, version="0.005", min_block=min_block)
