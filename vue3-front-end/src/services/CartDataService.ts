import http from "../http-common";
import AddtoCart from "../models/cart/add-to-cart";

class CartDataService {
  addCart(data: AddtoCart) {
    throw new Error("Method not implemented.");
  }
  getByUser(userId: number): Promise<any> {
    return http.get(`/cart/${userId}`);
  }

  delete(userId: number, marketId: number, productId: number): Promise<any> {
    return http.delete(`/cart/${userId}/${marketId}/${productId}`);
  }

  addToCart(data: AddtoCart): Promise<any> {
    return http.post("cart/product", data);
  }
}
export default new CartDataService();
