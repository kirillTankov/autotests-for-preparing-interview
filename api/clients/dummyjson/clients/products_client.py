from api.clients.dummyjson.clients.base_client import BaseClient
from api.clients.dummyjson.endpoints import Endpoints


class ProductsClient(BaseClient):
    def get_all_products(self):
        return self.get(Endpoints.PRODUCTS)

    def get_products_by_id(self, product_id):
        return self.get(f'{Endpoints.PRODUCTS}/{product_id}')

    def get_search_products(self, query):
        return self.get(
            f'{Endpoints.PRODUCTS}/search',
            params={'q': query}
        )

    def create_product(self, body):
        return self.post(f'{Endpoints.PRODUCTS}/add', json=body)

    def update_product(self, product_id, body):
        return self.put(f'{Endpoints.PRODUCTS}/{product_id}', json=body)

    def patch_product(self, product_id, body):
        return self.patch(f"{Endpoints.PRODUCTS}/{product_id}", json=body)

    def delete_product(self, product_id):
        return self.delete(f"{Endpoints.PRODUCTS}/{product_id}")