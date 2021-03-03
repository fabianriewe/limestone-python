from simple_graphql_client import GraphQLClient
from datetime import datetime
from typing import Optional

client = GraphQLClient("https://arweave.net/graphql")

limestone_query = """
query transactions(
  $type: String!
  $token: String!
  $version: String!
  $maxBlock: Int
) {
  transactions(
    tags: [
      { name: "app", values: "Limestone" }
      { name: "type", values: [$type] }
      { name: "token", values: [$token] }
      { name: "version", values: [$version] }
    ]
    block: { max: $maxBlock }
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


def _query(type: str, token: str, version: str, max_block: Optional[int]):
    # specify return object
    ret = {}

    # query limestone data
    variables = {
        "type": type,
        "token": token,
        "version": version,
        "maxBlock": max_block
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
            timestamp = datetime.utcfromtimestamp(float(value) / 1000)
            ret['updated'] = datetime.isoformat(timestamp)

    return ret


def get_price(token: str, at_block: Optional[int] = None):
    return _query(type="data-latest", token=token, version="0.005", max_block=at_block)
