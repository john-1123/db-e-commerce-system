import http from "../http-common";
import AddtoCart from "../models/product/add-product-cart";
import { CreateProduct } from "../models/product/create-product";
import { UpdateProduct } from "../models/product/update-prodcut";

class ProductDataService {
  getAll() {
    return http.get("/products");
  }

  get(productId: number) {
    return http.get(`/products/${productId}`);
  }

  getProductByMarket(marketId: number) {
    return http.get(`/products/market/${marketId}`);
  }

  create(data: CreateProduct) {
    return http.post("/products", data);
  }

  update(id: number, data: UpdateProduct): Promise<any> {
    return http.put(`/products/${id}`, data);
  }

  delete(id: number): Promise<any> {
    return http.delete(`/products/${id}`);
  }

  ProductToCart(data: AddtoCart): Promise<any> {
    return http.post("/cart/product");
  }
}
export default new ProductDataService();
